---
id: psr-standards
title: PSR Coding Style and Autoloading Standards (PSR-4, PSR-12)
category: psr
priority: HIGH
triggers: [psr-violation, naming-convention, autoload-mismatch, inconsistent-style]
tags: [psr4, psr12, autoloading, style, conventions]
---

# PSR Coding Style and Autoloading Standards

**Trigger Anchor:** Map namespaces directly to filesystem directories per PSR-4. Format code per PSR-12 / PER Coding Style 2.0. Use PascalCase for classes/enums, camelCase for methods/properties, and UPPER_SNAKE_CASE for constants.

---

### Bad
```php
<?php
// ❌ Violates PSR-12: missing declare(strict_types=1), wrong indentation, inconsistent braces
class user_account {
  var $UserName;

  function Process_Payment ($Amount) {
    if($Amount<=0){
    return false;}
  }
}
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ PSR-4: App\Billing\UserAccount matches src/Billing/UserAccount.php
namespace App\Billing;

final readonly class UserAccount
{
    public function __construct(
        public string $userName,
    ) {}

    public function processPayment(float $amount): bool
    {
        if ($amount <= 0.0) {
            return false;
        }

        return true;
    }
}
```
