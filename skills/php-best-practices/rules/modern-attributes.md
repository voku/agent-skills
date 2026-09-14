---
id: modern-attributes
title: Native Attributes and Override Checks
category: modern
priority: HIGH
triggers: [docblock-annotations, missing-override, attribute-metadata, php83-override]
tags: [attributes, override, reflection, modern-php, php83]
---

# Native Attributes and Override Checks

**Trigger Anchor:** Replace docblock annotations with native PHP attributes (`#[Attribute]`). Always annotate intentional method overrides with `#[\Override]` in PHP 8.3+ so the compiler detects broken contracts when parent signatures change.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Docblock annotations parsed with regex; missing #[\Override]
/**
 * @Route("/api/users", methods={"GET"})
 */
class UserController extends BaseController
{
    // If BaseController renames handleRequest() to handle(), this becomes a dead silent method!
    public function handleRequest(): void
    {
        // ...
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

use Attribute;

#[Attribute(Attribute::TARGET_CLASS | Attribute::TARGET_METHOD)]
final readonly class Route
{
    public function __construct(
        public string $path,
        public array $methods = ['GET'],
    ) {}
}

#[Route('/api/users', methods: ['GET'])]
final class UserController extends BaseController
{
    // ✅ Compiler ensures handleRequest() exists in BaseController; breaks build if renamed
    #[\Override]
    public function handleRequest(): void
    {
        // ...
    }
}
```
