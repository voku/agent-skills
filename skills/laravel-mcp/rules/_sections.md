# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Server registration, authentication middleware, and tool schemas | Server wiring and tool definition |
| HIGH | Response structuring, error handling, and testing | Payload formatting and unit test suites |

## Section Overview

### 1. Servers & Authentication (`servers-auth`)
- **Impact:** CRITICAL
- **Rules:** `mcp-servers-registration-auth`
- **Description:** Registering protected MCP server endpoints with Sanctum or OAuth authentication.

### 2. Tool Definition & Schemas (`tools`)
- **Impact:** CRITICAL
- **Rules:** `mcp-tool-definition-schemas`
- **Description:** Defining tools with descriptive names, typed parameter schemas, and dependency injection.

### 3. Responses & Error Handling (`responses`)
- **Impact:** HIGH
- **Rules:** `mcp-tool-responses-error-handling`
- **Description:** Returning structured TextContent responses; catching exceptions to return error payloads.

### 4. Resources & Testing (`resources-testing`)
- **Impact:** HIGH
- **Rules:** `mcp-resources-prompts-testing`
- **Description:** Parameterized URI resources, prompt templates, and Pest/PHPUnit tool test suites.
