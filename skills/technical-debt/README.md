# Technical Debt

Portable guidance for technical-debt discovery, evidence, prioritization, and remediation planning across PHP/Laravel/MySQL and Node/TypeScript/React projects.

## Canonical Source

`SKILL.md` defines activation, audit scope, result semantics, and the ranked debt-ledger contract. The files under `rules/` contain the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, count, tooling matrix, or compiled detection checklist.

## When to Use

Use this skill to audit technical debt, build a prioritized debt ledger, compare remediation candidates, or investigate code, security, design, dependency, test, performance, data, documentation, infrastructure, or process debt.

## Routing

1. Ground the requested scope and inspect the target repository's stack and configured tooling.
2. Read `SKILL.md` first.
3. Load only the canonical rules relevant to the observed debt candidates.
4. Prefer measured repository/tool evidence over generic thresholds or architecture preferences.
5. Record location/evidence, effort, impact, and remediation priority without conflating discovery with an immediate change mandate.

## Projection Boundary

Do not copy current rule IDs, counts, command catalogs, or long worked examples into this file. If this projection disagrees with `SKILL.md` or `rules/`, follow the canonical source and repair the projection.
