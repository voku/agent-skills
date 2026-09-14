---
id: factory-definitions
title: "Model Factories, States, Relationships, and Sequences"
category: factory
priority: CRITICAL
triggers: [manual-model-instantiation-test, hardcoded-foreign-key-test, missing-factory-state]
tags: [laravel, factories, states, relationships, test-data]
---

# Model Factories, States, Relationships, and Sequences

**Trigger Anchor:** Define minimal default factory states, encapsulate variations in explicit state methods (`admin()`, `canceled()`), chain relationships with `for()` and `has()`, and generate alternating values with sequences.

---

### Bad
```php
<?php

// ❌ Manual verbose database seeding repeated across test cases
test('admin sees report', function () {
    $user = User::create([
        'name' => 'Admin',
        'email' => 'admin@example.com',
        'password' => bcrypt('secret'),
        'role' => 'admin', // ❌ Manually configured magic values
        'is_active' => true,
    ]);
});
```

### Good
```php
<?php

declare(strict_types=1);

namespace Database\Factories;

use App\Enums\UserRole;
use App\Models\User;
use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends Factory<User>
 */
final class UserFactory extends Factory
{
    protected $model = User::class;

    public function definition(): array
    {
        return [
            'name' => fake()->name(),
            'email' => fake()->unique()->safeEmail(),
            'role' => UserRole::Customer,
            'is_active' => true,
        ];
    }

    public function admin(): static
    {
        return $this->state(fn (array $attributes) => [
            'role' => UserRole::Admin,
        ]);
    }

    public function unverified(): static
    {
        return $this->state(fn (array $attributes) => [
            'email_verified_at' => null,
        ]);
    }
}
```

```php
<?php

declare(strict_types=1);

// ✅ Chaining states, relationships, and sequences cleanly in tests
$admin = User::factory()->admin()->create();

// Create 3 orders with alternating payment statuses for a specific user
$orders = Order::factory()
    ->count(3)
    ->for($admin)
    ->sequence(
        ['status' => 'paid'],
        ['status' => 'pending'],
        ['status' => 'failed'],
    )
    ->hasItems(2)
    ->create();
```
