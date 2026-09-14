---
id: collab-hygiene
title: "Collaboration, Conflict Resolution, and Workspace Hygiene"
category: collab
priority: MEDIUM
triggers: [merge-conflict, gitignore-pollution, local-env-committed, non-actionable-review]
tags: [collaboration, merge-conflicts, gitignore, code-review]
---

# Collaboration, Conflict Resolution, and Workspace Hygiene

**Trigger Anchor:** Rebase frequently to prevent merge conflicts early, maintain a strict `.gitignore` free of OS/IDE artifacts, and provide actionable, respectful code reviews.

---

### Bad
```bash
# ❌ Committing IDE, OS, or local environment files
git add .idea/
git add .DS_Store
git add .env

# ❌ Resolving conflict blindly by accepting ours/theirs without understanding context
git checkout --ours package-lock.json # Breaks dependency resolution
```

### Good
```gitignore
# ✅ Standard workspace .gitignore covering build outputs, secrets, and IDEs
node_modules/
vendor/
.env
.env.local
.DS_Store
.idea/
.vscode/
*.log
dist/
build/
```

### Merge Conflict Protocol
1. **Rebase frequently:** Pull upstream changes into feature branches daily (`git rebase origin/main`).
2. **Lockfiles:** When lockfiles conflict, re-generate them deterministically (`npm install` or `composer update --lock`) rather than manually picking lines.
3. **Actionable Reviews:** When reviewing PRs, suggest specific diffs or rationale:
   - ❌ *"This code is bad."*
   - ✅ *"Consider using `array_map` here to eliminate the temporary accumulator variable (e.g. `return array_map(fn($u) => $u->id, $users);`)."*
