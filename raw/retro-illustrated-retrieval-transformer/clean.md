---
title: "The Illustrated Retrieval Transformer (RETRO)"
source: "https://jalammar.github.io/illustrated-retrieval-transformer/"
author: "Jay Alammar"
date_published: 2022-01-15
date_ingested: 2026-04-05
tags: [RETRO, retrieval-augmented, transformer, memorization, DeepMind]
type: article
status: raw
discovered_via: search
---

# The Illustrated Retrieval Transformer (RETRO)

## Core Concept

RETRO is a smaller language model that achieves GPT-3-level performance by augmenting its parameters with database retrieval. It matches GPT-3 performance despite being only 4% of its size — 7.5 billion parameters versus GPT-3's 185 billion.

## Separating Knowledge Types

Language models must encode two different information types:
1. Language patterns (grammar, word usage)
2. Factual world knowledge (dates, names, specific facts)

By using retrieval, models avoid encoding all factual information in parameters, enabling smaller, faster-training models deployable on affordable hardware.

## The Retrieval Database

RETRO's database is a key-value store containing 2 trillion multilingual tokens:
- Keys: BERT sentence embeddings
- Values: Text chunks with two parts:
  - Neighbor chunk (used to compute the key)
  - Completion chunk (continuation of original document)
- Both chunks are maximum 64 tokens each

## Database Lookup Process

Input prompt flows through BERT, generating contextualized embeddings. These are averaged into a sentence embedding vector which performs approximate nearest neighbor search retrieving the two closest matches from the database.

## Architecture

RETRO uses an encoder-decoder structure:

**Encoder Stack**: Processes retrieved neighbors, generating KEY and VALUE matrices for attention mechanisms.

**Decoder Stack**: Interleaves two block types:
- Standard transformer decoder blocks (self-attention + feed-forward)
- RETRO decoder blocks (self-attention + chunked cross-attention + feed-forward)

## Chunked Cross-Attention (CCA)

Starting at layer 9, every third decoder block becomes a RETRO block. These blocks incorporate retrieved information through chunked cross-attention, allowing the model to reference specific facts needed for completion.

## Key Insight

Building larger and larger models is not the only way to improve performance. Architectural innovations combining retrieval with smaller models represent an important research direction, decoupling memorization from reasoning.
