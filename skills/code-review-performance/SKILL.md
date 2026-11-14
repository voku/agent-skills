---
name: code-review-performance
description: Performance-focused review lens for identifying inefficiencies, high-cost query shapes, resource waste, and worst-case scalability issues during code review.
license: MIT
metadata:
  author: Agent Skills Team
  version: "2.0.0"
---

# Code Review Performance

Targeted performance review lens for query shape, algorithmic complexity, memory management, caching, and network I/O.

## Quick Reference

| Category | Priority | Rule File | Primary Focus |
|----------|----------|-----------|---------------|
| **Database Performance** | CRITICAL | [`perf-database-nplusone`](rules/perf-database-nplusone.md) | Eliminating N+1 queries, eager loading, index alignment, typed count queries |
| **Algorithmic Complexity** | CRITICAL | [`perf-algorithmic-collections`](rules/perf-algorithmic-collections.md) | O(1) hash maps / lookup sets over O(N^2) nested scans and linear in-array searches |
| **Memory Management** | HIGH | [`perf-memory-streaming`](rules/perf-memory-streaming.md) | Generators (`yield`), chunked iteration, constant memory streaming for files/data |
| **Caching Strategy** | HIGH | [`perf-caching-invalidation`](rules/perf-caching-invalidation.md) | Explicit TTLs, versioned cache keys, stampede / thundering-herd lock guards |
| **Network I/O & Batching** | HIGH | [`perf-network-batching`](rules/perf-network-batching.md) | Batching remote API / LDAP calls, avoiding over-fetching with narrow selects |

---

## Scope

Run this lens when cost, latency, throughput, or scalability is the dominant concern or a workflow explicitly dispatches it. Do not broaden into a generic review bundle.

Out of scope as primary concerns: type safety, security, retry hygiene without performance impact, architecture-only refactors, readability-only feedback.

## Handoff

When another concern becomes dominant, emit **at most one** focused handoff with the observed `path:line` and why that concern is dominant:

- `code-review-architecture` for ownership/layering defects causing the cost;
- `code-review-error-handling` for retries, timeout, or recovery behavior;
- `code-review-simplicity` for duplicated or over-abstracted work;
- `code-review-security` for adversarial resource exhaustion.

## Evidence Discipline

- Tie each finding to an observed cost path, query shape, allocation pattern, network call, or concurrency boundary.
- When the changed path can amplify work with input size, construct one credible worst-case input and estimate the relevant CPU/query/memory/network growth. Do not block unrelated changes merely because no synthetic worst case exists.
- Prefer removing work over adding caches or concurrency machinery when deletion solves the measured problem.
- If the claimed regression depends on unavailable runtime/query evidence, return `blocked` instead of guessing.

## Terminal Contract

```text
STATUS: findings
<path>:<line>: <CRITICAL|HIGH|MEDIUM|LOW> <problem>. <concrete fix>.
HANDOFF: <code-review-* lens> <path>:<line> <why this concern is dominant>   # optional, at most one
```

```text
STATUS: clean
```

```text
STATUS: blocked
UNKNOWN: <exact missing evidence>.
```

`STATUS` is this lens' judgment only. The caller owns merge, dedupe, precedence, approval, persistence, and workflow progression.

## Severity

- **CRITICAL**: N+1 queries in high-traffic endpoints, quadratic O(N^2) loops on unbounded collections, or memory exhaustion.
- **HIGH**: missing cache TTLs causing stale data drift, chatty remote API calls in loops, or missing database indexes on join keys.
- **MEDIUM**: over-fetching unused columns or missing chunking on moderate batch operations.
- **LOW**: minor local collection allocation efficiency.

## References

- [Pi Ensemble performance lens](https://raw.githubusercontent.com/randomm/pi-ensemble/main/skill/code-review-performance/SKILL.md)
- [High Performance MySQL](https://www.oreilly.com/library/view/high-performance-mysql/9781492080503/)
