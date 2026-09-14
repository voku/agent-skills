---
id: rq-mutations-optimistic
title: "React Query Mutations: Optimistic Updates, Rollback, and Invalidation"
category: mutation
priority: CRITICAL
triggers: [usemutation-setup, optimistic-update-rollback, cache-invalidation-pattern, setquerydata-mutation]
tags: [react-query, tanstack-query, usemutation, optimistic-updates, invalidation, rollback]
---

# React Query Mutations: Optimistic Updates, Rollback, and Invalidation

**Trigger Anchor:** Execute write operations via `useMutation`, apply optimistic UI updates by canceling inflight queries and snapshotting cache in `onMutate`, rollback on `onError`, and invalidate queries on `onSettled`.

---

### Bad
```tsx
// ❌ Optimistic update without rollback or query cancellation causes race conditions and lost data
const mutation = useMutation({
  mutationFn: updateTodo,
  onMutate: (updatedTodo) => {
    // ❌ No cancelQueries: inflight fetch can overwrite optimistic update immediately
    // ❌ No snapshot: if updateTodo fails on server, state remains corrupted in client cache
    queryClient.setQueryData(['todos'], (old: Todo[] = []) =>
      old.map((t) => (t.id === updatedTodo.id ? updatedTodo : t))
    );
  },
  onError: () => {
    // ❌ Can't recover previous state because it was never captured
    alert('Failed to update');
  },
});
```

### Good
```tsx
// ✅ Bulletproof optimistic update pattern with query cancellation, snapshot rollback, and settle invalidation
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { queryKeys } from '@/lib/queryKeys';

interface Todo {
  id: string;
  title: string;
  completed: boolean;
}

export function useToggleTodo() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async ({ id, completed }: { id: string; completed: boolean }) => {
      const res = await fetch(`/api/todos/${id}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ completed }),
      });
      if (!res.ok) throw new Error('Failed to toggle todo status');
      return res.json() as Promise<Todo>;
    },

    // When Mutate is called:
    onMutate: async (variables) => {
      const targetKey = ['todos', 'list'] as const;

      // 1. Cancel any outgoing refetches so they don't overwrite our optimistic update
      await queryClient.cancelQueries({ queryKey: targetKey });

      // 2. Snapshot the previous value
      const previousTodos = queryClient.getQueryData<Todo[]>(targetKey);

      // 3. Optimistically update to the new value
      queryClient.setQueryData<Todo[]>(targetKey, (old = []) =>
        old.map((todo) => (todo.id === variables.id ? { ...todo, completed: variables.completed } : todo))
      );

      // 4. Return context object with snapshotted value
      return { previousTodos, targetKey };
    },

    // If the mutation fails, use the context returned from onMutate to rollback
    onError: (err, variables, context) => {
      if (context?.previousTodos) {
        queryClient.setQueryData(context.targetKey, context.previousTodos);
      }
    },

    // Always refetch after error or success to guarantee synchronization with backend state
    onSettled: (data, error, variables, context) => {
      if (context?.targetKey) {
        queryClient.invalidateQueries({ queryKey: context.targetKey });
      }
    },
  });
}
```
