---
id: ai-testing-fakes
title: "Testing AI Features: Agent Mocks, Stray Prompt Prevention, and Assertions"
category: test
priority: HIGH
triggers: [test-ai-agents, fake-ai-prompts, prevent-stray-prompts, fake-image-audio]
tags: [laravel, ai, testing, pest, phpunit, fakes, assertions]
---

# Testing AI Features: Agent Mocks, Stray Prompt Prevention, and Assertions

**Trigger Anchor:** Use `Agent::fake()` to stub responses and assert prompts, enable `Ai::preventStrayPrompts()` to avoid leaking live API calls into test suites, and mock image/audio generators.

---

### Bad
```php
// ❌ Making live AI API requests in automated tests: slow, non-deterministic, and costly
test('support agent replies to inquiries', function () {
    // 🚨 Hits live Claude / OpenAI endpoint in CI: breaks offline, fluctuates constantly, costs money
    $reply = SupportAgent::make()->prompt('How do I reset my password?');

    expect((string) $reply)->toContain('password');
});
```

### Good
```php
// ✅ Deterministic test with fake responses, prompt assertions, and stray prompt guards
use App\Ai\Agents\SupportAgent;
use App\Ai\Agents\InvoiceExtractor;
use Laravel\Ai\Ai;
use Laravel\Ai\Image;
use Laravel\Ai\Audio;
use Laravel\Ai\Prompts\AgentPrompt;

beforeEach(function () {
    // Fail immediately if any test attempts to make an unmocked live AI API call
    Ai::preventStrayPrompts();
});

test('support agent provides expected response and records prompt', function () {
    // 1. Mock agent with sequence of responses
    SupportAgent::fake([
        'Please navigate to Settings > Security to reset your password.',
    ]);

    $reply = SupportAgent::make()->prompt('How do I reset my password?');

    expect((string) $reply)->toBe('Please navigate to Settings > Security to reset your password.');

    // 2. Assert agent was prompted with specific input
    SupportAgent::assertPrompted(function (AgentPrompt $prompt) {
        return $prompt->contains('reset my password');
    });

    SupportAgent::assertNotPrompted('Unrelated prompt text');
});

test('structured invoice extraction generates validated fake schema data', function () {
    // Structured output agents auto-generate valid mock data matching their JSON schema
    InvoiceExtractor::fake();

    $data = InvoiceExtractor::make()->prompt('Sample invoice text...');

    expect($data)->toHaveKeys(['vendor', 'total', 'currency', 'items']);
});

test('image and audio generators are safely faked', function () {
    Image::fake();
    Audio::fake();

    $image = Image::of('A futuristic city')->generate();
    $transcription = Audio::transcribe('/path/to/audio.mp3')->text();

    Image::assertGenerated(fn ($img) => $img->prompt === 'A futuristic city');
    Audio::assertTranscribed('/path/to/audio.mp3');
});
```
