---
id: form-useform-lifecycle
title: "Form Lifecycle: useForm, Validation Errors, and File Uploads"
category: form
priority: CRITICAL
triggers: [manual-form-state, missing-validation-errors, unhandled-file-upload, missing-processing-disabled]
tags: [inertia, react, useform, validation-errors, file-upload, progress-bar]
---

# Form Lifecycle: useForm, Validation Errors, and File Uploads

**Trigger Anchor:** Manage forms via Inertia's `useForm<T>()` hook, bind Laravel validation errors per field (`errors.field`), disable submit buttons during `processing`, and track file upload progress (`progress.percentage`).

---

### Bad
```tsx
// ❌ Manual useState and axios calls bypassing Inertia's validation and error pipelines
import { useState } from 'react';
import axios from 'axios';

export function BadForm() {
  const [name, setName] = useState('');
  const [error, setError] = useState('');

  const submit = async (e: any) => {
    e.preventDefault();
    try {
      await axios.post('/users', { name });
    } catch (err: any) {
      setError(err.response?.data?.message); // ❌ Loses Laravel field-level error mapping
    }
  };

  return <form onSubmit={submit}><input onChange={e => setName(e.target.value)} /></form>;
}
```

### Good
```tsx
import type { FormEvent } from 'react';
import { useForm } from '@inertiajs/react';

interface CreateUserForm {
  name: string;
  email: string;
  avatar: File | null;
}

export function CreateUserModal() {
  const { data, setData, post, processing, errors, progress, reset, isDirty } =
    useForm<CreateUserForm>({
      name: '',
      email: '',
      avatar: null,
    });

  const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    post('/users', {
      onSuccess: () => reset(),
      preserveScroll: true,
    });
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label htmlFor="name" className="block text-sm font-medium">Name</label>
        <input
          id="name"
          type="text"
          value={data.name}
          onChange={(e) => setData('name', e.target.value)}
          className="input"
        />
        {errors.name && <p className="text-red-600 text-sm mt-1">{errors.name}</p>}
      </div>

      <div>
        <label htmlFor="avatar" className="block text-sm font-medium">Avatar</label>
        <input
          id="avatar"
          type="file"
          onChange={(e) => setData('avatar', e.target.files?.[0] ?? null)}
        />
        {progress && (
          <progress value={progress.percentage} max={100} className="w-full mt-2">
            {progress.percentage}%
          </progress>
        )}
        {errors.avatar && <p className="text-red-600 text-sm mt-1">{errors.avatar}</p>}
      </div>

      <button
        type="submit"
        disabled={processing || !isDirty}
        className="btn btn--primary"
      >
        {processing ? 'Saving...' : 'Create User'}
      </button>
    </form>
  );
}
```
