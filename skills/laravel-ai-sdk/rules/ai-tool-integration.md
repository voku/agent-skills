---
id: ai-tool-integration
title: "Custom Tool Authoring, Parameter Schemas, and Built-in Providers"
category: tool
priority: HIGH
triggers: [laravel-ai-tool, make-tool-schema, tool-calling-agent, provider-tools-websearch]
tags: [laravel, ai, tools, json-schema, websearch, similarity-search]
---

# Custom Tool Authoring, Parameter Schemas, and Built-in Providers

**Trigger Anchor:** Implement custom tools with input validation schemas and handle execution methods, inject application dependencies via Laravel's container, and register them or built-in provider tools on agents with `HasTools`.

---

### Bad
```php
// ❌ Describing tools in prompt prose without executable tool definitions
class InventoryAssistant implements Agent
{
    use Promptable;

    public function instructions(): string
    {
        // LLM cannot directly invoke database queries or external APIs from prose descriptions
        return 'You are an inventory assistant. When asked about stock, query the database table items.';
    }
}
```

### Good
```php
// ✅ App/Ai/Tools/CheckInventory.php: Executable tool with JSON Schema validation and DI
namespace App\Ai\Tools;

use App\Models\Product;
use Illuminate\Contracts\JsonSchema\JsonSchema;
use Laravel\Ai\Contracts\Tool;
use Laravel\Ai\Tools\Request;

class CheckInventory implements Tool
{
    public function description(): string
    {
        return 'Check the remaining available warehouse stock quantity for a given product SKU.';
    }

    public function schema(JsonSchema $schema): array
    {
        return [
            'sku' => $schema->string()
                ->description('Product SKU identifier, e.g. PROD-1234')
                ->required(),
        ];
    }

    public function handle(Request $request): string
    {
        $product = Product::where('sku', $request['sku'])->first();

        if (! $product) {
            return json_encode(['error' => 'Product SKU not found']);
        }

        return json_encode([
            'sku' => $product->sku,
            'name' => $product->name,
            'in_stock' => $product->stock_quantity,
            'warehouse_location' => $product->warehouse_shelf,
        ]);
    }
}
```

```php
// ✅ Registering custom and built-in provider tools on an Agent
namespace App\Ai\Agents;

use App\Ai\Tools\CheckInventory;
use Laravel\Ai\Contracts\Agent;
use Laravel\Ai\Contracts\HasTools;
use Laravel\Ai\Promptable;
use Laravel\Ai\Tools\WebSearch; // Built-in provider web search

class InventoryAssistant implements Agent, HasTools
{
    use Promptable;

    public function instructions(): string
    {
        return 'Assist users with warehouse inventory queries and cross-reference online prices when requested.';
    }

    public function tools(): iterable
    {
        return [
            new CheckInventory,
            new WebSearch,
        ];
    }
}
```
