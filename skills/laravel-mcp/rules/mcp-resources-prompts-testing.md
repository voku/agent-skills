---
id: mcp-resources-prompts-testing
title: "MCP Resources, Prompt Templates, and Unit Testing"
category: resources-testing
priority: HIGH
triggers: [untested-mcp-tool, dynamic-mcp-resource, prompt-template-definition, mcp-inspector-testing]
tags: [mcp, laravel-mcp, resources, prompts, testing, pest, unit-testing]
---

# MCP Resources, Prompt Templates, and Unit Testing

**Trigger Anchor:** Expose read-only application state via parameterized URI resources (`app://users/{id}`), provide reusable prompt templates, and verify tool execution via unit tests with mock dependencies.

---

### Bad
```php
// ❌ Static queries exposed as tools when read-only resources are more appropriate
class GetDocTool extends Tool
{
    // A resource URI is the standard MCP convention for static documentation
}

// ❌ Untested MCP tools deployed without verifying schema or error handling
```

### Good
```php
// ✅ Dynamic Resource exposing customer records
namespace App\Mcp\Resources;

use Laravel\Mcp\Resource;
use Laravel\Mcp\Content\TextContent;
use App\Models\User;

class UserResource extends Resource
{
    protected string $uri = 'app://users/{id}';
    protected string $name = 'User Profile';
    protected string $mimeType = 'application/json';

    public function read(int $id): array
    {
        $user = User::findOrFail($id);
        return [
            TextContent::text($user->toJson()),
        ];
    }
}

// ✅ Unit test asserting tool behavior and schema compliance
test('search orders tool returns formatted orders', function () {
    $repo = Mockery::mock(OrderRepository::class);
    $repo->shouldReceive('search')
        ->once()
        ->with('pending', null, 20)
        ->andReturn([['id' => 101, 'status' => 'pending']]);

    $tool = new SearchOrdersTool($repo);
    $response = $tool->handle('pending');

    expect($response)->toHaveCount(1)
        ->and($response[0]['id'])->toBe(101);
});
```
