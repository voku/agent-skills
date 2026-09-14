---
id: rq-query-fundamentals
title: "React Query Fundamentals: Key Factories, Query Functions, and Select Transforms"
category: query
priority: CRITICAL
triggers: [react-query-setup, query-key-factory, usequery-pattern, conditional-query-enabled, select-data-transform]
tags: [react-query, tanstack-query, usequery, query-keys, select, enabled]
---

# React Query Fundamentals: Key Factories, Query Functions, and Select Transforms

**Trigger Anchor:** Organize query keys with typed array factories (`as const`), pass typed query functions with abort signals, gate executions with `enabled`, and optimize re-renders using `select` projections.

---

### Bad
```tsx
// ❌ Inline magic strings, untyped query functions, inline data munging causing unnecessary re-renders
export function BadUserView({ userId }: { userId?: string }) {
  // Magic string queryKey clashes easily; query runs even if userId is undefined
  const { data, isLoading } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetch(`/api/users/${userId}`).then((r) => r.json()),
  });

  // Re-filtering inside render body creates fresh reference every render
  const activeProjects = data?.projects.filter((p: any) => p.status === 'active') ?? [];

  return <div>{isLoading ? 'Loading...' : `Active: ${activeProjects.length}`}</div>;
}
```

### Good
```tsx
// ✅ lib/queryKeys.ts: Centralized, type-safe query key factory
export const queryKeys = {
  users: {
    all: ['users'] as const,
    lists: () => [...queryKeys.users.all, 'list'] as const,
    list: (filters: Record<string, unknown>) => [...queryKeys.users.lists(), filters] as const,
    details: () => [...queryKeys.users.all, 'detail'] as const,
    detail: (id: string) => [...queryKeys.users.details(), id] as const,
  },
};
```

```tsx
// ✅ hooks/useActiveProjects.ts: Typed query, gated with enabled, and memoized select transform
import { useQuery } from '@tanstack/react-query';
import { queryKeys } from '@/lib/queryKeys';

interface Project {
  id: string;
  name: string;
  status: 'active' | 'archived';
}

interface UserProfile {
  id: string;
  name: string;
  projects: Project[];
}

async function fetchUserProfile(userId: string, signal?: AbortSignal): Promise<UserProfile> {
  const res = await fetch(`/api/users/${userId}`, { signal });
  if (!res.ok) throw new Error(`Failed to fetch user profile: ${res.statusText}`);
  return res.json();
}

export function useActiveProjects(userId?: string) {
  return useQuery({
    queryKey: queryKeys.users.detail(userId ?? ''),
    queryFn: ({ signal }) => fetchUserProfile(userId!, signal),
    // Gated: Query does not fire until userId is present
    enabled: Boolean(userId),
    // Select: Component only re-renders when the transformed result changes shallowly
    select: (user): Project[] => user.projects.filter((p) => p.status === 'active'),
    staleTime: 1000 * 60 * 5, // 5 minutes fresh
  });
}
```
