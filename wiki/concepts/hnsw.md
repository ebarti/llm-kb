---
title: "HNSW (Hierarchical Navigable Small World)"
type: concept
sources: ["[[sources/pinecone-hnsw-explained]]", "[[sources/xenoss-vector-db-comparison]]"]
related: ["[[concepts/approximate-nearest-neighbor-search]]", "[[concepts/vector-search]]", "[[concepts/vector-databases]]", "[[entities/faiss]]"]
last_compiled: 2026-04-05
summary: "The dominant graph-based ANN algorithm for vector search: a multi-layer proximity graph enabling O(log n) nearest-neighbor queries with 80-99% recall at 1-50ms latency, used by nearly all major vector databases."
---

## Overview

Hierarchical Navigable Small World (HNSW) is a graph-based algorithm for [[concepts/approximate-nearest-neighbor-search]] in high-dimensional spaces. Introduced by Malkov and Yashunin (2016), it has become the default indexing algorithm in nearly all major [[concepts/vector-databases]] including [[entities/weaviate]], [[entities/qdrant]], and [[entities/faiss]].

HNSW combines two foundational ideas:
1. **Probability skip lists** (Pugh, 1990): Multi-layer data structures where higher layers provide express lanes for traversal
2. **Navigable small world graphs** (2011-2014): Networks where greedy routing efficiently finds short paths between any two nodes

## Multi-Layer Structure

HNSW builds a hierarchy of proximity graphs where each layer contains a subset of vectors:

- **Top layers**: Few nodes with long-range connections — fast coarse navigation
- **Bottom layer (layer 0)**: All nodes with short-range connections — precise local search

Vectors are assigned to layers probabilistically using: `floor(-ln(rand(0,1))) × mL` where mL = 1/ln(M). This creates exponential distribution:

| Layer | Vectors (1M total) |
|-------|-------------------|
| 0 | ~968,746 |
| 1 | ~30,276 |
| 2 | ~951 |
| 3+ | <100 each |

## Search Algorithm

1. Start at the top layer's entry point with ef=1
2. **Zoom-out phase**: Greedily traverse through sparse upper layers, finding the nearest neighbor at each layer
3. At each local minimum, descend to the next layer
4. **Zoom-in phase**: At the bottom layer, expand search with efSearch candidates
5. Return the top-k nearest neighbors from the candidate set

The hierarchical structure ensures logarithmic complexity — like taking highways (upper layers) to get near the destination, then local streets (lower layers) for the final approach.

## Construction Algorithm

Vectors are inserted sequentially:

1. **Phase 1** (upper layers): Greedy search with ef=1 to find insertion neighborhood
2. **Phase 2** (insertion layer and below): Increase ef to efConstruction, select M nearest neighbors as connections
3. Create bidirectional links. Layer 0 allows up to M_max0 = 2M connections; upper layers allow M_max = M.

## Critical Parameters

| Parameter | Function | Tuning Guidance |
|-----------|----------|----------------|
| **M** | Max bidirectional links per node (non-layer-0) | Higher = better recall, more memory. Start with 16-32. |
| **efConstruction** | Candidates evaluated during index building | Increase aggressively — minimal effect on query latency, improves recall. 100-400 typical. |
| **efSearch** | Candidates evaluated at query time | Primary recall vs speed knob. 40-200 typical. |
| **mL** | Layer assignment multiplier | Usually fixed at 1/ln(M). |

## Performance Characteristics (Sift1M)

| M | efSearch | Recall | Latency |
|---|---------|--------|---------|
| 4 | 40 | 80% | ~1ms |
| 16 | 100 | 95% | ~10ms |
| 32 | 200 | 99% | ~50ms |

**Memory**: Scales linearly with M. For 1M vectors: M=2 requires >0.5GB; M=512 requires ~5GB.

**Key insight**: efConstruction has negligible effect on single-query search time but significantly improves recall. It is the cheapest parameter to increase.

## Comparison to Alternatives

| Algorithm | Speed | Recall | Memory | Best For |
|-----------|-------|--------|--------|----------|
| **HNSW** | Fast | High | High | General purpose, most vector DBs |
| **IVF** | Fast | Medium | Lower | Large collections with memory constraints |
| **IVF+PQ** | Fast | Medium | Low | Billion-scale with compression |
| **Flat** | Slow | Perfect | Medium | Small collections, exact results |
| **LSH** | Fast | Low-Med | Low | Largely superseded by HNSW |

## Limitations

- **High memory**: Stores full vector connections (no quantization), unlike IVF+PQ
- **Build time**: Index construction is slower than IVF approaches
- **Not updatable in-place** in some implementations — requires periodic rebuild

## Sources

- [[sources/pinecone-hnsw-explained]] — comprehensive parameter analysis and Sift1M benchmarks
- [[sources/xenoss-vector-db-comparison]] — HNSW as the standard engine in Qdrant and Weaviate

## Related Concepts

- [[concepts/approximate-nearest-neighbor-search]] — the problem HNSW solves
- [[concepts/vector-search]] — the application domain
- [[concepts/vector-databases]] — where HNSW runs in production
