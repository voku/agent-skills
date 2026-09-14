---
id: sec-auth-fail-closed
title: "Authentication and Fail-Closed Authorization"
category: authorization
priority: CRITICAL
triggers: [unverified-session-user, missing-tenant-scope, idor-object-lookup, missing-policy-gate, fail-open-auth]
tags: [security, authentication, authorization, idor, rbac, fail-closed]
---

# Authentication and Fail-Closed Authorization

**Trigger Anchor:** Resolve authenticated user identity exclusively through verified session containers or tokens, scope entity lookups to the tenant/owner, and re-validate authorization gates server-side on every mutative request.

---

### Bad
```php
// ❌ Trusting unverified session integers or client-supplied IDs (IDOR)
$userId = (int)$_SESSION['user_id'];
$invoiceId = (int)$_GET['invoice_id'];

// Finding entity by bare ID allows any authenticated user to view any tenant's invoices!
$invoice = Invoice::find($invoiceId);

// ❌ Fail-open authorization check
if ($user->role !== 'admin') {
    // Falls through if role is empty or unexpected string
}
```

### Good
```php
// ✅ Fail-closed authenticated user retrieval via context container
$currentUser = AuthContext::authenticatedUserOrThrow();

// ✅ Enforce tenant/ownership scoping on database queries (prevents IDOR)
$invoice = Invoice::where('organization_id', $currentUser->getOrganizationId())
    ->where('id', (int)$_GET['invoice_id'])
    ->first();

if ($invoice === null) {
    throw new NotFoundHttpException('Invoice not found.');
}

// ✅ Explicit policy gate check
Gate::authorize('view', $invoice);
```
