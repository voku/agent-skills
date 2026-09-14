---
id: security-debt
title: "Security Debt: Credentials, Validation, and Auth Hardening"
category: security
priority: CRITICAL
triggers: [committed-secrets, missing-input-validation, weak-password-hashing, missing-authz, missing-rate-limit]
tags: [security, owasp, auth, credentials, validation]
---

# Security Debt: Credentials, Validation, and Auth Hardening

**Trigger Anchor:** Eliminate hardcoded credentials in source or git history, validate all HTTP/RPC input via strict schemas/FormRequests, hash passwords with modern algorithms (Argon2id/Bcrypt), enforce explicit authorization on every protected route, and rate-limit sensitive endpoints.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Hardcoded secrets, unvalidated input, and missing authorization check
class PaymentController extends Controller
{
    private const string STRIPE_KEY = 'sk_live_51Abc123...'; // ❌ Hardcoded credential

    public function charge(Request $request): JsonResponse
    {
        // ❌ Unvalidated raw user input passed to financial operation
        $amount = (float) $request->input('amount');
        $accountId = $request->input('account_id');

        // ❌ No authorization: any authenticated user can charge any account_id
        Stripe::setApiKey(self::STRIPE_KEY);
        $charge = StripeCharge::create(['amount' => $amount, 'customer' => $accountId]);

        return response()->json($charge);
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ Secret injection from env/vault, strict FormRequest, policy authorization & rate limit
final class ChargeRequest extends FormRequest
{
    public function authorize(): bool
    {
        $account = Account::findOrFail($this->route('account'));
        return $this->user()?->can('charge', $account) ?? false;
    }

    /**
     * @return array<string, list<string>>
     */
    public function rules(): array
    {
        return [
            'amount_cents' => ['required', 'integer', 'min:100', 'max:10000000'],
            'currency' => ['required', 'string', 'size:3', 'in:usd,eur,gbp'],
        ];
    }
}

final class PaymentController extends Controller
{
    public function __construct(
        private PaymentGatewayInterface $gateway,
    ) {}

    public function charge(ChargeRequest $request, Account $account): JsonResponse
    {
        $validated = $request->validated();
        $charge = $this->gateway->charge(
            $account,
            Money::fromCents($validated['amount_cents'], Currency::from($validated['currency'])),
        );

        return response()->json(['charge_id' => $charge->id], 201);
    }
}
```
