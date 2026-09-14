# PHP Best Practices

Modern PHP guidance for strict typing, language features, explicit error handling, security, performance, architecture, PSR standards, and static analysis.

## Canonical source

`SKILL.md` defines when this skill applies and the high-level contract. `rules/` contains the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, version table, or rule count.

## When to use

Use this skill for PHP implementation or review work where the dominant concern is language-level correctness, explicit contracts, modern PHP usage, error handling, security, performance, design, standards, or static-analysis-friendly code.

For analyzer-specific work where proving a type to PHPStan/Psalm is the primary task, prefer `php-static-analysis` as the focused implementation skill.

## Routing

1. Detect the target project's supported PHP version from its own configuration and runtime evidence.
2. Read `SKILL.md` to confirm scope and select the relevant canonical rule files.
3. Load only the rules needed for the verified problem instead of compiling the entire skill into context.
4. Apply project-local conventions and stronger repository instructions within their scope.
5. Validate through the repository's configured tests, static analysis, and formatter/fixer; report only observed results.

## Stable boundaries

- Do not recommend syntax or runtime behavior newer than the target project supports.
- Prefer native PHP types for enforceable contracts; use PHPDoc as a precision layer where PHP cannot express enough.
- Prefer explicit, analyzable APIs over magic-heavy behavior when both satisfy the same requirement.
- Make failures observable rather than suppressing diagnostics.
- Keep modernization and refactoring scoped to the evidence-backed problem.

## Projection boundary

Do not copy the current canonical rule list or rule count into this file. If this projection disagrees with `SKILL.md` or a file under `rules/`, preserve the mismatch as evidence and follow the canonical source.
