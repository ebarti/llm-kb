---
title: "Qdrant"
type: entity
entity_type: tool
sources: ["[[sources/xenoss-vector-db-comparison]]"]
related: ["[[concepts/vector-databases]]", "[[concepts/vector-search]]", "[[concepts/hnsw]]", "[[entities/pinecone]]", "[[entities/weaviate]]", "[[comparisons/pinecone-vs-qdrant-vs-weaviate]]"]
last_compiled: 2026-04-05
summary: "Open-source vector database written in Rust: HNSW indexing, richest feature set (hybrid search, geo-spatial, multi-vector, sparse vectors), 326 QPS, available as self-hosted, managed cloud, or hybrid deployment."
---

## Overview

Qdrant is an open-source [[concepts/vector-databases|vector database]] written in Rust, engineered for performance and feature richness. It offers the broadest feature set among the major vector databases, including [[concepts/hybrid-search]], geo-spatial search, multi-vector support, and sparse vectors.

## Key Features

- **Rust-based**: Memory safety and raw computational speed
- **[[concepts/hnsw]] indexing**: Sub-50ms ANN queries
- **Hybrid search**: Native BM25 + dense vector support
- **Multi-vector search**: Multiple embeddings per document
- **Sparse vector support**: For learned sparse models (SPLADE, etc.)
- **Geo-spatial search**: Location-based filtering
- **Deployment flexibility**: Self-hosted, managed cloud, hybrid cloud, private cloud
- **Compliance**: SOC 2 Type II, GDPR, HIPAA-ready enterprise

## Performance

- 326 QPS (vs Weaviate 791, Pinecone 150)
- Cloud Inference unifies embedding generation
- Answer generation remains in application layer (unlike Pinecone Assistant or Weaviate generative module)

## Pricing

- Free: 1GB cluster
- Hybrid cloud: $0.014/hour
- Custom private cloud pricing

## When to Choose Qdrant

Ideal for organizations needing advanced search features (hybrid, geo-spatial, multi-vector, sparse vectors) and cost-effective self-hosting. Particularly strong for teams comfortable managing infrastructure in exchange for flexibility and lower costs at scale.

## Mentioned In

- [[sources/xenoss-vector-db-comparison]] — comprehensive comparison with Pinecone and Weaviate
