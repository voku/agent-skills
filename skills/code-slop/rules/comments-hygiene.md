---
id: comments-hygiene
title: Comment Hygiene and Intentional Explanations
category: comments
priority: CRITICAL
triggers: [comment-narration, empty-docblock, placeholder-comment, closing-brace-label]
tags: [comments, documentation, slop-reduction, clean-code]
---

# Comment Hygiene and Intentional Explanations

**Trigger Anchor:** Strip line-by-line comment narration, empty redundant docblocks, closing-brace tags (`} // end if`), and lingering placeholder/TODO markers; comments must explain *why* (non-obvious domain constraints, external vendor quirks), never *what* the code already expresses.

---

### Bad
```php
<?php

declare(strict_types=1);

/**
 * Class UserManager
 * Handles user creation
 */
class UserManager
{
    /**
     * Create user
     * @param array $data
     * @return User
     */
    public function createUser(array $data): User
    {
        // Validate the incoming data
        $validated = Validator::make($data, ['email' => 'required|email'])->validate();

        // Instantiate and save the new user record
        $user = User::create($validated);

        // Send a welcome email to the newly created user
        Mail::to($user)->send(new WelcomeEmail($user));

        // Return the user model instance
        return $user;
    } // end createUser
} // end UserManager
```

```typescript
// ❌ Redundant narration and tutorial-style comments
function calculateTotal(items: CartItem[]): number {
  // Initialize total accumulator to 0
  let total = 0;

  // Loop through each item in the cart
  for (const item of items) {
    // Multiply price by quantity and add to total
    total += item.price * item.quantity;
  }

  // Return the accumulated total value
  return total;
} // end calculateTotal
```

### Good
```php
<?php

declare(strict_types=1);

final readonly class UserManager
{
    public function createUser(array $data): User
    {
        $validated = Validator::make($data, ['email' => 'required|email'])->validate();
        $user = User::create($validated);
        Mail::to($user)->send(new WelcomeEmail($user));

        return $user;
    }
}
```

```typescript
// ✅ Self-documenting code with comments reserved strictly for load-bearing constraints
function calculateTotal(items: CartItem[]): number {
  const subtotal = items.reduce((sum, item) => sum + item.price * item.quantity, 0);

  // Stripe rejects single charges > $999,999.99 (expressed in integer cents)
  return Math.min(subtotal, 99_999_999);
}
```
