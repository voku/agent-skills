---
id: ai-agent-architecture
title: "Agent Architecture: Configuration, Structured Output, Streaming, and Memory"
category: agent
priority: CRITICAL
triggers: [laravel-ai-agent, agent-promptable, structured-output-schema, agent-streaming, agent-conversation-memory]
tags: [laravel, ai, agent, promptable, structured-output, streaming, memory]
---

# Agent Architecture: Configuration, Structured Output, Streaming, and Memory

**Trigger Anchor:** Define agents as dedicated classes implementing `Agent` with `Promptable`, configure provider/model via PHP attributes, enforce structured JSON schemas via `HasStructuredOutput`, and stream or queue responses via `stream()` and `queue()`.

---

### Bad
```php
// ❌ Unstructured ad-hoc curl/Guzzle calls to OpenAI with zero testability or typing
class ChatController extends Controller
{
    public function reply(Request $request)
    {
        $client = new \GuzzleHttp\Client();
        $res = $client->post('https://api.openai.com/v1/chat/completions', [
            'headers' => ['Authorization' => 'Bearer ' . env('OPENAI_KEY')],
            'json' => [
                'model' => 'gpt-4o',
                'messages' => [['role' => 'user', 'content' => $request->input('message')]],
            ],
        ]);

        return json_decode($res->getBody(), true)['choices'][0]['message']['content'];
    }
}
```

### Good
```php
// ✅ App/Ai/Agents/InvoiceExtractor.php: Typed agent with PHP attributes and JSON schema
namespace App\Ai\Agents;

use Illuminate\Contracts\JsonSchema\JsonSchema;
use Laravel\Ai\Attributes\MaxTokens;
use Laravel\Ai\Attributes\Model;
use Laravel\Ai\Attributes\Provider;
use Laravel\Ai\Attributes\Temperature;
use Laravel\Ai\Contracts\Agent;
use Laravel\Ai\Contracts\HasStructuredOutput;
use Laravel\Ai\Enums\Lab;
use Laravel\Ai\Promptable;
use Laravel\Ai\RemembersConversations;

#[Provider(Lab::Anthropic)]
#[Model('claude-haiku-4-5-20251001')]
#[Temperature(0.1)]
#[MaxTokens(2048)]
class InvoiceExtractor implements Agent, HasStructuredOutput
{
    use Promptable, RemembersConversations;

    public function instructions(): string
    {
        return 'Extract vendor, total, currency, and line items from the provided invoice document.';
    }

    public function schema(JsonSchema $schema): array
    {
        return [
            'vendor' => $schema->string()->required(),
            'total' => $schema->number()->required(),
            'currency' => $schema->string()->minLength(3)->maxLength(3)->required(),
            'items' => $schema->array()->items([
                'description' => $schema->string()->required(),
                'amount' => $schema->number()->required(),
            ])->required(),
        ];
    }
}
```

```php
// ✅ Controller usage: Invocation, streaming, or queueing
use App\Ai\Agents\InvoiceExtractor;

// 1. Synchronous structured prompt
$invoiceData = InvoiceExtractor::make()->prompt('Invoice text: Acquired server hardware for $1,200...');
// Returns array validated against schema

// 2. Real-time streaming response (e.g. for Server-Sent Events / Inertia)
return response()->stream(function () {
    InvoiceExtractor::make()->stream('Generate monthly financial summary...', function ($chunk) {
        echo "data: " . json_encode(['delta' => $chunk]) . "\n\n";
        ob_flush();
        flush();
    });
});

// 3. Asynchronous background queueing
InvoiceExtractor::make()->queue('Process large uploaded batch...');
```
