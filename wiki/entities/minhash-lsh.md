---
title: "MinHash LSH"
type: entity
entity_type: tool
sources: ["[[sources/data-deduplication-trillion-scale]]", "[[sources/dclm-datacomp-language-models]]", "[[sources/fineweb-dataset-huggingface]]"]
related: ["[[concepts/data-deduplication]]", "[[concepts/training-data-curation]]"]
last_compiled: 2026-04-05
summary: "Probabilistic algorithm combining MinHash signatures with Locality-Sensitive Hashing to efficiently detect near-duplicate documents at trillion-token scale — the standard deduplication method for LLM training data."
---

## Overview

MinHash LSH (MinHash with Locality-Sensitive Hashing) is the dominant algorithm for near-duplicate detection in LLM training data pipelines. It estimates Jaccard similarity between document sets without computing explicit pairwise intersections, enabling scalable deduplication at trillion-token scale.

## How It Works

### Step 1: Shingling
Convert each document into a set of character n-grams (shingles). For example, "the cat" with n=3 produces {"the", "he ", "e c", " ca", "cat"}.

### Step 2: MinHash Signatures
Apply k independent hash functions to each shingle set. For each hash function, retain only the minimum hash value. The resulting k minimum values form the document's "signature" — a fixed-length vector that approximates the Jaccard similarity of the original sets.

### Step 3: LSH Banding
Divide each signature into b bands of r rows (k = b * r). Hash each band independently into buckets. If two documents share at least one bucket, they become candidate duplicates. The probability of detecting a duplicate pair with Jaccard similarity s is approximately 1 - (1 - s^r)^b, providing a tunable S-curve threshold.

## Performance Characteristics

- **Time complexity**: O(n * k) for signature generation, O(n) for LSH bucketing
- **Space complexity**: O(n * k) for signatures
- **Tunable tradeoff**: adjusting b and r controls the precision-recall balance
- **Scalability**: works at trillion-token scale with appropriate infrastructure

## Variants and Improvements

- **LSHBloom**: uses Bloom filter indices instead of prefix trees for memory efficiency
- **Weighted MinHash**: handles documents of varying importance
- **SuperMinHash**: improved variance reduction for small signature sizes

## Tools

- **text-dedup**: all-in-one Python library with MinHash implementation
- **duplodocus** (Allen AI): Rust-based for high performance
- **Milvus 2.6**: database-integrated MinHash LSH for end-to-end pipelines

## Mentioned In

- [[sources/data-deduplication-trillion-scale]] — detailed technique explanation
- [[sources/dclm-datacomp-language-models]] — compared with Bloom filter dedup
- [[sources/fineweb-dataset-huggingface]] — per-dump MinHash dedup strategy
