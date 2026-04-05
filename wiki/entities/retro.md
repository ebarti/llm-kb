---
title: "RETRO (Retrieval-Enhanced Transformer)"
type: entity
entity_type: paper
url: "https://arxiv.org/abs/2112.04426"
related: ["[[concepts/memory-augmented-neural-networks]]", "[[concepts/cross-attention]]", "[[concepts/knowledge-storage-in-transformers]]"]
tags: [RETRO, retrieval-augmented, DeepMind, transformer, memorization]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "DeepMind's 7.5B parameter model matching GPT-3 (185B) by augmenting a transformer with a 2-trillion-token retrieval database accessed via chunked cross-attention — decoupling factual memorization from language reasoning."
---

## Overview

RETRO (Retrieval-Enhanced Transformer) is a language model architecture from DeepMind that demonstrates parametric knowledge can be largely replaced by retrieval. By combining a relatively small 7.5B parameter transformer with a 2-trillion-token retrieval database, RETRO matches the performance of GPT-3 (185B parameters) — achieving equivalent results at just 4% of the parameter count.

## Key Facts

- **Type**: Paper / model architecture
- **URL**: https://arxiv.org/abs/2112.04426
- **Notable for**: Matching GPT-3 at 25x fewer parameters via retrieval augmentation
- **Authors**: Borgeaud et al. (DeepMind)
- **Published**: December 2021 (ICML 2022)

## Architecture

- **Retrieval database**: 2 trillion multilingual tokens, indexed by BERT sentence embeddings
- **Chunk size**: 64 tokens per chunk, with both the chunk and its document continuation stored
- **Retrieval mechanism**: Approximate nearest neighbor search over BERT embeddings
- **Integration**: Chunked Cross-Attention (CCA) in every third decoder block from layer 9 onward
- **Standard blocks**: Self-attention + FFN (like normal transformer decoder)
- **RETRO blocks**: Self-attention + Chunked Cross-Attention + FFN

## Significance

RETRO's key insight is the separation of two types of knowledge:
1. **Language competence** (grammar, reasoning patterns): Stored in parameters — needs relatively few parameters
2. **Factual knowledge** (specific dates, names, facts): Stored in the retrieval database — essentially unlimited capacity

This principle is foundational to modern [[concepts/memory-augmented-neural-networks]] and informs the design of all retrieval-augmented systems.

## Mentioned In

- [[sources/retro-illustrated-retrieval-transformer]] — Jay Alammar's illustrated guide
- [[concepts/memory-augmented-neural-networks]] — RETRO as modern MANN
- [[concepts/knowledge-storage-in-transformers]] — parametric vs non-parametric knowledge

## External References

- [arXiv Paper](https://arxiv.org/abs/2112.04426)
- [Jay Alammar's Illustrated Guide](https://jalammar.github.io/illustrated-retrieval-transformer/)
