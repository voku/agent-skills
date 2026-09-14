---
id: modern-readonly
title: Readonly Classes, Properties, and Typed Constants
category: modern
priority: CRITICAL
triggers: [mutable-dto, missing-readonly, mutable-state, untyped-constant]
tags: [readonly, immutability, typed-constants, php81, php82, php83]
---

# Readonly Classes, Properties, and Typed Constants

**Trigger Anchor:** Use `readonly` classes for immutable DTOs and Value Objects. Use `readonly` properties when only select fields are immutable. Type all class constants.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Mutable DTO, untyped constant, accidental state mutations
class UserDto
{
    const DEFAULT_ROLE = 'user'; // untyped constant

    public string $id;
    public string $email;

    public function __construct(string $id, string $email)
    {
        $this->id = $id;
        $this->email = $email;
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ Immutable readonly class with typed constant
final readonly class UserDto
{
    public const string DEFAULT_ROLE = 'user';

    public function __construct(
        public string $id,
        public string $email,
        public string $role = self::DEFAULT_ROLE,
    ) {}

    public function withEmail(string $newEmail): self
    {
        return new self($this->id, $newEmail, $this->role);
    }
}
```
