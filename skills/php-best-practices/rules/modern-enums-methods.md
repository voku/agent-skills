# Enum Methods

## Why it matters
When behaviour that belongs to a state lives in a separate class, those two things drift apart. A new case gets added to the enum, the helper class is not updated, and the mismatch causes a silent bug or an uncovered branch. Putting cohesive, domain-level behaviour directly on the enum co-locates the state and its rules, making omissions visible to static analysis.

## Rule
Add methods to enums for behaviour that is intrinsic to the state itself. Keep infrastructure concerns (database queries, HTTP calls, external formatting) out of enums.

## Bad
```php
<?php

declare(strict_types=1);

enum UserRole: string
{
    case Viewer = 'viewer';
    case Editor = 'editor';
    case Admin  = 'admin';
}

// Logic separated from the state — easy to forget a case when a new role is added
final class RolePermissions
{
    public static function canEdit(UserRole $role): bool
    {
        if ($role === UserRole::Viewer) {
            return false;
        }
        return true; // forgets to handle Admin explicitly — silent correctness risk
    }
}
```

## Better
```php
<?php

declare(strict_types=1);

enum UserRole: string
{
    case Viewer = 'viewer';
    case Editor = 'editor';
    case Admin  = 'admin';

    public function canEdit(): bool
    {
        return match ($this) {
            self::Viewer => false,
            self::Editor => true,
            self::Admin  => true,
        };
    }
}
```

## Best
```php
<?php

declare(strict_types=1);

interface HasPermissions
{
    public function canEdit(): bool;
    public function canDelete(): bool;
}

enum UserRole: string implements HasPermissions
{
    case Viewer = 'viewer';
    case Editor = 'editor';
    case Admin  = 'admin';

    public function canEdit(): bool
    {
        return match ($this) {
            self::Viewer => false,
            self::Editor, self::Admin => true,
        };
    }

    public function canDelete(): bool
    {
        return $this === self::Admin;
    }
}
```

## Exceptions / trade-offs
- Infrastructure concerns — database queries, HTTP calls, file I/O, external system formatting — must not go on enums. Keep those in services or repositories.
- Enums that accumulate many methods across multiple responsibilities are a sign the responsibility belongs in a service, not the enum.

## Static-analysis notes
PHPStan and Psalm verify exhaustive `match` inside enum methods, flagging missing cases when a new case is added without updating all match expressions. Implementing an interface on an enum is fully checked for method signature compliance.

## Version notes
`PHP 8.1+`

## Related topics
- [modern-enums.md](modern-enums.md) — foundational enum usage and backed enums
- [modern-match-expression.md](modern-match-expression.md) — exhaustive matching over enum cases
