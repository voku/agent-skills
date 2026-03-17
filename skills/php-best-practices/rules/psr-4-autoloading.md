# PSR-4 Autoloading

## Why it matters
Manual `require_once` chains break silently when a file is renamed, moved, or never loaded. PSR-4 makes class location deterministic: given the class name, Composer's autoloader resolves the file path algorithmically. One misconfigured namespace or mismatched filename causes a `Class "App\Domain\User\User" not found` error that can be impossible to trace when you have hundreds of files.

## Rule
Namespace-to-path consistency, one class per file, no clever directory tricks. The class `App\Domain\User\UserRepository` must live at `src/Domain/User/UserRepository.php` if `App\\` maps to `src/` in `composer.json`. Filename case must match class name case exactly — this matters on Linux.

## Bad

```php
<?php

// File: includes/classes/user_model.php
// Filename uses underscores; class uses PascalCase — autoloader cannot find it
class User_Model {}
```

```php
<?php

// File: lib/MyApp/Services/userService.php  (lowercase 'u')
// Class is UserService (uppercase 'U') — will fail on case-sensitive filesystems
namespace MyApp\Services;

class UserService {}
```

```php
<?php

// Manual includes — fragile, order-dependent, breaks on rename
require_once 'includes/classes/user_model.php';
require_once 'includes/classes/order_model.php';
require_once 'lib/helpers.php';
```

## Better

```php
<?php

declare(strict_types=1);

// File: src/Domain/User/User.php
namespace App\Domain\User;

final class User
{
    public function __construct(
        private readonly UserId $id,
        private readonly Email $email,
    ) {}
}
```

```json
{
    "autoload": {
        "psr-4": {
            "App\\": "src/",
            "Tests\\": "tests/"
        }
    }
}
```

## Best

```
project/
├── composer.json
├── src/
│   ├── Application/
│   │   ├── Order/
│   │   │   ├── CreateOrderCommand.php    → App\Application\Order\CreateOrderCommand
│   │   │   └── OrderService.php          → App\Application\Order\OrderService
│   ├── Domain/
│   │   ├── Order/
│   │   │   ├── Order.php                 → App\Domain\Order\Order
│   │   │   ├── OrderId.php               → App\Domain\Order\OrderId
│   │   │   └── OrderRepository.php       → App\Domain\Order\OrderRepository
│   │   └── User/
│   │       ├── User.php                  → App\Domain\User\User
│   │       ├── UserId.php                → App\Domain\User\UserId
│   │       └── UserRepository.php        → App\Domain\User\UserRepository
│   └── Infrastructure/
│       ├── Persistence/
│       │   ├── DoctrineOrderRepository.php → App\Infrastructure\Persistence\DoctrineOrderRepository
│       │   └── DoctrineUserRepository.php  → App\Infrastructure\Persistence\DoctrineUserRepository
│       └── Http/
│           └── Controllers/
│               └── OrderController.php     → App\Infrastructure\Http\Controllers\OrderController
└── tests/
    ├── Unit/
    │   └── Domain/
    │       └── User/
    │           └── UserTest.php            → Tests\Unit\Domain\User\UserTest
    └── Integration/
        └── OrderServiceTest.php            → Tests\Integration\OrderServiceTest
```

```php
<?php

declare(strict_types=1);

// File: src/Domain/User/UserId.php
namespace App\Domain\User;

final readonly class UserId
{
    public function __construct(public readonly string $value)
    {
        if (trim($value) === '') {
            throw new \InvalidArgumentException('UserId cannot be empty');
        }
    }
}
```

```php
<?php

declare(strict_types=1);

// File: src/Infrastructure/Persistence/DoctrineUserRepository.php
namespace App\Infrastructure\Persistence;

use App\Domain\User\User;
use App\Domain\User\UserId;
use App\Domain\User\UserRepository;
use Doctrine\ORM\EntityManagerInterface;

final class DoctrineUserRepository implements UserRepository
{
    public function __construct(
        private readonly EntityManagerInterface $em,
    ) {}

    public function find(UserId $id): ?User
    {
        return $this->em->find(User::class, $id->value);
    }

    public function save(User $user): void
    {
        $this->em->persist($user);
        $this->em->flush();
    }
}
```

## Exceptions / trade-offs
Bootstrap files (`index.php`, `artisan`, `bin/console`) live outside `src/` and are not autoloaded — they are entry points. Helpers files registered via `autoload.files` in `composer.json` are also exempt. Never use `classmap` autoloading for new code; it requires `composer dump-autoload` on every file addition and breaks the deterministic mapping.

## Static-analysis notes
PHPStan and Psalm both rely on PSR-4 mapping (via `composer.json`) to resolve class locations. If the mapping is wrong, analysis fails silently or reports phantom "class not found" errors. Run `composer dump-autoload --optimize` in CI to validate the autoload map is coherent.

## Related topics
- [psr-file-structure.md](psr-file-structure.md) — file structure inside each class file
- [psr-namespace-usage.md](psr-namespace-usage.md) — namespace conventions that make PSR-4 mapping readable
