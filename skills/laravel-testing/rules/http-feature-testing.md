---
id: http-feature-testing
title: HTTP Feature Tests and Fluent JSON Assertions
category: http
priority: CRITICAL
triggers: [untested-endpoint, fragile-json-match, missing-refresh-database, noisy-status-assertion]
tags: [laravel, testing, http, pest, phpunit, json, feature-test]
---

# HTTP Feature Tests and Fluent JSON Assertions

**Trigger Anchor:** Structure HTTP endpoint tests around Arrange-Act-Assert, isolate tests with `RefreshDatabase`, and verify API payloads using fluent JSON assertions (`AssertableJson`).

---

### Bad
```php
<?php

// ❌ Fragile exact JSON string match and untested status codes
it('tests api orders', function () {
    $response = $this->get('/api/orders');

    // ❌ Breaks whenever timestamps or unrelated fields change
    $response->assertExactJson([
        'data' => [
            ['id' => 1, 'amount' => 100],
        ],
    ]);
});
```

### Good
```php
<?php

declare(strict_types=1);

use App\Models\Order;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Testing\Fluent\AssertableJson;

uses(RefreshDatabase::class);

test('returns a paginated list of orders for authenticated user', function () {
    // Arrange
    $user = User::factory()->create();
    Order::factory()->count(3)->for($user)->create();

    // Act
    $response = $this->actingAs($user)->getJson('/api/orders');

    // Assert
    $response->assertOk()
        ->assertJson(fn (AssertableJson $json) =>
            $json->has('data', 3)
                ->has('data.0', fn (AssertableJson $item) =>
                    $item->hasAll(['id', 'amount_cents', 'status', 'created_at'])
                        ->whereType('id', 'integer')
                        ->whereType('amount_cents', 'integer')
                        ->etc()
                )
                ->has('links')
                ->has('meta')
        );
});
```
