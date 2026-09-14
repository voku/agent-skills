---
id: pr-lifecycle
title: "Pull Request Lifecycle: Scope, Templates, and Squash-Merging"
category: pr
priority: HIGH
triggers: [massive-pr, empty-pr-description, failing-ci-merge, uninspected-pr-merge, noisy-merge-commits]
tags: [pull-request, code-review, ci, squash-merge, templates]
---

# Pull Request Lifecycle: Scope, Templates, and Squash-Merging

**Trigger Anchor:** Keep PRs small and focused (<400 lines), use structured templates with test evidence, open Draft PRs early, require green CI checks before merge, and prefer squash-merging feature branches.

---

### Bad
```text
# ❌ Massive PR with empty description and bypassing CI
PR Title: "Updates"
Diff: +2,840 lines, -1,420 lines across 84 files
Description: (blank)
CI: ❌ 2 failed checks
Action: Merged anyway via admin override
```

### Good
```markdown
# ✅ Structured PR description with bounded scope and verification evidence

## Summary
Implements Stripe PaymentElement in checkout flow, replacing deprecated CardElement.

- Bounds network retries with exponential backoff
- Adds form validation before gateway submission
- Includes unit tests for payment webhook handling

Closes #382

## Verification
- [x] Unit tests pass: `npm test -- --run`
- [x] E2E checkout smoke test passes locally
- [x] Tested with Stripe test card numbers (3DS challenge and immediate decline)

## Size & Strategy
- +180 lines, -45 lines (Small / Focused)
- Squash & merge to maintain clean linear trunk history
```

### Pull Request Rules
1. **Size Budget:** Aim for < 400 lines changed. Break larger features into stacked PRs or feature-flagged slices.
2. **Draft PRs:** Open early as `Draft` to get architecture feedback before finishing implementation.
3. **CI Gate:** All checks (lint, tests, build) must pass green. Never bypass failing CI for "urgent" fixes.
4. **Squash Merge:** Squash feature branches into a single clean commit on `main` to eliminate WIP noise.
