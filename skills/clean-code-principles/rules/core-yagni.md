---
id: core-yagni
title: You Aren't Gonna Need It (YAGNI)
category: core-principles
priority: critical
tags: [YAGNI, speculative-features, premature-abstraction, simplicity, lean]
related: [core-kiss, core-dry, solid-ocp]
---

# You Aren't Gonna Need It (YAGNI)

Do not implement code, features, or architectural abstractions based on speculative future requirements. Implement only what is required to satisfy current, verified needs.

Anticipated needs rarely match the real future, and speculative code incurs immediate maintenance, testing, and cognitive overhead.

---

## 1. Avoid Speculative Features

Building unused parameters, extra database columns, or unrequested features "just in case" bloats the codebase and creates dead range logic.

### Bad Example

```typescript
// ❌ Building features and configurations that were not requested
interface UserRegistration {
  email: string;
  password: string;
  // Speculative fields added "in case we need them later":
  middleName?: string;
  faxNumber?: string;
  pagerNumber?: string;
  preferredCommunicationChannel?: 'sms' | 'email' | 'push' | 'carrier_pigeon';
  customMetadata?: Record<string, any>;
}
```

### Good Example

```typescript
// ✅ Implement only what current requirements demand
interface UserRegistration {
  email: string;
  password: string;
}
```

---

## 2. Avoid Premature Abstractions

Do not create plugin systems, multi-tiered factory hierarchies, or generic adapters when there is only one concrete implementation.

### Bad Example

```typescript
// ❌ Creating a multi-channel notification engine when the project only sends emails
interface NotificationPayload { /* ... */ }
interface NotificationChannel {
  send(payload: NotificationPayload): Promise<void>;
  supports(type: string): boolean;
}

class NotificationChannelRegistry { /* ... */ }
class ChannelRouter { /* ... */ }
class DynamicNotificationDispatcher { /* ... */ }
```

### Good Example

```typescript
// ✅ Simple, direct implementation until variance is proven
class EmailService {
  async sendWelcomeEmail(to: string, userName: string): Promise<void> {
    await mailClient.send({ to, subject: 'Welcome!', template: 'welcome' });
  }
}
```

## When to Introduce Abstractions

Extract an abstraction only when:
1. You have **at least two real, active implementations** that must vary at runtime.
2. An abstraction is strictly required to decouple a boundary for unit testing (e.g., isolating an external payment gateway).
3. The requirement is explicit and authorized, not assumed.

## Why it Matters

1. **Faster Delivery**: Less code to write, review, test, and document.
2. **Right Abstractions Later**: When requirements actually change, you have real evidence of the variance, allowing you to design the right abstraction rather than fighting an incorrect speculative one.
3. **Less Dead Code**: Prevents untested, unmaintained code paths from lurking in production.
