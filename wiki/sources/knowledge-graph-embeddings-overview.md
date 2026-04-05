---
title: "Source: Knowledge Graph Embedding — Technical Overview"
type: source-summary
source: "[[raw/knowledge-graph-embeddings-overview]]"
related: ["[[concepts/knowledge-graph-embeddings]]", "[[concepts/knowledge-graph-completion]]", "[[concepts/knowledge-graph]]"]
last_compiled: 2026-04-05
summary: "Comprehensive overview of KGE models: tensor decomposition (DistMult, ComplEx), geometric (TransE family, RotatE), deep learning (ConvE, CapsE), with training methodology, benchmarks, and relationship to modern LLMs."
reading_time: "2 min"
---

## Key Points

- KGE learns low-dimensional representations of entities and relations preserving semantic meaning
- Three model families: tensor decomposition (DistMult, ComplEx, TuckER), geometric (TransE, TransH, TransR, RotatE), deep learning (ConvE, ConvKB, CapsE)
- Training via corrupted triple generation and loss minimization
- Evaluation: Hits@K, Mean Rank, Mean Reciprocal Rank on FB15k, WN18, FB15k-237, WN18RR, YAGO3-10
- Applications: link prediction, relation prediction, triple classification, recommender systems, drug repurposing
- KGE complements LLMs — structured interpretable embeddings vs. broad semantic patterns

## Detailed Summary

Knowledge graph embeddings map entities and relations to continuous vector spaces where a scoring function f_r(h,t) measures triple plausibility. The three major model families represent different mathematical approaches:

**Tensor decomposition models** (DistMult, ComplEx, TuckER, SimplE) decompose the knowledge graph tensor into factor matrices. ComplEx extends DistMult to complex vector spaces, enabling asymmetric relation handling.

**Geometric models** represent relations as geometric transformations. TransE enforces h + r = t but struggles with one-to-many relations. Extensions (TransH, TransR, TransD) project into relation-specific spaces. RotatE uses complex rotations for superior expressiveness.

**Deep learning models** (ConvE with 2D convolutions, ConvKB with 1D filters, CapsE with capsule networks) learn non-linear interaction patterns, with ConvE achieving 8x parameter reduction vs. DistMult.

These traditional KGE methods are increasingly complemented by LLM approaches, which capture broader semantic patterns but trade off the structured interpretability that KGE provides.

## Related Concepts

- [[concepts/knowledge-graph-embeddings]] — the central topic
- [[concepts/knowledge-graph-completion]] — primary application
