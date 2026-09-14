---
id: docs-currency
title: "Documentation Debt: Stale Guidance, Missing API Contracts, and Drift"
category: docs
priority: MEDIUM
triggers: [stale-comment, outdated-readme, missing-api-docs, architecture-drift]
tags: [documentation, openapi, readme, comments, onboarding]
---

# Documentation Debt: Stale Guidance, Missing API Contracts, and Drift

**Trigger Anchor:** Keep architecture decision records and README setup up-to-date, delete contradictory or stale comments, and document public APIs with OpenAPI or typed signatures.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Stale comment directly contradicts what the code does
class UserRepository
{
    /**
     * Finds active users only.
     * Note: Does not return soft-deleted or pending records.
     */
    public function getEligibleUsers(): Collection
    {
        // ❌ Bug / Drift: Soft-delete check was removed 6 months ago, but comment remained
        return User::where('status', '!=', 'banned')->get();
    }
}
```

```markdown
<!-- ❌ Outdated README instructions with dead links and wrong ports -->
### Setup
1. Run `docker-compose up -d` (fails on Docker v2+)
2. Visit `http://localhost:8000` (service actually runs on 3000)
3. Run `php artisan seed:old` (command deleted last year)
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ Precise method names and types eliminate the need for drift-prone narrative comments
final readonly class UserRepository
{
    /**
     * @return Collection<int, User>
     */
    public function findNonBannedUsers(): Collection
    {
        return User::query()
            ->where('status', '!=', UserStatus::Banned->value)
            ->get();
    }
}
```

```yaml
# ✅ OpenAPI 3.1 contract as executable, testable documentation
openapi: 3.1.0
paths:
  /api/v1/users:
    get:
      summary: List non-banned users
      responses:
        '200':
          description: A paginated list of users
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserListResponse'
```
