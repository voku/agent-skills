---
id: cov-test-resilience
title: Detect Real Regressions Without Harmless-Change Breakage
category: cov
priority: HIGH
triggers: [brittle-ui-text, css-order-test, snapshot-abuse, implementation-coupled-test, missed-regression, test-hardening, work-probe-review]
tags: [testing, tdd, mutation, resilience, regression]
---

# Regression Sensitivity and Refactoring Resilience

**Trigger Anchor:** When concrete evidence suggests a brittle or ineffective test, check both directions: harmless changes should survive; realistic contract violations should fail. This is not a default per-test mutation ritual.

## Two-Sided Probe

Use this procedure only when it can answer a material test-quality question more economically than reviewing the existing contract and assertions.

1. Identify the test's declared behavioral contract and distinguish it from presentation/implementation details.
2. Choose one bounded, contract-preserving perturbation: translation, whitespace, wrapper markup, internal refactor, or irrelevant class ordering, *only if the changed detail is not itself part of the requirement*.
3. Choose one plausible behavioral mutation: wrong destination, bypassed authorization, incorrect result, missing side effect, or rejected valid input.
4. On an isolated disposable workspace, execute the relevant focused tests against baseline, benign perturbation, and defect; restore all temporary changes.
5. Report each observed result separately as PASS, FAIL, NOT_RUN, or UNKNOWN. A skipped or unexecuted experiment is not successful evidence.

A test that stays green for both changes may be too weak. A test that goes red for both may be too coupled. Neither observation alone proves overall correctness. Prefer targeted inexpensive probes in normal development and broader mutation testing only where supported and justified.

## UI Example

Bad assertion: the page includes the German string `Zurück zur Auswahl`. It can pass while navigation is broken and fail after translation.

Better: find the intended control by accessible role/name where the role/name is stable, or by a dedicated semantic test selector such as `[data-testid="request-back"]` when necessary; activate it and assert the expected navigation or state.

A test ID is an intentional selector contract, not proof of functionality. Do not add one for every element or treat CSS class names as test contracts by default.

## After Implementation: Test or Probe?

Review checks independently of the implementation when their disposition affects the task. **Promote** a check to the regression suite when its oracle comes from an approved contract and it catches a plausible defect without rejecting harmless changes. **Keep as a work probe** when it only helps the agent explore, reproduce, or validate a draft. Retain a bounded, sanitized diagnostic record (purpose, command, observed result, limitation, candidate SHA) **only if an unexpected result, material uncertainty, or later review need makes it decision-useful**; otherwise discard uninformative scratch files. Do not automatically save every green probe, delete all implementation checks, or add every probe to CI.

**Bad:** Keep a test asserting button text `Submit` as proof that submission works; delete every exploratory check after GREEN.

**Better:** In CI, exercise submission and assert the authorized state change. Keep the temporary label check only when it explains a validation decision or uncovered blind spot. Exact text belongs in CI when the wording itself is contractual.

This is a conditional review responsibility, **not** a new agent, workflow phase, permanent probe archive, per-task ritual, or mandatory CI gate.

## Important Exceptions

- Explicit copy, localization, accessibility naming, formatting, and public serialization contracts often *require* exact text or structure assertions.
- A styling test can intentionally check layout or classes; it should be identified as such rather than "hardened" into an assertion that detects nothing.
- Mutation testing is evidence of fault detection for the tested faults, not universal completeness.
- If no safe, executable probe exists, keep the risk UNKNOWN and specify the smallest useful follow-up.
