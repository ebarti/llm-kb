---
title: "Source: Hierarchical Navigable Small Worlds (HNSW)"
type: source-summary
source: "[[raw/pinecone-hnsw-explained]]"
related: ["[[concepts/hnsw]]", "[[concepts/approximate-nearest-neighbor-search]]", "[[concepts/vector-search]]", "[[entities/faiss]]"]
last_compiled: 2026-04-05
summary: "Pinecone's deep technical walkthrough of the HNSW algorithm: multi-layer graph structure, parameters (M, efConstruction, efSearch), performance characteristics on Sift1M, and memory tradeoffs."
reading_time: "2 min"
---

## Key Points

- HNSW combines skip lists (1990) and navigable small world graphs (2011-2014) into a hierarchical multi-layer graph
- Layer distribution: 1M vectors yields ~968K at layer 0, ~30K at layer 1, ~950 at layer 2, <100 at layers 3+
- Search: greedy traversal from top layer entry point, descending at local minima
- Key parameters: M (neighbors per vertex), efConstruction (build-time candidates), efSearch (query-time candidates)
- Sift1M: M=4/efSearch=40 gives 80% recall at 1ms; M=32/efSearch=200 gives 99% recall at 50ms
- Memory scales linearly with M: 0.5GB (M=2) to 5GB (M=512) for 1M vectors
- Complexity: O(log n) search, O(M*n) space
- efConstruction improves recall with negligible effect on single-query search time

## Detailed Summary

The article provides the most thorough technical treatment of [[concepts/hnsw]] found in this research. It explains how the algorithm constructs a multi-layer graph where each layer contains an exponentially decreasing subset of vectors. Search proceeds greedily from the sparse top layer (long-range navigation) to the dense bottom layer (fine-grained nearest neighbors). The practical tuning guidance is especially valuable: increase efConstruction aggressively for better recall at minimal latency cost; tune M and efSearch against memory budget; consider composite indexes (HNSW+PQ) for memory-constrained deployments.

## Related Concepts

- [[concepts/hnsw]] — the algorithm itself
- [[concepts/approximate-nearest-neighbor-search]] — the problem class
- [[concepts/vector-search]] — the application domain
- [[entities/faiss]] — library implementing HNSW
