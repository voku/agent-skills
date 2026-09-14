# Code Review Error Handling — Agent Projection

**Version:** 2.0.0  
**Rules:** 5 consolidated rules  
**License:** MIT

This file is a compact projection for agents. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add independent resilience-review semantics here.

## Fast Path

1. Use this lens only when resilience or failure behavior is the dominant concern.
2. Read `SKILL.md` first.
3. Load only the rule files relevant to the fallible operation or failure path.
4. Trace what is logged, retried, persisted, returned, and cleaned up before proposing recovery behavior.
5. If another concern becomes dominant, hand off to at most one focused review lens.

## Rule Index

| Rule | Priority | Focus |
|------|----------|-------|
| [`err-signalling-hygiene`](rules/err-signalling-hygiene.md) | CRITICAL | Typed signalling, cause chaining, no swallowed errors |
| [`err-outcome-batch-discipline`](rules/err-outcome-batch-discipline.md) | HIGH | Exact branch outcomes and aggregate batch status |
| [`err-timeouts-cancellation`](rules/err-timeouts-cancellation.md) | CRITICAL | Explicit timeouts, bounded waits, cancellation propagation |
| [`err-retry-idempotency`](rules/err-retry-idempotency.md) | HIGH | Retryability, idempotency, backoff, jitter |
| [`err-cleanup-observability`](rules/err-cleanup-observability.md) | HIGH | Cleanup, audit ordering, contextual observability |

## Evidence Boundary

- Test timeout/transient/permanent/eventual-success behavior only when the changed path actually contains a fallible external operation.
- Prefer one clear failure contract over defensive layers that merely hide uncertainty.
- If required failure-path evidence cannot be inspected, report `blocked` rather than guessing.

## Terminal Contract

Follow the exact `STATUS: findings|clean|blocked` contract in `SKILL.md`. The caller owns merge, dedupe, approval, persistence, and workflow progression.
