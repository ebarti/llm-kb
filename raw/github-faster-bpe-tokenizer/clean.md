---
title: "So Many Tokens, So Little Time: Introducing a Faster, More Flexible Byte-Pair Tokenizer"
source: "https://github.blog/ai-and-ml/llms/so-many-tokens-so-little-time-introducing-a-faster-more-flexible-byte-pair-tokenizer/"
author: "GitHub Engineering"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [tokenization, bpe, performance, rust, tiktoken, github-copilot]
type: article
status: clean
discovered_via: search
---

# So Many Tokens, So Little Time: A Faster BPE Tokenizer

## Overview

GitHub released an open-source BPE tokenizer that dramatically improves upon existing implementations. Addresses critical scaling challenges for systems processing billions of code embeddings and supporting features like GitHub Copilot's retrieval-augmented generation.

## The Problem: Why Speed Matters

Traditional BPE tokenizers operate on complete input texts, forcing entire reprocessing when inputs change. This creates substantial inefficiencies for dynamic use cases where token budgets must be tracked during text construction.

Real-world demands at GitHub include:
- Splitting code files into token-bounded chunks for embedding
- Dynamically tracking token contributions while building prompts
- Processing untrusted code without pathological performance degradation

## The Algorithmic Innovation

The breakthrough relies on a principle called **compatibility**: appending tokens to a valid encoding produces another valid encoding if the final token pair remains valid under BPE rules.

Rather than repeatedly scanning entire texts (quadratic complexity) or maintaining heaps of token pairs (O(n log n)), GitHub's approach builds encodings left-to-right incrementally. The algorithm uses an Aho-Corasick automaton for string matching and constant-time pair retokenization, achieving **linear time complexity**.

## Performance

**Benchmarks (o200k_base model):**
- 4x faster than tiktoken
- 10x faster than Huggingface tokenizers

**Worst-case pathological inputs:** Linear degradation versus tiktoken's quadratic — essential for production stability when processing untrusted source code.

## Implementation

Rust crate providing three specialized encoders:
1. **Incremental encoders** — constant-time token counting and rollback snapshots
2. **Full-text encoder** — backtracking for standard encoding needs
3. **Interval encoder** — O(1) token counting on text subranges after O(n) preprocessing

## Availability

MIT-licensed at GitHub's Rust-gems repository, published on crates.io as `bpe` and `bpe-openai`, supporting recent OpenAI token models.
