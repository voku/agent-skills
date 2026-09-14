---
id: sec-core-security
title: Core Security (SQL Injection, Escaping, Passwords, File Uploads)
category: sec
priority: CRITICAL
triggers: [sqli, xss, raw-password, unvalidated-upload, unescaped-output]
tags: [security, pdo, prepared-statements, xss, password_hash, file-uploads]
---

# Core Security

**Trigger Anchor:** Use prepared statements for every SQL query. Validate input and escape output strictly by sink (HTML, JSON, CLI). Use `password_hash()` for credentials. Validate file uploads with MIME type inspection and randomized storage names.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ SQL injection, XSS vulnerability, obsolete md5 password hashing
$user = $_POST['user'];
$pass = $_POST['pass'];

// String interpolation in SQL
$pdo->query("SELECT * FROM users WHERE username = '{$user}'");

// Weak password hashing
$hashed = md5($pass);

// Direct unescaped output
echo "<div>Welcome, " . $_GET['name'] . "</div>";
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ Parameterized SQL, robust password hashing, context-aware escaping
$stmt = $pdo->prepare('SELECT id, password_hash FROM users WHERE username = :username');
$stmt->execute(['username' => $username]);
$user = $stmt->fetch();

if ($user && password_verify($password, $user['password_hash'])) {
    // Rehash if modern algorithm parameters changed
    if (password_needs_rehash($user['password_hash'], PASSWORD_DEFAULT)) {
        $newHash = password_hash($password, PASSWORD_DEFAULT);
        // update hash
    }
}

// Escaped HTML output
$safeName = htmlspecialchars($name, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
echo "<div>Welcome, {$safeName}</div>";
```
