---
id: modern-constructor-arguments
title: Constructor Promotion and Named Arguments
category: modern
priority: CRITICAL
triggers: [boilerplate-constructor, named-arguments, parameter-order-confusion]
tags: [constructor-promotion, named-arguments, modern-php, php80]
---

# Constructor Promotion and Named Arguments

**Trigger Anchor:** Use constructor property promotion to declare and assign class properties directly. Use named arguments for clarity at call sites, especially with boolean flags or optional parameters.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Triple declaration of properties (declared, typed in constructor, assigned)
class Customer
{
    private string $id;
    private string $name;
    private bool $isActive;

    public function __construct(string $id, string $name, bool $isActive = true)
    {
        $this->id = $id;
        $this->name = $name;
        $this->isActive = $isActive;
    }
}

// ❌ Unclear boolean literal at call site
$customer = new Customer('123', 'Acme Corp', true);
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ Constructor promotion eliminates boilerplate
final readonly class Customer
{
    public function __construct(
        public string $id,
        public string $name,
        public bool $isActive = true,
    ) {}
}

// ✅ Named arguments make parameter roles obvious
$customer = new Customer(
    id: '123',
    name: 'Acme Corp',
    isActive: true,
);
```
