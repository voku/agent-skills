---
id: commit-conventions
title: Conventional and Atomic Commits
category: commit
priority: CRITICAL
triggers: [vague-commit-message, non-atomic-commit, breaking-change-format, missing-issue-reference]
tags: [git, commit, conventional-commits, changelog, semver]
---

# Conventional and Atomic Commits

**Trigger Anchor:** Write atomic, imperative conventional commits (`feat:`, `fix:`, `refactor:`, `BREAKING CHANGE:`) with explanatory body context and ticket references; enforce with commitlint hooks.

---

### Bad
```bash
# ❌ Vague, past tense, non-atomic bundled changes without context
git commit -m "fixed bugs and updated stuff"

# ❌ Giant commit mixing formatting, feature, refactoring, and library bumps
git commit -m "WIP work on checkout"
```

### Good
```bash
# ✅ Atomic commit in imperative mood with scope, body rationale, and ticket reference
git commit -m "fix(billing): prevent double-charge on rapid checkout button clicks

Debounce the payment submission handler and track an in-flight submission token
in state. Previously, users with high-latency connections could trigger multiple
POST /api/charges requests before button disable evaluated.

Fixes #412
BREAKING CHANGE: None"
```

### Format Standard
```text
<type>(<scope>): <imperative subject line (<= 72 chars)>

<problem description and rationale for this exact change>

<footer references, e.g. Fixes #123, BREAKING CHANGE: ...>
```

| Type | When to Use |
|------|-------------|
| `feat` | Adds user-facing capability |
| `fix` | Corrects unintended behavior |
| `refactor` | Restructures code without changing external behavior |
| `perf` | Measurable performance improvement |
| `test` | Adds or updates tests only |
| `chore` | Build tools, dependencies, or auxiliary configuration |
