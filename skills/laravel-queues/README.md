# Laravel Queues & Jobs

Portable guidance for production Laravel queue and background-job work.

## Canonical Source

`SKILL.md` defines when this skill applies and the high-level routing contract. `rules/` contains the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, count, framework-version table, worker cookbook, or compiled set of examples.

## When to Use

Use this skill for work involving queue-driver configuration, queued job design and idempotency, retries/failures, worker scaling, Bus batching/chaining, Horizon, or queue testing/operations.

## Routing

1. Ground the target repository's Laravel version, queue connection, persistence backend, worker/supervisor configuration, and monitoring.
2. Read `SKILL.md` to select the canonical rules matching the observed problem.
3. Load only those rule files instead of compiling the whole queue guide into context.
4. Preserve application transaction boundaries, failure semantics, and operational constraints unless evidence supports changing them.
5. Validate through the target repository's configured toolchain and report only observed results.

## Stable Boundaries

- Queued work must make retry/idempotency behavior explicit.
- Transaction dispatch, attempts, backoff, timeouts, worker flags, and failed-job retention are runtime contracts, not style preferences.
- Batch and chain semantics differ and should match the dependency/failure model of the work.
- Production worker and Horizon changes require target-environment evidence.

## Projection Boundary

Do not copy current rule IDs, counts, version tables, or operational recipes into this file. If this projection disagrees with `SKILL.md` or a file under `rules/`, follow the canonical source and repair the projection.
