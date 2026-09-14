---
id: pw-locators-strict-mode
title: "Accessible Role Locators and Strict-Mode Disambiguation"
category: locators
priority: CRITICAL
triggers: [brittle-css-selector, xpath-locator, strict-mode-violation, get-by-role-accessible]
tags: [playwright, e2e, locators, accessibility, testing, strict-mode]
---

# Accessible Role Locators and Strict-Mode Disambiguation

**Trigger Anchor:** Locate elements via user-facing accessible roles and labels (`page.getByRole()`, `page.getByLabel()`, `page.getByText()`) rather than brittle CSS classes or XPath; disambiguate multiple matches using `.filter({ hasText: ... })` or parent scoping.

---

### Bad
```typescript
// ❌ Brittle CSS selectors that break on class name refactoring
await page.locator('.btn.btn-primary.submit-btn').click();

// ❌ Fragile XPath selector coupled to DOM structure
await page.locator('//div[@id="root"]/div[2]/form/div[3]/button').click();

// ❌ Strict mode violation: multiple buttons match, throwing Playwright error
await page.getByRole('button', { name: 'Delete' }).click(); // Error: resolved to 3 elements!
```

### Good
```typescript
// ✅ Accessible role locator matching what the user sees
await page.getByRole('button', { name: 'Save Changes' }).click();

// ✅ Form inputs located by accessible form label
await page.getByLabel('Email Address').fill('user@example.com');

// ✅ Disambiguate strict-mode violations using scoping or filtering
const userRow = page.getByRole('row').filter({ hasText: 'Alice Johnson' });
await userRow.getByRole('button', { name: 'Delete' }).click();
```
