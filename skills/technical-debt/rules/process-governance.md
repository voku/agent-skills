---
id: process-governance
title: "Process Debt: Stale Feature Flags, Aging TODOs, and Ownership Gaps"
category: process
priority: MEDIUM
triggers: [lingering-feature-flag, aging-todo-fixme, unowned-code, untracked-debt, unversioned-deprecation]
tags: [process, feature-flags, todos, code-ownership, debt-tracking]
---

# Process Debt: Stale Feature Flags, Aging TODOs, and Ownership Gaps

**Trigger Anchor:** Track technical debt in a prioritized ledger, retire stale feature flags and `@deprecated` markers after release cycles, prune aged `TODO`/`FIXME` comments (>6 months), and assign clear code ownership.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Permanent feature flag cluttering control flow years after launch
class CheckoutService
{
    public function calculateFee(Order $order): Money
    {
        // ❌ Flag rolled out 18 months ago, 100% active, but dead legacy branch remains
        if (Feature::active('new_fee_structure_2023')) {
            return $this->newFeeEngine->calculate($order);
        }

        // Dead code path: maintainers still have to understand and test this
        return $this->legacyFeeEngine->calculate($order);
    }
}

// ❌ Untracked, unowned aging TODO without ticket or context
// TODO: refactor this whole method, it's slow and broken
function legacyBatchExport() {}
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ Clean code paths after flag rollout; deprecations have target version and ticket
final readonly class CheckoutService
{
    public function calculateFee(Order $order): Money
    {
        return $this->feeEngine->calculate($order);
    }
}

/**
 * @deprecated Deprecated since v2.4; scheduled for removal in v3.0. Use `ExportService::csv()` instead.
 * @see https://github.com/org/repo/issues/482
 */
function legacyBatchExport(): void
{
    // ...
}
```

```text
# ✅ CODEOWNERS ensures every module has an accountable maintenance team
/app/Domain/Billing/    @org/billing-team
/app/Domain/Auth/       @org/security-team
```
