# Laravel Database Optimization — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add an independent database rule inventory, version table, benchmark catalog, or compiled copy of rule examples here.

## Fast Path

1. Ground the target database, Laravel/PHP versions, schema, query shape, and observed performance evidence before recommending optimization.
2. Read `SKILL.md` first and load only the canonical rule files relevant to the verified problem.
3. Keep query shape, indexing, Eloquent hot paths, caching, large-dataset iteration, locking, migrations, profiling, and naming in their owning rule boundaries.
4. Prefer measured query plans, timings, row counts, lock behavior, and production constraints over folklore optimizations.
5. Validate with the target repository/database tooling and report only observed results.

## Ownership Boundary

- `SKILL.md` owns activation and high-level routing.
- `rules/` owns detailed database optimization guidance and examples.
- the target repository owns schema, supported database/version, query workload, cache topology, migration constraints, and validation commands.
- database/Laravel upstream documentation owns version-sensitive behavior.
- this projection owns no independent optimization semantics.

## Evidence Boundary

- Do not claim an index or query rewrite is faster without evidence appropriate to the target database/workload.
- Treat N+1, unbounded loads, lock scope, migration locking, and stale cache behavior as concrete contracts to inspect, not style preferences.
- Keep production migration/backfill plans explicit and reversible where the platform allows it.
- Route general Laravel application-architecture concerns back to `laravel-best-practices` when database behavior is no longer the dominant issue.

## Projection Boundary

Do not copy current canonical rule IDs, counts, category totals, framework-version tables, or expanded examples into this file. If this projection disagrees with `SKILL.md` or a rule file, preserve the mismatch as evidence and follow the canonical source.
