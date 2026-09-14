# Code Review Type Safety — Agent Projection

**Version:** 2.0.0  
**Rules:** 4 consolidated rules  
**License:** MIT

This file is a compact projection for agents. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add independent type-safety review semantics here.

## Fast Path

1. Use this lens only when typing or contract honesty is the dominant concern.
2. Read `SKILL.md` first.
3. Load only rule files relevant to the producer/consumer or trust-boundary contract.
4. Compare declared types with actual producers, consumers, runtime validation, and nullability.
5. Hand off to at most one focused review lens when another concern becomes dominant.

## Rule Index

| Rule | Priority | Focus |
|------|----------|-------|
| [`type-strict-native-declarations`](rules/type-strict-native-declarations.md) | CRITICAL | Native declarations and strict comparison |
| [`type-shape-validation-boundaries`](rules/type-shape-validation-boundaries.md) | CRITICAL | DTO/shape validation at trust boundaries |
| [`type-symmetric-rigor`](rules/type-symmetric-rigor.md) | HIGH | Symmetric contracts across sibling paths |
| [`type-nullability-truthfulness`](rules/type-nullability-truthfulness.md) | HIGH | Honest nullable contracts |

## Evidence Boundary

- Trace one relevant unexpected value only when external input, coercion, nullability, or shape constraints changed.
- Prefer narrow explicit domain types over `mixed`, unchecked casts, or speculative generic machinery.
- If required producer/consumer evidence cannot be inspected, report `blocked` rather than guessing.

## Terminal Contract

Follow the exact `STATUS: findings|clean|blocked` contract in `SKILL.md`. The caller owns merge, dedupe, approval, persistence, and workflow progression.
