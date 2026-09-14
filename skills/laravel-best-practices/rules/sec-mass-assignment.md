---
id: sec-mass-assignment
title: Mass Assignment Protection and Attribute Guarding
category: sec
priority: HIGH
triggers: [unguarded-models, fillable-empty-array, mass-assignment-vulnerability, unvalidated-request-all]
tags: [laravel, security, mass-assignment, fillable, guarded]
---

# Mass Assignment Protection and Attribute Guarding

**Trigger Anchor:** Protect models from mass-assignment privilege escalation by explicitly declaring `$fillable` attributes or using `Model::shouldBeStrict()`, and never pass raw `$request->all()` to model creation or updates.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Vulnerable to privilege escalation: unvalidated all() input passed to model
class ProfileController extends Controller
{
    public function update(Request $request, User $user): RedirectResponse
    {
        // ❌ Attacker injects ['is_admin' => true, 'role' => 'superadmin']
        $user->update($request->all());

        return redirect()->back();
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

final class User extends Model
{
    /**
     * ✅ Whitelist strictly editable user attributes
     *
     * @var list<string>
     */
    protected $fillable = [
        'name',
        'email',
        'avatar_url',
    ];
}
```

```php
<?php

declare(strict_types=1);

namespace App\Http\Controllers;

use App\Http\Requests\UpdateProfileRequest;
use App\Models\User;
use Illuminate\Http\RedirectResponse;

final class ProfileController
{
    public function update(UpdateProfileRequest $request, User $user): RedirectResponse
    {
        // ✅ Only safe, validated parameters reach the model
        $user->update($request->validated());

        return redirect()->route('profile.show');
    }
}
```
