---
title: "Source: What is ColBERT and Late Interaction"
type: source-summary
source: "[[raw/jina-colbert-late-interaction]]"
related: ["[[concepts/colbert-late-interaction]]", "[[concepts/bi-encoder-vs-cross-encoder]]", "[[concepts/text-embeddings]]"]
last_compiled: 2026-04-05
summary: "Jina AI's technical overview of ColBERT's late interaction mechanism: per-token embeddings with MaxSim scoring, 180-23,000x faster than BERT reranking, and ColBERTv2's 6-10x storage compression."
reading_time: "1 min"
---

## Key Points

- ColBERT generates per-token embeddings (128 dims each) for both queries and documents, unlike single-vector bi-encoders
- MaxSim scoring: dot-product between all query-document token pairs, max-pool per query token, sum for final score
- 180x fewer FLOPs than BERT at k=10; 23,000x at k=2000
- ColBERT Recall@50 exceeds BM25 Recall@1000
- ColBERTv2 adds residual compression (6-10x storage reduction) and denoised supervision
- Jina-ColBERT extends context to 8192 tokens; BEIR NDCG 52.6 vs ColBERTv2's 51.7
- Training: learning rate 3e-6, batch size 32, 200k iterations on MS MARCO

## Detailed Summary

The article explains how [[concepts/colbert-late-interaction]] occupies a middle ground between fast but lossy bi-encoders and accurate but slow cross-encoders. By encoding queries and documents independently at the token level, ColBERT enables pre-computation of document representations (like bi-encoders) while preserving fine-grained semantic matching (like cross-encoders). The MaxSim operation is the key innovation: for each query token, find its best-matching document token, then sum these maximum similarities. ColBERTv2 made this practical at scale through residual compression, and Jina-ColBERT further extends it to long documents.

## Related Concepts

- [[concepts/colbert-late-interaction]] — the retrieval paradigm
- [[concepts/bi-encoder-vs-cross-encoder]] — the architecture spectrum ColBERT bridges
- [[concepts/text-embeddings]] — the underlying representation
