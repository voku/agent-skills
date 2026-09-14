---
id: perf-database-nplusone
title: "Database Query Shape, N+1 Prevention, and Index Alignment"
category: database
priority: CRITICAL
triggers: [n-plus-one-query, missing-eager-load, unindexed-filter, query-in-loop, count-zero-folding]
tags: [performance, database, n-plus-one, eager-loading, indexing, sql-queries]
---

# Database Query Shape, N+1 Prevention, and Index Alignment

**Trigger Anchor:** Eliminate queries inside loops via eager loading or bulk lookups (`WHERE IN (...)`); verify index alignment for filtered columns; use strict count queries returning exact integer counts instead of loading full result sets.

---

### Bad
```php
// ❌ N+1 query problem: executing a query per item inside loop
$users = $db->query('SELECT id, name FROM users LIMIT 100')->fetchAll();
foreach ($users as $user) {
    // 100 queries executed sequentially against the database!
    $userProfile = $db->query('SELECT bio FROM profiles WHERE user_id = ' . (int)$user['id'])->fetch();
}

// ❌ Loading entire result set into memory merely to count rows
$rows = $db->query('SELECT * FROM orders WHERE status = "pending"')->fetchAll();
$count = count($rows);

// ❌ Using deprecated query helper that folds 0 count into -1
$count = $pdo->querySingleItem("SELECT COUNT(*) FROM tasks WHERE status = 'done'");
```

### Good
```php
// ✅ Eager loading / bulk lookup using WHERE IN (...) in a single query
$users = $db->query('SELECT id, name FROM users LIMIT 100')->fetchAll();
$userIds = array_column($users, 'id');

if ($userIds !== []) {
    $placeholders = implode(',', array_fill(0, count($userIds), '?'));
    $stmt = $db->prepare("SELECT user_id, bio FROM profiles WHERE user_id IN ($placeholders)");
    $stmt->execute($userIds);
    $profiles = $stmt->fetchAll(\PDO::FETCH_GROUP | \PDO::FETCH_UNIQUE);
}

// ✅ Efficient index-backed count query returning typed integer
$count = (int)$db->querySingleItemAsIntOrThrowException(
    'SELECT COUNT(*) FROM orders WHERE status = "pending"'
);
```
