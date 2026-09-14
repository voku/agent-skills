---
id: validation-rules
title: "Form Requests, Array Validation, and Custom Rules"
category: validation
priority: HIGH
triggers: [inline-controller-validation, nested-array-unvalidated, custom-regex-rule, missing-after-hook]
tags: [laravel, validation, form-requests, rules, nested-arrays]
---

# Form Requests, Array Validation, and Custom Rules

**Trigger Anchor:** Encapsulate validation in dedicated FormRequest classes, validate complex nested arrays using wildcard notation (`items.*.id`), leverage `Rule::when()` for conditional constraints, and create invokable `ValidationRule` classes for domain checks.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Inline controller validation with loose array validation and unverified items
class CheckoutController extends Controller
{
    public function store(Request $request)
    {
        // ❌ Missing child validation: caller can send items without price or negative quantity
        $validated = $request->validate([
            'customer_email' => 'required',
            'items' => 'required|array', // Leaves items.* completely unchecked
        ]);
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

namespace App\Http\Requests\Orders;

use App\Rules\SufficientInventoryRule;
use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Validation\Rule;

final class StoreOrderRequest extends FormRequest
{
    public function authorize(): bool
    {
        return $this->user() !== null;
    }

    /**
     * @return array<string, list<mixed>>
     */
    public function rules(): array
    {
        return [
            'customer_email' => ['required', 'string', 'email:rfc,dns', 'max:255'],
            'coupon_code' => ['nullable', 'string', 'max:50'],
            'items' => ['required', 'array', 'min:1'],
            // ✅ Strict wildcard validation for nested collection arrays
            'items.*.product_id' => ['required', 'integer', 'exists:products,id'],
            'items.*.quantity' => ['required', 'integer', 'min:1', 'max:100', new SufficientInventoryRule()],
            'shipping_method' => ['required', 'string', Rule::in(['standard', 'express'])],
            // ✅ Conditional validation
            'express_notes' => [
                Rule::when($this->input('shipping_method') === 'express', ['required', 'string', 'max:500']),
            ],
        ];
    }
}
```
