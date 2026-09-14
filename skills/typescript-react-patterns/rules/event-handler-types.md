---
id: event-handler-types
title: DOM Event Handlers and SyntheticEvent Generics
category: event
priority: HIGH
triggers: [untyped-event-handler, any-event-parameter, missing-html-element-target, event-type-mismatch]
tags: [react, typescript, events, form-event, mouse-event, change-event]
---

# DOM Event Handlers and SyntheticEvent Generics

**Trigger Anchor:** Type event handlers using React's SyntheticEvent generics specifying the exact HTML target element (`ChangeEvent<HTMLInputElement>`, `FormEvent<HTMLFormElement>`, `MouseEvent<HTMLButtonElement>`).

---

### Bad
```tsx
// ❌ Using `any` or native DOM Event instead of React SyntheticEvents
export function SearchForm() {
  const handleChange = (e: any) => {
    console.log(e.target.value);
  };

  const handleSubmit = (e: Event) => { // ❌ Native Event causes type error on form onSubmit
    e.preventDefault();
  };

  return (
    <form onSubmit={handleSubmit}>
      <input onChange={handleChange} />
    </form>
  );
}
```

### Good
```tsx
import type { ChangeEvent, FormEvent, KeyboardEvent, MouseEvent } from 'react';

export function SearchForm() {
  // ✅ Precise React ChangeEvent with specific HTMLInputElement generic
  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    console.log(e.target.value); // Typed as string
  };

  // ✅ FormEvent with HTMLFormElement
  const handleFormSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
  };

  // ✅ Keyboard event checking specific keys
  const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      console.log('Submitted via Enter');
    }
  };

  // ✅ Button click with MouseEvent<HTMLButtonElement>
  const handleClear = (e: MouseEvent<HTMLButtonElement>) => {
    e.stopPropagation();
  };

  return (
    <form onSubmit={handleFormSubmit}>
      <input type="text" onChange={handleInputChange} onKeyDown={handleKeyDown} />
      <button type="button" onClick={handleClear}>Clear</button>
    </form>
  );
}
```
