---
title: "Source: Introduction to Matryoshka Embedding Models"
type: source-summary
source: "[[raw/huggingface-matryoshka-embeddings]]"
related: ["[[concepts/matryoshka-representation-learning]]", "[[concepts/text-embeddings]]", "[[entities/sentence-transformers]]"]
last_compiled: 2026-04-05
summary: "Hugging Face tutorial on Matryoshka Representation Learning: training embeddings that can be truncated to any dimension with minimal quality loss, preserving 98.37% performance at just 8.3% of original size."
reading_time: "2 min"
---

## Key Points

- Matryoshka models frontload important information in earlier dimensions, enabling truncation without retraining
- Training applies the same loss function at multiple dimensions simultaneously (e.g., 768, 512, 256, 128, 64) with no notable training overhead
- At 64 dimensions (8.3% of 768), Matryoshka model preserves 98.37% of full-size performance vs 96.46% for standard models
- MRL consistently outperforms post-hoc PCA at equivalent compression ratios
- Inference speed for embedding generation is identical regardless of target dimension; downstream tasks (retrieval, clustering) are significantly faster
- Normalization must happen after truncation, not before

## Detailed Summary

The article provides a complete tutorial on [[concepts/matryoshka-representation-learning]], from theory through implementation with [[entities/sentence-transformers]]. The key innovation is that a single model produces embeddings usable at any dimension by training with `MatryoshkaLoss` — the loss function is applied to truncated versions of the embedding at each target dimension. This eliminates the need to train separate models for different deployment constraints. The practical implications are significant: teams can use shorter embeddings for fast retrieval and full-length embeddings for reranking, all from one model. Production-ready models like nomic-embed-text-v1.5 (10.5M downloads) already include Matryoshka training.

## Notable Quotes

> "Rather than applying a loss function on only the full-size embeddings, MRL also applies that same loss function on truncated portions of the embeddings."

## Related Concepts

- [[concepts/matryoshka-representation-learning]] — the core technique
- [[concepts/text-embeddings]] — the broader field
- [[entities/sentence-transformers]] — the library providing training support
