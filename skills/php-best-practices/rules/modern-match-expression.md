# Match Expression

## Why it matters
`switch` has two traps: loose comparison (`==`) silently coerces types, and fall-through means a missing `break` delivers the wrong branch without any error. `match` uses strict comparison, always returns a value, and throws `UnhandledMatchError` on a missing arm — bugs surface immediately instead of silently misbehaving.

## Rule
Prefer `match` over `switch` for expression-oriented branching. When matching an enum, omit `default` so `UnhandledMatchError` fires on unhandled cases rather than silently using a fallback.

## Bad
```php
<?php

declare(strict_types=1);

function label(string $status): string
{
    switch ($status) {
        case 'active':
            $label = 'Active';
            break;
        case 'inactive':
            $label = 'Inactive';
            // missing break — falls through to default silently
        default:
            $label = 'Unknown';
    }
    return $label;
}
```

## Better
```php
<?php

declare(strict_types=1);

function label(string $status): string
{
    return match ($status) {
        'active'   => 'Active',
        'inactive' => 'Inactive',
        default    => 'Unknown',
    };
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

// No default: UnhandledMatchError fires if a new case is added but not handled here
function label(OrderStatus $status): string
{
    return match ($status) {
        OrderStatus::Pending  => 'Awaiting payment',
        OrderStatus::Paid     => 'Payment received',
        OrderStatus::Shipped  => 'On its way',
    };
}
```

## Exceptions / trade-offs
- When genuine fall-through is needed (multiple inputs share one result), `match` supports comma-separated arms: `'a', 'b' => 'result'` — this is not a reason to keep `switch`.
- Complex compound conditions that cannot be expressed as simple value equality (e.g., range checks, regex, multiple variables) are better served by `if`/`elseif` or a strategy pattern.

## Static-analysis notes
PHPStan and Psalm verify exhaustiveness when `match` operates on an enum type with no `default` arm. Adding a new enum case without updating every `match` site becomes a static analysis error.

## Version notes
`PHP 8.0+`

## Related topics
- [modern-enums.md](modern-enums.md) — backed enums as safe match subjects
- [modern-enums-methods.md](modern-enums-methods.md) — exhaustive match inside enum methods
