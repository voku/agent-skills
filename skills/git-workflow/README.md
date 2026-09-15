# Git Workflow

Portable Git workflow guidance for commit quality, branch lifecycle, pull requests, history hygiene, and collaboration.

## Canonical Source

`SKILL.md` defines activation and the high-level contract. The files under `rules/` contain the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, count, branching-strategy matrix, or command cookbook.

## When to Use

Use this skill when reviewing commit history, shaping commits or branches, preparing pull requests, cleaning private branch history, or evaluating repository collaboration practices.

## Routing

1. Ground the target repository's current Git and contribution policy.
2. Read `SKILL.md` first.
3. Load only the relevant rule files for commits, branches, PRs, history, or collaboration.
4. Preserve repository-specific merge/release policy and required CI checks.
5. Prefer observable repository state over generic tool or workflow assumptions.

## Safety Boundary

Shared history must not be rewritten; failing CI must not be bypassed to force a merge; repository-wide workflow settings are changed only when the task authorizes that scope. Tooling such as commitlint, Husky, semantic-release, or a particular Git-flow model must be discovered from the target repository rather than assumed from this skill.

## Projection Boundary

If this projection disagrees with `SKILL.md` or `rules/`, follow the canonical source and repair the projection. Do not copy current rule IDs, counts, version tables, or long examples into this file.
