---
title: "Source: The Illustrated Retrieval Transformer (RETRO)"
type: source-summary
source: "[[raw/retro-illustrated-retrieval-transformer]]"
related: ["[[entities/retro]]", "[[concepts/memory-augmented-neural-networks]]", "[[concepts/knowledge-storage-in-transformers]]", "[[concepts/cross-attention]]"]
tags: [RETRO, retrieval-augmented, memorization, DeepMind, transformer]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Jay Alammar's illustrated guide to DeepMind's RETRO: a 7.5B parameter model matching GPT-3 (185B) by decoupling memorization from reasoning via a 2-trillion-token retrieval database with chunked cross-attention."
---

## Key Points

- RETRO matches GPT-3 performance at 4% of the parameter count (7.5B vs 185B)
- Decouples two types of knowledge: language patterns (stored in parameters) and factual knowledge (stored in retrieval database)
- Retrieval database: 2 trillion multilingual tokens, indexed by BERT embeddings, with 64-token chunks
- Architecture interleaves standard decoder blocks with RETRO blocks containing chunked cross-attention (CCA)
- Every third decoder block from layer 9 onward is a RETRO block
- Key insight: smaller models + retrieval can match larger models without retrieval

## Detailed Summary

Jay Alammar's visual walkthrough of DeepMind's RETRO (Retrieval-Enhanced Transformer) illustrates how retrieval can substitute for raw parameter count. The fundamental insight is that language models encode two fundamentally different types of information: **language patterns** (grammar, syntax, style) and **factual knowledge** (specific dates, names, facts). RETRO externalizes the factual knowledge into a searchable database, allowing the model parameters to focus on language competence.

The retrieval database is a massive key-value store with 2 trillion tokens. Keys are BERT sentence embeddings; values are 64-token text chunks paired with their document continuations. At inference time, the input is chunked, embedded via BERT, and used for approximate nearest-neighbor search to retrieve the two closest database entries.

The model architecture modifies the standard transformer decoder by inserting RETRO blocks at every third position starting from layer 9. These blocks add a **chunked cross-attention** (CCA) layer between the standard self-attention and feed-forward layers. In CCA, queries come from the decoder's hidden states while keys and values come from the encoded retrieved neighbors, allowing the model to condition generation on retrieved facts.

This represents a paradigm for scaling language models: rather than making models larger to memorize more facts, combine smaller models with larger databases.

## Concepts Introduced or Discussed

- [[concepts/memory-augmented-neural-networks]] — RETRO as retrieval-augmented memory
- [[concepts/cross-attention]] — the mechanism connecting decoder to retrieved content
- [[concepts/knowledge-storage-in-transformers]] — decoupling parametric from non-parametric knowledge

## Metadata

- **Author**: Jay Alammar
- **Date Published**: 2022-01
- **Format**: illustrated article
- **URL**: https://jalammar.github.io/illustrated-retrieval-transformer/
