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
# ❌ Force-pushing shared branches can overwrite teammates' commits.
# There is deliberately no runnable command for this destructive anti-pattern.

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

# ✅ Ordinary feature branch publication must not rewrite remote history
git push origin feat/my-branch

# ✅ Worktrees for parallel branch work without stashing
git worktree add ../repo-hotfix hotfix/critical-security-patch
git worktree remove ../repo-hotfix

# ✅ Annotated semantic release tags
git tag -a v2.4.0 -m "Release v2.4.0: Stripe payment upgrade"
git push origin v2.4.0
```

When a private feature branch was rebased after publication and a history rewrite is unavoidable, obtain explicit agreement from its sole owner, verify the remote head and use a lease tied to the exact observed commit. Never rewrite a shared or protected branch. A plain push is the safe default.
