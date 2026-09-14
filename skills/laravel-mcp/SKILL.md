---
name: laravel-mcp
description: Laravel MCP server development. Use when building MCP servers, tools, prompts, or resources for AI client integration. Triggers on tasks involving laravel/mcp, MCP tools, MCP prompts, MCP resources, or AI client protocols.
license: MIT
metadata:
  author: Laravel Community
  version: "1.0.0"
  laravelVersion: "13.x"
  phpVersion: "8.3+"
---

# Laravel MCP

Comprehensive guide for building MCP (Model Context Protocol) servers with Laravel, covering server registration/authentication, tool schemas and responses, resources/prompts, and testing.

## When to Apply

Reference these guidelines when:
- Creating MCP servers (web or local)
- Building tools that AI clients can call
- Defining prompts for reusable AI interactions
- Exposing resources for AI context
- Protecting MCP servers with OAuth or Sanctum
- Testing MCP servers, tools, prompts, and resources

## Rule Categories by Priority

| Priority | Category | Impact | Rule File |
|----------|----------|--------|-----------|
| 1 | Servers & Auth | CRITICAL | [`mcp-servers-registration-auth`](rules/mcp-servers-registration-auth.md) |
| 2 | Tool Schemas | CRITICAL | [`mcp-tool-definition-schemas`](rules/mcp-tool-definition-schemas.md) |
| 3 | Tool Responses | HIGH | [`mcp-tool-responses-error-handling`](rules/mcp-tool-responses-error-handling.md) |
| 4 | Resources & Testing | HIGH | [`mcp-resources-prompts-testing`](rules/mcp-resources-prompts-testing.md) |

## Quick Reference

### 1. Servers & Authentication (CRITICAL)
- [`mcp-servers-registration-auth`](rules/mcp-servers-registration-auth.md) — Register protected web endpoints with Sanctum / OAuth authentication

### 2. Tools & Schemas (CRITICAL)
- [`mcp-tool-definition-schemas`](rules/mcp-tool-definition-schemas.md) — Descriptive tool names, strongly-typed JSON schemas, dependency injection

### 3. Responses & Error Handling (HIGH)
- [`mcp-tool-responses-error-handling`](rules/mcp-tool-responses-error-handling.md) — Structured TextContent payloads, catching exceptions to return error objects

### 4. Resources & Testing (HIGH)
- [`mcp-resources-prompts-testing`](rules/mcp-resources-prompts-testing.md) — Dynamic URI resources, prompt templates, and Pest/PHPUnit tool test suites

## Essential Patterns

### Creating an MCP Server

```php
<?php

namespace App\Mcp\Servers;

use Laravel\Mcp\Server;
use Laravel\Mcp\Server\Attributes\Instructions;
use Laravel\Mcp\Server\Attributes\Name;
use Laravel\Mcp\Server\Attributes\Version;

#[Name('Weather Server')]
#[Version('1.0.0')]
#[Instructions('This server provides weather information.')]
class WeatherServer extends Server
{
    protected array $tools = [
        CurrentWeatherTool::class,
    ];

    protected array $resources = [];

    protected array $prompts = [];
}
```

### Registering in routes/ai.php

```php
use App\Mcp\Servers\WeatherServer;
use Laravel\Mcp\Facades\Mcp;

Mcp::web('/mcp/weather', WeatherServer::class);
Mcp::local('weather', WeatherServer::class);
```

### Creating a Tool

```php
<?php

namespace App\Mcp\Tools;

use Illuminate\Contracts\JsonSchema\JsonSchema;
use Laravel\Mcp\Request;
use Laravel\Mcp\Response;
use Laravel\Mcp\Server\Attributes\Description;
use Laravel\Mcp\Server\Tool;

#[Description('Fetches the current weather for a location.')]
class CurrentWeatherTool extends Tool
{
    public function handle(Request $request): Response
    {
        $location = $request->get('location');

        return Response::text("The weather in {$location} is sunny, 72°F.");
    }

    public function schema(JsonSchema $schema): array
    {
        return [
            'location' => $schema->string()
                ->description('The location to get the weather for.')
                ->required(),
        ];
    }
}
```

## How to Use

Read individual rule files for detailed explanations and code examples.

Each rule file contains:
- YAML frontmatter with metadata (title, impact, tags)
- Brief explanation of why it matters
- Bad Example with explanation
- Good Example with explanation
- Laravel 13 and PHP 8.3 specific context and references

`AGENTS.md` and `README.md` are supporting routing projections only. If either disagrees with this file or a rule under `rules/`, follow the canonical source and repair the projection.
