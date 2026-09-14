---
name: laravel-ai-sdk
description: Laravel AI SDK for building AI-powered features. Use when creating agents, generating images or audio, working with embeddings, vector search, or testing AI features. Triggers on tasks involving laravel/ai, AI agents, tool-calling, structured output, streaming, embeddings, reranking, or AI faking in tests.
license: MIT
metadata:
  author: Laravel Community
  version: "1.0.0"
  laravelVersion: "13.x"
  phpVersion: "8.3+"
---

# Laravel AI SDK

Curated, high-density guide for building AI-powered features with the Laravel AI SDK (`laravel/ai`). Covers agent configuration, tool calling, vector embeddings/RAG, media generation, and deterministic test faking.

## Quick Reference

| Domain | Impact | Rule File | Primary Focus |
|--------|--------|-----------|---------------|
| **Agent Architecture** | CRITICAL | [`ai-agent-architecture`](rules/ai-agent-architecture.md) | Agent classes, PHP attributes (`#[Provider]`, `#[Model]`), structured output schemas, streaming |
| **Tool Integration** | HIGH | [`ai-tool-integration`](rules/ai-tool-integration.md) | Custom tools, JSON schema parameter validation, DI handling, built-in provider tools |
| **Embeddings & RAG** | HIGH | [`ai-embeddings-rag`](rules/ai-embeddings-rag.md) | `Str::toEmbeddings()`, embedding caching, pgvector cosine search, cross-encoder reranking |
| **Media & Resilience** | MEDIUM | [`ai-media-resilience`](rules/ai-media-resilience.md) | `Image::of()`, `Audio::transcribe()`, `Audio::speak()`, multi-provider failover chains |
| **Testing & Fakes** | HIGH | [`ai-testing-fakes`](rules/ai-testing-fakes.md) | `Agent::fake()`, `Ai::preventStrayPrompts()`, prompt assertions, mock media generation |

## Core Patterns

### Agent with Structured Output

```php
namespace App\Ai\Agents;

use Illuminate\Contracts\JsonSchema\JsonSchema;
use Laravel\Ai\Attributes\Model;
use Laravel\Ai\Attributes\Provider;
use Laravel\Ai\Contracts\Agent;
use Laravel\Ai\Contracts\HasStructuredOutput;
use Laravel\Ai\Enums\Lab;
use Laravel\Ai\Promptable;

#[Provider(Lab::Anthropic)]
#[Model('claude-haiku-4-5-20251001')]
class SalesSummary implements Agent, HasStructuredOutput
{
    use Promptable;

    public function instructions(): string
    {
        return 'Summarize sales calls into actionable key takeaways.';
    }

    public function schema(JsonSchema $schema): array
    {
        return [
            'sentiment' => $schema->string()->enum(['positive', 'neutral', 'negative'])->required(),
            'action_items' => $schema->array()->items($schema->string())->required(),
        ];
    }
}
```

### Testing with Fakes

```php
use App\Ai\Agents\SalesSummary;
use Laravel\Ai\Ai;

beforeEach(fn () => Ai::preventStrayPrompts());

test('sales summary agent returns structured feedback', function () {
    SalesSummary::fake();

    $result = SalesSummary::make()->prompt('Transcript of call...');

    expect($result)->toHaveKeys(['sentiment', 'action_items']);
    SalesSummary::assertPrompted(fn ($p) => $p->contains('Transcript'));
});
```
