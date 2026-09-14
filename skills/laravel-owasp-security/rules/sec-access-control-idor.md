---
id: sec-access-control-idor
title: "Broken Access Control, IDOR, and Route Gates"
category: access-control
priority: CRITICAL
triggers: [missing-policy-gate, idor-unscoped-model-binding, client-only-admin-guard, missing-role-middleware]
tags: [security, laravel, access-control, idor, policies, gates, rbac, owasp]
---

# Broken Access Control, IDOR, and Route Gates

**Trigger Anchor:** Enforce authorization server-side on every request using Laravel Policies (`$this->authorize()`), explicit Gate checks, or user-scoped relationships; never rely on UI-hidden components or unvalidated route IDs.

---

### Bad
```php
// ❌ IDOR: direct model retrieval without checking user/tenant ownership
class InvoiceController extends Controller
{
    public function show(int $id): Response
    {
        // Any authenticated user can view any customer's invoice by changing ID in URL!
        $invoice = Invoice::findOrFail($id);
        return Inertia::render('invoices/show', ['invoice' => $invoice]);
    }

    // ❌ Client-only role enforcement: endpoint lacks server-side authorization check
    public function destroy(User $user): RedirectResponse
    {
        // If an attacker sends POST /users/{id} directly, admin check in React UI is bypassed!
        $user->delete();
        return back();
    }
}
```

### Good
```php
// ✅ Enforce ownership via policy authorization or scoped relationship
class InvoiceController extends Controller
{
    public function show(Invoice $invoice): Response
    {
        $this->authorize('view', $invoice); // Enforces InvoicePolicy::view($user, $invoice)

        // Or query-scoped alternative:
        // $invoice = auth()->user()->invoices()->findOrFail($invoice->id);

        return Inertia::render('invoices/show', [
            'invoice' => new InvoiceResource($invoice),
        ]);
    }

    // ✅ Server-side gate authorization
    public function destroy(User $user): RedirectResponse
    {
        $this->authorize('delete', $user);

        $user->delete();
        return back()->with('success', 'User deleted successfully.');
    }
}
```
