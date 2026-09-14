# Code Review Error Handling

Targeted resilience review lens for signalling, propagation, timeouts, retries, cleanup, and observable failure behavior.

## Canonical source

`SKILL.md` and `rules/` are the canonical contract for this skill. This README is a summary projection and must not introduce an independent rule inventory.

## Consolidated rules

| Rule | Priority | Primary focus |
|------|----------|---------------|
| `err-signalling-hygiene` | CRITICAL | Typed signalling, cause chaining, no swallowed errors |
| `err-outcome-batch-discipline` | HIGH | Exact branch outcomes and aggregate batch status |
| `err-timeouts-cancellation` | CRITICAL | Explicit timeouts, bounded waits, cancellation propagation |
| `err-retry-idempotency` | HIGH | Retryability, idempotency, backoff, jitter |
| `err-cleanup-observability` | HIGH | Cleanup, audit ordering, contextual observability |

## Usage

Use this lens when resilience or failure behavior is the dominant review concern. Keep it focused and hand off when security, performance, architecture, type safety, or simplicity becomes primary.

## References

- [Pi Ensemble error-handling lens](https://raw.githubusercontent.com/randomm/pi-ensemble/main/skill/code-review-error-handling/SKILL.md)
- [Release It! patterns](https://pragprog.com/titles/mnee2/release-it-second-edition/)
