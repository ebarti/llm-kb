---
title: "Source: Data Deduplication at Trillion Scale"
type: source-summary
source: "[[raw/data-deduplication-trillion-scale]]"
related: ["[[concepts/data-deduplication]]", "[[concepts/training-data-curation]]", "[[entities/minhash-lsh]]"]
last_compiled: 2026-04-05
summary: "Practical guide to deduplicating LLM training data at trillion-token scale: exact matching, MinHash LSH, and semantic methods with trade-offs between precision, recall, and computational cost."
---

## Key Points

- Unchecked duplication causes: wasted compute, overfitting, verbatim memorization, evaluation leakage
- Three approaches: exact matching (fast but misses near-dupes), semantic matching (accurate but expensive), approximate/MinHash LSH (best tradeoff at scale)
- MinHash estimates Jaccard similarity via document → shingles → hash functions → min-value signatures
- LSH accelerates by dividing signatures into bands, hashing each into buckets
- LSHBloom uses Bloom filter indices instead of prefix trees for better memory efficiency
- Open-source tools: text-dedup, duplodocus (Rust, Allen AI), semhash (semantic)

## Detailed Summary

Data deduplication is a foundational but often underappreciated step in the LLM training data pipeline. This source provides a practical taxonomy of approaches and their tradeoffs at different scales.

Exact matching via cryptographic hashing is the simplest approach but misses near-duplicates — web content frequently appears with minor formatting variations across domains. Semantic matching using vector embeddings catches conceptual duplicates but is prohibitively expensive at trillion-token scale.

The sweet spot is [[entities/minhash-lsh]]: a probabilistic method that converts documents into fixed-length signatures via min-hashing of n-gram shingles, then uses locality-sensitive hashing to efficiently group candidate duplicates. The banding strategy provides a tunable precision-recall tradeoff by adjusting the number and size of bands.

Recent innovations include LSHBloom (Bloom filter-based indexing for better memory efficiency) and integration into vector databases like Milvus for end-to-end deduplication pipelines.

## Related Concepts

- [[concepts/data-deduplication]] — comprehensive treatment of dedup methods
- [[concepts/training-data-curation]] — dedup as a key pipeline stage
- [[concepts/benchmark-contamination]] — duplicate content spanning train/test as evaluation leakage
