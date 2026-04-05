---
title: "Implementing A Byte Pair Encoding (BPE) Tokenizer From Scratch"
source: "https://sebastianraschka.com/blog/2025/bpe-from-scratch.html"
author: "Sebastian Raschka"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [tokenization, bpe, implementation, tutorial]
type: article
status: raw
discovered_via: search
---

# Implementing A Byte Pair Encoding (BPE) Tokenizer From Scratch

## Core Concept

BPE converts text into integer token representations for language model training. Rather than encoding each character individually, it builds a vocabulary of frequently occurring subword units, dramatically reducing sequence length.

## The Algorithm: Three Core Steps

**1. Identify Frequent Pairs**
Scan text to find the most commonly occurring byte or character pair in each iteration.

**2. Replace and Record**
Replace that pair with a new placeholder ID (starting from 256, after the initial ASCII bytes) and document this mapping in a lookup table.

**3. Repeat Until Saturation**
Continue merging the highest-frequency pairs until reaching the desired vocabulary size or hitting diminishing returns.

## Why BPE Matters

The comparison is stark: a 17-character phrase "This is some text" requires 17 tokens using character-level encoding, but only 4 tokens with GPT-2's BPE approach. This efficiency becomes critical for processing longer documents.

## Implementation Architecture

The `BPETokenizerSimple` class provides:

- **Training**: Learns merge patterns from training text
- **Encoding**: Converts text to token IDs using learned merges
- **Decoding**: Reconstructs original text from token IDs
- **Persistence**: Save/load functionality for trained vocabularies
- **OpenAI Compatibility**: Load pretrained GPT-2 tokenizer files

## Practical Encoding Process

The encoding method splits input text into words, applies special whitespace handling using "Ġ" notation (a GPT-2 convention), then iteratively merges adjacent tokens matching learned pairs — prioritized by merge rank from lowest to highest.

## Historical Context

The algorithm originated from a 1994 compression paper by Philip Gage. Modern implementations like OpenAI's tiktoken offer superior performance, while educational implementations prioritize clarity over speed.
