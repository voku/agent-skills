---
id: branch-lifecycle
title: Branch Strategy and Lifecycle Management
category: branch
priority: HIGH
triggers: [unstructured-branch-name, long-lived-branch, unprotected-main, unpruned-branch, monorepo-branching]
tags: [git, branching, trunk-based, branch-naming, branch-protection]
---

# Branch Strategy and Lifecycle Management

**Trigger Anchor:** Use short-lived typed branches (`feat/`, `fix/`, `chore/`), keep `main` protected from direct pushes, delete branches upon merge, and branch per-feature/package in monorepos.

---

### Bad
```bash
# ❌ Chaotic naming, long-lived branches, and pushing directly to main
git checkout -b johns-work
git checkout -b test2
git push origin main --force # ❌ Direct push to shared production branch
```

### Good
```bash
# ✅ Consistent naming prefix, linked issue, and automatic remote prune
git checkout -b feat/checkout-stripe-elements-412
git push -u origin feat/checkout-stripe-elements-412

# ✅ Delete merged branches automatically
git branch -d feat/checkout-stripe-elements-412
git remote prune origin
```

### Naming Conventions

| Prefix | Usage | Example |
|--------|-------|---------|
| `feat/` | New functionality | `feat/oauth-github-login` |
| `fix/` | Defect repair | `fix/user-avatar-upload-crash` |
| `refactor/` | Internal restructuring | `refactor/consolidate-skills` |
| `chore/` | Tooling & dependency updates | `chore/bump-phpstan-1.12` |
| `release/` | Version stabilization | `release/v2.4.0` |

### Invariants
1. **Protected `main`:** Require pull requests, code reviews, and passing CI status checks before merging.
2. **Short-lived:** Merge within 1–3 days to prevent diverging divergence and integration hell.
3. **Auto-delete on merge:** Configure repository settings to automatically delete head branches upon merge.
