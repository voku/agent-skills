---
name: code-review-architecture
description: Architecture-focused review lens for assessing coupling, module boundaries, abstraction quality, and rollback-safe design during code review. Use when reviewing design quality, separation of concerns, transaction boundaries, or structural maintainability.
license: MIT
metadata:
  author: Agent Skills Team
  version: "2.0.0"
---

# Code Review Architecture

Targeted architecture review lens for design quality, coupling, cohesion, boundaries, and rollback-safe side effects.

## Quick Reference

| Category | Priority | Rule File | Primary Focus |
|----------|----------|-----------|---------------|
| **Transactions & Rollback** | CRITICAL | [`arch-transaction-side-effects`](rules/arch-transaction-side-effects.md) | External side effects strictly outside DB transactions, outbox pattern |
| **Separation of Concerns** | CRITICAL | [`arch-separation-domain-presentation`](rules/arch-separation-domain-presentation.md) | Thin controllers, pure presentation templates, encapsulated domain logic |
| **Coupling & Cohesion** | HIGH | [`arch-coupling-cohesion`](rules/arch-coupling-cohesion.md) | Dependency inversion, avoiding direct database driver leaks in domain services |
| **Data Flow** | HIGH | [`arch-unidirectional-data-flow`](rules/arch-unidirectional-data-flow.md) | Unidirectional flow, immutable DTOs, eliminating ambient mutable globals |
| **Contract Rigor** | MEDIUM | [`arch-contract-rigor-extensibility`](rules/arch-contract-rigor-extensibility.md) | Composition over deep inheritance trees, narrow role interfaces |

---

## Scope

Run this lens when architecture is the dominant concern or a workflow explicitly dispatches it. Do not broaden into a generic review bundle.

Out of scope as primary concerns: type coverage, security vulnerabilities, timeout/retry hygiene, micro-optimization, naming-only feedback.

## Handoff

Stay on architecture evidence. When another concern becomes dominant, emit **at most one** focused handoff with the observed `path:line` and why that concern is dominant:

- `code-review-performance` for cost/query/resource growth;
- `code-review-error-handling` for local rollback, cleanup, or partial failure;
- `code-review-security` for authz, isolation, or trust boundaries;
- `code-review-simplicity` for over-abstraction without an architectural defect.

A handoff is a recommendation, not workflow approval and not permission to run every lens.

## Evidence Discipline

- Tie each finding to real source and caller/boundary evidence.
- For transactional or bulk-persistence changes, inspect the transaction entry point, persisted types, and relevant lifecycle hooks.
- If a claimed architectural defect depends on unavailable cross-file evidence, return `blocked` instead of guessing.
- Prefer deletion and direct ownership over a new abstraction when both solve the verified problem.

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

- **CRITICAL**: external side effects in DB transaction causing unrecoverable data drift, or direct database queries in UI templates.
- **HIGH**: circular dependencies, leaky infrastructure abstractions, or god-classes mixing business and transport.
- **MEDIUM**: brittle inheritance hierarchies or excessive parameter passing lacking DTO structure.
- **LOW**: minor boundary misalignment or local interface granularity issues.

## References

- [Pi Ensemble architecture lens](https://raw.githubusercontent.com/randomm/pi-ensemble/main/skill/code-review-architecture/SKILL.md)
- [Clean Architecture (Robert C. Martin)](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
