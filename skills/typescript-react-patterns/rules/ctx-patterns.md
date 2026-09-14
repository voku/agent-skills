---
id: ctx-patterns
title: "Context Typing: Null Initialization and Provider Guards"
category: ctx
priority: MEDIUM
triggers: [context-default-undefined-error, missing-provider-guard, untyped-context-value, context-reducer-pairing]
tags: [react, typescript, context, usecontext, custom-hook, provider]
---

# Context Typing: Null Initialization and Provider Guards

**Trigger Anchor:** Initialize Context with `null` default, export a custom hook that throws an informative error when invoked outside its Provider, and bundle Context with `useReducer` for modular state.

---

### Bad
```tsx
// ❌ Creating context with empty object cast as any; caller silently fails outside provider
import { createContext, useContext } from 'react';

const AuthContext = createContext<any>({}); // Hides missing provider bugs

export function useAuth() {
  return useContext(AuthContext); // Inferred as any, no type safety
}
```

### Good
```tsx
import { createContext, useContext, useMemo, useState, type ReactNode } from 'react';

interface AuthContextValue {
  user: User | null;
  isAuthenticated: boolean;
  login: (token: string) => Promise<void>;
  logout: () => void;
}

// ✅ Explicit null default avoids fabricating a fake initial context state
const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);

  const value = useMemo<AuthContextValue>(
    () => ({
      user,
      isAuthenticated: user !== null,
      login: async (token) => { /* ... */ },
      logout: () => setUser(null),
    }),
    [user],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

// ✅ Guarded custom hook guarantees non-null context value for consumers
export function useAuth(): AuthContextValue {
  const context = useContext(AuthContext);

  if (context === null) {
    throw new Error('useAuth must be used within an <AuthProvider>');
  }

  return context;
}
```
