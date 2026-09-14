# Code Slop Detection

Qualitative code-review guidance for low-signal comments, weak naming, unnecessary abstraction, defensive noise, inauthentic tests, and style escape hatches in PHP/Laravel and TypeScript/React codebases.

## Canonical Source

`SKILL.md` defines activation, evidence boundaries, stack grounding, and review-output semantics. The files under `rules/` contain the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, count, authorship heuristic catalog, or compiled example set.

## When to Use

Use this skill for AI-assisted PR review, maintainability/taste audits, boilerplate cleanup, and review-checklist hardening.

## Routing

1. Inspect the target repository and the actual changed code.
2. Read `SKILL.md` first.
3. Load only the relevant rule files for comments, naming, over-engineering, defensive balance, test authenticity, or style fingerprints.
4. Tie every finding to observable code and repository context.
5. Treat the heuristics as code-quality signals, not proof that a human or an LLM authored the code.

## Relationship to `technical-debt`

`technical-debt` focuses on more quantitative or mechanically observable debt. `code-slop` focuses on qualitative comprehension and maintainability costs that may survive ordinary linting and tests.

## Projection Boundary

Do not copy current rule IDs, counts, framework-version tables, or long worked examples into this file. If this projection disagrees with `SKILL.md` or `rules/`, follow the canonical source and repair the projection.
