---
id: solid-isp
title: Interface Segregation Principle (ISP)
category: solid-principles
priority: critical
triggers: [fat-interface, mock-everything-anti-pattern, empty-method-stubs, throw-not-implemented]
tags: [SOLID, ISP, interface-segregation, role-interfaces]
---

# Interface Segregation Principle (ISP)

**Trigger Anchor:** Clients should not depend on interfaces they do not use. Prefer multiple small, client-specific role interfaces over one "fat" general-purpose contract.

---

### Bad
```typescript
// ❌ "Fat" interface: forcing callers and test doubles to implement/depend on unused methods
interface UserService {
  login(email: string, pass: string): Promise<Token>;
  logout(userId: string): Promise<void>;
  updateProfile(userId: string, data: Profile): Promise<void>;
  uploadAvatar(userId: string, img: Buffer): Promise<string>;
  sendNotification(userId: string, msg: string): Promise<void>;
  getAnalytics(userId: string): Promise<Analytics>;
}

// LoginPage only logs in, but is coupled to 15+ unrelated methods
class LoginPage {
  constructor(private service: UserService) {}
}

// Test mock forced to stub irrelevant methods
class MockUserService implements UserService {
  async login() { return { token: 'mock' }; }
  async logout() {}
  async updateProfile() { throw new Error('Not implemented'); }
  async uploadAvatar() { throw new Error('Not implemented'); }
  async sendNotification() { throw new Error('Not implemented'); }
  async getAnalytics() { throw new Error('Not implemented'); }
}
```

### Good
```typescript
// ✅ Narrow, client-focused role interfaces
interface Authenticator {
  login(email: string, pass: string): Promise<Token>;
  logout(userId: string): Promise<void>;
}

interface ProfileManager {
  updateProfile(userId: string, data: Profile): Promise<void>;
}

// LoginPage only depends on Authenticator
class LoginPage {
  constructor(private auth: Authenticator) {}
}

// Mocking requires only 1-2 methods
const mockAuth: Authenticator = {
  login: async () => ({ token: 'mock' }),
  logout: async () => {}
};
```
