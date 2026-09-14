# Laravel Best Practices — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add an independent Laravel rule inventory, framework-version table, or compiled copy of rule examples here.

## Fast Path

1. Ground the target project's Laravel/PHP versions and existing architecture from repository evidence.
2. Read `SKILL.md` first and load only the canonical rule files relevant to the verified task.
3. Keep architecture, Eloquent, controllers/resources, validation, and security concerns in their owning rule boundaries.
4. Prefer the target repository's established actions/services, requests, resources, model conventions, queues, and authorization patterns over invented alternatives.
5. Validate with the repository's configured tests/static analysis/style tools and report only observed results.

## Ownership Boundary

- `SKILL.md` owns activation and high-level routing.
- `rules/` owns detailed Laravel guidance and examples.
- the target repository owns its supported versions, local architecture, persistence conventions, and validation commands.
- Laravel upstream documentation owns version-sensitive framework behavior.
- this projection owns no independent Laravel semantics.

## Evidence Boundary

- Inspect real controllers, requests, resources, models, queries, events/jobs, and authorization boundaries before proposing a pattern change.
- Do not infer framework features from generic examples; verify they exist in the project's supported Laravel/PHP versions.
- Prefer explicit typed boundaries and observable failures over magic or silent behavior.
- Keep performance/database-specialist work with the focused owner when it exceeds this skill's application-level guidance.

## Projection Boundary

Do not copy current canonical rule IDs, rule counts, category totals, framework-version tables, or expanded examples into this file. If this projection disagrees with `SKILL.md` or a rule file, preserve the mismatch as evidence and follow the canonical source.
