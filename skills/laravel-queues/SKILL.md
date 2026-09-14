---
name: laravel-queues
description: Laravel queue and job patterns — driver choice, job design (idempotency, ShouldQueue, model serialisation), retry and failure handling, worker scaling, Bus batching and chaining, Horizon, and testing. 6 rules across 6 categories. Triggers on "Laravel queue", "Laravel job", "background job", "Horizon setup", "failed jobs", "Bus batch", "queue worker tuning".
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
---

# Laravel Queues & Jobs

Production-grade queue and background job patterns for Laravel applications (MySQL + Redis). Contains **6 consolidated rules across 6 categories** covering driver configuration, job idempotency, retry/failure lifecycle, worker scaling, Bus batching/chaining, and testing/monitoring.

## Metadata

- **Version:** 2.0.0
- **Scope:** PHP / Laravel 11.x - 13.x + MySQL + Redis (optional Horizon)
- **Rule Count:** 6 rules across 6 categories
- **License:** MIT

## When to Apply

Reference these guidelines when:
- Designing background jobs (`php artisan make:job`)
- Configuring `config/queue.php` and `after_commit` settings
- Handling job retries, backoff, and terminal `failed()` hooks
- Configuring worker processes via Supervisor, systemd, or Horizon
- Executing parallel jobs via `Bus::batch()` or sequential `Bus::chain()`
- Writing unit and feature tests with `Queue::fake()` or `Bus::fake()`

## Rule Categories by Priority

| Priority | Category | Impact | Prefix | Rules |
|----------|----------|--------|--------|-------|
| 1 | Driver & Config | CRITICAL | `config-` | 1 |
| 2 | Job Design | CRITICAL | `design-` | 1 |
| 3 | Retry & Failure | HIGH | `retry-` | 1 |
| 4 | Scaling & Workers | HIGH | `scaling-` | 1 |
| 5 | Batching & Chaining | HIGH | `bus-` | 1 |
| 6 | Testing & Operations | MEDIUM | `ops-` | 1 |

## Quick Reference

### 1. Driver & Config (CRITICAL) — 1 rule
- [config-drivers-commits.md](rules/config-drivers-commits.md) - Set `after_commit => true` across queue connections to eliminate race conditions with uncommitted database rows, use Redis for high-throughput production, and ensure persistent failed job storage.

### 2. Job Design (CRITICAL) — 1 rule
- [design-job-idempotency.md](rules/design-job-idempotency.md) - Always implement `ShouldQueue`, keep constructors pure (pass IDs rather than stale models), and guarantee idempotency using atomic state checks or `ShouldBeUnique`.

### 3. Retry & Failure (HIGH) — 1 rule
- [retry-failure-handling.md](rules/retry-failure-handling.md) - Configure explicit `$tries` and exponential `$backoff`, use `#[FailOnTimeout]` to prevent hung jobs from exhausting attempts, implement `failed(Throwable $e)` for terminal recovery, and distinguish transient network retries from permanent data errors.

### 4. Scaling & Workers (HIGH) — 1 rule
- [scaling-worker-management.md](rules/scaling-worker-management.md) - Configure multi-queue priority lanes (`--queue=high,default,low`), ensure supervisor `stopwaitsecs` exceeds worker `timeout`, and recycle processes (`--max-jobs=1000 --max-time=3600`) to prevent PHP memory exhaustion.

### 5. Batching & Chaining (HIGH) — 1 rule
- [bus-batching-chaining.md](rules/bus-batching-chaining.md) - Choose parallel `Bus::batch()` for independent progress-tracked jobs, `Bus::chain()` for strict sequential steps where failure aborts subsequent tasks, and dispatch large sets in chunked sub-batches.

### 6. Testing & Operations (MEDIUM) — 1 rule
- [ops-testing-monitoring.md](rules/ops-testing-monitoring.md) - Fake queues in tests (`Queue::fake()`, `Bus::fake()`), prevent overlapping scheduled jobs with `withoutOverlapping()`, and monitor throughput and queue wait times with Laravel Horizon.

## How to Use

Read individual rule files in `rules/` for concise triggers, Bad vs Good code comparisons, and concrete queue recipes.
