# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Core agent architecture & execution | Always |
| HIGH | Tools, vector search, and test fakes | Production apps |
| MEDIUM | Media generation and infrastructure failover | Media/resilience features |

## Section Overview

### 1. Agent Architecture (`agent`)
- **Impact:** CRITICAL
- **Rules:** `ai-agent-architecture`
- **Description:** Agent class definitions with `Promptable`, configuration attributes (`#[Provider]`, `#[Model]`, `#[Temperature]`), structured JSON schemas, streaming, and conversation memory.

### 2. Custom & Built-in Tools (`tool`)
- **Impact:** HIGH
- **Rules:** `ai-tool-integration`
- **Description:** Implementing custom tools with input JSON schema validation, dependency injection, registering tools on agents, and utilizing built-in provider tools (`WebSearch`, `SimilaritySearch`).

### 3. Embeddings, RAG, & Search (`embed`)
- **Impact:** HIGH
- **Rules:** `ai-embeddings-rag`
- **Description:** Generating and caching vector embeddings (`Str::toEmbeddings()`), vector database search (`pgvector`), cross-encoder relevance reranking (`Ai::rerank()`), and vector stores.

### 4. Media & Resilience (`media`)
- **Impact:** MEDIUM
- **Rules:** `ai-media-resilience`
- **Description:** Image generation with `Image::of()`, speech audio transcription and text-to-speech, and automatic multi-provider fallback chains for uptime resilience.

### 5. Deterministic Testing (`test`)
- **Impact:** HIGH
- **Rules:** `ai-testing-fakes`
- **Description:** Mocking agent responses via `Agent::fake()`, validating prompt inputs with assertions, preventing accidental live API calls with `Ai::preventStrayPrompts()`, and media fakes.
