---
id: data-chunking-pagination
title: "Large Datasets: Chunking, Lazy Cursors, and Cursor Pagination"
category: data
priority: HIGH
triggers: [memory-exhaustion, unbounded-query, offset-pagination-slowdown, batch-processing-oom]
tags: [laravel, chunking, chunkById, cursor, cursorPaginate, memory-limit]
---

# Large Datasets: Chunking, Lazy Cursors, and Cursor Pagination

**Trigger Anchor:** Stream large result sets using `chunkById()` or lazy cursors (`cursor()`), ban unbounded `all()` queries, and implement cursor pagination (`cursorPaginate()`) for large or infinite-scroll datasets.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Loading 500k rows into memory blows the 128M PHP memory limit
$orders = Order::where('status', 'pending')->get(); // Out of memory fatal error

// ❌ Offset pagination on page 10,000 scans and discards 200,000 rows
// SELECT * FROM events ORDER BY id DESC LIMIT 20 OFFSET 200000;
$events = Event::orderBy('id', 'desc')->paginate(20);
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ chunkById processes constant-memory batches without offset degradation
Order::query()
    ->where('status', 'pending')
    ->chunkById(500, function ($batch): void {
        foreach ($batch as $order) {
            $this->processOrder($order);
        }
    });

// ✅ cursor() hydrates one model at a time via a streaming database cursor
foreach (User::query()->cursor() as $user) {
    $this->exportUserToCsv($user);
}

// ✅ cursorPaginate uses WHERE id < ? instead of OFFSET, executing in O(1) time
$events = Event::query()
    ->orderBy('id', 'desc')
    ->cursorPaginate(20);
```
