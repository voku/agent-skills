---
id: arch-contract-rigor-extensibility
title: "Contract Rigor and Resisting Over-Engineering"
category: maintainability
priority: MEDIUM
triggers: [over-abstracted-plugin-system, deep-inheritance-hierarchy, fragile-base-class, speculative-extension-point]
tags: [architecture, composition-over-inheritance, yagni, contracts, extensibility]
---

# Contract Rigor and Resisting Over-Engineering

**Trigger Anchor:** Prefer composition over deep inheritance hierarchies; design narrow, focused interfaces rather than sprawling god-classes; avoid speculative extension points.

---

### Bad
```php
// ❌ Deep, fragile inheritance hierarchy with sprawling base classes
abstract class BaseController { ... }
abstract class CrudController extends BaseController { ... }
abstract class ResourceAdminController extends CrudController { ... }
abstract class SearchableResourceAdminController extends ResourceAdminController { ... }
class UserController extends SearchableResourceAdminController
{
    // Inherits 45 protected methods, coupling tightly to ancestor internal changes
}

// ❌ Sprawling god-interface violating Interface Segregation Principle
interface UserManagerInterface
{
    public function createUser(): void;
    public function deleteUser(): void;
    public function sendWelcomeEmail(): void;
    public function generatePdfInvoice(): void;
    public function exportCsv(): void;
}
```

### Good
```php
// ✅ Composition of small, focused collaborators
class UserController
{
    public function __construct(
        private readonly UserSearchService $searchService,
        private readonly UserRegistrationService $registrationService,
    ) {}

    // Methods cleanly delegate to dedicated, independently testable collaborators
}

// ✅ Narrow, role-specific interfaces
interface UserReaderInterface
{
    public function findById(int $id): ?User;
}

interface UserWriterInterface
{
    public function save(User $user): void;
}
```
