---
id: ref-dom-imperative
title: "DOM Refs, Callback Refs, and Imperative Handles"
category: ref
priority: HIGH
triggers: [untyped-ref, ref-current-null-error, missing-use-imperative-handle-type, callback-ref-typing]
tags: [react, typescript, refs, useref, useimperativehandle, callback-ref]
---

# DOM Refs, Callback Refs, and Imperative Handles

**Trigger Anchor:** Initialize DOM refs with `useRef<T>(null)` using concrete HTMLElement types, use callback refs for dynamic nodes or ResizeObservers, and define handle interfaces when exposing methods via `useImperativeHandle`.

---

### Bad
```tsx
// ❌ Untyped ref, missing null initialization, and unsafe imperative exposure
import { useImperativeHandle, useRef } from 'react';

export function TextInput(props: any) {
  const inputRef = useRef(); // Inferred as RefObject<undefined>
  // inputRef.current.focus() causes TypeScript compilation error
}
```

### Good
```tsx
import { forwardRef, useImperativeHandle, useRef } from 'react';

// ✅ Interface defining the exact imperative methods exposed to parent
export interface TextInputHandle {
  focus: () => void;
  reset: () => void;
}

interface TextInputProps {
  label: string;
}

// ✅ forwardRef with <Handle, Props> generics
export const TextInput = forwardRef<TextInputHandle, TextInputProps>(function TextInput(
  { label },
  ref,
) {
  // ✅ Concrete DOM element type initialized with null
  const inputRef = useRef<HTMLInputElement>(null);

  useImperativeHandle(
    ref,
    () => ({
      focus: () => inputRef.current?.focus(),
      reset: () => {
        if (inputRef.current) {
          inputRef.current.value = '';
        }
      },
    }),
    [],
  );

  return (
    <label>
      {label}
      <input ref={inputRef} type="text" />
    </label>
  );
});
```
