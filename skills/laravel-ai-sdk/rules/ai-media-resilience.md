---
id: ai-media-resilience
title: "Media Generation, Speech Audio Processing, and Multi-Provider Failover"
category: media
priority: MEDIUM
triggers: [laravel-ai-images, audio-transcription-whisper, text-to-speech, ai-provider-failover]
tags: [laravel, ai, images, audio, whisper, tts, failover, resilience]
---

# Media Generation, Speech Audio Processing, and Multi-Provider Failover

**Trigger Anchor:** Generate images via `Image::of()`, perform speech transcription with `Audio::transcribe()`, convert text to audio with `Audio::speak()`, and configure automatic multi-provider fallback chains for high availability.

---

### Bad
```php
// ❌ Single-point-of-failure provider calls without fallback; unmanaged raw audio handling
use Laravel\Ai\Image;

public function generateAvatar(string $prompt)
{
    // If OpenAI is experiencing an outage or rate-limit, entire application feature crashes
    return Image::of($prompt)->provider('openai')->generate();
}
```

### Good
```php
// ✅ Multi-provider failover configuration in config/ai.php
// 'default' => 'anthropic',
// 'failover' => [
//     'anthropic' => ['openai', 'gemini'],
//     'openai' => ['anthropic'],
// ],

use Laravel\Ai\Audio;
use Laravel\Ai\Image;
use Illuminate\Http\UploadedFile;

class MediaService
{
    // 1. Image generation with landscape/portrait formatting and storage
    public function generateProductBanner(string $prompt): string
    {
        $image = Image::of($prompt)
            ->landscape()
            ->generate();

        return $image->store('ai-banners', 's3');
    }

    // 2. Speech-to-text audio transcription
    public function transcribeMeetingAudio(UploadedFile $audioFile): string
    {
        return Audio::transcribe($audioFile->getRealPath())
            ->language('en')
            ->text();
    }

    // 3. Text-to-speech generation
    public function generateWelcomeAudio(string $welcomeText): string
    {
        $audio = Audio::speak($welcomeText)
            ->voice('alloy')
            ->generate();

        return $audio->store('audio-greetings', 'public');
    }
}
```
