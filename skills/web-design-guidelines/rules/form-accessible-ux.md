---
id: form-accessible-ux
title: "Accessible Forms: Labels, Input Types, Autocomplete, and Validation Feedback"
category: form
priority: HIGH
triggers: [form-accessibility, missing-form-label, inline-validation-ux, input-autocomplete, aria-describedby-error]
tags: [forms, a11y, validation, autocomplete, aria, ux]
---

# Accessible Forms: Labels, Input Types, Autocomplete, and Validation Feedback

**Trigger Anchor:** Associate every input with a persistent `<label>`, link error messages via `aria-describedby` and `aria-invalid`, specify exact `type` and `autoComplete` attributes, and validate on blur/submit rather than premature keystrokes.

---

### Bad
```tsx
// ❌ Placeholder as label, missing autocomplete, generic input types, premature validation
export function BadLoginForm() {
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');

  return (
    <form>
      {/* ❌ Placeholder disappears on typing; screen readers have no permanent label */}
      <input
        type="text" // ❌ Missing type="email" breaks mobile keyboard optimizations
        placeholder="Enter email address"
        value={email}
        onChange={(e) => {
          setEmail(e.target.value);
          // ❌ Aggressive premature validation while the user is still typing their first character
          if (!e.target.value.includes('@')) setError('Invalid email');
        }}
      />
      {/* ❌ Error text is unlinked from input: screen readers will not announce the error on focus */}
      {error && <span style={{ color: 'red' }}>{error}</span>}
      <button type="submit">Submit</button>
    </form>
  );
}
```

### Good
```tsx
// ✅ Fully accessible form input with persistent label, autocomplete, aria-describedby, and blur validation
import { useState, useId } from 'react';

export function AccessibleInputField({
  label,
  type = 'text',
  autoComplete,
  required = false,
  validate,
}: {
  label: string;
  type?: string;
  autoComplete?: string;
  required?: boolean;
  validate?: (val: string) => string | null;
}) {
  const inputId = useId();
  const errorId = `${inputId}-error`;
  const [value, setValue] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [touched, setTouched] = useState(false);

  const handleBlur = () => {
    setTouched(true);
    if (validate) setError(validate(value));
  };

  return (
    <div className="flex flex-col space-y-1.5">
      <label htmlFor={inputId} className="text-sm font-medium text-zinc-900">
        {label} {required && <span aria-hidden="true" className="text-rose-600">*</span>}
      </label>

      <input
        id={inputId}
        type={type}
        autoComplete={autoComplete}
        required={required}
        aria-required={required}
        aria-invalid={Boolean(touched && error)}
        aria-describedby={touched && error ? errorId : undefined}
        value={value}
        onChange={(e) => {
          setValue(e.target.value);
          // Clear error when user corrects it, but re-validate on blur
          if (error && validate) setError(validate(e.target.value));
        }}
        onBlur={handleBlur}
        className={`rounded-lg border px-3.5 py-2 text-sm text-zinc-900 transition focus:outline-none focus:ring-2 ${
          touched && error
            ? 'border-rose-500 focus:border-rose-500 focus:ring-rose-200'
            : 'border-zinc-300 focus:border-indigo-600 focus:ring-indigo-100'
        }`}
      />

      {touched && error && (
        <p id={errorId} role="alert" className="text-xs font-medium text-rose-600">
          {error}
        </p>
      )}
    </div>
  );
}
```
