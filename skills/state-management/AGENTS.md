# State Management — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not maintain a second TanStack Query/Zustand rule inventory, migration guide, count, or compiled example set here.

## Fast Path

1. Inspect installed TanStack Query/Zustand versions and the repository's existing QueryClient/store/session setup.
2. Classify the state as server-owned, client-owned, or derived before choosing a storage mechanism.
3. Read `SKILL.md` first and load only the relevant canonical rule files.
4. Prefer existing repository conventions over adding another cache/store/persistence layer.
5. Validate observable loading, cache, mutation, rollback, persistence, and render behavior with repository tooling.

## Ownership Boundary

- `SKILL.md` owns activation, v5 migration invariants, state-ownership boundaries, and security constraints.
- `rules/` owns detailed query, mutation, cache, advanced-query, Zustand architecture, and persistence guidance.
- the target repository owns installed versions, auth/session architecture, query defaults, store boundaries, persistence choices, and validation commands.
- TanStack Query/Zustand upstream own version-sensitive API behavior.
- this projection owns no independent state-management semantics.

## Security and State Boundary

- Do not mirror server/API data into Zustand without a concrete ownership reason.
- Never persist auth tokens, passwords, encryption keys, or equivalent secrets in browser storage or Zustand persist.
- Use persistence selectively for non-sensitive client state and keep `partialize` intentionally narrow.
- Do not apply v5 migration advice to a repository that is not actually on the relevant v5 library version.

## Projection Boundary

If this file disagrees with `SKILL.md`, `rules/`, or stronger repository/task instructions, follow the authoritative source and repair this projection. Do not copy current rule IDs, counts, migration tables, or long examples back into this file.
