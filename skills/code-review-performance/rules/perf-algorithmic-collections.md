---
id: perf-algorithmic-collections
title: "Algorithmic Complexity, Lookup Sets, and Hash Maps"
category: algorithms
priority: CRITICAL
triggers: [o-n-squared-in-array, nested-loop-scan, linear-search-large-array, hash-map-lookup]
tags: [performance, algorithmic-complexity, big-o, hash-maps, set-lookup]
---

# Algorithmic Complexity, Lookup Sets, and Hash Maps

**Trigger Anchor:** Replace O(N^2) nested array searches with O(1) hash maps or key-indexed lookups (`array_flip` / associative sets); avoid linear array scans (`in_array`) in tight loops.

---

### Bad
```php
// ❌ O(N * M) nested scan: quadratic complexity on large lists
$matchedOrders = [];
foreach ($customers as $customer) {
    foreach ($orders as $order) {
        if ($order['customer_id'] === $customer['id']) {
            $matchedOrders[$customer['id']][] = $order;
        }
    }
}

// ❌ Linear in_array search inside loop (O(N * M))
foreach ($pendingTransactions as $tx) {
    if (in_array($tx['id'], $completedIds, true)) {
        continue;
    }
}
```

### Good
```php
// ✅ O(N + M) grouping using associative hash map
$ordersByCustomer = [];
foreach ($orders as $order) {
    $ordersByCustomer[$order['customer_id']][] = $order;
}

$matchedOrders = [];
foreach ($customers as $customer) {
    if (isset($ordersByCustomer[$customer['id']])) {
        $matchedOrders[$customer['id']] = $ordersByCustomer[$customer['id']];
    }
}

// ✅ O(1) hash lookup set using array_flip
$completedLookup = array_flip($completedIds);
foreach ($pendingTransactions as $tx) {
    if (isset($completedLookup[$tx['id']])) {
        continue;
    }
}
```
