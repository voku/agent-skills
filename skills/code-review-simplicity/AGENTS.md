# Code Review Simplicity — Agent Projection

**Version:** 2.0.0  
**Rules:** 5 consolidated rules  
**License:** MIT

This file is a compact projection for agents. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add independent review semantics here.

## Fast Path

1. Use this lens only when simplicity or maintainability is the dominant concern.
2. Read `SKILL.md` first.
3. Load only the rule files relevant to the changed behavior.
4. Tie findings to source and callers; do not infer dead code or broken bounds from a diff alone.
5. If another concern becomes dominant, hand off to at most one focused review lens.

## Rule Index

| Rule | Priority | Focus |
|------|----------|-------|
| [`simp-premature-abstraction`](rules/simp-premature-abstraction.md) | HIGH | Single-use abstractions and speculative indirection |
| [`simp-shallow-control-flow`](rules/simp-shallow-control-flow.md) | HIGH | Guard clauses, nesting, boolean control flow |
| [`simp-bounds-range-clarity`](rules/simp-bounds-range-clarity.md) | CRITICAL | Collapsed bounds, dead ranges, tautological comparisons |
| [`simp-intention-revealing-naming`](rules/simp-intention-revealing-naming.md) | MEDIUM | Domain naming and noise reduction |
| [`simp-dead-code-elimination`](rules/simp-dead-code-elimination.md) | HIGH | Unused code and asymmetric sibling branches |

## Evidence Boundary

- Prefer a local deletion or simplification over a new abstraction without a demonstrated second use.
- Enumerate relevant boundary cases only when bounds, clamps, floors, caps, or range transformations changed.
- If removal safety depends on unavailable callers or behavior, report `blocked` rather than guessing.
- Do not invent a mandatory bound-range exercise for unrelated changes.

## Terminal Contract

Follow the exact `STATUS: findings|clean|blocked` contract in `SKILL.md`. The caller owns merge, dedupe, approval, persistence, and workflow progression.
