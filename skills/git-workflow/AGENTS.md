# Git Workflow — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not maintain a second Git rule inventory, count, branching matrix, or compiled command cookbook here.

## Fast Path

1. Inspect the target repository's current branch, remotes, contribution guidance, CI, release process, and merge conventions before changing Git state.
2. Read `SKILL.md` first and load only the relevant canonical rule files.
3. Prefer the repository's established branch and merge policy over generic workflow preferences.
4. Keep commits atomic and reviewable; preserve evidence for the actual change rather than manufacturing a cosmetically clean history.
5. Run the repository's configured validation before proposing or performing a merge.

## Ownership Boundary

- `SKILL.md` owns activation and the high-level Git workflow contract.
- `rules/` owns detailed commit, branch, PR, history, and collaboration guidance.
- the target repository owns branch protection, required checks, merge method, release/tag policy, CODEOWNERS, hooks, and contribution requirements.
- Git/Git-host upstream documentation owns version-sensitive command and platform behavior.
- this projection owns no independent workflow semantics.

## Safety and Evidence Boundary

- Never rewrite shared history or force-push a shared branch.
- Treat force-with-lease as a private-branch technique only when repository policy permits it.
- Do not bypass failing CI merely to land a change.
- Do not change branch protection, release automation, hooks, or repository-wide workflow policy unless the task actually authorizes that scope.
- Resolve conflicts from semantic understanding and regenerated artifacts where appropriate, not blind ours/theirs selection.
- Do not infer installed tooling such as commitlint, Husky, or semantic-release from this skill; inspect the repository.

## Projection Boundary

If this file disagrees with `SKILL.md`, `rules/`, or stronger repository/task instructions, follow the authoritative source and repair this projection. Do not copy current rule IDs, counts, tool versions, or long examples back into this file.
