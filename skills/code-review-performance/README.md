# Code Review Performance

Targeted performance review lens for query shape, algorithmic complexity, memory management, caching, and network I/O.

## Canonical source

`SKILL.md` and `rules/` are the canonical contract for this skill. This README is a summary projection and must not introduce an independent rule inventory.

## Consolidated rules

| Rule | Priority | Primary focus |
|------|----------|---------------|
| `perf-database-nplusone` | CRITICAL | N+1 queries, eager loading, index/query shape |
| `perf-algorithmic-collections` | CRITICAL | Collection lookup shape and asymptotic cost |
| `perf-memory-streaming` | HIGH | Streaming, chunking, bounded memory |
| `perf-caching-invalidation` | HIGH | TTLs, cache-key versioning, stampede protection |
| `perf-network-batching` | HIGH | Remote-call batching and over-fetching |

## Usage

Use this lens when cost, latency, throughput, or scalability is the dominant review concern. Keep it focused and hand off when security, architecture, resilience, type safety, or simplicity becomes the primary issue.

## References

- [Pi Ensemble performance lens](https://raw.githubusercontent.com/randomm/pi-ensemble/main/skill/code-review-performance/SKILL.md)
- [High Performance MySQL](https://www.oreilly.com/library/view/high-performance-mysql/9781492080503/)
