---
name: laravel-database-optimization
description: Laravel database optimization patterns for queries, indexing, Redis caching, pagination, transactions, migrations, and debugging. Use when writing Eloquent queries, creating migrations, configuring caching, debugging slow queries, or optimizing database performance. Triggers on tasks involving N+1 queries, indexing, Redis caching, pagination, or database transactions.
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
---

# Laravel Database Optimization

High-performance database guidance for Laravel applications covering query shape, indexing, Eloquent hot paths, Redis caching, large datasets, locking, production migrations, profiling, and naming conventions.

## When to Apply

Reference these guidelines when:
- Writing Eloquent queries or using the query builder
- Diagnosing and fixing N+1 query problems
- Adding or reviewing database indexes
- Implementing Redis caching and invalidation
- Paginating or streaming large datasets
- Designing concurrency-safe database transactions
- Creating production migrations for large tables
- Debugging slow queries and query plans

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Query Performance & N+1 | CRITICAL | `query-` |
| 2 | Indexing Strategies | CRITICAL | `index-` |
| 3 | Eloquent Optimization | HIGH | `eloquent-` |
| 4 | Caching with Redis | HIGH | `cache-` |
| 5 | Pagination & Large Datasets | HIGH | `data-` |
| 6 | Transactions & Locking | HIGH | `lock-` |
| 7 | Migrations | HIGH | `migrate-` |
| 8 | Query Debugging | MEDIUM | `debug-` |
| 9 | Naming Conventions | HIGH | `naming-` |

## Quick Reference

### Query Performance & N+1 (CRITICAL)
- [query-n-plus-one.md](rules/query-n-plus-one.md) - Eliminate N+1 queries, prevent accidental lazy loading where appropriate, and select only required data.

### Indexing Strategies (CRITICAL)
- [index-strategies.md](rules/index-strategies.md) - Design indexes around real query shapes, foreign keys, ordering, and selective access patterns.

### Eloquent Optimization (HIGH)
- [eloquent-subqueries.md](rules/eloquent-subqueries.md) - Reduce hydration/query overhead with aggregates, subqueries, `whereExists()`, and lower-level query paths where evidence justifies them.

### Caching with Redis (HIGH)
- [cache-redis-patterns.md](rules/cache-redis-patterns.md) - Cache expensive reads with explicit TTL/invalidation ownership instead of accidental stale data.

### Pagination & Large Datasets (HIGH)
- [data-chunking-pagination.md](rules/data-chunking-pagination.md) - Bound memory and query work with chunking, cursors, and cursor pagination rather than unbounded loads.

### Transactions & Locking (HIGH)
- [lock-concurrency.md](rules/lock-concurrency.md) - Keep transactions short, make conflicting writes explicit, and handle deadlocks/retries deliberately.

### Migrations (HIGH)
- [migrate-zero-downtime.md](rules/migrate-zero-downtime.md) - Separate schema change and backfill concerns and choose migration operations that respect production locking constraints.

### Query Debugging (MEDIUM)
- [debug-query-profiling.md](rules/debug-query-profiling.md) - Use query plans and measured slow-query evidence instead of guessing at bottlenecks.

### Naming Conventions (HIGH)
- [naming-conventions.md](rules/naming-conventions.md) - Follow explicit, predictable Eloquent/table/relationship naming so convention-based behavior stays visible.

## How to Use

Read only the rule files relevant to the current database problem. `README.md`, `AGENTS.md`, and `metadata.json` are supporting projections; if they disagree with this file or `rules/`, follow the canonical source and repair the projection.
