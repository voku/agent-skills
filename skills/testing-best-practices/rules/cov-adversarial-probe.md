
---
title: Probe Adversarially Before Writing Happy-Path Tests
impact: HIGH
impactDescription: New validation covered only by the cases it was designed for, leaving the paths an attacker or a stale client would take untested
tags: testing, testing-best-practices, coverage, cov-adversarial-probe
---

## Rule

After adding a guard, probe it by hand with hostile input before writing the test suite. The probes that fail become the tests; the happy path is written last.

## What to Do

- Try input from the wrong scope or tenant, an identifier that does not exist, a stale or replayed submission, differing case, and the exact boundary value.
- Try the state transitions the guard does not mention: already-deleted, already-approved, concurrent second submit.
- Turn every probe that got through into a test before writing the ones you expect to pass.
- When no probe gets through, say so as a residual gap rather than implying exhaustive coverage.

## Incorrect

```text
The new permission check is covered by one test with a valid user and one with no user,
and the case of a valid user from another tenant is never exercised.
```

## Correct

```text
Manual probing found that an identifier from another tenant passed the check; that case is now
the first test in the file, followed by the boundary and the happy path.
```

## Notes

- This is cheapest immediately after writing the guard, while its assumptions are still in your head.
- A probe list is also the review evidence that the guard was tested against something it might not survive.
