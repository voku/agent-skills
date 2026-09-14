---
id: rq-advanced-patterns
title: "Advanced React Query: Infinite Scrolling, Parallel Queries, and Cancellation"
category: advanced
priority: HIGH
triggers: [infinite-queries-pagination, usequeries-parallel, dependent-queries, query-cancellation-abortsignal, usesuspensequery]
tags: [react-query, infinite-scroll, useinfinitequery, usequeries, abortsignal, suspense]
---

# Advanced React Query: Infinite Scrolling, Parallel Queries, and Cancellation

**Trigger Anchor:** Use `useInfiniteQuery` with `initialPageParam` for cursor/offset streams, coordinate dynamic parallel fetches with `useQueries`, pass `signal` for automatic cancellation, and replace `suspense: true` with `useSuspenseQuery`.

---

### Bad
```tsx
// ❌ Manual pagination state in useEffect, un-cancellable requests, and deprecated suspense option
function BadFeed() {
  const [pages, setPages] = useState<any[]>([]); // Manually managing array state creates desync bugs
  const [cursor, setCursor] = useState<string | null>(null);

  // ❌ Deprecated in v5: `suspense: true` is no longer supported on standard useQuery
  const { data } = useQuery({
    queryKey: ['feed', cursor],
    queryFn: () => fetch(`/api/feed?cursor=${cursor}`).then((r) => r.json()), // No AbortSignal support
    suspense: true,
  });

  useEffect(() => {
    if (data) setPages((prev) => [...prev, ...data.items]);
  }, [data]);
}
```

### Good
```tsx
// ✅ TanStack Query v5: Typed infinite query with intersection observer and AbortSignal cancellation
import { useInfiniteQuery, useQueries, useSuspenseQuery } from '@tanstack/react-query';
import { useEffect, useRef } from 'react';

interface FeedResponse {
  items: Array<{ id: string; title: string }>;
  nextCursor: string | null;
}

// 1. Infinite Stream Query
export function useInfiniteFeed() {
  return useInfiniteQuery({
    queryKey: ['feed', 'stream'] as const,
    queryFn: async ({ pageParam, signal }): Promise<FeedResponse> => {
      const url = pageParam ? `/api/feed?cursor=${pageParam}` : '/api/feed';
      const res = await fetch(url, { signal }); // Native browser cancellation when unmounted/superseded
      if (!res.ok) throw new Error('Failed to fetch stream page');
      return res.json();
    },
    initialPageParam: null as string | null,
    getNextPageParam: (lastPage) => lastPage.nextCursor,
    maxPages: 10, // Prevent runaway memory growth on extended mobile scrolling
  });
}

// 2. Infinite Scroll Component with Intersection Observer
export function FeedList() {
  const { data, fetchNextPage, hasNextPage, isFetchingNextPage } = useInfiniteFeed();
  const sentinelRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!sentinelRef.current || !hasNextPage || isFetchingNextPage) return;

    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) fetchNextPage();
    });

    observer.observe(sentinelRef.current);
    return () => observer.disconnect();
  }, [hasNextPage, isFetchingNextPage, fetchNextPage]);

  const allItems = data?.pages.flatMap((page) => page.items) ?? [];

  return (
    <div>
      {allItems.map((item) => (
        <article key={item.id}>{item.title}</article>
      ))}
      <div ref={sentinelRef} className="h-4" />
      {isFetchingNextPage && <p>Loading more...</p>}
    </div>
  );
}

// 3. Dynamic Parallel Queries with useQueries
export function useMultipleProfiles(userIds: string[]) {
  return useQueries({
    queries: userIds.map((id) => ({
      queryKey: ['user', id] as const,
      queryFn: ({ signal }: { signal: AbortSignal }) =>
        fetch(`/api/users/${id}`, { signal }).then((r) => r.json()),
      staleTime: 1000 * 60 * 5,
    })),
  });
}
```
