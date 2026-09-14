# Laravel Database Optimization

Portable guidance for evidence-backed Laravel database performance work across queries, indexes, Eloquent hot paths, caching, large datasets, locking, migrations, profiling, and naming.

## Canonical Source

`SKILL.md` defines when this skill applies and the high-level routing contract. `rules/` contains the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, category count, framework-version table, benchmark catalog, or compiled examples.

## When to Use

Use this skill when database behavior is the dominant concern: N+1 queries, query plans, indexes, cache invalidation, pagination/streaming, transaction contention, production migrations, or slow-query diagnosis.

For broader Laravel application structure, controllers, requests, resources, or model-write boundaries, prefer `laravel-best-practices`.

## Routing

1. Ground the target database, schema, Laravel/PHP versions, and real query/workload evidence.
2. Read `SKILL.md` to select the canonical rules matching the observed problem.
3. Load only those rules instead of compiling the entire optimization catalog into context.
4. Preserve target-database and production constraints rather than importing assumptions from generic examples.
5. Validate through the repository/database tooling and report only observed results.

## Stable Boundaries

- Measure before claiming an optimization improved cost or latency.
- Design indexes from real query shapes and selectivity, not from column popularity.
- Keep transactions bounded and make conflicting-write semantics explicit.
- Treat cache invalidation as part of the data contract, not an afterthought.
- Separate production schema changes from potentially long-running data backfills when needed.
- Use query-plan evidence to distinguish database work from application-level speculation.

## Projection Boundary

Do not copy current rule IDs, counts, category totals, framework-version tables, or expanded examples into this file. If this projection disagrees with `SKILL.md` or a file under `rules/`, preserve the mismatch as evidence and follow the canonical source.

## References

- [Laravel Eloquent](https://laravel.com/docs/13.x/eloquent)
- [Laravel Queries](https://laravel.com/docs/13.x/queries)
- [Laravel Cache](https://laravel.com/docs/13.x/cache)
- [Laravel Pagination](https://laravel.com/docs/13.x/pagination)
- [Laravel Migrations](https://laravel.com/docs/13.x/migrations)
