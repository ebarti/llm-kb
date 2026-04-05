---
title: "Vector Search"
type: concept
sources: ["[[sources/pinecone-hnsw-explained]]", "[[sources/redis-semantic-vs-keyword-search]]", "[[sources/weaviate-hybrid-search-explained]]", "[[sources/xenoss-vector-db-comparison]]"]
related: ["[[concepts/text-embeddings]]", "[[concepts/hnsw]]", "[[concepts/approximate-nearest-neighbor-search]]", "[[concepts/semantic-search]]", "[[concepts/hybrid-search]]", "[[concepts/vector-databases]]"]
last_compiled: 2026-04-05
summary: "Finding similar items by computing distance between dense vector embeddings in high-dimensional space, typically using ANN algorithms like HNSW for sub-millisecond retrieval at scale."
reading_time: "3 min"
---

## Overview

Vector search (also called vector similarity search) finds the items most similar to a query by computing distances between dense vector embeddings in high-dimensional space. It is the retrieval mechanism underlying [[concepts/semantic-search]] and the backbone of modern RAG pipelines.

## How It Works

1. **Embedding**: Convert all documents and queries into dense vectors using an [[concepts/text-embeddings]] model
2. **Indexing**: Store document vectors in a data structure optimized for nearest-neighbor lookup (e.g., [[concepts/hnsw]] graph, IVF index, or flat scan)
3. **Querying**: Encode the query into a vector, then find the k-nearest document vectors using a distance metric
4. **Ranking**: Return documents ordered by similarity score

## Distance Metrics

| Metric | Formula | Use Case |
|--------|---------|----------|
| **Cosine similarity** | A·B / (||A|| × ||B||) | Most common for text; range [-1, 1] |
| **Dot product** | A·B | Equivalent to cosine for normalized vectors; faster |
| **Euclidean (L2)** | sqrt(Σ(a-b)²) | Used in some HNSW implementations |

When embeddings are L2-normalized (standard practice), cosine similarity and dot product produce identical rankings.

## Indexing Algorithms

### Exact (Flat/Brute-Force)

Computes distance to every vector. Perfect recall but O(n) per query — only viable for small collections (<100K vectors).

### Approximate Nearest Neighbor (ANN)

Trade a small amount of accuracy for dramatic speed improvement. The dominant algorithms:

- **[[concepts/hnsw]]**: Graph-based, logarithmic search complexity. The most popular choice in production vector databases. 80-99% recall at 1-50ms depending on parameters.
- **IVF (Inverted File Index)**: Clusters vectors into partitions, searches only nearby partitions. pgvector's default (nprobes=3 gives ~50% recall; increase for better accuracy).
- **Product Quantization (PQ)**: Compresses vectors to reduce memory. Often combined with IVF or HNSW for large-scale deployment.
- **LSH (Locality-Sensitive Hashing)**: Hash-based approach. Largely superseded by HNSW for most applications.
- **ScaNN (Google)**: Quantization-based with learned scoring. Strong for very large collections.

See [[concepts/approximate-nearest-neighbor-search]] for algorithm details.

## Performance Characteristics

Based on Sift1M benchmark (1 million vectors):

| Configuration | Recall | Latency |
|--------------|--------|---------|
| HNSW M=4, efSearch=40 | 80% | ~1ms |
| HNSW M=32, efSearch=200 | 99% | ~50ms |
| Flat (exact) | 100% | ~100ms+ |
| IVF nprobes=3 | ~50% | <1ms |

The fundamental tradeoff is recall (accuracy) vs latency (speed). HNSW provides the best balance for most applications.

## Infrastructure Options

Vector search can run on:

- **Dedicated vector databases**: [[entities/pinecone]], [[entities/qdrant]], [[entities/weaviate]], Milvus, Chroma
- **Database extensions**: pgvector (PostgreSQL), Elasticsearch kNN
- **Libraries**: [[entities/faiss]], Annoy, ScaNN (embedded in application)
- **Cloud services**: Vertex AI Vector Search, Azure AI Search, Amazon OpenSearch

See [[concepts/vector-databases]] for when to use each option.

## Limitations

- **Approximate**: ANN algorithms may miss true nearest neighbors (the core tradeoff)
- **Embedding quality ceiling**: Results are only as good as the embeddings; garbage in, garbage out
- **Vocabulary gap**: Pure vector search can miss exact-match needs (product codes, error identifiers) — see [[concepts/hybrid-search]]
- **Dimensionality cost**: Higher dimensions = more memory and slower search
- **Cold start**: Requires embedding all documents before first query

## Sources

- [[sources/pinecone-hnsw-explained]] — detailed HNSW algorithm analysis with benchmarks
- [[sources/redis-semantic-vs-keyword-search]] — vector search architecture and index options
- [[sources/weaviate-hybrid-search-explained]] — dense vector component of hybrid search
- [[sources/xenoss-vector-db-comparison]] — infrastructure options and performance

## Related Concepts

- [[concepts/text-embeddings]] — what produces the vectors
- [[concepts/hnsw]] — the dominant ANN algorithm
- [[concepts/approximate-nearest-neighbor-search]] — the problem class
- [[concepts/semantic-search]] — the search paradigm
- [[concepts/hybrid-search]] — combining vector with keyword search
- [[concepts/vector-databases]] — where vectors are stored
