# Strict Types Declaration

## Why it matters
Without `declare(strict_types=1)`, PHP silently coerces types at call sites: a `float` passed to an `int` parameter is truncated, a numeric string passes where an `int` is expected, and bugs hide until production. Every hour of debugging a coercion-related bug is a direct cost of omitting one line.

## Rule
Every PHP file must begin with `<?php` followed immediately by `declare(strict_types=1);` as the first statement — no namespace, no use, no blank lines between `<?php` and the declare.

## Bad

```php
<?php

declare(strict_types=1);

// no strict_types — numeric strings silently coerce
function calculateTotal(int $price, int $quantity): int
{
    return $price * $quantity;
}

calculateTotal("10", "5");  // returns 50 — bug hidden
calculateTotal(10.99, 2);   // returns 20 — float truncated silently
```

## Better

```php
<?php

declare(strict_types=1);

// strict_types present, but declare is buried after namespace
namespace App\Services;

declare(strict_types=1); // wrong position — must come first
```

## Best

```php
<?php

declare(strict_types=1);

namespace App\Services;

use App\Contracts\UserRepositoryInterface;
use App\Exceptions\UserNotFoundException;
use App\Models\User;

final class UserService
{
    public function __construct(
        private readonly UserRepositoryInterface $repository,
    ) {}

    public function findById(int $id): User
    {
        $user = $this->repository->find($id);

        if ($user === null) {
            throw new UserNotFoundException($id);
        }

        return $user;
    }

    /**
     * @param array<int> $ids
     * @return list<User>
     */
    public function findMany(array $ids): array
    {
        return $this->repository->findMany($ids);
    }
}
```

## Exceptions / trade-offs
- **Generated files**: Auto-generated stubs (e.g., protobuf, migration snapshots) may omit strict types if the generator does not support it. Add it when the generator allows.
- **Call-site scoping**: `declare(strict_types=1)` only affects calls *made from* the file where it is declared; it does not change the behaviour of functions defined in that file when called from a non-strict file.
- **`ini_set` has no effect**: You cannot enable strict mode via `php.ini` or `ini_set` — the declare is the only mechanism.

## Static-analysis notes
PHPStan and Psalm enforce type correctness independently of `strict_types`, but the combination catches coercion bugs at both static-analysis time and runtime. Set `phpstan.neon` level ≥ 6 alongside strict types for maximum coverage. IDEs (PhpStorm) use the declare to enable stronger inspections automatically.

## Version notes
`PHP 7.0+`

## Related topics
- [type-parameter-types.md](type-parameter-types.md) — parameter types enforced by strict mode
- [type-return-types.md](type-return-types.md) — return types enforced by strict mode
- [type-property-types.md](type-property-types.md) — property types complement strict mode
