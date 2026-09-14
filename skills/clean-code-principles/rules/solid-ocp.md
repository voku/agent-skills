---
id: solid-ocp
title: SOLID - Open/Closed Principle (OCP)
category: solid-principles
priority: critical
tags: [SOLID, OCP, open-closed, extensibility, abstraction, design-patterns]
related: [solid-srp, solid-dip, solid-lsp]
---

# Open/Closed Principle (OCP)

Software entities (classes, modules, functions) should be **open for extension, but closed for modification**. You should be able to add new behavior without altering existing, tested source code.

---

## The Anti-Pattern: Modifying Core Classes with Switch / If Chains

### Bad Example

```typescript
// ❌ Core class must be modified every time a new payment provider or report format is added
class PaymentProcessor {
  processPayment(payment: Payment): PaymentResult {
    switch (payment.method) {
      case 'credit_card':
        return this.processCreditCard(payment);
      case 'paypal':
        return this.processPayPal(payment);
      case 'apple_pay':
        return this.processApplePay(payment);
      default:
        throw new Error(`Unsupported method: ${payment.method}`);
    }
  }

  private processCreditCard(p: Payment) { /* ... */ }
  private processPayPal(p: Payment) { /* ... */ }
  private processApplePay(p: Payment) { /* ... */ }
}
```

Every new payment method or format requires editing `PaymentProcessor`, re-testing all existing methods, and risking regressions in unrelated payment paths.

---

## The Solution: Extension via Abstraction & Polymorphism

### Good Example

```typescript
// ✅ 1. Define a stable abstraction
interface PaymentMethodHandler {
  supports(method: string): boolean;
  process(payment: Payment): Promise<PaymentResult>;
}

// ✅ 2. Implement individual strategies
class CreditCardHandler implements PaymentMethodHandler {
  supports(method: string): boolean {
    return method === 'credit_card';
  }

  async process(payment: Payment): Promise<PaymentResult> {
    // Isolated credit card processing
    return { success: true, transactionId: 'cc_123' };
  }
}

class PayPalHandler implements PaymentMethodHandler {
  supports(method: string): boolean {
    return method === 'paypal';
  }

  async process(payment: Payment): Promise<PaymentResult> {
    // Isolated PayPal processing
    return { success: true, transactionId: 'pp_456' };
  }
}

// ✅ 3. Core processor is closed for modification, open for new handlers via registration/injection
class PaymentProcessor {
  constructor(private handlers: PaymentMethodHandler[]) {}

  async process(payment: Payment): Promise<PaymentResult> {
    const handler = this.handlers.find(h => h.supports(payment.method));
    if (!handler) {
      throw new Error(`Unsupported payment method: ${payment.method}`);
    }
    return handler.process(payment);
  }
}

// Adding ApplePay requires ONLY adding ApplePayHandler, zero edits to PaymentProcessor
class ApplePayHandler implements PaymentMethodHandler {
  supports(method: string): boolean {
    return method === 'apple_pay';
  }

  async process(payment: Payment): Promise<PaymentResult> {
    return { success: true, transactionId: 'ap_789' };
  }
}
```

## Why it Matters

1. **Regression Prevention**: Existing handlers and the processor are untouched when adding new features.
2. **Parallel Development**: Different developers can add new handlers simultaneously without merge conflicts in a central file.
3. **Pluggability**: Behaviors can be injected or replaced based on environment, configuration, or feature flags.
