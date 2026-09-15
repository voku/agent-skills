---
name: state-management
description: TanStack Query v5 and Zustand v5 patterns for server-state caching, mutations, client-state stores, persistence, and ownership boundaries. Use when implementing data fetching, caching, mutations, or client-side state.
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
---

# State Management with TanStack Query v5 + Zustand v5

Portable state-management guidance for separating backend-owned server state from local UI state while preserving cache, mutation, persistence, and rendering semantics.

## Grounding and Ownership

Before applying version-specific guidance, inspect the target repository's installed TanStack Query and Zustand versions, existing QueryClient/store setup, persistence middleware, authentication/session model, and test/validation tooling.

- TanStack Query owns server-state fetching, caching, invalidation, retries, and mutation coordination.
- Zustand owns local client/UI state where a dedicated store is justified.
- Do not mirror backend/API responses into Zustand merely to make them globally reachable.
- The target repository owns session/auth architecture, persistence choices, query defaults, store boundaries, and validation commands.
- Upstream TanStack/Zustand documentation owns version-sensitive API behavior.

## v5 Migration Invariants

For TanStack Query v5:
- hooks use the single object-argument form;
- `cacheTime` became `gcTime`;
- `keepPreviousData: true` and `isPreviousData` were replaced by `placeholderData: keepPreviousData` and `isPlaceholderData`;
- `onSuccess`, `onError`, and `onSettled` were removed from queries, while mutation callbacks remain supported;
- `suspense: true` on `useQuery` was replaced by `useSuspenseQuery`.

For Zustand v5:
- selectors that create new array/object references need stable outputs; use `useShallow` when selecting multiple values where shallow comparison is appropriate.

## Security Boundary

Never persist auth tokens, passwords, encryption keys, or equivalent secrets in `localStorage`, `sessionStorage`, or Zustand `persist`. Prefer server-managed session mechanisms such as HttpOnly cookies when the application architecture supports them. Use `partialize` to keep persisted client state intentionally narrow.

## Canonical Rule Boundaries

### Query Fundamentals
- [rq-query-fundamentals.md](rules/rq-query-fundamentals.md) — typed query keys/functions, conditional execution, cancellation signals, and `select` projections.

### Mutations and Optimistic Updates
- [rq-mutations-optimistic.md](rules/rq-mutations-optimistic.md) — mutation lifecycle, optimistic cache changes, rollback, and invalidation.

### Cache Lifecycles
- [rq-cache-lifecycles.md](rules/rq-cache-lifecycles.md) — `staleTime`, `gcTime`, placeholder data, prefetching, and retry behavior.

### Advanced Queries
- [rq-advanced-patterns.md](rules/rq-advanced-patterns.md) — infinite/parallel queries, cancellation, and suspense-oriented patterns.

### Zustand Architecture
- [zs-store-architecture.md](rules/zs-store-architecture.md) — typed stores, co-located actions, selectors, and render stability.

### Persistence and Coordination
- [zs-persist-coordination.md](rules/zs-persist-coordination.md) — persistence security and the server-state/client-state ownership boundary.

## Decision Discipline

1. Classify the state as server-owned, client-owned, or derived before choosing a tool.
2. Load only the rule files relevant to the current problem.
3. Prefer existing QueryClient/store conventions over introducing a second state model.
4. Keep persistence minimal and non-sensitive.
5. Validate observable loading, mutation, cache, rollback, and render behavior with the repository's configured tests/tooling.

`README.md`, `AGENTS.md`, and `metadata.json` are supporting projections. If they disagree with this file or `rules/`, follow the canonical source and repair the projection.
