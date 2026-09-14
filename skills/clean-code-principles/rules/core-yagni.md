---
id: core-yagni
title: You Aren't Gonna Need It (YAGNI)
category: core-principles
priority: critical
triggers: [speculative-features, unused-config-fields, premature-abstractions-single-impl, just-in-case-code]
tags: [YAGNI, simplicity, lean, minimal-change]
---

# You Aren't Gonna Need It (YAGNI)

**Trigger Anchor:** Implement only verified, current requirements. Do not build speculative features, parameters, or abstractions "just in case."

---

### Bad (Speculative Fields & Anticipated Variance)
```typescript
// ❌ Adding speculative options and fields nobody asked for
interface UserRegistration {
  email: string;
  password: string;
  // Speculative bloat:
  faxNumber?: string;
  preferredChannel?: 'email' | 'sms' | 'push';
  customMetadata?: Record<string, unknown>;
}

// ❌ Multi-channel router when the app only sends emails
class NotificationChannelFactory { /* ... */ }
class ChannelRouter { /* ... */ }
```

### Good (Minimal Sufficient Implementation)
```typescript
// ✅ Implement strictly what current verified requirements demand
interface UserRegistration {
  email: string;
  password: string;
}

class EmailService {
  async sendWelcome(email: string) {
    await mailClient.send({ to: email, template: 'welcome' });
  }
}
```

### Abstraction Gate
Extract an abstraction only when:
1. You have **at least two real, active implementations** in the repository.
2. It is strictly required to decouple external infrastructure for unit testing.
