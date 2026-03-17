---
title: Value Objects Over Primitives
impact: HIGH
impactDescription: Eliminates primitive obsession, enforces domain invariants, improves type safety
tags: design, value-objects, domain-driven-design, primitives, type-safety
---

# Value Objects Over Primitives

Replace bare primitives (string, int, float) with small, immutable value objects that encapsulate domain meaning and invariants. A `string $email` says nothing about validity; an `Email` type guarantees a valid email address at construction time.

## Bad Example

```php
<?php

declare(strict_types=1);

// Primitive obsession — strings and ints everywhere
class OrderService
{
    public function createOrder(
        int $userId,          // Any integer? Negative IDs valid?
        string $email,        // Any string? "not-an-email" accepted?
        float $amount,        // Zero? Negative? What currency?
        string $currency,     // "BITCOIN"? "xyz"? No constraint
        string $status,       // "pending"|"active"? No enforcement
    ): void {
        // Validation scattered across every entry point
        if ($amount <= 0) {
            throw new \InvalidArgumentException('Amount must be positive');
        }
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new \InvalidArgumentException('Invalid email');
        }
        // ...
    }
}

// Caller can pass arguments in wrong order — no type system protection
$service->createOrder(
    userId: 42,
    email: 'user@example.com',
    amount: 99.99,
    currency: 'USD',
    status: 'pending',
);

// This is also valid PHP — same types, wrong values:
$service->createOrder(42, 'USD', 0.0, 'user@example.com', 'xyz');
```

## Good Example

```php
<?php

declare(strict_types=1);

// Value objects with self-validating constructors
final class UserId
{
    public function __construct(
        public readonly int $value,
    ) {
        if ($value <= 0) {
            throw new \InvalidArgumentException("UserId must be positive, got {$value}");
        }
    }

    public function equals(self $other): bool
    {
        return $this->value === $other->value;
    }

    public function __toString(): string
    {
        return (string) $this->value;
    }
}

final class Email
{
    public readonly string $value;

    public function __construct(string $raw)
    {
        $normalized = strtolower(trim($raw));
        if (!filter_var($normalized, FILTER_VALIDATE_EMAIL)) {
            throw new \InvalidArgumentException("Invalid email address: {$raw}");
        }
        $this->value = $normalized;
    }

    public function domain(): string
    {
        // '@' is guaranteed by the constructor's email validation
        $atPos = (int) strpos($this->value, '@');
        return substr($this->value, $atPos + 1);
    }

    public function equals(self $other): bool
    {
        return $this->value === $other->value;
    }
}

final class Money
{
    public function __construct(
        public readonly int $amount,      // always in minor units (cents)
        public readonly Currency $currency,
    ) {
        if ($amount < 0) {
            throw new \InvalidArgumentException('Money amount cannot be negative');
        }
    }

    public function add(self $other): self
    {
        if (!$this->currency->equals($other->currency)) {
            throw new \LogicException('Cannot add money in different currencies');
        }
        return new self($this->amount + $other->amount, $this->currency);
    }

    public function isZero(): bool
    {
        return $this->amount === 0;
    }
}

enum Currency: string
{
    case USD = 'USD';
    case EUR = 'EUR';
    case GBP = 'GBP';

    public function equals(self $other): bool
    {
        return $this === $other;
    }
}

enum OrderStatus: string
{
    case Pending  = 'pending';
    case Paid     = 'paid';
    case Shipped  = 'shipped';
    case Cancelled = 'cancelled';
}

// Service now has fully typed, self-validating parameters
class OrderService
{
    public function createOrder(
        UserId $userId,
        Email $email,
        Money $amount,
        OrderStatus $status = OrderStatus::Pending,
    ): Order {
        // No validation needed here — values are already valid
        return new Order($userId, $email, $amount, $status);
    }
}

// Impossible to pass arguments in wrong order — types are distinct
$service->createOrder(
    userId: new UserId(42),
    email: new Email('user@example.com'),
    amount: new Money(9999, Currency::USD),
);
```

## Designing Value Objects

A good value object:

```php
<?php

declare(strict_types=1);

/**
 * Immutable value object. Two Coordinates are equal when lat+lng match.
 */
final class Coordinates
{
    public function __construct(
        public readonly float $latitude,
        public readonly float $longitude,
    ) {
        if ($latitude < -90.0 || $latitude > 90.0) {
            throw new \InvalidArgumentException("Latitude {$latitude} out of range [-90, 90]");
        }
        if ($longitude < -180.0 || $longitude > 180.0) {
            throw new \InvalidArgumentException("Longitude {$longitude} out of range [-180, 180]");
        }
    }

    public function equals(self $other): bool
    {
        return $this->latitude === $other->latitude
            && $this->longitude === $other->longitude;
    }

    public function distanceKmTo(self $other): float
    {
        // Haversine formula — behavior lives with data
        $R  = 6371.0;
        $dLat = deg2rad($other->latitude  - $this->latitude);
        $dLng = deg2rad($other->longitude - $this->longitude);
        $a = sin($dLat / 2) ** 2
            + cos(deg2rad($this->latitude)) * cos(deg2rad($other->latitude)) * sin($dLng / 2) ** 2;
        return $R * 2 * atan2(sqrt($a), sqrt(1 - $a));
    }

    public function __toString(): string
    {
        return "{$this->latitude},{$this->longitude}";
    }
}
```

## When to Create a Value Object

| Primitive | Candidate Value Object | Reason |
|-----------|------------------------|--------|
| `string $email` | `Email` | Validation, normalization, domain methods |
| `int $userId` | `UserId` | Prevents mixing with other IDs; `positive-int` constraint |
| `float $amount` + `string $currency` | `Money` | Prevents currency mismatch; arithmetic behavior |
| `string $slug` | `Slug` | URL-safe validation, generation |
| `string $uuid` | `Uuid` | Format validation, version detection |
| `string $phone` | `PhoneNumber` | E.164 normalization, country code access |

## Why

- **Single Validation Point**: Invariants are enforced once, in the constructor, and guaranteed for the object's lifetime
- **Eliminates Primitive Obsession**: Distinct types prevent accidentally passing a `$userId` where a `$productId` is expected
- **Domain Behaviour Co-located with Data**: Methods like `Money::add()` or `Email::domain()` live on the type, not scattered in services
- **No Defensive Copies**: Immutable objects are safe to share and return
- **Self-Documenting**: `function ship(OrderId $id, Address $to)` is clearer than `function ship(int $id, string $street, string $city, string $zip)`

Reference: [Domain-Driven Design — Evans](https://www.domainlanguage.com/ddd/) | [PHP The Right Way — Value Objects](https://phptherightway.com/)
