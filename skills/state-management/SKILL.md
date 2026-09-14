---
name: state-management
description: React Query and Zustand patterns for state management. Use when implementing data fetching, caching, mutations, or client-side state. Triggers on tasks involving useQuery, useMutation, Zustand stores, caching, or state management.
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
---

# State Management with TanStack Query v5 + Zustand v5

Curated, high-density state management patterns covering server-state caching (TanStack Query v5) and client-state stores (Zustand v5).

## Quick Reference

| Domain | Impact | Rule File | Primary Focus |
|--------|--------|-----------|---------------|
| **Query Fundamentals** | CRITICAL | [`rq-query-fundamentals`](rules/rq-query-fundamentals.md) | Query key factories, `enabled` conditionals, typed `useQuery`, `select` transform memoization |
| **Mutations & Updates** | CRITICAL | [`rq-mutations-optimistic`](rules/rq-mutations-optimistic.md) | `useMutation`, optimistic UI updates with snapshot rollback in `onMutate`, cache invalidation |
| **Cache Lifecycles** | HIGH | [`rq-cache-lifecycles`](rules/rq-cache-lifecycles.md) | `staleTime` vs `gcTime`, `placeholderData: keepPreviousData`, intent prefetching, retry backoff |
| **Advanced Queries** | HIGH | [`rq-advanced-patterns`](rules/rq-advanced-patterns.md) | `useInfiniteQuery` streams, `useQueries` parallel fetching, `signal` cancellation, `useSuspenseQuery` |
| **Zustand Architecture** | CRITICAL | [`zs-store-architecture`](rules/zs-store-architecture.md) | Type-safe store slices, co-located actions, atomic selectors, `useShallow` re-render prevention |
| **Persistence & Security** | HIGH | [`zs-persist-coordination`](rules/zs-persist-coordination.md) | `persist` with `partialize` (zero tokens in localStorage), strict server-vs-client state boundaries |

## Essential Invariants

### 1. v5 API Changes
- **TanStack Query**: `cacheTime` is now `gcTime`. `keepPreviousData: true` is replaced by `placeholderData: keepPreviousData`. `suspense: true` is replaced by `useSuspenseQuery`.
- **Zustand**: For multiple property selection, wrap the selector in `useShallow` from `zustand/shallow` to avoid infinite re-render loops.

### 2. State Ownership Boundary
- **Server Cache (React Query)**: Anything originating from or synced with a backend API (users, posts, search results). Do not mirror API responses into Zustand.
- **Client UI (Zustand)**: Ephemeral interface state (modals, active tabs, theme, audio playback, sidebar collapse).
- **Security**: Never persist auth tokens, passwords, or encryption keys in `localStorage` or Zustand `persist`. Manage auth sessions with HttpOnly cookies.
