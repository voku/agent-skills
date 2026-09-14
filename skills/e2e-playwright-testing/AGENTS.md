# E2E Playwright Testing — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not maintain a second Playwright rule inventory, count, framework-version table, or compiled example set here.

## Fast Path

1. Confirm the target repository actually uses Playwright and inspect its config before applying this skill.
2. Ground frontend navigation, authentication, shared state, worker parallelism, and installed versions in the target repository.
3. Read `SKILL.md` first and load only the relevant canonical rule files.
4. Prefer accessible locators, web-first assertions, reusable auth state, and Playwright form APIs over brittle selectors, sleeps, repeated UI login, or hand-simulated input behavior.
5. Run the repository's configured browser-test commands and report only observed evidence.

## Ownership Boundary

- `SKILL.md` owns activation, stack grounding, flow discipline, and high-level operational boundaries.
- `rules/` owns detailed locator, assertion, auth-state, and form-interaction guidance.
- the target repository owns installed Playwright/Node versions, app framework behavior, auth setup, test data, worker configuration, and validation commands.
- Playwright upstream owns version-sensitive APIs and browser behavior.
- this projection owns no independent E2E semantics.

## Evidence Boundary

- Do not assume SPA navigation behavior, auth storage, rate limiting, or shared-state constraints without repository evidence.
- Do not use arbitrary sleeps as a substitute for an observable browser condition.
- Do not invent selectors when the live DOM or app-owned test hooks can establish a durable locator.
- For editable controlled/date inputs, follow the canonical form rule and actual control behavior rather than stale keyboard recipes.

## Projection Boundary

If this file disagrees with `SKILL.md` or a file under `rules/`, follow the canonical source and repair this projection. Current rule IDs and counts belong to the canonical surfaces, not here.
