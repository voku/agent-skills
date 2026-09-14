# PHP Best Practices — Agent Projection

This file is a compact routing projection for agents. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add an independent rule inventory, version table, rule count, or copied PHP semantics here.

## Fast path

1. Ground the target PHP version and repository toolchain from current project evidence.
2. Read `SKILL.md` and select only the canonical rule files relevant to the task.
3. Prefer explicit native types, strict contracts, observable failures, and small evidence-backed changes.
4. Use PHPDoc where it adds precision that native PHP cannot express; do not use it to conceal a dishonest runtime contract.
5. Validate with the repository's configured tests, PHPStan/static analysis, and formatter/fixer; report observed results only.

## Version boundary

Only apply features available in the target project's supported PHP/runtime version. A feature being documented by this skill does not make it valid for an older target.

## Ownership boundary

- `SKILL.md` owns scope, triggers, and high-level routing.
- `rules/` owns detailed PHP guidance and examples.
- the target repository owns its supported PHP version, dependencies, conventions, and validation commands.
- focused tools or skills own their narrower domains when the task becomes primarily about those domains.

For analyzer-specific proof work, use `php-static-analysis` rather than expanding this projection into a second static-analysis manual.

## Evidence contract

- Do not suppress diagnostics merely to make validation quiet.
- Do not claim a command passed unless its actual result was observed.
- Preserve unknown or blocked states when required repository evidence is unavailable.
- Keep unrelated modernization out of a focused fix.

## Projection boundary

Do not copy the current canonical rule IDs or counts into this file. If this projection disagrees with `SKILL.md` or a rule file, preserve the mismatch as evidence and follow the canonical source.
