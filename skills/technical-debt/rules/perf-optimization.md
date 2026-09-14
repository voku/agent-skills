---
id: perf-optimization
title: "Performance Debt: N+1 Queries, Unbounded Lists, and Bundle Bloat"
category: perf
priority: HIGH
triggers: [n-plus-one-query, missing-pagination, unbounded-query, bundle-bloat, missing-caching]
tags: [performance, n-plus-one, pagination, caching, bundle-size]
---

# Performance Debt: N+1 Queries, Unbounded Lists, and Bundle Bloat

**Trigger Anchor:** Eliminate N+1 queries with eager loading, enforce pagination on all list endpoints, cache expensive read aggregations, and split frontend bundle chunks (<200KB initial load).

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ N+1 query loop and unbounded result set
class OrderController extends Controller
{
    public function index(): JsonResponse
    {
        // ❌ Returns entire table without pagination (crashes at 10k rows)
        $orders = Order::all();

        $data = [];
        foreach ($orders as $order) {
            // ❌ N+1 queries: triggers 1 query per iteration to fetch user
            $data[] = [
                'id' => $order->id,
                'customer_email' => $order->user->email,
            ];
        }

        return response()->json($data);
    }
}
```

```typescript
// ❌ Monolithic bundle import pulls heavy charting & PDF libraries into initial chunk
import { HeavyPdfGenerator } from 'large-pdf-lib'; // 850 KB in main.js
import { FullDashboardCharts } from 'large-chart-lib'; // 1.2 MB in main.js
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ Eager loading and cursor/length-aware pagination
class OrderController extends Controller
{
    public function index(Request $request): JsonResponse
    {
        $orders = Order::query()
            ->with(['user:id,email'])
            ->latest('id')
            ->paginate(perPage: 25);

        return response()->json($orders);
    }
}
```

```typescript
// ✅ Dynamic route-level code splitting keeps entry bundle under budget (<200 KB)
import { lazy, Suspense } from 'react';

const HeavyPdfGenerator = lazy(() => import('large-pdf-lib'));
const FullDashboardCharts = lazy(() => import('large-chart-lib'));

export function AnalyticsPage() {
  return (
    <Suspense fallback={<Spinner />}>
      <FullDashboardCharts />
    </Suspense>
  );
}
```
