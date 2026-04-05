---
title: "Approximate Nearest Neighbor Search (ANN)"
type: concept
sources: ["[[sources/pinecone-hnsw-explained]]", "[[sources/xenoss-vector-db-comparison]]"]
related: ["[[concepts/hnsw]]", "[[concepts/vector-search]]", "[[concepts/vector-databases]]"]
last_compiled: 2026-04-05
summary: "Trading small amounts of accuracy for dramatic speed gains when searching high-dimensional vector spaces: the foundational tradeoff underlying all vector database indexing."
---

## Overview

Approximate Nearest Neighbor (ANN) search finds vectors close to a query vector without guaranteeing the exact nearest neighbors. This tradeoff — accepting slightly imperfect results for orders-of-magnitude speed improvement — is the foundation of scalable [[concepts/vector-search]].

Exact nearest-neighbor search requires computing distances to every vector in the collection (O(n) per query). At million or billion scale, this is impractical. ANN algorithms reduce query complexity to O(log n) or O(sqrt(n)) by building index structures that enable guided traversal of the vector space.

## The Fundamental Tradeoff

**Recall** measures what fraction of true nearest neighbors the ANN algorithm finds. A recall of 95% means 5% of the time the algorithm misses a true nearest neighbor and returns a slightly more distant vector instead.

This is why the HN debate captured in [[sources/hn-vector-database-debate]] argues that the real question is not "do you need a vector database?" but "do you need approximate nearest-neighbor search?" — because ANN is inherently approximate.

## Major Algorithm Families

### Graph-Based: [[concepts/hnsw]]
Build a multi-layer proximity graph. Navigate greedily from coarse to fine layers. Dominant approach in modern vector databases. Best balance of speed, recall, and generality.

### Partition-Based: IVF (Inverted File Index)
Cluster vectors using k-means, then search only nearby clusters. Fast with low memory but recall depends on number of probes (nprobes). pgvector's default uses IVF with nprobes=3, yielding only ~50% recall.

### Quantization-Based: Product Quantization (PQ)
Compress vectors by splitting into sub-vectors and quantizing each. Dramatically reduces memory (often 10-100x). Can combine with IVF or HNSW. Trades recall/speed for memory savings.

### Hash-Based: Locality-Sensitive Hashing (LSH)
Hash similar vectors to the same buckets. Simple and fast but generally lower recall than graph-based methods. Largely superseded by HNSW for most applications.

## Choosing an Algorithm

- **General purpose, high recall**: HNSW (most vector databases default to this)
- **Memory constrained, billion scale**: IVF+PQ or HNSW+PQ composites
- **Perfect accuracy needed**: Flat/brute-force (only viable for <100K vectors)
- **Existing PostgreSQL**: pgvector with HNSW index (not the default IVF)

## Sources

- [[sources/pinecone-hnsw-explained]] — detailed HNSW analysis as the leading ANN approach
- [[sources/xenoss-vector-db-comparison]] — ANN implementations across vector databases

## Related Concepts

- [[concepts/hnsw]] — the dominant ANN algorithm
- [[concepts/vector-search]] — the application that needs ANN
- [[concepts/vector-databases]] — infrastructure implementing ANN
