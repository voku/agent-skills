---
id: sec-authentication-rate-limiting
title: "Authentication, Rate Limiting, and Session Fixation"
category: authentication
priority: HIGH
triggers: [missing-login-throttle, brute-force-vulnerability, session-fixation, weak-password-rules]
tags: [security, laravel, authentication, rate-limiting, session-fixation, brute-force, owasp]
---

# Authentication, Rate Limiting, and Session Fixation

**Trigger Anchor:** Apply rate limiting (`throttle:login` or `RateLimiter`) on authentication and sensitive endpoints; regenerate session IDs upon login to prevent session fixation; enforce strong password rules using `Password::defaults()`.

---

### Bad
```php
// ❌ Unthrottled login endpoint vulnerable to credential stuffing and brute force
Route::post('/login', [AuthController::class, 'login']);

// ❌ Missing session regeneration after successful login allows session fixation
class AuthController extends Controller
{
    public function login(Request $request): Response
    {
        if (Auth::attempt($request->only('email', 'password'))) {
            // Session ID not regenerated! Attacker with pre-set session gains access!
            return redirect()->intended('/dashboard');
        }
        return back()->withErrors(['email' => 'Invalid credentials']);
    }
}
```

### Good
```php
// ✅ Throttle rate limiting applied to authentication routes
Route::post('/login', [AuthController::class, 'login'])
    ->middleware('throttle:5,1'); // Max 5 attempts per minute

// ✅ Session regeneration on login and password validation rules
class AuthController extends Controller
{
    public function login(Request $request): RedirectResponse
    {
        $credentials = $request->validate([
            'email'    => ['required', 'email'],
            'password' => ['required', 'string'],
        ]);

        if (Auth::attempt($credentials, $request->boolean('remember'))) {
            $request->session()->regenerate(); // Prevents session fixation attacks
            return redirect()->intended('/dashboard');
        }

        return back()->withErrors(['email' => 'The provided credentials do not match our records.']);
    }
}
```
