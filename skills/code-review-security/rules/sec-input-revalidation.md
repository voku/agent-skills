---
id: sec-input-revalidation
title: "Server-Side Input Re-validation and Selection Boundaries"
category: validation
priority: HIGH
triggers: [unvalidated-dropdown-selection, missing-foreign-key-filter, mass-assignment-vulnerability, client-side-only-validation]
tags: [security, validation, foreign-key, mass-assignment, dropdown-validation]
---

# Server-Side Input Re-validation and Selection Boundaries

**Trigger Anchor:** Re-validate all client-submitted choices, foreign keys, and status flags server-side against the same active filters used to populate dropdowns; guard against mass-assignment by explicitly declaring fillable fields.

---

### Bad
```php
// ❌ Trusting client-side form options: bare existence check allows linking inactive/deleted items
$selectedProductId = (int)$_POST['product_id'];
$product = Product::find($selectedProductId); // Even if product is archived/inactive!
$order->items()->create(['product_id' => $product->id]);

// ❌ Mass-assignment vulnerability allows client to overwrite sensitive attributes
$user->update($_POST); // Client can pass ['role' => 'admin', 'is_verified' => true]!
```

### Good
```php
// ✅ Server-side re-validation: enforce the same status/active filter as the UI dropdown
$selectedProductId = (int)$_POST['product_id'];
$product = Product::where('status', 'active')
    ->where('is_archived', false)
    ->find($selectedProductId);

if ($product === null) {
    throw new UnprocessableEntityHttpException('Selected product is inactive or does not exist.');
}
$order->items()->create(['product_id' => $product->id]);

// ✅ Guard against mass-assignment with explicit validated fields or Form Requests
$validated = $request->validate([
    'name' => ['required', 'string', 'max:255'],
    'email' => ['required', 'email', 'max:255'],
]);
$user->update($validated); // Only allows explicitly validated attributes
```
