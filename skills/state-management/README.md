# State Management with TanStack Query v5 + Zustand v5

Portable guidance for server-state caching and client-state stores.

## Canonical Source

`SKILL.md` defines activation, v5 migration invariants, state ownership, and security boundaries. The files under `rules/` contain the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, migration table, count, or compiled example set.

## When to Use

Use this skill for TanStack Query data fetching/caching/mutations, Zustand client state, persistence, optimistic updates, or questions about server-state versus client-state ownership.

## Routing

1. Inspect installed package versions and existing QueryClient/store/session architecture.
2. Classify the state before choosing Query, Zustand, component state, or derived state.
3. Read `SKILL.md` first and load only relevant canonical rules.
4. Preserve repository-specific query/store conventions and authentication architecture.
5. Validate cache, mutation, rollback, persistence, and render behavior with repository tooling.

## Security Boundary

Never persist auth tokens, passwords, encryption keys, or equivalent secrets in browser storage or Zustand persist. Do not mirror API data into Zustand merely for global access.

## Projection Boundary

If this projection disagrees with `SKILL.md` or `rules/`, follow the canonical source and repair the projection. Do not copy current rule IDs, counts, version tables, or long examples into this file.
