# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Essential for production apps | Always |
| HIGH | Significant performance & UX impact | Most projects |
| MEDIUM | Polish and coordination patterns | When scaling |

## Section Overview

### 1. Query Fundamentals (`query`)
- **Impact:** CRITICAL
- **Rules:** `rq-query-fundamentals`
- **Description:** React Query basics: QueryClient configuration, query key factories with tuple `as const`, strongly-typed query functions with AbortSignal, conditional execution with `enabled`, and fine-grained data projection with `select`.

### 2. Mutation & Updates (`mutation`)
- **Impact:** CRITICAL
- **Rules:** `rq-mutations-optimistic`
- **Description:** Server write operations with `useMutation`: optimistic updates with cache cancellation, snapshot capture in `onMutate`, error rollback via context, and cache invalidation on settle.

### 3. Cache Lifecycles & Prefetching (`cache`)
- **Impact:** HIGH
- **Rules:** `rq-cache-lifecycles`
- **Description:** Cache freshness vs garbage collection (`staleTime` vs `gcTime`), smooth page transitions via `placeholderData: keepPreviousData`, proactive prefetching, and retry strategies with exponential backoff.

### 4. Advanced Queries & Concurrency (`advanced`)
- **Impact:** HIGH
- **Rules:** `rq-advanced-patterns`
- **Description:** Cursor and offset infinite lists via `useInfiniteQuery`, dynamic parallel requests with `useQueries`, request cancellation via `signal`, and React 18+ streaming with `useSuspenseQuery`.

### 5. Zustand Store Architecture (`zustand`)
- **Impact:** CRITICAL
- **Rules:** `zs-store-architecture`
- **Description:** Type-safe Zustand store definitions, co-located actions, atomic scalar selectors, and shallow multi-property comparisons with `useShallow` to prevent render loops.

### 6. Persistence & Server-Client Boundary (`zustand`)
- **Impact:** HIGH
- **Rules:** `zs-persist-coordination`
- **Description:** Storage persistence security using `partialize` (strictly excluding auth tokens, passwords, and sensitive keys), and clear architectural separation between React Query server state and Zustand UI state.
