---
id: solid-dip
title: SOLID - Dependency Inversion Principle (DIP)
category: solid-principles
priority: critical
tags: [SOLID, DIP, dependency-inversion, dependency-injection, abstractions, testability]
related: [solid-ocp, solid-isp, pattern-repository]
---

# Dependency Inversion Principle (DIP)

1. **High-level modules should not depend on low-level modules.** Both should depend on abstractions.
2. **Abstractions should not depend on details.** Details (concrete implementations) should depend on abstractions.

In practice, this means coding against interfaces and injecting dependencies rather than directly instantiating concrete classes.

---

## The Anti-Pattern: Direct Instantiation of Concrete Details

When a high-level business service instantiates concrete databases, loggers, or external API clients inside its constructor, it cannot be tested without live infrastructure and cannot adapt to alternative providers.

### Bad Example

```typescript
// ❌ High-level service tightly coupled to concrete third-party services & DB drivers
class OrderService {
  private database: MySQLDatabase;
  private mailer: SmtpEmailSender;
  private paymentGateway: StripeGateway;

  constructor() {
    // Hardcoded dependencies prevent unit testing and environment swaps
    this.database = new MySQLDatabase(process.env.DB_HOST);
    this.mailer = new SmtpEmailSender(process.env.SMTP_USER);
    this.paymentGateway = new StripeGateway(process.env.STRIPE_KEY);
  }

  async placeOrder(order: Order): Promise<void> {
    await this.paymentGateway.charge(order.total);
    await this.database.save(order);
    await this.mailer.send(order.customerEmail, 'Order Placed');
  }
}
```

---

## The Solution: Inverting Dependencies via Interfaces and Injection

Define the contract needed by the high-level policy as an abstraction, and inject the concrete implementation from outside.

### Good Example

```typescript
// ✅ 1. High-level module defines the contracts it needs
interface OrderRepository {
  save(order: Order): Promise<void>;
}

interface PaymentGateway {
  charge(amount: number): Promise<PaymentResult>;
}

interface NotificationSender {
  notify(recipient: string, message: string): Promise<void>;
}

// ✅ 2. High-level service depends strictly on abstractions via constructor injection
class OrderService {
  constructor(
    private repository: OrderRepository,
    private payment: PaymentGateway,
    private notifications: NotificationSender
  ) {}

  async placeOrder(order: Order): Promise<void> {
    await this.payment.charge(order.total);
    await this.repository.save(order);
    await this.notifications.notify(order.customerEmail, 'Order Placed');
  }
}

// ✅ 3. Low-level adapters implement the abstractions
class PostgresOrderRepository implements OrderRepository {
  async save(order: Order): Promise<void> { /* DB query */ }
}

class StripeAdapter implements PaymentGateway {
  async charge(amount: number): Promise<PaymentResult> { /* Stripe API call */ }
}
```

## Why it Matters

1. **Effortless Unit Testing**: Test `OrderService` in isolation by injecting fast in-memory test doubles without any database or network calls.
2. **Pluggable Architecture**: Switch from MySQL to Postgres, or from SendGrid to Postmark, by writing a new adapter—`OrderService` never changes.
3. **Decoupled Architecture**: High-level business logic is shielded from external library breaking changes and infrastructure details.
