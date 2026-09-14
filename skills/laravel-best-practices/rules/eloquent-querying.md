---
id: eloquent-querying
title: "Eloquent Querying: Eager Loading, Chunking, and Scopes"
category: eloquent
priority: CRITICAL
triggers: [n-plus-one-query, memory-exhaustion-chunking, un-scoped-query, missing-with-relationship]
tags: [laravel, eloquent, eager-loading, chunking, query-scopes, performance]
---

# Eloquent Querying: Eager Loading, Chunking, and Scopes

**Trigger Anchor:** Prevent N+1 queries with eager loading (`with()`), process large record sets via cursor/chunking (`lazy()`, `chunkById()`), and encapsulate reusable query constraints in dedicated local query scopes.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ N+1 queries and memory exhaustion from loading all rows into RAM
class ReportGenerator
{
    public function run(): void
    {
        // ❌ Loads 100,000 records into memory at once
        $orders = Order::where('status', 'active')->get();

        foreach ($orders as $order) {
            // ❌ N+1 queries triggered on each iteration
            $customerName = $order->customer->name;
            $items = $order->items;
        }
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;

final class Order extends Model
{
    /**
     * ✅ Reusable, testable query scope
     *
     * @param Builder<self> $query
     */
    public function scopeActiveAndPaid(Builder $query): void
    {
        $query->where('status', OrderStatus::Active)
            ->whereNotNull('paid_at');
    }
}
```

```php
<?php

declare(strict_types=1);

// ✅ Eager loading with indexed chunkById avoids memory spikes and N+1 queries
Order::query()
    ->activeAndPaid()
    ->with(['customer:id,name', 'items.product:id,title'])
    ->chunkById(500, function ($orders): void {
        foreach ($orders as $order) {
            $this->processOrderSummary($order);
        }
    });
```
