---
id: debug-query-profiling
title: "Query Profiling: EXPLAIN, Slow Logs, and Threshold Alerts"
category: debug
priority: MEDIUM
triggers: [unexplained-slow-query, missing-slow-query-alert, hidden-query-bottleneck, profiling-gap]
tags: [debugging, explain, explain-analyze, slow-query-log, profiling, laravel-pulse]
---

# Query Profiling: EXPLAIN, Slow Logs, and Threshold Alerts

**Trigger Anchor:** Profile query execution plans with `EXPLAIN / EXPLAIN ANALYZE`, log queries exceeding 200ms using `DB::whenQueryingForLongerThan()`, and inspect query counts with Laravel Pulse or Debugbar.

---

### Bad
```php
<?php

// ❌ Guessing why a query takes 4 seconds without inspecting the execution plan
$orders = Order::where('status', 'processing')
    ->where('total_amount', '>', 500)
    ->orderBy('created_at', 'desc')
    ->get();
```

### Good
```php
<?php

declare(strict_types=1);

namespace App\Providers;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\ServiceProvider;

final class DatabaseServiceProvider extends ServiceProvider
{
    public function boot(): void
    {
        // ✅ Log any single query executing longer than 200 milliseconds
        DB::listen(function ($query): void {
            if ($query->time > 200) {
                Log::warning('Slow database query detected', [
                    'sql' => $query->sql,
                    'bindings' => $query->bindings,
                    'time_ms' => $query->time,
                ]);
            }
        });

        // ✅ Alert if aggregate request database time exceeds 1 second
        DB::whenQueryingForLongerThan(1000, function ($connection): void {
            Log::alert("Database spending excessive time: {$connection->totalQueryDuration()}ms");
        });
    }
}
```

```bash
# ✅ Analyze query plan in MySQL CLI / Laravel Tinker
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 12 AND status = 'active';
# Look for: type: ALL (full table scan) vs type: ref / range (index scan)
```
