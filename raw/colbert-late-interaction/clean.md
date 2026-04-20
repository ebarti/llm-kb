---
title: "Late Interaction Retrieval Models: ColBERT, ColPali, and ColQwen"
source: "https://weaviate.io/blog/late-interaction-overview"
author: "Weaviate Team"
date_published: 2024-11-15
date_ingested: 2026-04-05
tags: [colbert, late-interaction, retrieval, colpali, colqwen, multimodal]
type: article
status: raw
discovered_via: search
---

# Late Interaction Retrieval Models: ColBERT, ColPali, and ColQwen

## What Are Late Interaction Models?

Late interaction retrieval models represent a middle ground between bi-encoders (single vector per document) and cross-encoders (full query-document processing at query time). They "keep token-level embeddings and apply the MaxSim operator to calculate the relevance scores."

## Core Technical Mechanism

1. For each query token, compute similarity scores against all document tokens
2. Retain only the maximum similarity score per query token (MaxSim)
3. Sum all maximum scores into a final relevance ranking

This captures contextual nuances without expensive query-time cross-encoding.

## ColBERT: Text-Based Late Interaction

ColBERT (Contextualized Late Interaction over BERT) builds on BERT's 110M-parameter foundation. Reduces embedding dimensionality from 768 to 128 dimensions. Stores individual token embeddings rather than pooled document vectors.

**Storage Trade-offs**: ColBERTv2 introduced aggressive quantization reducing vectors from 256 bytes to 20 bytes through "residual compression" — still roughly 6-10x more space than single-vector approaches.

**Performance**: Competitive with BERT-based models while executing two orders-of-magnitude faster and requiring four orders-of-magnitude fewer FLOPs per query. Particularly strong at zero-shot retrieval in new domains.

## Multimodal Extensions

**ColPali** (~3B parameters, PaliGemma vision model): Treats PDFs as images processed into uniform patches, eliminating complex OCR pipelines.

**ColQwen** (~2B parameters, Qwen2-VL, Apache 2.0): Same approach with different vision backbone.

Both maintain 128-dimensional embedding standard while processing document patches rather than text tokens.

## Practical Applications

- Legal document RAG pipelines requiring contextual precision
- Financial verification systems
- Complex PDF analysis with mixed content types

## RAGatouille

The RAGatouille library makes it easy to use ColBERT in any RAG pipeline, focusing on modularity and ease-of-use.
