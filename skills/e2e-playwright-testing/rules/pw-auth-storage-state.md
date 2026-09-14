---
id: pw-auth-storage-state
title: "Authenticated Sessions and Storage State Isolation"
category: authentication
priority: HIGH
triggers: [repeated-ui-login, slow-test-suite-auth, missing-storage-state, setup-project-auth]
tags: [playwright, e2e, authentication, storage-state, performance, session]
---

# Authenticated Sessions and Storage State Isolation

**Trigger Anchor:** Authenticate once in a global setup project and preserve session state to a `storageState` JSON file; reuse the storage state across test workers to eliminate redundant UI logins in every test spec.

---

### Bad
```typescript
// ❌ Logging in through the UI in every single test file adds 3-5 seconds per test
test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.getByLabel('Email').fill('admin@example.com');
    await page.getByLabel('Password').fill('secret');
    await page.getByRole('button', { name: 'Sign in' }).click();
    await page.waitForURL('/dashboard');
});

test('can view dashboard statistics', async ({ page }) => {
    // Repeated login overhead executed hundreds of times!
});
```

### Good
```typescript
// ✅ 1. Define global authentication setup in auth.setup.ts:
import { test as setup, expect } from '@playwright/test';

const authFile = 'playwright/.auth/user.json';

setup('authenticate', async ({ page }) => {
    await page.goto('/login');
    await page.getByLabel('Email').fill('admin@example.com');
    await page.getByLabel('Password').fill('secret');
    await page.getByRole('button', { name: 'Sign in' }).click();
    await page.waitForURL('/dashboard');
    await page.context().storageState({ path: authFile });
});

// ✅ 2. Configure dependencies in playwright.config.ts:
// projects: [
//   { name: 'setup', testMatch: /.*\.setup\.ts/ },
//   { name: 'e2e', dependencies: ['setup'], use: { storageState: 'playwright/.auth/user.json' } },
// ]

// ✅ 3. Tests start immediately authenticated:
test('can view dashboard statistics', async ({ page }) => {
    await page.goto('/dashboard');
    await expect(page.getByRole('heading', { name: 'Overview' })).toBeVisible();
});
```
