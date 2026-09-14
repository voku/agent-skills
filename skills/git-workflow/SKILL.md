---
name: git-workflow
description: Git best practices, branching strategies, conventional commits, PR workflows, and history hygiene. 5 rules across 5 categories. Use when reviewing git history, writing commits, setting up branching strategy, or improving git practices. Triggers on "git best practices", "commit message", "branching strategy", or "PR workflow".
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
---

# Git Workflow

Git best practices, conventional commit standards, branching strategies, pull request lifecycle, and history hygiene. Contains **5 consolidated rules across 5 categories** for maintaining a clean, linear, and collaboration-friendly git repository.

## Metadata

- **Version:** 2.0.0
- **Rule Count:** 5 rules across 5 categories
- **License:** MIT

## When to Apply

Reference these guidelines when:
- Writing and formatting commit messages
- Creating and naming branches
- Designing branching strategies (Trunk-based, GitHub flow)
- Opening, reviewing, and merging pull requests
- Rebasing, squashing, and managing release tags

## Rule Categories by Priority

| Priority | Category | Impact | Prefix | Rules |
|----------|----------|--------|--------|-------|
| 1 | Commit Messages | CRITICAL | `commit-` | 1 |
| 2 | Branching Strategy | HIGH | `branch-` | 1 |
| 3 | Pull Requests | HIGH | `pr-` | 1 |
| 4 | History Management | MEDIUM | `history-` | 1 |
| 5 | Collaboration & Hygiene | MEDIUM | `collab-` | 1 |

## Quick Reference

### 1. Commit Messages (CRITICAL) — 1 rule
- [commit-conventions.md](rules/commit-conventions.md) - Write atomic, imperative conventional commits (`feat:`, `fix:`, `refactor:`, `BREAKING CHANGE:`) with explanatory body context and ticket references; enforce with commitlint hooks.

### 2. Branching Strategy (HIGH) — 1 rule
- [branch-lifecycle.md](rules/branch-lifecycle.md) - Use short-lived typed branches (`feat/`, `fix/`, `chore/`), keep `main` protected from direct pushes, delete branches upon merge, and branch per-feature/package in monorepos.

### 3. Pull Requests (HIGH) — 1 rule
- [pr-lifecycle.md](rules/pr-lifecycle.md) - Keep PRs small and focused (<400 lines), use structured templates with test evidence, open Draft PRs early, require green CI checks before merge, and prefer squash-merging feature branches.

### 4. History Management (MEDIUM) — 1 rule
- [history-hygiene.md](rules/history-hygiene.md) - Maintain a clean linear history with interactive rebase (`git rebase -i`), never force-push to shared branches, tag semantic releases (`v1.2.3`), and isolate parallel work with `git worktree`.

### 5. Collaboration & Hygiene (MEDIUM) — 1 rule
- [collab-hygiene.md](rules/collab-hygiene.md) - Rebase frequently to prevent merge conflicts early, maintain a strict `.gitignore` free of OS/IDE artifacts, and provide actionable, respectful code reviews.

## Conventional Commit Reference

```text
<type>(<scope>): <subject>

<body>

<footer>
```

- **Types:** `feat` (new feature), `fix` (bug fix), `refactor` (code restructuring), `perf` (performance), `test` (test coverage), `chore` (maintenance, build).
- **Rule:** Write in the imperative mood (*"add feature"* not *"added feature"*). Limit subject line to 72 characters.

## How to Use

Read individual rule files in `rules/` for concise triggers, Bad vs Good CLI examples, and team workflow recipes.
