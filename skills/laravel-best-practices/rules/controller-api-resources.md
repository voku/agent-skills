---
id: controller-api-resources
title: API Response Transformation with JsonResource
category: controller
priority: HIGH
triggers: [direct-model-json-leak, inconsistent-api-response, missing-api-resource, sensitive-data-serialization]
tags: [laravel, api, json-resource, serialization, security]
---

# API Response Transformation with JsonResource

**Trigger Anchor:** Always transform HTTP API responses using `JsonResource` or `ResourceCollection` classes; never serialize Eloquent models directly to JSON to avoid leaking database schema, internal attributes, or relationship cycles.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Returning raw Eloquent models directly exposes database schema and sensitive attributes
class UserController extends Controller
{
    public function show(User $user): JsonResponse
    {
        // ❌ Leaks hidden columns, password_hash, remember_token, internal IDs
        return response()->json($user);
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

namespace App\Http\Resources;

use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

/**
 * @mixin User
 */
final class UserResource extends JsonResource
{
    /**
     * @return array<string, mixed>
     */
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            'created_at' => $this->created_at?->toIso8601String(),
            // ✅ Only include relationships when explicitly eager-loaded
            'orders' => OrderResource::collection($this->whenLoaded('orders')),
        ];
    }
}
```

```php
<?php

declare(strict_types=1);

namespace App\Http\Controllers\Api;

use App\Http\Resources\UserResource;
use App\Models\User;

final class UserController
{
    public function show(User $user): UserResource
    {
        return new UserResource($user->loadMissing('orders'));
    }
}
```
