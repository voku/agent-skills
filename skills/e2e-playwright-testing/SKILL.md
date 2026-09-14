---
name: e2e-playwright-testing
description: End-to-end browser testing with Playwright for web applications. Use when writing or reviewing Playwright E2E tests, browser automation, form flows, authentication flows, locator strategy, or flaky browser-test behavior. Ground framework, auth, installed versions, and test configuration in the target repository before applying examples.
license: MIT
metadata:
  author: Agent Skills Contributors
  version: "1.0.0"
---

# E2E Playwright Testing

Portable guidance for reliable browser-level tests with Playwright. The detailed contract is intentionally concentrated in the canonical rules under `rules/`; this file owns activation, repository grounding, and high-level flow discipline.

## Applicability and Stack Grounding

Before writing or reviewing E2E tests:

- inspect `package.json` and Playwright configuration to confirm `@playwright/test` is actually in use;
- if the project uses Cypress or another browser-test framework instead, do not force Playwright guidance onto it;
- inspect the frontend/navigation model (for example React, Inertia, Vue, Next.js) before choosing navigation waits or selectors;
- inspect the authentication model and existing test setup before deciding how session state should be created or reused;
- inspect shared mutable state, database setup, and configured workers before changing parallelism;
- use the target repository's installed Playwright/Node versions and validation commands instead of assuming fixed version floors from this skill.

## Flow Discipline

- Start with one concrete end-user path before automating nearby variants.
- Prefer the narrowest meaningful E2E scope the repository tooling supports.
- Inspect the live DOM or application markup before inventing brittle selectors.
- Assert the visible browser transition first; verify persistence or backend side effects separately only when the repository has a stable mechanism for that evidence.
- Prefer app-owned durable hooks over styling-driven CSS chains when accessible role/label locators are insufficient.

## Canonical Rule Boundaries

### Accessible Locators
- [`pw-locators-strict-mode`](rules/pw-locators-strict-mode.md) — prefer role/label/user-facing locators and resolve strict-mode ambiguity through scoping or filtering rather than brittle DOM selectors.

### Web-First Assertions
- [`pw-web-first-assertions`](rules/pw-web-first-assertions.md) — use auto-retrying Playwright assertions and explicit event waits; avoid arbitrary `waitForTimeout()` sleeps and immediate boolean checks.

### Authenticated Sessions
- [`pw-auth-storage-state`](rules/pw-auth-storage-state.md) — reuse authenticated browser state through Playwright setup projects and `storageState` when that matches the target application's auth model.

### Controlled Forms & Inputs
- [`pw-form-interactions-custom-inputs`](rules/pw-form-interactions-custom-inputs.md) — use Playwright's form APIs for controlled inputs, interact with custom/hidden controls through accessible surfaces, and prefer direct `.fill()` for editable date/text inputs when supported by the actual control.

## Operational Boundaries

- Do not encode framework-specific navigation assumptions without evidence from the target app.
- Do not repeat UI login in every test when the repository can safely reuse isolated authenticated state.
- Do not increase worker parallelism when tests share mutable state unless isolation evidence supports it.
- Do not treat retries as a substitute for deterministic waits and assertions.
- Keep selectors coupled to user-visible semantics or intentional test hooks, not incidental CSS structure.

## Validation and Evidence

Run the repository's existing Playwright/test commands in its documented order. Report observed failures, traces, screenshots, or browser transitions rather than inventing expected results. `README.md`, `AGENTS.md`, and `metadata.json` are supporting projections; if they disagree with this file or `rules/`, follow the canonical source and repair the projection.
