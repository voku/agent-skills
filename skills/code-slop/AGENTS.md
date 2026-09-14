# Code Slop Detection — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not maintain a second slop-rule inventory, count, authorship heuristic catalog, or compiled example set here.

## Fast Path

1. Inspect the target repository and changed diff before applying generic review heuristics.
2. Read `SKILL.md` first and load only the relevant canonical rule files.
3. Report concrete maintainability findings such as narration, weak naming, unnecessary abstraction, swallowed failures, mock-heavy tests, or type/debug escape hatches.
4. Use the target repository's configured analyzers and tests when they can verify the concern mechanically.
5. Treat verdicts as prioritization aids, not proof of who or what authored the code.

## Ownership Boundary

- `SKILL.md` owns activation, evidence/provenance boundaries, stack grounding, and review-output semantics.
- `rules/` owns detailed qualitative review guidance and examples.
- the target repository owns its language versions, style conventions, architecture, test strategy, and validation commands.
- static analyzers, linters, and test frameworks own mechanically decidable diagnostics.
- this projection owns no independent review semantics.

## Evidence Boundary

- A style pattern is evidence about the code, not an authorship signal.
- Prefer a concrete defect or comprehension cost over statements that code "looks AI-written".
- Do not penalize code for merely being consistent, clean, or lacking human-looking imperfections.
- Escalate only findings that remain meaningful in the target repository's actual context.

## Projection Boundary

If this file disagrees with `SKILL.md` or a file under `rules/`, follow the canonical source and repair this projection. Current rule IDs and counts belong to the canonical surfaces, not here.
