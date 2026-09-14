---
id: page-props-reloads
title: Page Props, TypeScript Contracts, Head, and Partial Reloads
category: page
priority: CRITICAL
triggers: [untyped-inertia-page-props, missing-head-title, full-page-reload-overhead, scroll-reset-on-filter]
tags: [inertia, react, typescript, pageprops, head, partial-reloads]
---

# Page Props, TypeScript Contracts, Head, and Partial Reloads

**Trigger Anchor:** Strongly type Inertia page props with `PageProps<T>`, manage title and SEO metadata with `<Head>`, and optimize filtering/pagination with partial reloads (`only: ['users']`) and scroll preservation (`preserveScroll: true`).

---

### Bad
```tsx
// ❌ Untyped props, missing Head component, and full-page payload re-fetching
export default function UsersIndex(props: any) {
  const applyFilter = (role: string) => {
    // ❌ Reloads the entire page payload including heavy shared data and auth user
    window.location.href = `/users?role=${role}`;
  };

  return <div>{props.users.map((u: any) => u.name)}</div>;
}
```

### Good
```tsx
import type { PageProps } from '@/types';
import { Head, router } from '@inertiajs/react';

interface UserItem {
  id: number;
  name: string;
  email: string;
}

interface UsersIndexProps extends PageProps {
  users: {
    data: UserItem[];
    total: number;
  };
  filters: {
    role?: string;
  };
}

export default function UsersIndex({ users, filters }: UsersIndexProps) {
  const handleRoleFilter = (role: string) => {
    // ✅ Partial reload fetches only `users` and preserves vertical scroll position
    router.get(
      '/users',
      { role },
      {
        only: ['users', 'filters'],
        preserveState: true,
        preserveScroll: true,
      },
    );
  };

  return (
    <>
      <Head title="User Directory">
        <meta name="description" content="Manage organizational users and roles" />
      </Head>

      <div className="p-6">
        <h1 className="text-2xl font-bold">Users ({users.total})</h1>
        {/* Render filtered users */}
      </div>
    </>
  );
}
```
