---
id: mcp-tool-responses-error-handling
title: "Structured Responses, Error Signaling, and Multi-Content Payloads"
category: responses
priority: HIGH
triggers: [unhandled-mcp-exception, broken-transport-crash, raw-exception-leak, unstructured-mcp-output]
tags: [mcp, laravel-mcp, tool-responses, error-handling, text-content, payloads]
---

# Structured Responses, Error Signaling, and Multi-Content Payloads

**Trigger Anchor:** Format tool results using structured MCP response objects (`TextContent`, `ImageContent`); catch expected domain exceptions and return `Response::error()` so the AI client receives an informative failure message rather than crashing the transport connection.

---

### Bad
```php
// ❌ Uncaught exception crashes the MCP process/SSE transport
public function handle(int $order_id): string
{
    // If order not found, ModelNotFoundException crashes the entire MCP session!
    $order = Order::findOrFail($order_id);
    return json_encode($order);
}

// ❌ Returning unstructured string blobs without schema
public function handle(string $query): string
{
    return 'Done: 42 items updated.'; // Hard for LLM to parse or verify
}
```

### Good
```php
use Laravel\Mcp\Response;
use Laravel\Mcp\Content\TextContent;

public function handle(int $order_id): Response
{
    try {
        $order = Order::with('items')->find($order_id);

        if ($order === null) {
            return Response::error(sprintf('Order #%d was not found.', $order_id));
        }

        return Response::make([
            TextContent::text(json_encode([
                'id' => $order->id,
                'status' => $order->status,
                'total' => $order->total_formatted,
                'items_count' => $order->items->count(),
            ], JSON_PRETTY_PRINT)),
        ]);
    } catch (\Throwable $e) {
        return Response::error('Internal query error: ' . $e->getMessage());
    }
}
```
