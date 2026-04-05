---
title: "Data Deduplication"
type: concept
sources: ["[[sources/data-deduplication-trillion-scale]]", "[[sources/dclm-datacomp-language-models]]", "[[sources/fineweb-dataset-huggingface]]", "[[sources/nemotron-cc-nvidia]]"]
related: ["[[concepts/training-data-curation]]", "[[concepts/benchmark-contamination]]", "[[entities/minhash-lsh]]"]
last_compiled: 2026-04-05
summary: "Removing duplicate and near-duplicate documents from LLM training data at trillion-token scale using exact matching, MinHash LSH, or semantic methods — essential for preventing wasted compute, memorization, and evaluation leakage."
---

## Overview

Data deduplication removes identical and near-identical documents from LLM training corpora. At web scale, duplication is systemic: popular pages get mirrored, content syndicates across domains, and formatting variants create near-duplicates. Unchecked duplication wastes compute, promotes overfitting, enables verbatim memorization (a privacy concern), and creates evaluation leakage when duplicates span training and test sets.

## Methods

### Exact Matching

Cryptographic hashing (SHA-256, MD5) identifies byte-identical documents. Fast, precise, and simple to implement at any scale. The limitation is that it misses near-duplicates — a document with one changed word produces a completely different hash. Useful as a first pass but insufficient alone.

### MinHash Locality-Sensitive Hashing (LSH)

The dominant approach for near-duplicate detection at trillion-token scale. [[entities/minhash-lsh]] works in three steps:

1. **Shingling**: convert documents into sets of n-gram character sequences
2. **Min-hashing**: apply k independent hash functions, keep minimum values to create fixed-length signatures
3. **Banding**: divide signatures into b bands of r rows; hash each band into buckets; documents sharing any bucket become candidate duplicates

The banding strategy provides a tunable precision-recall tradeoff: more bands increase recall (catch more true duplicates) but also increase false positives.

[[sources/dclm-datacomp-language-models]] found MinHash-based approaches and modified Bloom filtering perform comparably (within 0.2 points on downstream metrics), but Bloom filters scale better beyond 10TB. Recent innovations include LSHBloom (Bloom filter indices for memory efficiency) and integration into vector databases for end-to-end pipelines.

### Semantic Deduplication

Embedding-based methods using models like SentenceTransformers to detect conceptually duplicate content (e.g., a news article rewritten for different outlets). Highly accurate but computationally expensive at trillion-token scale. Tools like semhash from MinishLab provide practical implementations.

## The Per-Dump vs Cross-Dump Discovery

[[sources/fineweb-dataset-huggingface]] discovered that deduplicating each Common Crawl dump independently outperforms global deduplication across dumps. When cross-dump dedup was applied chronologically, one dump lost 94% of its tokens — but models trained on the "duplicate" data actually performed better. The explanation: temporal repetition of genuinely high-quality content (popular, well-maintained pages) can be beneficial for training.

This finding has been widely adopted: both FineWeb and subsequent datasets use per-dump deduplication as the default strategy.

## Scale Challenges

[[sources/nemotron-cc-nvidia]] found that both DCLM and FineWeb-Edu contain approximately 80% near-duplicates after their respective filtering pipelines. For short training runs this is manageable (each document is seen approximately once), but for long-horizon training (15T+ tokens), models begin to see significant repetition, reducing the effective dataset diversity.

## Open-Source Tools

| Tool | Approach | Language | Notes |
|------|----------|----------|-------|
| text-dedup | All-in-one (exact, MinHash, SimHash, semantic) | Python | Most popular general tool |
| duplodocus (Allen AI) | Exact + MinHash | Rust | High performance for large datasets |
| semhash (MinishLab) | Semantic | Python | Multimodal support |
| LSHBloom | MinHash with Bloom filter index | Python | Memory-efficient alternative |

## Sources

- [[sources/data-deduplication-trillion-scale]] — practical guide to dedup at scale
- [[sources/dclm-datacomp-language-models]] — Bloom filter vs MinHash comparison
- [[sources/fineweb-dataset-huggingface]] — per-dump vs cross-dump discovery
- [[sources/nemotron-cc-nvidia]] — 80% near-duplicate finding in filtered datasets

## Related Concepts

- [[concepts/training-data-curation]] — dedup as a key pipeline stage
- [[concepts/benchmark-contamination]] — train/test overlap as a form of duplication
- [[concepts/model-based-filtering]] — interacts with dedup in the pipeline order
