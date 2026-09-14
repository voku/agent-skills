---
id: type-strict-declarations
title: Strict Types and Declarative Signatures
category: type
priority: CRITICAL
triggers: [untyped-parameter, missing-return-type, untyped-property, mixed-type, loose-coercion]
tags: [types, strict_types, parameters, properties, return-types]
---

# Strict Types and Declarative Signatures

**Trigger Anchor:** Declare `declare(strict_types=1);` in every file. Fully type all parameters, class properties, and return types; avoid `mixed` unless handling truly arbitrary input.

---

### Bad
```php
<?php
// ❌ No strict types, untyped parameters, untyped property, and mixed return
class OrderProcessor
{
    private $status;

    public function process($order, $amount)
    {
        $this->status = 'processed';
        return $amount * 1.19; // implicit float conversion or string coercion
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ Strict types declared, explicit property types, parameter types, and return types
final class OrderProcessor
{
    private OrderStatus $status;

    public function process(Order $order, float $amount): float
    {
        $this->status = OrderStatus::Processed;
        return $amount * 1.19;
    }
}
```
