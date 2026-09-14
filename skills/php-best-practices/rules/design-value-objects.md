---
id: design-value-objects
title: Domain Value Objects and Magic Method Rejection
category: design
priority: HIGH
triggers: [primitive-obsession, magic-properties, invalid-domain-primitive, unvalidated-scalar]
tags: [value-objects, domain-design, no-magic, immutability]
---

# Domain Value Objects and Magic Method Rejection

**Trigger Anchor:** Replace bare primitives with immutable, self-validating Value Objects. Avoid dynamic magic methods (`__get`, `__set`, `__call`) that destroy static analysis and IDE autocompletion.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Primitive obsession and magic properties
class Account
{
    private array $data = [];

    // Magic __get / __set hides fields from static analysis
    public function __set(string $name, mixed $value): void
    {
        $this->data[$name] = $value;
    }

    public function transfer(string $email, int $amount): void
    {
        // $email could be invalid; $amount could be negative or in unknown currency
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ Explicit, immutable, self-validating Value Object
final readonly class EmailAddress
{
    public string $value;

    public function __construct(string $value)
    {
        $trimmed = trim($value);
        if (!filter_var($trimmed, FILTER_VALIDATE_EMAIL)) {
            throw new InvalidArgumentException("Invalid email address: {$value}");
        }
        $this->value = strtolower($trimmed);
    }

    public function domain(): string
    {
        return substr(strrchr($this->value, '@') ?: '', 1);
    }
}

final readonly class Money
{
    public function __construct(
        public int $amountInCents,
        public string $currency = 'EUR'
    ) {
        if ($this->amountInCents < 0) {
            throw new InvalidArgumentException('Amount cannot be negative');
        }
    }
}

final class Account
{
    public function transfer(EmailAddress $recipient, Money $amount): void
    {
        // Safe: recipient and amount are guaranteed valid domain values
    }
}
```
