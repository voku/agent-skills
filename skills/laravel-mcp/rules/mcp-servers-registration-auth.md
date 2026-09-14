---
id: mcp-servers-registration-auth
title: "MCP Server Architecture, Registration, and Token Protection"
category: servers-auth
priority: CRITICAL
triggers: [unprotected-mcp-server, mcp-server-registration, mcp-sse-transport, sanctum-mcp-auth]
tags: [mcp, laravel-mcp, servers, authentication, sanctum, sse]
---

# MCP Server Architecture, Registration, and Token Protection

**Trigger Anchor:** Register MCP servers with explicit transport types (local stdio or remote HTTP/SSE) and enforce token-based authentication (Sanctum or OAuth 2.1) on all remote web endpoints; never expose unauthenticated MCP endpoints to the public internet.

---

### Bad
```php
// ❌ Exposing MCP server route without authentication middleware
Route::mcp('/mcp/sse', AppMcpServer::class); // Publicly accessible to anyone!

// ❌ Mixing stdio local server commands with web routes
class AppMcpServer extends Server
{
    // No transport isolation or auth guards
}
```

### Good
```php
// ✅ Register protected web MCP endpoint with auth:sanctum middleware
Route::mcp('/mcp/sse', AppMcpServer::class)
    ->middleware(['auth:sanctum', 'throttle:60,1']);

// ✅ Server definition with explicit capability declaration
namespace App\Mcp\Servers;

use Laravel\Mcp\Server;
use App\Mcp\Tools\OrderSearchTool;

class AppMcpServer extends Server
{
    protected string $name = 'E-Commerce MCP Server';
    protected string $version = '1.0.0';

    protected array $tools = [
        OrderSearchTool::class,
    ];
}
```
