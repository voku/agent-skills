---
name: code-review-simplicity
description: Simplicity-focused review lens for identifying unnecessary complexity, dead logic, unclear naming, duplicated behavior, and maintainability drag during code review.
license: MIT
metadata:
  author: Agent Skills Team
  version: "2.0.0"
---

# Code Review Simplicity

Targeted simplicity review lens for readability, cognitive load, premature abstraction, dead logic, and bounds clarity.

## Quick Reference

| Category | Priority | Rule File | Primary Focus |
|----------|----------|-----------|---------------|
| **Premature Abstraction** | HIGH | [`simp-premature-abstraction`](rules/simp-premature-abstraction.md) | Single-use interfaces, speculative factories, avoiding bespoke wrappers purely for mocking |
| **Control Flow** | HIGH | [`simp-shallow-control-flow`](rules/simp-shallow-control-flow.md) | Guard clauses over nested arrow if/else pyramids, avoiding boolean flag parameters |
| **Bounds & Range** | CRITICAL | [`simp-bounds-range-clarity`](rules/simp-bounds-range-clarity.md) | Collapsed clamp bounds, dead range conditions, tautological comparisons |
| **Naming & Clarity** | MEDIUM | [`simp-intention-revealing-naming`](rules/simp-intention-revealing-naming.md) | Domain verbs and nouns, affirmative booleans, eliminating noisy comments |
| **Dead Code & Symmetry** | HIGH | [`simp-dead-code-elimination`](rules/simp-dead-code-elimination.md) | Deleting unused methods/parameters and commented code, symmetric branch rigor |

---

## Scope

Run this lens when complexity or maintainability is the dominant concern or a workflow explicitly dispatches it. Do not broaden into a generic review bundle.

Out of scope as primary concerns: security, retry semantics, performance-only bottlenecks, architecture/type defects that merely happen to look complex.

Do not call required validation, contextual exceptions, security checks, or focused regression tests "bloat".

## Handoff

When another concern becomes dominant, emit **at most one** focused handoff with the observed `path:line` and why that concern is dominant:

- `code-review-architecture` for structural ownership/abstraction defects;
- `code-review-performance` for duplicated expensive work;
- `code-review-type-safety` for dishonest constraints or dead typed branches;
- `code-review-error-handling` for hidden failure paths or cleanup.

## Evidence Discipline

- Tie each finding to real source and callers; do not infer dead code from the diff alone.
- Rank by maintenance surface removed, not cleverness.
- When constants, clamps, floors, caps, or range transformations changed, enumerate the relevant boundary cases and check for collapsed/dead ranges. Otherwise do **not** manufacture a bound-range exercise.
- Prefer a local deletion/simplification over a new helper, interface, manager, strategy, or configuration point with no demonstrated second use.
- If removal safety depends on unavailable callers or behavior, return `blocked` instead of guessing.

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

- **CRITICAL**: collapsed bounds, dead ranges causing inverted behavior, or broken logic masking severe bugs.
- **HIGH**: high-cyclomatic arrow nesting, single-implementation abstraction sprawl, or dead methods.
- **MEDIUM**: misleading names, redundant noise comments, or asymmetric branch handling.
- **LOW**: minor local readability or formatting improvements.

## References

- [Pi Ensemble simplicity lens](https://raw.githubusercontent.com/randomm/pi-ensemble/main/skill/code-review-simplicity/SKILL.md)
- [A Philosophy of Software Design](https://www.goodreads.com/book/show/39996759-a-philosophy-of-software-design)
