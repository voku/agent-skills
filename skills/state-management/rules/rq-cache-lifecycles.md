---
id: rq-cache-lifecycles
title: "Cache Staleness, Garbage Collection, Prefetching, and Placeholder Data"
category: cache
priority: HIGH
triggers: [stale-time-vs-gctime, query-prefetching, keep-previous-data, placeholder-vs-initial-data, retry-exponential-backoff]
tags: [react-query, caching, staletime, gctime, prefetch, placeholderdata]
---

# Cache Staleness, Garbage Collection, Prefetching, and Placeholder Data

**Trigger Anchor:** Set explicit `staleTime` for data freshness and `gcTime` for memory retention, smooth paginated transitions with `placeholderData: keepPreviousData`, and prefetch data on navigation intent.

---

### Bad
```tsx
// ❌ Deprecated v4 API options and zero cache configuration causing refetch storms
const { data, isPreviousData } = useQuery({
  queryKey: ['items', page],
  queryFn: () => fetchItems(page),
  cacheTime: 1000 * 60 * 10, // ❌ Deprecated in v5: renamed to gcTime
  keepPreviousData: true, // ❌ Deprecated in v5: replaced by placeholderData helper
  staleTime: 0, // Default 0 causes every component mount / window focus to trigger network requests
});
```

### Good
```tsx
// ✅ TanStack Query v5: Correct gcTime, placeholderData, prefetching, and retry backoff
import { useQuery, useQueryClient, keepPreviousData } from '@tanstack/react-query';
import { queryKeys } from '@/lib/queryKeys';

// Global configuration in QueryClient
export const queryClientConfig = {
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60 * 2, // Data remains "fresh" for 2 min before background refetches occur
      gcTime: 1000 * 60 * 30, // Unused inactive queries remain in memory cache for 30 min
      retry: (failureCount: number, error: any) => {
        if (error?.status === 404 || error?.status === 401) return false; // Never retry client errors
        return failureCount < 3; // Retry server errors up to 3 times
      },
      retryDelay: (attemptIndex: number) => Math.min(1000 * 2 ** attemptIndex, 30000), // Exponential backoff
    },
  },
};

// Paginated query with smooth transitions
export function usePaginatedItems(page: number) {
  const queryClient = useQueryClient();

  const query = useQuery({
    queryKey: ['items', page] as const,
    queryFn: () => fetch(`/api/items?page=${page}`).then((r) => r.json()),
    placeholderData: keepPreviousData, // Keeps previous page visible while fetching next page
  });

  // Prefetch the next page on idle / current view
  const prefetchNextPage = () => {
    queryClient.prefetchQuery({
      queryKey: ['items', page + 1] as const,
      queryFn: () => fetch(`/api/items?page=${page + 1}`).then((r) => r.json()),
      staleTime: 1000 * 60 * 2,
    });
  };

  return { ...query, prefetchNextPage };
}
```
