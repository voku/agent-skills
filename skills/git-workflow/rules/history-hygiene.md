---
id: history-hygiene
title: "Git History Hygiene, Rebasing, Tags, and Worktrees"
category: history
priority: MEDIUM
triggers: [force-push-shared-branch, messy-merge-bubbles, missing-release-tag, context-switching-stash]
tags: [git, rebase, worktree, git-tags, semver, linear-history]
---

# Git History Hygiene, Rebasing, Tags, and Worktrees

**Trigger Anchor:** Maintain a clean linear history with interactive rebase (`git rebase -i`), never force-push to shared branches, tag semantic releases (`v1.2.3`), and isolate parallel work with `git worktree`.

---

### Bad
```bash
# ❌ Force-pushing to shared branches clobbering teammate commits
git push origin main --force

# ❌ Messy merge bubbles polluting history
git merge main # within feature branch creates pointless merge commits

# ❌ Stashing WIP back and forth when context-switching across branches
git stash && git checkout other-fix && git stash pop
```

### Good
```bash
# ✅ Rebase onto main to maintain linear history
git fetch origin
git rebase origin/main

# ✅ Interactive rebase to clean up fixup commits before review
git rebase -i HEAD~3
# (squash/fixup intermediate commits into cohesive logical changes)

# ✅ Safe force-push only on private feature branches
git push --force-with-lease origin feat/my-branch

# ✅ Worktrees for parallel branch work without stashing
git worktree add ../repo-hotfix hotfix/critical-security-patch
git worktree remove ../repo-hotfix

# ✅ Annotated semantic release tags
git tag -a v2.4.0 -m "Release v2.4.0: Stripe payment upgrade"
git push origin v2.4.0
```
