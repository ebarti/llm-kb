---
title: "Weaviate"
type: entity
entity_type: tool
sources: ["[[sources/xenoss-vector-db-comparison]]", "[[sources/weaviate-hybrid-search-explained]]", "[[sources/weaviate-chunking-strategies]]"]
related: ["[[concepts/vector-databases]]", "[[concepts/hybrid-search]]", "[[concepts/hnsw]]", "[[entities/pinecone]]", "[[entities/qdrant]]", "[[comparisons/pinecone-vs-qdrant-vs-weaviate]]"]
last_compiled: 2026-04-05
summary: "Cloud-native open-source vector database: highest QPS (791), native hybrid search with alpha parameter and BM25F, generative module for server-side RAG, HIPAA on AWS (2025)."
---

## Overview

Weaviate is a cloud-native, open-source [[concepts/vector-databases|vector database]] that delivers the highest raw query throughput among the major vector databases and the most seamless [[concepts/hybrid-search]] integration.

## Key Features

- **Optimized [[concepts/hnsw]]**: Sub-50ms ANN query response
- **Highest QPS**: 791 (vs Qdrant 326, Pinecone 150)
- **Native hybrid search**: Alpha parameter (0-1) controls keyword/vector balance; default 0.75
- **[[concepts/bm25|BM25F]]**: Per-field weighting for keyword search (v1.17+)
- **Two fusion algorithms**: rankedFusion (default) and relativeScoreFusion
- **Generative module** (v1.30+): Register LLM providers for server-side RAG in a single API call
- **Deployment**: Self-hosted, serverless, enterprise cloud
- **Compliance**: SOC 2 Type II, GDPR, HIPAA on AWS (2025)

## Hybrid Search Implementation

Weaviate's hybrid search is the most thoroughly documented:

```
{
  Get {
    Article(
      hybrid: {
        query: "machine learning"
        alpha: 0.75  // 0=keyword, 1=vector
      }
    ) {
      title
      content
    }
  }
}
```

Results merged via Reciprocal Rank Fusion or relative score fusion.

## Pricing

- Serverless: $25/month
- Enterprise: $2.64/AI unit
- Custom private cloud options

## When to Choose Weaviate

Ideal for teams requiring highest query throughput, seamless full-text + vector search integration, and native server-side RAG capabilities. Strong open-source community with comprehensive documentation.

## Mentioned In

- [[sources/xenoss-vector-db-comparison]] — full comparison with Pinecone and Qdrant
- [[sources/weaviate-hybrid-search-explained]] — hybrid search architecture
- [[sources/weaviate-chunking-strategies]] — chunking strategy guide
