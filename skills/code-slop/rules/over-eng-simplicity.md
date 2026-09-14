---
id: over-eng-simplicity
title: Practical Simplicity vs Premature Abstraction
category: over-eng
priority: HIGH
triggers: [premature-interface, single-method-class, useless-wrapper, dependency-creep]
tags: [simplicity, yagni, architecture, anti-patterns]
---

# Practical Simplicity vs Premature Abstraction

**Trigger Anchor:** Reject premature single-implementation interfaces, single-method wrapper classes, pass-through delegate functions, and dependency sprawl; prefer top-level functions, native standard library methods, and direct class usage until polymorphism is genuinely required.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Interface with exactly one implementation and no planned polymorphism
interface TaxCalculationServiceInterface
{
    public function calculate(Money $subtotal): Money;
}

// ❌ Single-method class that wraps a 1-line standard calculation
final readonly class TaxCalculationService implements TaxCalculationServiceInterface
{
    public function calculate(Money $subtotal): Money
    {
        return $subtotal->multiply(0.20);
    }
}

// ❌ Useless wrapper that only forwards arguments without adding value
class OrderBillingCoordinator
{
    public function __construct(private TaxCalculationServiceInterface $taxService) {}

    public function getTax(Money $amount): Money
    {
        return $this->taxService->calculate($amount);
    }
}
```

```typescript
// ❌ Adding an external NPM library (`is-even`, `left-pad`, `uuid` when crypto.randomUUID() exists)
import { v4 as uuidv4 } from 'uuid'; // Unnecessary dependency creep

export class IdGeneratorService {
  generateUniqueId(): string {
    return uuidv4();
  }
}
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ Direct domain class or pure calculation until multiple tax engines exist
final readonly class TaxCalculator
{
    public function calculate(Money $subtotal, TaxRate $rate): Money
    {
        return $subtotal->multiply($rate->percentage);
    }
}
```

```typescript
// ✅ Built-in runtime standard library without dependency bloat or wrapper layers
export function generateId(): string {
  return crypto.randomUUID();
}
```
