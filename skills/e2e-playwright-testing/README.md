# E2E Playwright Testing

Portable Playwright guidance for reliable end-to-end browser tests.

## Canonical Source

`SKILL.md` defines activation, repository grounding, flow discipline, and high-level operational boundaries. The files under `rules/` contain the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, count, framework-version table, or compiled example set.

## When to Use

Use this skill for Playwright E2E tests, browser automation, locator strategy, authentication reuse, form interactions, flaky browser tests, or browser-level user flows.

## Routing

1. Confirm Playwright is actually configured in the target repository.
2. Read `SKILL.md` first.
3. Load only the relevant rule files for locators, web-first assertions, auth storage state, or controlled form/input interactions.
4. Ground navigation, auth, worker parallelism, and installed versions in the target project.
5. Prefer observable browser transitions and repository-configured test evidence over sleeps or assumptions.

## Projection Boundary

Do not copy current rule IDs, counts, tool-version floors, or long worked examples into this file. If this projection disagrees with `SKILL.md` or `rules/`, follow the canonical source and repair the projection.
