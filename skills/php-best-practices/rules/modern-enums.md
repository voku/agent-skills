# Enums

## Why it matters
Class constants typed as `string` or `int` accept any value of that type — passing `'AKTIVE'` instead of `'active'` is a silent runtime bug. Enums create a closed set enforced by the type system: an invalid case literally cannot be constructed, and every match or comparison is checked by static analysis and the runtime.

## Rule
Prefer backed enums over magic strings and class constants for any fixed set of domain states or categories. Use `from()` / `tryFrom()` at the boundary (input parsing) and the enum type everywhere else.

## Bad
```php
<?php

declare(strict_types=1);

final class OrderStatus
{
    public const PENDING  = 'pending';
    public const PAID     = 'paid';
    public const SHIPPED  = 'shipped';
}

// Accepts any string — no compile-time or static-analysis safety
function shipOrder(string $status): void
{
    if ($status === OrderStatus::SHIPPED) { /* ... */ }
}

shipOrder('shiped'); // typo — no error, wrong branch taken
```

## Better
```php
<?php

declare(strict_types=1);

enum OrderStatus
{
    case Pending;
    case Paid;
    case Shipped;
}

// Unit enum: type-safe, but no serialisation value
function shipOrder(OrderStatus $status): void
{
    if ($status === OrderStatus::Shipped) { /* ... */ }
}
```

## Best
```php
<?php

declare(strict_types=1);

enum OrderStatus: string
{
    case Pending  = 'pending';
    case Paid     = 'paid';
    case Shipped  = 'shipped';
}

// Safe boundary conversion — returns null on unknown value
$status = OrderStatus::tryFrom($request->get('status'));

if ($status === null) {
    throw new \InvalidArgumentException('Unknown order status.');
}

// Everywhere else: the type system prevents invalid values
function shipOrder(OrderStatus $status): void
{
    if ($status === OrderStatus::Shipped) { /* ... */ }
}
```

## Exceptions / trade-offs
- Open-ended or user-defined value sets (e.g., user-created tags, plugin-registered types) are not a fixed set — use a validated string or a domain class instead.
- When the set of valid values is driven entirely by external configuration or a database, enums are the wrong tool.

## Static-analysis notes
PHPStan and Psalm enforce exhaustive `match` on enum types, flagging unhandled cases. Attempting to pass a plain string where an enum is expected is a type error. `from()` is typed as returning the enum; `tryFrom()` returns `?EnumType`, forcing explicit null handling.

## Version notes
`PHP 8.1+`

## Related topics
- [modern-enums-methods.md](modern-enums-methods.md) — add behaviour directly to enums
- [modern-match-expression.md](modern-match-expression.md) — exhaustive matching over enum cases
