# Technical Debt — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not maintain a second debt-rule inventory, count, tooling matrix, or compiled set of detection commands here.

## Fast Path

1. Ground the requested scope and inspect the target repository before classifying debt.
2. Read `SKILL.md` for the audit/output contract and load only the relevant canonical debt rules.
3. Use repository-configured analyzers, package audits, tests, database evidence, and observability before introducing generic tooling.
4. Record concrete location/evidence, effort, and impact for findings; distinguish verified debt from hypotheses that still need measurement.
5. Rank remediation by risk and leverage rather than mechanically maximizing the number of findings.

## Ownership Boundary

- `SKILL.md` owns activation, audit scope, PASS/FAIL/N/A semantics, and the ranked debt-ledger contract.
- `rules/` owns detailed code, security, design, dependency, test, performance, data, documentation, infrastructure, and process-debt guidance.
- the target repository owns its actual architecture, runtime/dependency floors, tooling, performance budgets, data constraints, and remediation priorities.
- analyzers, package managers, databases, and observability systems own their measured diagnostics.
- this projection owns no independent technical-debt semantics.

## Evidence Boundary

- Do not label code as debt solely because it differs from a generic preferred architecture.
- Treat thresholds and suggested tools as contextual guidance; prefer project evidence and configured quality gates.
- Do not claim a CVE, N+1, missing index, stale dependency, or performance regression without evidence from the relevant owner/tool.
- Separate debt discovery from the decision to remediate it now.

## Projection Boundary

If this file disagrees with `SKILL.md` or a file under `rules/`, follow the canonical source and repair this projection. Current rule IDs, counts, commands, and tool inventories belong to canonical or target-repository surfaces, not here.
