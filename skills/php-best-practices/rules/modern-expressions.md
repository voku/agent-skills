---
id: modern-expressions
title: Modern Expressions (Match, Nullsafe, Callables, Arrow Functions)
category: modern
priority: CRITICAL
triggers: [loose-switch, verbose-closure, nullsafe-chain, first-class-callable]
tags: [match, nullsafe, arrow-functions, first-class-callables, modern-php]
---

# Modern Expressions (Match, Nullsafe, Callables, Arrow Functions)

**Trigger Anchor:** Replace `switch` with `match` expressions. Use nullsafe operators (`?->`) for safe property/method chaining. Use arrow functions (`fn() => ...`) and first-class callables (`$this->method(...)`) over verbose closures.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Loose-comparison switch, manual null checking, verbose closure syntax
function formatUserStatus(?User $user): string
{
    if ($user === null || $user->getAddress() === null) {
        $country = 'Unknown';
    } else {
        $country = $user->getAddress()->getCountry();
    }

    switch ($user ? $user->getStatus() : '') {
        case 0: // loose comparison: matches false, null, empty string!
            $label = 'Inactive';
            break;
        case 'active':
            $label = 'Active';
            break;
        default:
            $label = 'Other';
    }

    $names = array_map(function ($item) {
        return trim($item);
    }, [' Alice ', ' Bob ']);

    return "{$country}: {$label}";
}
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ Match expression with strict comparison, nullsafe chain, first-class callable
function formatUserStatus(?User $user): string
{
    $country = $user?->getAddress()?->getCountry() ?? 'Unknown';

    $label = match ($user?->getStatus()) {
        'inactive' => 'Inactive',
        'active' => 'Active',
        default => 'Other',
    };

    // First-class callable trim(...) and arrow function
    $names = array_map(trim(...), [' Alice ', ' Bob ']);
    $upper = array_map(fn(string $s): string => strtoupper($s), $names);

    return "{$country}: {$label}";
}
```
