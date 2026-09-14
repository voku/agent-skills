---
id: shared-props-middleware
title: Shared Props and Global State via HandleInertiaRequests
category: shared
priority: HIGH
triggers: [duplicated-auth-prop-in-controllers, missing-flash-notification, untyped-usepage-hook]
tags: [inertia, laravel, middleware, HandleInertiaRequests, shared-data, flash-messages]
---

# Shared Props and Global State via HandleInertiaRequests

**Trigger Anchor:** Centralize global application state (authenticated user, flash messages, Ziggy routes) in `HandleInertiaRequests::share()`, and access them type-safely via `usePage<PageProps>()`.

---

### Bad
```php
<?php

// ❌ Duplicating authenticated user and flash state manually across 30 controllers
class DashboardController extends Controller
{
    public function index()
    {
        return Inertia::render('Dashboard', [
            'auth_user' => auth()->user(), // ❌ Manual duplicate in every controller
            'flash_success' => session('success'),
        ]);
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

namespace App\Http\Middleware;

use Illuminate\Http\Request;
use Inertia\Middleware;

final class HandleInertiaRequests extends Middleware
{
    protected $rootView = 'app';

    /**
     * @return array<string, mixed>
     */
    public function share(Request $request): array
    {
        return [
            ...parent::share($request),
            // ✅ Global auth state shared lazily
            'auth' => [
                'user' => $request->user() ? [
                    'id' => $request->user()->id,
                    'name' => $request->user()->name,
                    'email' => $request->user()->email,
                    'role' => $request->user()->role,
                ] : null,
            ],
            // ✅ Global flash messages
            'flash' => [
                'success' => fn () => $request->session()->get('success'),
                'error' => fn () => $request->session()->get('error'),
            ],
        ];
    }
}
```

```tsx
import type { PageProps } from '@/types';
import { usePage } from '@inertiajs/react';

export function FlashBanner() {
  // ✅ Strongly-typed shared props
  const { flash, auth } = usePage<PageProps>().props;

  if (!flash.success) return null;

  return (
    <div className="alert alert--success">
      <p>{flash.success}</p>
    </div>
  );
}
```
