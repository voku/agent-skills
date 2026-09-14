# Laravel Testing — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add an independent test-rule inventory, framework-version table, or compiled copy of examples here.

## Fast Path

1. Inspect the target repository's `composer.json`, `tests/Pest.php`, test tree, and existing conventions before choosing Pest or PHPUnit syntax.
2. Read `SKILL.md` first and load only the canonical rule files relevant to the current task.
3. Keep HTTP testing, factories, database assertions, facade fakes, authentication, and test organization in their owning rule boundaries.
4. Prefer observable behavior and project-configured test infrastructure over implementation-detail mocking.
5. Run the target repository's configured test command and report only observed results.

## Ownership Boundary

- `SKILL.md` owns activation, framework-selection guidance, and high-level routing.
- `rules/` owns detailed Laravel testing guidance and examples.
- the target repository owns Pest/PHPUnit selection, installed versions, base test classes, traits, datasets, helpers, database strategy, and validation commands.
- Laravel/Pest/PHPUnit upstream documentation owns version-sensitive APIs.
- this projection owns no independent test semantics.

## Evidence Boundary

- Do not assume Pest merely because this skill contains Pest examples; verify repository configuration.
- Do not invent a test runner or version when the project does not establish one.
- Keep database isolation, authentication context, and side-effect fakes explicit in tests that depend on them.
- Assert externally observable behavior and durable state rather than private implementation details unless the task specifically targets that boundary.

## Projection Boundary

If this file disagrees with `SKILL.md` or a file under `rules/`, follow the canonical source and repair this projection. Current rule IDs, counts, framework-version matrices, and compiled examples do not belong here.
