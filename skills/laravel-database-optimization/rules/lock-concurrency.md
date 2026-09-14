---
id: lock-concurrency
title: "Transactions, Pessimistic Locking, and Deadlock Retries"
category: lock
priority: HIGH
triggers: [deadlock-error, race-condition-balance, long-transaction-block, optimistic-locking-failure]
tags: [transactions, locking, lockForUpdate, deadlocks, concurrency, mysql]
---

# Transactions, Pessimistic Locking, and Deadlock Retries

**Trigger Anchor:** Keep database transactions short to minimize lock contention, use pessimistic locks (`lockForUpdate()`) on balance/inventory updates, and wrap deadlock-prone writes in `DB::transaction(..., attempts: 3)`.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Race condition: concurrent requests read same balance, both withdraw successfully
$account = Account::find($id);
if ($account->balance >= $amount) {
    // ❌ Slow HTTP API call inside transaction holds DB row lock for seconds
    Http::post('https://payment.gateway.com/charge');

    $account->decrement('balance', $amount);
}
```

### Good
```php
<?php

declare(strict_types=1);

use Illuminate\Support\Facades\DB;

// ✅ Deadlock retry attempts + pessimistic row-level lock (FOR UPDATE)
DB::transaction(function () use ($accountId, $amount): void {
    // Row is locked against concurrent reads and writes until transaction commits
    $account = Account::where('id', $accountId)->lockForUpdate()->firstOrFail();

    if ($account->balance < $amount) {
        throw new InsufficientFundsException('Balance too low');
    }

    $account->decrement('balance', $amount);
}, attempts: 3); // Automatically retries upon MySQL 1213 Deadlock
```

### Transaction Invariants
1. **Never perform network calls inside transactions:** Dispatch HTTP requests or email sends *before* or *after* the database commit.
2. **Deterministic order:** Acquire locks in consistent primary key order (e.g. `sort($ids)`) to prevent mutual wait cycles.
