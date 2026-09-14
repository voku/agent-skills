---
name: laravel-database-optimization
description: Laravel database optimization patterns for queries, indexing, Redis caching, pagination, transactions, migrations, and debugging. 9 rules across 9 categories. Use when writing Eloquent queries, creating migrations, configuring caching, debugging slow queries, or optimizing database performance. Triggers on tasks involving N+1 queries, indexing, Redis caching, pagination, or database transactions.
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
---

# Laravel Database Optimization

High-performance database patterns for Laravel 11.x - 13.x applications. Contains **9 consolidated rules across 9 categories** for eliminating N+1 queries, architecting indexes, Redis caching, cursor streaming, deadlock-safe concurrency, zero-downtime migrations, and query profiling.

## Metadata

- **Version:** 2.0.0
- **Framework:** Laravel 11.x - 13.x
- **PHP:** 8.2+
- **Rule Count:** 9 rules across 9 categories
- **License:** MIT

## When to Apply

Reference these guidelines when:
- Writing Eloquent queries or using the query builder
- Diagnosing and fixing N+1 query problems
- Adding database indexes to migrations
- Implementing Redis caching and cache tags
- Paginating or streaming large datasets
- Wrapping operations in concurrency-safe database transactions
- Creating production migrations for large tables
- Debugging slow queries with EXPLAIN ANALYZE or query listeners

## Rule Categories by Priority

| Priority | Category | Impact | Prefix | Rules |
|----------|----------|--------|--------|-------|
| 1 | Query Performance & N+1 | CRITICAL | `query-` | 1 |
| 2 | Indexing Strategies | CRITICAL | `index-` | 1 |
| 3 | Eloquent Optimization | HIGH | `eloquent-` | 1 |
| 4 | Caching with Redis | HIGH | `cache-` | 1 |
| 5 | Pagination & Large Datasets | HIGH | `data-` | 1 |
| 6 | Transactions & Locking | HIGH | `lock-` | 1 |
| 7 | Migrations | HIGH | `migrate-` | 1 |
| 8 | Query Debugging | MEDIUM | `debug-` | 1 |
| 9 | Naming Conventions | HIGH | `naming-` | 1 |

## Quick Reference

### 1. Query Performance & N+1 (CRITICAL) — 1 rule
- [query-n-plus-one.md](rules/query-n-plus-one.md) - Eliminate N+1 queries with eager loading (`with()`), disable lazy loading in local/CI (`Model::preventLazyLoading(!app()->isProduction())`), and select only required columns.

### 2. Indexing Strategies (CRITICAL) — 1 rule
- [index-strategies.md](rules/index-strategies.md) - Index all foreign keys, create composite indexes matching multi-column WHERE/ORDER BY query shapes following the leftmost prefix rule, and utilize covering indexes.

### 3. Eloquent Optimization (HIGH) — 1 rule
- [eloquent-subqueries.md](rules/eloquent-subqueries.md) - Avoid hydration overhead on read-heavy hot paths with Query Builder, load aggregate counts via `withCount()`, and replace slow `whereHas()` with subquery selects or `whereExists()`.

### 4. Caching with Redis (HIGH) — 1 rule
- [cache-redis-patterns.md](rules/cache-redis-patterns.md) - Cache expensive database queries with `Cache::remember()` using strict TTLs, and invalidate selectively via cache tags (`Cache::tags(['users'])`) or model event observers.

### 5. Pagination & Large Datasets (HIGH) — 1 rule
- [data-chunking-pagination.md](rules/data-chunking-pagination.md) - Stream large result sets using `chunkById()` or lazy cursors (`cursor()`), ban unbounded `all()` queries, and implement cursor pagination (`cursorPaginate()`).

### 6. Transactions & Locking (HIGH) — 1 rule
- [lock-concurrency.md](rules/lock-concurrency.md) - Keep database transactions short to minimize lock contention, use pessimistic locks (`lockForUpdate()`) on balance/inventory updates, and wrap deadlock-prone writes in `DB::transaction(..., attempts: 3)`.

### 7. Migrations (HIGH) — 1 rule
- [migrate-zero-downtime.md](rules/migrate-zero-downtime.md) - Execute schema changes without downtime by adding nullable/defaulted columns, creating large indexes concurrently/algorithmically (`ALGORITHM=INPLACE`), and separating schema additions from data backfills.

### 8. Query Debugging (MEDIUM) — 1 rule
- [debug-query-profiling.md](rules/debug-query-profiling.md) - Profile query execution plans with `EXPLAIN / EXPLAIN ANALYZE`, log queries exceeding 200ms using `DB::whenQueryingForLongerThan()`, and inspect query counts with Laravel Pulse or Debugbar.

### 9. Naming Conventions (HIGH) — 1 rule
- [naming-conventions.md](rules/naming-conventions.md) - Follow standard Eloquent naming conventions (snake_case plural tables, singular snake_case FKs `user_id`, camelCase relationships) to prevent silent query failure.

## How to Use

Read individual rule files in `rules/` for concise triggers, Bad vs Good code comparisons, and concrete SQL/Eloquent optimizations.
