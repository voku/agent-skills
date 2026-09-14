# Laravel Queues & Jobs — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add an independent queue rule inventory, version table, worker cookbook, or compiled copy of rule examples here.

## Fast Path

1. Ground the target repository's Laravel version, configured queue connection, persistence backend, worker supervisor, and monitoring before recommending queue behavior.
2. Read `SKILL.md` first and load only the canonical rule files relevant to the current task.
3. Keep driver/commit behavior, job idempotency, retry/failure lifecycle, worker scaling, Bus orchestration, and testing/operations in their owning rule boundaries.
4. Treat retries, timeouts, uniqueness, transaction dispatch, and worker flags as runtime contracts that require target-repository evidence.
5. Validate with the target repository's configured tests and operational tooling; report only observed results.

## Ownership Boundary

- `SKILL.md` owns activation and high-level routing.
- `rules/` owns detailed queue/job guidance and examples.
- the target repository owns installed Laravel version, queue driver configuration, job classes, worker/supervisor configuration, Horizon usage, persistence, and validation commands.
- Laravel/driver upstream documentation owns version-sensitive runtime behavior.
- this projection owns no independent queue semantics.

## Evidence Boundary

- Verify `ShouldQueue`, idempotency, serialized inputs, attempts/backoff/timeout, and failure hooks in real job classes before making claims.
- Verify transaction/dispatch settings in `config/queue.php` rather than assuming defaults.
- Verify supervisor/Horizon worker flags before recommending scaling changes.
- Do not claim throughput or latency improvements without workload evidence.
- Keep failed-job evidence and terminal failure behavior observable.

## Projection Boundary

If this file disagrees with `SKILL.md` or a file under `rules/`, follow the canonical source and repair this projection. Current rule IDs, counts, framework-version tables, and operational recipes do not belong here.
