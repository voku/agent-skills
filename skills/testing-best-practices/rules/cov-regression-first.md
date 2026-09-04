
---
title: Regression Test Before the Fix
impact: HIGH
impactDescription: Bug fixes shipped without a test that fails on the old code, so the bug can return unnoticed
tags: testing, testing-best-practices, coverage, cov-regression-first
---

## Rule

Every bug fix ships with a test that reproduces the bug. Write it before the fix, watch it fail for the reported reason, then make it pass.

## What to Do

- Reproduce the reported behavior with the smallest input that triggers it.
- Confirm the test fails against the unfixed code; a regression test that was never red proves nothing.
- Assert the behavior that was wrong, not the implementation that happened to change.
- When a fix is urgent and the test genuinely cannot be written yet, say so explicitly and track the missing test as work, rather than closing the fix silently.

## Incorrect

```text
The fix changes a comparison and the existing happy-path test still passes,
so no new test is added. The next refactor reintroduces the same off-by-one.
```

## Correct

```text
A focused test feeds the exact input from the report, fails with the reported symptom on the
old code, and passes after the fix. It stays as the guard against a repeat.
```

## Notes

- One precise regression test beats three broad ones written after the fact.
- If the bug came from a missing contract rather than a wrong line, the test belongs at the contract's boundary.
