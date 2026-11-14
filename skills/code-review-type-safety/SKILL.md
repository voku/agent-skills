---
name: code-review-type-safety
description: Type-safety review lens for catching schema mismatches, unsafe coercions, missing annotations, and weak contracts during code review.
license: MIT
metadata:
  author: Agent Skills Team
  version: "2.0.0"
---

# Code Review Type Safety

Targeted type-safety review lens for honest contracts, native types, shape validation, symmetric rigor, and truthful nullability.

## Quick Reference

| Category | Priority | Rule File | Primary Focus |
|----------|----------|-----------|---------------|
| **Native Declarations** | CRITICAL | [`type-strict-native-declarations`](rules/type-strict-native-declarations.md) | Native property types, strict comparisons (`===`), eliminating false-folded returns |
| **Shape Validation** | CRITICAL | [`type-shape-validation-boundaries`](rules/type-shape-validation-boundaries.md) | Typed DTOs over loose arrays at trust boundaries, shape validation |
| **Symmetric Rigor** | HIGH | [`type-symmetric-rigor`](rules/type-symmetric-rigor.md) | Symmetric type contracts across branches, consistent normalization |
| **Honest Nullability** | HIGH | [`type-nullability-truthfulness`](rules/type-nullability-truthfulness.md) | Truthful nullable returns (`?Type`), avoiding false non-null assertions |

---

## Scope

Run this lens when typing/contracts are the dominant concern or a workflow explicitly dispatches it. Do not broaden into a generic review bundle.

Out of scope as primary concerns: security vulnerabilities, retry/timeout behavior, performance-only questions, architecture/readability concerns without a type-contract defect.

## Handoff

When another concern becomes dominant, emit **at most one** focused handoff with the observed `path:line` and why that concern is dominant:

- `code-review-security` for untyped external input at a trust boundary;
- `code-review-architecture` for a leaky or wrongly owned contract;
- `code-review-simplicity` for needless generic machinery or dead constraints;
- `code-review-error-handling` for dishonest failure/result types.

## Evidence Discipline

- Compare declared types with actual producers, consumers, and runtime validation.
- When the diff changes external/untyped input, nullability, coercion, or shape constraints, construct one relevant unexpected value and trace both static proof and runtime behavior. Do not manufacture adversarial typing exercises for unrelated code.
- Prefer explicit domain types and narrow unions/shapes over `mixed`, unchecked casts, or speculative generics.
- If the claimed contract defect depends on unavailable producer/consumer evidence, return `blocked` instead of guessing.

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

- **CRITICAL**: loose equality comparisons causing security/data drift, untyped active-row properties, or runtime TypeErrors on valid input.
- **HIGH**: unvalidated arrays across trust boundaries or asymmetric return types causing caller branching bugs.
- **MEDIUM**: missing PHPDoc array shape annotations or unnecessary mixed parameters.
- **LOW**: minor annotation formatting or redundant docblocks.

## References

- [Pi Ensemble type-safety lens](https://raw.githubusercontent.com/randomm/pi-ensemble/main/skill/code-review-type-safety/SKILL.md)
- [PHPStan Documentation](https://phpstan.org/user-guide/getting-started)
