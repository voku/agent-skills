---
id: solid-srp
title: SOLID - Single Responsibility Principle (SRP)
category: solid-principles
priority: critical
tags: [SOLID, SRP, single-responsibility, class-design, function-design]
related: [solid-ocp, solid-isp, core-separation-concerns]
---

# Single Responsibility Principle (SRP)

A module, class, or function should have only one reason to change. At the class level, that means one cohesive domain or actor responsibility; at the function level, that means doing one thing, doing it well, and doing it only.

---

## Class-Level SRP

A class should not mix persistence, notification, validation, and domain logic.

### Bad Example

```typescript
// ❌ Anti-pattern: Class handles multiple disparate responsibilities
class UserManager {
  private db: Database;
  private mailer: EmailService;

  constructor() {
    this.db = new Database();
    this.mailer = new EmailService();
  }

  async createUser(userData: UserData): Promise<User> {
    // 1. Validation logic
    if (!userData.email.includes('@')) {
      throw new Error('Invalid email');
    }

    // 2. Database persistence
    const user = await this.db.users.create(userData);

    // 3. Email notification
    await this.mailer.sendWelcomeEmail(user.email);

    // 4. Activity logging
    fs.appendFileSync('audit.log', `User created: ${user.id}\n`);

    return user;
  }
}
```

### Good Example

```typescript
// ✅ Cohesive classes with single responsibilities

class UserValidator {
  static validate(userData: UserData): void {
    if (!userData.email.includes('@')) {
      throw new ValidationError('Invalid email format');
    }
  }
}

class UserRepository {
  constructor(private db: Database) {}

  async create(userData: UserData): Promise<User> {
    return this.db.users.create(userData);
  }
}

class UserNotificationService {
  constructor(private mailer: EmailService) {}

  async sendWelcome(email: string): Promise<void> {
    await this.mailer.sendWelcomeEmail(email);
  }
}

// Orchestrator coordinates single-responsibility components
class CreateUserUseCase {
  constructor(
    private repository: UserRepository,
    private notifications: UserNotificationService,
    private logger: AuditLogger
  ) {}

  async execute(userData: UserData): Promise<User> {
    UserValidator.validate(userData);
    const user = await this.repository.create(userData);
    await this.notifications.sendWelcome(user.email);
    await this.logger.log(`User created: ${user.id}`);
    return user;
  }
}
```

---

## Function-Level SRP

A function should have a single purpose described without conjunctions like "and" or "or".

### Bad Example

```typescript
// ❌ Monolithic function mixing retrieval, pricing, inventory, payment, and notifications
async function processOrder(orderId: string): Promise<void> {
  const order = await db.query('SELECT * FROM orders WHERE id = ?', [orderId]);
  if (!order || order.status !== 'pending') throw new Error('Invalid order');

  let total = 0;
  for (const item of order.items) {
    const product = await db.query('SELECT price FROM products WHERE id = ?', [item.productId]);
    total += product.price * item.quantity;
  }
  const tax = total * 0.1;
  const grandTotal = total + tax + (total > 100 ? 0 : 10);

  for (const item of order.items) {
    await db.query('UPDATE products SET stock = stock - ? WHERE id = ?', [item.quantity, item.productId]);
  }

  const payment = await stripe.charges.create({ amount: Math.round(grandTotal * 100), customer: order.customerId });
  await db.query('UPDATE orders SET status = "completed", payment_id = ? WHERE id = ?', [payment.id, orderId]);
  await sendgrid.send({ to: order.customerEmail, subject: 'Confirmed', html: `<p>Total: ${grandTotal}</p>` });
}
```

### Good Example

```typescript
// ✅ Composed pipeline of single-purpose functions

async function processOrder(orderId: string): Promise<ProcessedOrder> {
  const order = await fetchAndValidateOrder(orderId);
  const pricing = calculateOrderPricing(order);

  await reserveInventory(order.items);
  try {
    const payment = await processPayment(order.customerId, pricing.total);
    const completed = await finalizeOrder(order, pricing, payment);
    await sendOrderConfirmation(completed);
    return completed;
  } catch (error) {
    await releaseInventory(order.items);
    throw error;
  }
}

function calculateOrderPricing(order: Order): OrderPricing {
  const subtotal = order.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  const tax = subtotal * 0.1;
  const shipping = subtotal > 100 ? 0 : 10;
  return { subtotal, tax, shipping, total: subtotal + tax + shipping };
}
```

## Why it Matters

1. **Isolated Reasons to Change**: Updating email templates never risks breaking payment calculations or database persistence.
2. **Independent Testability**: Units can be tested in isolation without complex mocks.
3. **Composability**: Small, single-purpose functions and classes can be reused across different workflows.
