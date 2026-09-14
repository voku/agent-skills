---
id: fake-facades
title: "Faking Built-in Facades: Mail, Queues, Events, Storage"
category: fake
priority: HIGH
triggers: [real-email-sent-in-test, real-disk-written-in-test, un-faked-event-listener, un-faked-queue-job]
tags: [laravel, testing, fakes, mail-fake, queue-fake, event-fake, storage-fake]
---

# Faking Built-in Facades: Mail, Queues, Events, Storage

**Trigger Anchor:** Intercept and test side effects by faking Laravel facades (`Mail::fake()`, `Queue::fake()`, `Event::fake()`, `Storage::fake()`) with callback assertions verifying payload contents.

---

### Bad
```php
<?php

// ❌ Never let feature tests write to real disks, send network requests, or queue live jobs
test('uploads avatar and sends confirmation', function () {
    // ❌ Writes to real storage/app/public directory
    $file = UploadedFile::fake()->image('avatar.jpg');
    $this->post('/avatar', ['file' => $file]);

    // ❌ Attempts to send real email or fails if SMTP server is down
});
```

### Good
```php
<?php

declare(strict_types=1);

use App\Events\OrderShipped;
use App\Jobs\ProcessVideoJob;
use App\Mail\OrderReceiptMail;
use Illuminate\Http\UploadedFile;
use Illuminate\Support\Facades\Event;
use Illuminate\Support\Facades\Mail;
use Illuminate\Support\Facades\Queue;
use Illuminate\Support\Facades\Storage;

test('fakes storage, mail, queues, and events with exact payload assertions', function () {
    // 1. Storage Fake
    Storage::fake('avatars');
    $file = UploadedFile::fake()->image('profile.png');
    $this->postJson('/api/me/avatar', ['avatar' => $file])->assertOk();
    Storage::disk('avatars')->assertExists($file->hashName());

    // 2. Mail Fake
    Mail::fake();
    // ... trigger order action ...
    Mail::assertSent(OrderReceiptMail::class, function ($mail) {
        return $mail->hasTo('customer@example.com') && $mail->order->total_cents === 5000;
    });

    // 3. Queue Fake
    Queue::fake();
    // ... trigger video upload ...
    Queue::assertPushed(ProcessVideoJob::class, fn ($job) => $job->videoId === 42);

    // 4. Event Fake
    Event::fake([OrderShipped::class]);
    // ... mark order shipped ...
    Event::assertDispatched(OrderShipped::class);
});
```
