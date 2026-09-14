---
id: style-fingerprints
title: Natural Engineering Idioms vs AI Fingerprints
category: style
priority: MEDIUM
triggers: [debug-artifacts, type-escape-hatch, trivial-boolean-boilerplate, hyper-consistent-slop]
tags: [style, idioms, typescript, php, code-review]
---

# Natural Engineering Idioms vs AI Fingerprints

**Trigger Anchor:** Eliminate debug dumps (`console.log`, `dd()`), type-system escape hatches (`as any`, `@ts-ignore`), and trivial boilerplate (`if (x) return true; else return false`); write idiomatic, direct expressions.

---

### Bad
```typescript
// ❌ Debug left behind, type escape hatch, and verbose boolean boilerplate
export function isUserEligible(user: unknown): boolean {
  console.log('Evaluating user eligibility:', user); // ❌ Debug artifact

  // ❌ Blind type escape rather than runtime guard / narrowing
  const roleName = (user as any)?.role?.name;

  // ❌ Trivial boolean branch
  if (roleName === 'admin' || roleName === 'manager') {
    return true;
  } else {
    return false;
  }
}
```

```php
<?php

declare(strict_types=1);

// ❌ Leftover dump and verbose boilerplate
class CartValidator
{
    public function isValid(Cart $cart): bool
    {
        dump($cart->items); // ❌ Leftover debug artifact

        // ❌ Redundant variable assignment and ternary boilerplate
        $itemCount = count($cart->items);
        $hasItems = $itemCount > 0 ? true : false;

        return $hasItems;
    }
}
```

### Good
```typescript
// ✅ Type-safe narrowing, zero console leaks, idiomatic boolean return
interface UserWithRole {
  role: { name: string };
}

function hasRole(user: unknown): user is UserWithRole {
  return typeof user === 'object' && user !== null && 'role' in user;
}

export function isUserEligible(user: unknown): boolean {
  if (!hasRole(user)) {
    return false;
  }

  return user.role.name === 'admin' || user.role.name === 'manager';
}
```

```php
<?php

declare(strict_types=1);

// ✅ Direct, readable expression with zero debug clutter
final readonly class CartValidator
{
    public function isValid(Cart $cart): bool
    {
        return count($cart->items) > 0;
    }
}
```
