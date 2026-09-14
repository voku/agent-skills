---
id: pw-form-interactions-custom-inputs
title: "Controlled Form Inputs, Custom Checkboxes, and Date Pickers"
category: forms
priority: HIGH
triggers: [hidden-checkbox-input, custom-switch-toggle, react-controlled-input, date-picker-interaction]
tags: [playwright, e2e, forms, react, inputs, custom-checkboxes]
---

# Controlled Form Inputs, Custom Checkboxes, and Date Pickers

**Trigger Anchor:** Use `.fill()` to set values on controlled React/Inertia inputs; interact with styled/hidden custom checkboxes by clicking their visible label or using `{ force: true }`; wait for state transitions before submitting.

---

### Bad
```typescript
// ❌ Clicking a visually hidden <input type="checkbox" className="sr-only" /> throws element not visible error
await page.locator('input[type="checkbox"]').click(); // Error: Element is not visible!

// ❌ Simulating individual key presses without triggering React onChange state updates
await page.getByLabel('Search').pressSequentially('query'); // Can miss debounced state updates

// ❌ Interacting with custom date picker by clicking through 12 calendar month arrows
for (let i = 0; i < 12; i++) {
    await page.getByRole('button', { name: 'Next Month' }).click();
}
```

### Good
```typescript
// ✅ Check custom checkbox by clicking its accessible label or passing force: true
await page.getByLabel('Accept Terms and Conditions').check({ force: true });
// Or click the visible label wrapper:
// await page.locator('label:has-text("Accept Terms")').click();

// ✅ Fill controlled text input reliably (triggers input, change, and React synthetic events)
await page.getByLabel('Search').fill('query');

// ✅ Fill date input directly using ISO date string if input is editable
await page.getByLabel('Birth Date').fill('1990-05-15');
```
