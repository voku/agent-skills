---
id: auth-testing
title: "Authentication Testing: Web Guards and Sanctum Tokens"
category: auth
priority: HIGH
triggers: [unauthenticated-401-in-test, sanctum-token-scope-test, acting-as-guard-mismatch]
tags: [laravel, testing, auth, sanctum, actingAs, guards, permissions]
---

# Authentication Testing: Web Guards and Sanctum Tokens

**Trigger Anchor:** Authenticate test requests using `actingAs($user, $guard)` for session web guards, and `Sanctum::actingAs($user, $abilities)` for token-authenticated API endpoints.

---

### Bad
```php
<?php

// ❌ Manually forging session cookies or sending raw passwords to login endpoint repeatedly
test('user updates profile', function () {
    // ❌ Slow: makes 2 HTTP requests per test instead of actingAs
    $this->post('/login', ['email' => 'user@example.com', 'password' => 'secret']);
    $response = $this->put('/profile', ['name' => 'New Name']);
});
```

### Good
```php
<?php

declare(strict_types=1);

use App\Models\User;
use Laravel\Sanctum\Sanctum;

// ✅ Session-based authentication via actingAs helper
test('authenticated user can view dashboard', function () {
    $user = User::factory()->create();

    $this->actingAs($user)
        ->get('/dashboard')
        ->assertOk()
        ->assertSee($user->name);
});

// ✅ Sanctum API token authentication with explicit ability scopes
test('token with write ability can update settings', function () {
    $user = User::factory()->create();

    Sanctum::actingAs($user, ['settings:write']);

    $this->putJson('/api/settings', ['theme' => 'dark'])
        ->assertOk();
});

test('token without write ability is forbidden', function () {
    $user = User::factory()->create();

    Sanctum::actingAs($user, ['settings:read']); // Missing write scope

    $this->putJson('/api/settings', ['theme' => 'dark'])
        ->assertForbidden();
});
```
