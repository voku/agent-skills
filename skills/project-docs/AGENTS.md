# Project Documentation — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not maintain a second documentation-rule inventory, count, stack matrix, or compiled copy of examples here.

## Fast Path

1. Inspect the target repository before deciding which documentation mode applies.
2. Read `SKILL.md` for bootstrap/audit routing and load only the relevant canonical rule files.
3. For audits, classify documentation with evidence and keep the ledger explicit.
4. Treat deletion as a human-authority boundary: surface candidates and reasons first; do not silently remove documentation.
5. Validate names, links, structure, and freshness with the target repository's configured tooling where available.

## Ownership Boundary

- `SKILL.md` owns activation, operating modes, and the audit-ledger contract.
- `rules/` owns detailed structure, baseline, quality, cleanup, and lifecycle guidance.
- the target repository owns its actual documentation layout, project stack, generated-doc tooling, conventions, and retention requirements.
- upstream documentation owns version-sensitive behavior of tools such as Markdownlint, static-site generators, or link checkers.
- this projection owns no independent documentation semantics.

## Evidence Boundary

- Inspect the repository before declaring a document stale, duplicate, generated, or obsolete.
- Do not treat age alone as proof that documentation is wrong.
- Preserve historical material when it still carries decision or operational value; archive rather than delete when appropriate.
- Do not invent missing project conventions merely to satisfy this skill.

## Projection Boundary

If this file disagrees with `SKILL.md` or a file under `rules/`, follow the canonical source and repair this projection. Current rule IDs and counts belong to the canonical surfaces, not here.
