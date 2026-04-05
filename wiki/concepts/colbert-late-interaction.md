---
title: "ColBERT and Late Interaction"
type: concept
sources: ["[[sources/jina-colbert-late-interaction]]"]
related: ["[[concepts/bi-encoder-vs-cross-encoder]]", "[[concepts/text-embeddings]]", "[[concepts/vector-search]]", "[[concepts/reranking]]"]
last_compiled: 2026-04-05
summary: "A retrieval paradigm between bi-encoders and cross-encoders: encode queries and documents independently at the token level, then score via MaxSim — achieving near-cross-encoder accuracy at orders of magnitude less compute."
---

## Overview

ColBERT (Contextualized Late Interaction over BERT) is a retrieval model from Stanford that occupies the middle ground between fast-but-lossy bi-encoders and accurate-but-slow cross-encoders. It was introduced at SIGIR 2020 and has become a key architecture for high-quality retrieval at scale.

The core innovation: instead of compressing a document into a single vector (bi-encoder) or requiring joint query-document processing (cross-encoder), ColBERT produces **per-token embeddings** for both queries and documents. These are compared through a lightweight "late interaction" mechanism that preserves fine-grained semantic matching.

## How It Works

### Encoding

- **Query encoder**: Prepends [Q] token after BERT's [CLS], pads to Nq=32 tokens with [mask] tokens, runs through BERT + CNN layer + L2 normalization. Output: 32 vectors of 128 dimensions each.
- **Document encoder**: Prepends [D] token, no padding, same processing pipeline. Output: one 128-dim vector per document token.

Documents can be encoded offline (like bi-encoders), enabling pre-computation.

### MaxSim Scoring

The relevance score is computed via "late interaction":

1. **Dot product**: Compute similarities between all query-token and document-token pairs
2. **Max-pool**: For each query token, find its maximum similarity across all document tokens
3. **Sum**: Add up all the max similarities to get the final score

```
Score(q, d) = Σᵢ maxⱼ (qᵢ · dⱼ)
```

This MaxSim operation is the key: it captures which document tokens best match each query token, preserving fine-grained semantics without the full O(n*m) attention of a cross-encoder.

## Performance

ColBERT's efficiency gains are dramatic:

| Reranking Depth k | BERT FLOPs / ColBERT FLOPs |
|-------------------|---------------------------|
| 10 | 180x |
| 1000 | 13,900x |
| 2000 | 23,000x |

ColBERT's Recall@50 exceeds BM25's Recall@1000, demonstrating that late interaction captures far more relevant documents than keyword-based retrieval.

## ColBERTv2

ColBERTv2 (NAACL 2022) added two key improvements:

1. **Residual compression**: Instead of storing full token embeddings, store only the difference from the nearest centroid. Reduces storage by **6-10x**.
2. **Denoised supervision**: Iterative hard-negative mining using a cross-encoder (MiniLM) for distillation, improving training data quality.

## Jina-ColBERT

Jina AI extended ColBERT with:
- **8192 token context** (vs original 512-token limit)
- **Multilingual support**
- BEIR average NDCG: 52.6 (vs ColBERTv2's 51.7)
- Long-context benchmark (LoCo): 83.7 (vs ColBERTv2's 74.3)

## Tradeoffs

| Aspect | Bi-Encoder | ColBERT | Cross-Encoder |
|--------|-----------|---------|---------------|
| Speed | Fastest | Fast | Slowest |
| Accuracy | Good | Very Good | Best |
| Storage | 1 vector/doc | N vectors/doc | N/A (no pre-computation) |
| Pre-computation | Yes | Yes | No |
| Scalability | Billions | Millions | Thousands |

## Sources

- [[sources/jina-colbert-late-interaction]] — comprehensive technical overview

## Related Concepts

- [[concepts/bi-encoder-vs-cross-encoder]] — the architecture spectrum ColBERT bridges
- [[concepts/text-embeddings]] — the per-token embeddings ColBERT produces
- [[concepts/vector-search]] — retrieval infrastructure for ColBERT indexes
- [[concepts/reranking]] — what ColBERT partly replaces
