---
id: mcp-tool-definition-schemas
title: "Tool Definition, Strongly-Typed Schemas, and Dependency Injection"
category: tools
priority: CRITICAL
triggers: [vague-tool-description, untyped-tool-argument, missing-schema-validation, manual-tool-instantiation]
tags: [mcp, laravel-mcp, tools, schemas, dependency-injection, ai-tools]
---

# Tool Definition, Strongly-Typed Schemas, and Dependency Injection

**Trigger Anchor:** Define tools with unambiguous names, precise LLM-oriented descriptions, strongly-typed parameter schemas, and resolve service dependencies through container injection.

---

### Bad
```php
// ❌ Vague description and missing input types confuse LLM tool-calling engines
class DoStuffTool extends Tool
{
    protected string $name = 'do_stuff';
    protected string $description = 'Does stuff with database'; // Too vague!

    public function handle(array $args): string
    {
        // Unsafe raw array access without validation
        $order = DB::table('orders')->find($args['id']);
        return json_encode($order);
    }
}
```

### Good
```php
// ✅ Precise description, typed input schema, and dependency injection
namespace App\Mcp\Tools;

use Laravel\Mcp\Tool;
use App\Repositories\OrderRepository;

class SearchOrdersTool extends Tool
{
    protected string $name = 'search_orders';
    protected string $description = 'Search customer orders by status, date range, or customer ID. Returns a list of matching orders with totals and item counts.';

    public function __construct(
        private readonly OrderRepository $orders,
    ) {}

    public function schema(): array
    {
        return [
            'type' => 'object',
            'properties' => [
                'status' => [
                    'type' => 'string',
                    'enum' => ['pending', 'processing', 'completed', 'cancelled'],
                    'description' => 'Filter orders by current status',
                ],
                'customer_id' => [
                    'type' => 'integer',
                    'description' => 'Optional customer ID filter',
                ],
                'limit' => [
                    'type' => 'integer',
                    'default' => 20,
                    'maximum' => 100,
                    'description' => 'Maximum number of orders to return',
                ],
            ],
            'required' => ['status'],
        ];
    }

    public function handle(string $status, ?int $customer_id = null, int $limit = 20): array
    {
        return $this->orders->search(status: $status, customerId: $customer_id, limit: $limit);
    }
}
```
