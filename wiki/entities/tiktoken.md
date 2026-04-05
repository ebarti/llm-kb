---
title: "tiktoken"
type: entity
entity_type: tool
sources: ["[[sources/winder-token-count-practical-guide]]", "[[sources/github-faster-bpe-tokenizer]]", "[[sources/raschka-bpe-from-scratch]]"]
related: ["[[concepts/byte-pair-encoding]]", "[[concepts/tokenization]]", "[[concepts/token-counting]]"]
last_compiled: 2026-04-05
summary: "OpenAI's fast BPE tokenizer library, written in Rust with a Python API — the standard tool for counting tokens for GPT models."
---

## Overview

tiktoken is OpenAI's open-source tokenizer library, implemented in Rust with a thin Python wrapper. It provides fast [[concepts/byte-pair-encoding]] tokenization for all OpenAI models, with a minimal API focused on encode, decode, and count operations.

## Key Features

- **Speed**: 2-3x faster than HuggingFace Tokenizers for standard use (though [[sources/github-faster-bpe-tokenizer]] reports GitHub's tokenizer is 4x faster)
- **Minimal API**: encode, decode, count — no training capability
- **Model-specific encodings**: cl100k_base (GPT-4, GPT-3.5-turbo), p50k_base (Codex), r50k_base (GPT-3), o200k_base (newer models)
- **Rust core**: High performance without Python GIL limitations

## Limitations

- Cannot train new tokenizers — only uses pre-built vocabularies
- Only supports OpenAI model encodings (not general-purpose)
- Quadratic worst-case time complexity on pathological inputs (addressed by GitHub's alternative)

## Mentioned In

- [[sources/winder-token-count-practical-guide]] — primary tool for OpenAI token counting
- [[sources/github-faster-bpe-tokenizer]] — baseline that GitHub's tokenizer outperforms (4x on standard, massively on pathological inputs)
- [[sources/raschka-bpe-from-scratch]] — referenced as production-grade alternative to educational BPE implementations
