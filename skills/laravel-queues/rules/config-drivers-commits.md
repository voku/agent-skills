---
id: config-drivers-commits
title: Queue Drivers, Database Transactions, and after_commit
category: config
priority: CRITICAL
triggers: [race-condition-uncommitted-job, wrong-queue-driver, missing-failed-jobs-table]
tags: [laravel, queues, redis, database-queue, after-commit, configuration]
---

# Queue Drivers, Database Transactions, and after_commit

**Trigger Anchor:** Set `after_commit => true` across queue connections to eliminate race conditions with uncommitted database rows, use Redis for high-throughput production, and ensure persistent failed job storage.

---

### Bad
```php
<?php

// ❌ Race condition: Job dispatches before the surrounding DB transaction commits
DB::transaction(function () use ($userData) {
    $user = User::create($userData);

    // ❌ Worker picks up job immediately, queries User::findOrFail($id), and throws 404!
    SendWelcomeEmail::dispatch($user->id);
});
```

### Good
```php
// config/queue.php
return [
    'default' => env('QUEUE_CONNECTION', 'redis'),

    'connections' => [
        'redis' => [
            'driver' => 'redis',
            'connection' => env('REDIS_QUEUE_CONNECTION', 'default'),
            'queue' => env('REDIS_QUEUE', 'default'),
            'retry_after' => 90,
            'block_for' => 2,
            // ✅ Guarantees jobs are held until outer DB transaction commits
            'after_commit' => true,
        ],
    ],

    'failed' => [
        'driver' => env('QUEUE_FAILED_DRIVER', 'database-uuids'),
        'database' => env('DB_CONNECTION', 'mysql'),
        'table' => 'failed_jobs',
    ],
];
```
