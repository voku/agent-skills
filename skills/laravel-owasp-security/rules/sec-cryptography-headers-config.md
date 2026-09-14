---
id: sec-cryptography-headers-config
title: "Cryptography, CSRF, Security Headers, and Production Configuration"
category: configuration
priority: HIGH
triggers: [unhashed-password, disabled-csrf-protection, app-debug-in-production, missing-security-headers, dangerously-set-inner-html]
tags: [security, laravel, cryptography, csrf, headers, production-config, xss, owasp]
---

# Cryptography, CSRF, Security Headers, and Production Configuration

**Trigger Anchor:** Enforce password hashing via `Hash::make()` or `'hashed'` casts; keep CSRF middleware enabled on all state-changing web routes; ensure `APP_DEBUG=false` in production; sanitize dangerous HTML with DOMPurify.

---

### Bad
```php
// ❌ Storing plaintext password or weak MD5 hash
$user->password = md5($request->input('password'));

// ❌ Disabling CSRF protection across all web routes in bootstrap/app.php
->withMiddleware(function (Middleware $middleware) {
    $middleware->validateCsrfTokens(except: ['*']); // Never bypass CSRF globally!
})

// ❌ React component using dangerouslySetInnerHTML without sanitization
function CommentBody({ htmlContent }: { htmlContent: string }) {
    return <div dangerouslySetInnerHTML={{ __html: htmlContent }} />; // XSS hazard!
}
```

### Good
```php
// ✅ Modern Bcrypt / Argon2id password hashing via Eloquent cast
// In User model:
protected function casts(): array
{
    return [
        'password' => 'hashed',
    ];
}

// ✅ Only exempt genuine stateless webhook endpoints from CSRF
->withMiddleware(function (Middleware $middleware) {
    $middleware->validateCsrfTokens(except: [
        'stripe/webhook',
        'github/webhook',
    ]);
})

// ✅ Sanitize raw HTML with DOMPurify before rendering
import DOMPurify from 'dompurify';

function CommentBody({ htmlContent }: { htmlContent: string }) {
    const cleanHtml = DOMPurify.sanitize(htmlContent);
    return <div dangerouslySetInnerHTML={{ __html: cleanHtml }} />;
}
```
