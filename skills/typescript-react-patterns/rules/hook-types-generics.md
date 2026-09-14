---
id: hook-types-generics
title: "Hook Typing: Generics, Reducers, and Return Tuples"
category: hook
priority: CRITICAL
triggers: [untyped-use-state, unconstrained-custom-hook, use-reducer-any-action, missing-as-const-tuple]
tags: [react, typescript, hooks, usestate, usereducer, generics]
---

# Hook Typing: Generics, Reducers, and Return Tuples

**Trigger Anchor:** Provide explicit generic types when `useState<T>` initial values are null/optional, type `useReducer` actions as discriminated unions with exhaustive checks, and type custom hook return tuples using `as const`.

---

### Bad
```tsx
// ❌ Untyped state inferred as null / never, generic reducer action without discrimination
import { useReducer, useState } from 'react';

export function BadComponent() {
  const [user, setUser] = useState(null); // Inferred as null, setUser({ name: 'Alice' }) errors!

  const [state, dispatch] = useReducer((state: any, action: any) => {
    switch (action.type) {
      case 'INCREMENT': return { count: state.count + action.payload };
    }
  }, { count: 0 });
}
```

### Good
```tsx
import { useCallback, useReducer, useState } from 'react';

interface User {
  id: string;
  name: string;
}

// ✅ Explicit generic type for optional or delayed state
export function UserProfile() {
  const [user, setUser] = useState<User | null>(null);
}

// ✅ Discriminated union actions for useReducer
type CounterAction =
  | { type: 'increment'; step?: number }
  | { type: 'decrement'; step?: number }
  | { type: 'reset' };

interface CounterState {
  count: number;
}

function counterReducer(state: CounterState, action: CounterAction): CounterState {
  switch (action.type) {
    case 'increment':
      return { count: state.count + (action.step ?? 1) };
    case 'decrement':
      return { count: state.count - (action.step ?? 1) };
    case 'reset':
      return { count: 0 };
    default: {
      const _exhaustive: never = action;
      return state;
    }
  }
}

// ✅ Custom hook returning typed tuple using `as const`
export function useToggle(initialValue = false) {
  const [value, setValue] = useState(initialValue);
  const toggle = useCallback(() => setValue((prev) => !prev), []);

  return [value, toggle] as const; // Infers readonly [boolean, () => void] instead of (boolean | (() => void))[]
}
```
