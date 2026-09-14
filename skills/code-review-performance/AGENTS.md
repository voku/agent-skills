# Code Review Performance — Agent Projection

**Version:** 2.0.0  
**Rules:** 5 consolidated rules  
**License:** MIT

This file is a compact projection for agents. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add independent performance-review semantics here.

## Fast Path

1. Use this lens only when cost, latency, throughput, or scalability is the dominant concern.
2. Read `SKILL.md` first.
3. Load only the rule files relevant to the observed cost path.
4. Tie findings to real query, CPU, memory, network, or concurrency evidence.
5. If another concern becomes dominant, hand off to at most one focused review lens.

## Rule Index

| Rule | Priority | Focus |
|------|----------|-------|
| [`perf-database-nplusone`](rules/perf-database-nplusone.md) | CRITICAL | N+1 queries, eager loading, index/query shape |
| [`perf-algorithmic-collections`](rules/perf-algorithmic-collections.md) | CRITICAL | Collection lookup shape and asymptotic cost |
| [`perf-memory-streaming`](rules/perf-memory-streaming.md) | HIGH | Streaming, chunking, bounded memory |
| [`perf-caching-invalidation`](rules/perf-caching-invalidation.md) | HIGH | TTLs, key versioning, stampede protection |
| [`perf-network-batching`](rules/perf-network-batching.md) | HIGH | Remote-call batching and over-fetching |

## Evidence Boundary

- Construct a worst-case input only when changed behavior can amplify work with input size.
- Prefer removing unnecessary work before adding caches or concurrency machinery.
- If a claimed regression depends on unavailable runtime/query evidence, report `blocked` rather than guessing.

## Terminal Contract

Follow the exact `STATUS: findings|clean|blocked` contract in `SKILL.md`. The caller owns merge, dedupe, approval, persistence, and workflow progression.
