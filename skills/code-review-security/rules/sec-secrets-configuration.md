---
id: sec-secrets-configuration
title: "Secrets Hygiene, Cryptographic Defaults, and Secure Headers"
category: configuration
priority: HIGH
triggers: [hardcoded-api-key, plaintext-secret-in-git, weak-hash-md5, insecure-cookie-flags, debug-mode-production]
tags: [security, secrets, cryptography, cookies, headers, configuration]
---

# Secrets Hygiene, Cryptographic Defaults, and Secure Headers

**Trigger Anchor:** Read credentials and API keys exclusively from environment variables or secret vaults; use modern password hashing (Argon2id or Bcrypt with cost >= 12); configure session cookies with `Secure`, `HttpOnly`, and `SameSite=Lax/Strict`.

---

### Bad
```php
// ❌ A literal credential embedded in PHP source can leak into Git history.
// Do not include even realistic-looking hardcoded credentials in sample code.
// The secure alternative below injects the secret from a controlled source.

// ❌ Using obsolete/broken cryptographic hashes for sensitive data
$passwordHash = md5($rawPassword);
$token = sha1(microtime() . $userId);

// ❌ Insecure cookies vulnerable to XSS theft and CSRF
setcookie('session_id', $token, time() + 3600, '/', '', false, false);
```

### Good
```php
// ✅ Inject secrets via environment variables or secret manager
class StripeService
{
    public function __construct(
        #[\SensitiveParameter]
        private readonly string $apiKey,
    ) {}
}
// Wired via config: new StripeService(getenv('STRIPE_SECRET_KEY') ?: throw new \RuntimeException('Key missing'));

// ✅ Strong password hashing with Argon2id / modern algorithms
$passwordHash = password_hash($rawPassword, PASSWORD_ARGON2ID);
$token = bin2hex(random_bytes(32));

// ✅ Secure cookie configuration with HttpOnly, Secure, and SameSite
setcookie('session_id', $token, [
    'expires'  => time() + 3600,
    'path'     => '/',
    'domain'   => '',
    'secure'   => true,      // HTTPS only
    'httponly' => true,      // Prevent JavaScript access
    'samesite' => 'Lax',     // Mitigate CSRF
]);
```
