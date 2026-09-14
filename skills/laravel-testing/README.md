# Laravel Testing — Pest PHP & PHPUnit

Portable guidance for testing Laravel applications with the framework and conventions configured by the target repository.

## Canonical Source

`SKILL.md` defines activation, framework-selection guidance, and high-level routing. `rules/` contains the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, count, Pest/PHPUnit version matrix, or compiled set of examples.

## When to Use

Use this skill for HTTP/feature tests, model factories, database assertions, facade fakes, authentication tests, and test-suite organization in Laravel applications.

## Routing

1. Inspect `composer.json`, `tests/Pest.php`, and existing tests to determine Pest vs PHPUnit conventions.
2. Read `SKILL.md` to select the canonical rules matching the observed testing problem.
3. Load only those rule files instead of compiling the whole testing guide into context.
4. Preserve project-local test base classes, database isolation strategy, helpers, and assertion conventions unless evidence supports changing them.
5. Run the repository's configured test command and report only observed results.

## Stable Boundaries

- Test observable behavior and durable state rather than private implementation details by default.
- Use factories and explicit scenario states for test data.
- Isolate external side effects with framework fakes where that boundary is under test.
- Match authentication setup to the route/application contract.
- Do not infer Pest/PHPUnit versions or syntax from this README.

## Projection Boundary

Do not copy current rule IDs, counts, or test-framework version tables into this file. If this projection disagrees with `SKILL.md` or a file under `rules/`, follow the canonical source and repair the projection.
