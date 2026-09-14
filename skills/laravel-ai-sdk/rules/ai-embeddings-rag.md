---
id: ai-embeddings-rag
title: "Vector Embeddings, Similarity Search, Reranking, and RAG Stores"
category: embed
priority: HIGH
triggers: [vector-embeddings-cache, similarity-search-pgvector, rerank-documents, rag-file-vector-store]
tags: [laravel, ai, embeddings, pgvector, rerank, rag, vector-search]
---

# Vector Embeddings, Similarity Search, Reranking, and RAG Stores

**Trigger Anchor:** Generate and cache vector embeddings via `Str::toEmbeddings()`, query vector databases (e.g. PostgreSQL `pgvector`), rerank candidate documents using `Ai::rerank()`, and attach document stores for RAG context.

---

### Bad
```php
// ❌ Generating embeddings on every search query without caching or reranking
public function searchDocumentation(string $query)
{
    // Re-computing embeddings on every search without cache burns unnecessary API quota
    $vector = Http::post('https://api.openai.com/v1/embeddings', [
        'input' => $query,
        'model' => 'text-embedding-3-small',
    ])->json()['data'][0]['embedding'];

    // Taking top raw cosine similarity without cross-encoder reranking yields inaccurate semantic matches
    return Article::query()->orderByRaw('embedding <=> ?', [json_encode($vector)])->take(5)->get();
}
```

### Good
```php
// ✅ Generating, caching, querying, and reranking documentation embeddings
use Illuminate\Support\Facades\Cache;
use Illuminate\Support\Str;
use Laravel\Ai\Ai;
use App\Models\DocumentationArticle;

class SearchService
{
    public function search(string $userQuery): array
    {
        // 1. Generate query embedding with transparent caching for repeated queries
        $cacheKey = 'query_emb_' . md5($userQuery);
        $queryEmbedding = Cache::remember($cacheKey, now()->addDays(7), function () use ($userQuery) {
            return Str::of($userQuery)->toEmbeddings();
        });

        // 2. Coarse retrieval: Fetch top 20 candidate documents using pgvector cosine distance
        $candidates = DocumentationArticle::query()
            ->select(['id', 'title', 'content'])
            ->orderByRaw('embedding <=> ?', [json_encode($queryEmbedding)])
            ->take(20)
            ->get();

        // 3. Fine retrieval: Cross-encoder reranking to accurately score relevance
        $reranked = Ai::rerank(
            query: $userQuery,
            documents: $candidates->pluck('content', 'id')->all(),
            limit: 5
        );

        return $candidates->whereIn('id', array_keys($reranked))->values()->all();
    }
}
```
