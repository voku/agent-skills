---
id: pw-web-first-assertions
title: "Web-First Assertions and Zero-Arbitrary Sleeps"
category: assertions
priority: CRITICAL
triggers: [wait-for-timeout-sleep, unwrapped-boolean-assertion, flaky-timing-test, missing-web-first-expect]
tags: [playwright, e2e, assertions, web-first, flakiness, async-testing]
---

# Web-First Assertions and Zero-Arbitrary Sleeps

**Trigger Anchor:** Use auto-retrying web-first assertions (`await expect(locator).toBeVisible()`) rather than evaluating booleans (`expect(await locator.isVisible()).toBe(true)`); never use `page.waitForTimeout()` arbitrary sleeps.

---

### Bad
```typescript
// ❌ Arbitrary hardcoded sleep introduces flaky tests and slows execution
await page.getByRole('button', { name: 'Submit' }).click();
await page.waitForTimeout(3000); // Flaky anti-pattern!

// ❌ Evaluating boolean immediately without auto-retrying
const isVisible = await page.getByText('Order Placed').isVisible();
expect(isVisible).toBe(true); // Fails immediately if DOM hasn't rendered yet!

// ❌ Unwrapped text assertion without polling
const text = await page.getByRole('status').textContent();
expect(text).toContain('Success'); // No auto-retry!
```

### Good
```typescript
// ✅ Web-first assertion automatically retries until condition is met or timeout expires
await page.getByRole('button', { name: 'Submit' }).click();
await expect(page.getByText('Order Placed')).toBeVisible();

// ✅ Auto-retrying text assertion
await expect(page.getByRole('status')).toHaveText('Success');

// ✅ Explicit event waiting when awaiting network response
const responsePromise = page.waitForResponse('/api/v1/orders');
await page.getByRole('button', { name: 'Submit' }).click();
const response = await responsePromise;
expect(response.status()).toBe(201);
```
