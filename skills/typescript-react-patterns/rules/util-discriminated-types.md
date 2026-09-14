---
id: util-discriminated-types
title: "Utility Types, Discriminated Unions, and Prop Derivations"
category: util
priority: LOW
triggers: [un-discriminated-loading-state, manual-prop-duplication, missing-component-props-without-ref]
tags: [typescript, utility-types, discriminated-unions, pick, omit, componentpropswithoutref]
---

# Utility Types, Discriminated Unions, and Prop Derivations

**Trigger Anchor:** Model asynchronous UI states as discriminated unions (`idle | loading | success | error`), inherit HTML element attributes via `ComponentPropsWithoutRef<T>`, and derive related prop types with `Pick` and `Omit`.

---

### Bad
```tsx
// ❌ Impossible state combinations: loading=true AND error="Failed" AND data=[...]
interface FetchState {
  isLoading: boolean;
  error: string | null;
  data: string[] | null;
}

// ❌ Manually re-declaring HTML button attributes
interface CustomButtonProps {
  label: string;
  disabled?: boolean;
  type?: 'button' | 'submit' | 'reset';
  tabIndex?: number;
  // Missing 30 other standard button attributes
}
```

### Good
```tsx
import type { ComponentPropsWithoutRef } from 'react';

// ✅ Discriminated union enforces strictly valid UI state combinations
export type AsyncDataState<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; error: Error };

// ✅ Inherit native HTML attributes while omitting or overriding specific keys
export interface CustomButtonProps
  extends Omit<ComponentPropsWithoutRef<'button'>, 'className'> {
  variant: 'primary' | 'danger' | 'ghost';
  isLoading?: boolean;
}

export function CustomButton({
  variant,
  isLoading = false,
  children,
  disabled,
  ...props
}: CustomButtonProps) {
  return (
    <button
      className={`btn btn--${variant}`}
      disabled={disabled || isLoading}
      {...props}
    >
      {isLoading ? <span className="spinner" /> : children}
    </button>
  );
}
```
