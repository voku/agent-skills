---
id: modern-enums
title: Enums as First-Class Domain Types
category: modern
priority: CRITICAL
triggers: [magic-constants, string-type-flags, enum-methods, enum-interface]
tags: [enums, backed-enums, modern-php, php81]
---

# Enums as First-Class Domain Types

**Trigger Anchor:** Replace class constants and string flags with backed or pure enums. Add domain methods and implement interfaces directly on enums.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Untyped string constants prone to typos and missing compiler validation
class Order
{
    public const STATUS_PENDING = 'pending';
    public const STATUS_PAID = 'paid';
    public const STATUS_CANCELLED = 'cancelled';

    public function setStatus(string $status): void
    {
        // accepts any string, e.g. "pendng"
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

interface HasLabel
{
    public function label(): string;
}

// ✅ Backed enum with methods, type safety, and exhaustive match validation
enum OrderStatus: string implements HasLabel
{
    case Pending = 'pending';
    case Paid = 'paid';
    case Cancelled = 'cancelled';

    public function label(): string
    {
        return match ($this) {
            self::Pending => 'Pending Payment',
            self::Paid => 'Paid and Confirmed',
            self::Cancelled => 'Order Cancelled',
        };
    }

    public function isTerminal(): bool
    {
        return $this === self::Cancelled || $this === self::Paid;
    }
}

final class Order
{
    public function __construct(
        private OrderStatus $status = OrderStatus::Pending
    ) {}

    public function setStatus(OrderStatus $status): void
    {
        $this->status = $status;
    }
}
```
