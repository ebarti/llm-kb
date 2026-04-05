---
title: "Matryoshka Representation Learning"
type: concept
sources: ["[[sources/huggingface-matryoshka-embeddings]]", "[[sources/modal-mteb-leaderboard]]"]
related: ["[[concepts/text-embeddings]]", "[[concepts/vector-search]]", "[[entities/sentence-transformers]]"]
last_compiled: 2026-04-05
summary: "Training technique that produces embeddings usable at any dimension by frontloading important information in earlier dimensions — preserving 98.37% of performance at just 8.3% of original size, now standard in state-of-the-art models."
---

## Overview

Matryoshka Representation Learning (MRL) is a training technique introduced by Kusupati et al. (NeurIPS 2022) that produces [[concepts/text-embeddings]] whose first d dimensions form a useful embedding for any d, not just the full dimensionality. Named after Russian nesting dolls, MRL models concentrate the most important information in the earliest dimensions, with later dimensions adding refinement.

This enables a single model to serve multiple deployment scenarios — from memory-constrained edge devices (64 dims) to high-accuracy cloud retrieval (768+ dims) — without training separate models for each.

## How It Works

### Standard Training

A normal embedding model trains with a loss function (e.g., CoSENT, contrastive) applied only to the full-dimensional output:

```
Loss = L(embed_768(text_a), embed_768(text_b))
```

### Matryoshka Training

MRL applies the **same loss function at multiple truncated dimensions simultaneously**:

```
Loss = L(embed_768) + L(embed_512) + L(embed_256) + L(embed_128) + L(embed_64)
```

Each truncated embedding `embed_d` is simply the first d dimensions of the full embedding. By optimizing all truncations jointly, the model learns to place the most discriminative information in the earliest dimensions.

Key properties:
- **No training overhead**: Training with MatryoshkaLoss adds negligible time compared to standard training
- **Weights optional**: Each dimension's loss can be weighted differently (default: equal weights)
- **Any loss function**: Works with CoSENT, contrastive, triplet, or any standard embedding loss

## Performance

Tested on STSBenchmark with mpnet-base architecture:

| Dimensions | % of Full Size | Matryoshka Performance | Standard Performance |
|-----------|---------------|----------------------|---------------------|
| 768 | 100% | Baseline (higher) | Baseline |
| 512 | 66.7% | ~99.5% | ~99% |
| 256 | 33.3% | ~99% | ~98% |
| 128 | 16.7% | ~98.8% | ~97.5% |
| 64 | 8.3% | **98.37%** | 96.46% |

The Matryoshka model degrades significantly more gracefully — a nearly 2 percentage point advantage at 64 dimensions.

## Comparison to PCA

Post-hoc dimensionality reduction via PCA is an alternative to reduce embedding size after training. However, MRL **almost always outperforms PCA** at equivalent compression ratios because:

- PCA is a linear transformation applied after the fact — it cannot restructure what information the model encodes
- MRL trains the model to produce high-quality representations at small sizes as a **primary objective**

## Practical Usage

### Inference

```python
model = SentenceTransformer("nomic-ai/nomic-embed-text-v1.5", truncate_dim=64)
embeddings = model.encode(["Hello world"])  # Shape: (1, 64)
```

**Critical**: Normalize embeddings **after** truncation, not before. Normalizing only before truncation produces slightly incorrect results.

### Two-Stage Retrieval Application

MRL enables an elegant two-stage approach within a single model:
1. **Fast retrieval**: Use 64-dim truncated embeddings for initial candidate selection (faster distance computation, smaller index)
2. **Accurate reranking**: Re-score top candidates using full 768-dim embeddings from the same model

## Adoption

As of 2025-2026, Matryoshka training is standard in state-of-the-art embedding models:

- **OpenAI text-embedding-3-small/large**: Native MRL support
- **Nomic Embed v1.5**: 10.5M+ downloads, native MRL
- **Gemini Embedding 2 Preview** (March 2026): Native MRL, 3072 dims
- **stella_en_1.5B_v5**: Matryoshka variable dimensions
- **BGE Base Financial Matryoshka**: Domain-specific with MRL

## Sources

- [[sources/huggingface-matryoshka-embeddings]] — complete tutorial with training and inference code
- [[sources/modal-mteb-leaderboard]] — MRL adoption in top MTEB models

## Related Concepts

- [[concepts/text-embeddings]] — the representations being compressed
- [[concepts/vector-search]] — benefits from reduced dimensions (faster retrieval, smaller index)
- [[entities/sentence-transformers]] — the library supporting MRL training
