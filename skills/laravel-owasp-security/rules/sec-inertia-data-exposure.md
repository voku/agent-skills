---
id: sec-inertia-data-exposure
title: "Prevent Inertia.js Data Exposure and Model Over-Serialization"
category: inertia-security
priority: CRITICAL
triggers: [inertia-raw-model-prop, secret-in-data-page, unmasked-api-key-frontend, handle-inertia-requests-leak]
tags: [security, laravel, inertia, react, data-exposure, api-resources, owasp]
---

# Prevent Inertia.js Data Exposure and Model Over-Serialization

**Trigger Anchor:** Never pass raw Eloquent models or secret credentials into `Inertia::render()` props or `HandleInertiaRequests::share()`; props serialize into the HTML `data-page` attribute and are publicly visible in page source. Use API Resources or explicit array filtering.

---

### Bad
```php
// ❌ Passing raw Eloquent model exposes password_hash, remember_token, and 2FA secrets
class UserController extends Controller
{
    public function show(User $user): Response
    {
        return Inertia::render('admin/users/show', [
            'user' => $user, // Serializes all hidden/protected attributes into data-page!
        ]);
    }
}

// ❌ Passing secret API keys to frontend props
class SettingsController extends Controller
{
    public function index(): Response
    {
        return Inertia::render('admin/settings/index', [
            'stripe_secret' => config('services.stripe.secret'), // Publicly visible in HTML source!
        ]);
    }
}
```

### Good
```php
// ✅ Explicit transformation via JsonResource or mapped array selection
class UserController extends Controller
{
    public function show(User $user): Response
    {
        return Inertia::render('admin/users/show', [
            'user' => [
                'id'         => $user->id,
                'name'       => $user->name,
                'email'      => $user->email,
                'role'       => $user->role,
                'created_at' => $user->created_at?->toIso8601String(),
            ],
        ]);
    }
}

// ✅ Expose only masked metadata or public publishable keys
class SettingsController extends Controller
{
    public function index(): Response
    {
        return Inertia::render('admin/settings/index', [
            'stripe_key'     => config('services.stripe.key'), // Public key only
            'has_secret_set' => filled(config('services.stripe.secret')), // Boolean indicator
        ]);
    }
}
```
