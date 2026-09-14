---
id: solid-isp
title: SOLID - Interface Segregation Principle (ISP)
category: solid-principles
priority: critical
tags: [SOLID, ISP, interface-segregation, cohesion, client-design]
related: [solid-srp, solid-dip, core-separation-concerns]
---

# Interface Segregation Principle (ISP)

Clients should not be forced to depend on methods or interfaces they do not use. Prefer many small, client-specific interfaces over one large, general-purpose "fat" interface.

---

## The Anti-Pattern: The "Fat" Interface

When an interface bundles authentication, profile editing, analytics, and permissions into a single type, every consumer becomes tightly coupled to unrelated features. Furthermore, mock implementations and lightweight implementers are forced to write empty stubs or throw `NotImplementedError`.

### Bad Example

```typescript
// ❌ "Fat" interface forcing callers and implementers into unnecessary coupling
interface UserService {
  login(email: string, pass: string): Promise<AuthToken>;
  logout(userId: string): Promise<void>;
  updateProfile(userId: string, data: Profile): Promise<void>;
  uploadAvatar(userId: string, img: Buffer): Promise<string>;
  sendNotification(userId: string, msg: string): Promise<void>;
  getAnalytics(userId: string): Promise<UserAnalytics>;
}

// LoginPage only needs to authenticate, but depends on 15+ unrelated methods
class LoginPage {
  constructor(private service: UserService) {} // Coupling overkill
}

// In-memory test mock must stub 15+ methods just to test login
class MockUserService implements UserService {
  async login() { return { token: 'mock' }; }
  async logout() {}
  async updateProfile() { throw new Error('Not implemented'); }
  async uploadAvatar() { throw new Error('Not implemented'); }
  async sendNotification() { throw new Error('Not implemented'); }
  async getAnalytics() { throw new Error('Not implemented'); }
}
```

---

## The Solution: Focused, Role-Based Interfaces

Split interfaces by client intent and role. Classes can implement multiple narrow interfaces, while clients depend only on what they invoke.

### Good Example

```typescript
// ✅ Narrow, role-oriented interfaces
interface Authenticator {
  login(email: string, pass: string): Promise<AuthToken>;
  logout(userId: string): Promise<void>;
}

interface ProfileManager {
  updateProfile(userId: string, data: Profile): Promise<void>;
  uploadAvatar(userId: string, img: Buffer): Promise<string>;
}

interface UserNotifier {
  sendNotification(userId: string, msg: string): Promise<void>;
}

// LoginPage only depends on Authenticator
class LoginPage {
  constructor(private auth: Authenticator) {}

  async submit(email: string, pass: string) {
    return this.auth.login(email, pass);
  }
}

// A full backend service can implement multiple interfaces without polluting clients
class UserApplicationService implements Authenticator, ProfileManager, UserNotifier {
  async login(email: string, pass: string): Promise<AuthToken> { /* ... */ }
  async logout(userId: string): Promise<void> { /* ... */ }
  async updateProfile(userId: string, data: Profile): Promise<void> { /* ... */ }
  async uploadAvatar(userId: string, img: Buffer): Promise<string> { /* ... */ }
  async sendNotification(userId: string, msg: string): Promise<void> { /* ... */ }
}
```

## Why it Matters

1. **Focused Client Contracts**: Changes to notification APIs do not force re-compilation or re-testing of the login page.
2. **Effortless Mocks**: Testing `LoginPage` requires mocking an interface with just 2 methods instead of 20.
3. **No Stub / Throw Anti-Patterns**: Implementers only implement contracts they legitimately fulfill.
