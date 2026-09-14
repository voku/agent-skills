---
id: modern-property-hooks
title: Property Hooks and Asymmetric Visibility (PHP 8.4+)
category: modern
priority: HIGH
triggers: [boilerplate-getter-setter, asymmetric-visibility, property-hooks, php84-features]
tags: [property-hooks, asymmetric-visibility, modern-php, php84]
---

# Property Hooks and Asymmetric Visibility

**Trigger Anchor:** In PHP 8.4+, replace repetitive boilerplate getters/setters with property hooks. Use asymmetric visibility (`public private(set)`) for properties read publicly but written only internally.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Verbose getters/setters for simple mutations or validation
class BankAccount
{
    private int $balanceInCents;

    public function __construct(int $initial)
    {
        $this->balanceInCents = $initial;
    }

    public function getBalanceInCents(): int
    {
        return $this->balanceInCents;
    }

    public function getBalanceInEur(): float
    {
        return $this->balanceInCents / 100;
    }

    private function setBalance(int $amount): void
    {
        $this->balanceInCents = max(0, $amount);
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ PHP 8.4+ asymmetric visibility and property hooks
class BankAccount
{
    // Publicly readable, privately writable
    public private(set) int $balanceInCents {
        set => max(0, $value);
    }

    // Virtual computed property hook
    public float $balanceInEur {
        get => $this->balanceInCents / 100;
    }

    public function __construct(int $initial)
    {
        $this->balanceInCents = $initial;
    }

    public function deposit(int $amount): void
    {
        $this->balanceInCents += $amount;
    }
}
```
