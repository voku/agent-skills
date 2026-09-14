---
id: sec-sink-appropriate-escaping
title: "Sink-Appropriate Escaping and Context Encoding"
category: data-protection
priority: HIGH
triggers: [xss-vulnerability, premature-html-escaping, unescaped-template-echo, double-escaping, raw-html-output]
tags: [security, xss, escaping, encoding, html-sanitization, sink-awareness]
---

# Sink-Appropriate Escaping and Context Encoding

**Trigger Anchor:** Escape exclusively at the final destination sink (HTML, JSON, CLI, LDAP); store raw unescaped data in databases and directory services to avoid data corruption and double-escaping bugs.

---

### Bad
```php
// ❌ Premature HTML escaping before storage in database or LDAP
$description = htmlspecialchars($_POST['description'], ENT_QUOTES, 'UTF-8');
// Writes "ACME &amp; Co." into database/LDAP, breaking searches and downstream exports!
$userRepository->updateDescription($userId, $description);

// ❌ Unescaped raw output in template creates XSS vulnerability
echo '<div class="user-bio">' . $user->bio . '</div>';
// Or in Blade / Twig / Smarty templates:
// {!! $user->bio !!} or {$user->bio nofilter}
```

### Good
```php
// ✅ Store clean, raw strings in the database / directory service
$rawDescription = (string)$_POST['description'];
$userRepository->updateDescription($userId, $rawDescription);

// ✅ Escape strictly at the rendering sink (HTML output)
// In PHP templates:
echo '<div class="user-bio">' . htmlspecialchars($user->bio, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') . '</div>';

// In Blade: standard auto-escaping {{ }}
// <div>{{ $user->bio }}</div>

// In Smarty: auto-escaped template variable
// <div>{$user->bio|escape:'html'}</div>
```
