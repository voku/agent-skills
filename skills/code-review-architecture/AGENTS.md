# Code Review Architecture — Agent Projection

**Version:** 2.0.0  
**Rules:** 5 consolidated rules  
**License:** MIT

This file is a compact projection for agents. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add independent architecture-review semantics here.

## Fast Path

1. Use this lens only when architecture is the dominant concern.
2. Read `SKILL.md` first.
3. Load only rule files relevant to the observed boundary or ownership defect.
4. Tie findings to real source, callers, transaction boundaries, and lifecycle hooks.
5. Hand off to at most one focused review lens when another concern becomes dominant.

## Rule Index

| Rule | Priority | Focus |
|------|----------|-------|
| [`arch-transaction-side-effects`](rules/arch-transaction-side-effects.md) | CRITICAL | External side effects outside DB transactions |
| [`arch-separation-domain-presentation`](rules/arch-separation-domain-presentation.md) | CRITICAL | Domain/presentation separation |
| [`arch-coupling-cohesion`](rules/arch-coupling-cohesion.md) | HIGH | Dependency direction and cohesive ownership |
| [`arch-unidirectional-data-flow`](rules/arch-unidirectional-data-flow.md) | HIGH | Explicit data flow and immutable transfer objects |
| [`arch-contract-rigor-extensibility`](rules/arch-contract-rigor-extensibility.md) | MEDIUM | Narrow contracts and composition |

## Evidence Boundary

- Inspect transaction entry points, persisted types, and relevant hooks when persistence boundaries changed.
- Prefer direct ownership and deletion over a new abstraction when both solve the verified defect.
- If cross-file evidence required to prove the defect is unavailable, report `blocked` rather than guessing.

## Terminal Contract

Follow the exact `STATUS: findings|clean|blocked` contract in `SKILL.md`. The caller owns merge, dedupe, approval, persistence, and workflow progression.
