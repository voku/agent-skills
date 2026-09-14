---
name: laravel-queues
description: Laravel queue and job patterns for driver choice, job idempotency, retry/failure handling, worker scaling, Bus batching/chaining, Horizon, and testing. Triggers on "Laravel queue", "Laravel job", "background job", "Horizon setup", "failed jobs", "Bus batch", "queue worker tuning".
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
---

# Laravel Queues & Jobs

Production-grade queue and background job patterns for Laravel applications using database/Redis-backed queues and optional Horizon.

## When to Apply

Reference these guidelines when:
- Designing background jobs (`php artisan make:job`)
- Configuring `config/queue.php` and commit/dispatch behavior
- Handling job retries, backoff, and terminal failure hooks
- Configuring worker processes via Supervisor, systemd, or Horizon
- Executing parallel work via `Bus::batch()` or sequential work via `Bus::chain()`
- Writing tests with `Queue::fake()` or `Bus::fake()`

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Driver & Config | CRITICAL | `config-` |
| 2 | Job Design | CRITICAL | `design-` |
| 3 | Retry & Failure | HIGH | `retry-` |
| 4 | Scaling & Workers | HIGH | `scaling-` |
| 5 | Batching & Chaining | HIGH | `bus-` |
| 6 | Testing & Operations | MEDIUM | `ops-` |

## Quick Reference

### Driver & Config
- [config-drivers-commits.md](rules/config-drivers-commits.md) - Choose the queue driver deliberately, make dispatch/transaction behavior explicit, and keep failed-job evidence durable.

### Job Design
- [design-job-idempotency.md](rules/design-job-idempotency.md) - Use explicit queued-job contracts, keep constructors safe to serialize, and make retried work idempotent.

### Retry & Failure
- [retry-failure-handling.md](rules/retry-failure-handling.md) - Configure explicit attempts/backoff/timeout behavior and distinguish transient retry from terminal failure.

### Scaling & Workers
- [scaling-worker-management.md](rules/scaling-worker-management.md) - Configure queue priorities and worker lifecycles so process supervision matches job timeout and memory behavior.

### Batching & Chaining
- [bus-batching-chaining.md](rules/bus-batching-chaining.md) - Use batching for independent parallel work and chaining for ordered failure-coupled work.

### Testing & Operations
- [ops-testing-monitoring.md](rules/ops-testing-monitoring.md) - Fake queues/buses in tests and keep production queue throughput, failures, and overlap behavior observable.

## How to Use

Read only the rule files relevant to the current task. Ground driver capabilities, Laravel APIs, worker flags, and Horizon behavior in the target repository and supported framework version. `README.md`, `AGENTS.md`, and `metadata.json` are supporting projections; if they disagree with this file or `rules/`, follow the canonical source and repair the projection.
