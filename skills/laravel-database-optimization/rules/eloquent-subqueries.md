---
id: eloquent-subqueries
title: "Eloquent Optimization: Subqueries, Aggregates, and Query Builder"
category: eloquent
priority: HIGH
triggers: [slow-where-has, hydration-overhead, manual-aggregate-counting, correlated-subquery]
tags: [laravel, eloquent, with-count, subquery-select, where-exists, query-builder]
---

# Eloquent Optimization: Subqueries, Aggregates, and Query Builder

**Trigger Anchor:** Avoid hydration overhead on read-heavy hot paths with Query Builder, load aggregate counts via `withCount()`, and replace slow `whereHas()` with subquery selects or `whereExists()`.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Loading full relationship collections just to count items or fetch one latest value
$authors = Author::with('books')->get();
foreach ($authors as $author) {
    $bookCount = $author->books->count(); // ❌ Hydrates all book models into memory
}

// ❌ Inefficient whereHas produces slow correlated subqueries on large datasets
$authorsWithRecentBooks = Author::whereHas('books', function ($query) {
    $query->where('published_at', '>=', now()->subYear());
})->get();
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ withCount runs a single optimized COUNT(*) subquery without model hydration
$authors = Author::query()
    ->withCount('books')
    ->withMax('books as latest_book_published_at', 'published_at')
    ->get();

// ✅ Optimized exists subquery replaces heavy whereHas join
$authorsWithRecentBooks = Author::query()
    ->whereExists(function ($query) {
        $query->select(DB::raw(1))
            ->from('books')
            ->whereColumn('books.author_id', 'authors.id')
            ->where('books.published_at', '>=', now()->subYear());
    })
    ->get();

// ✅ Fast direct Query Builder for read-only throughput-critical endpoints
$data = DB::table('logs')
    ->where('level', 'error')
    ->latest('created_at')
    ->limit(100)
    ->get(['id', 'message', 'created_at']);
```
