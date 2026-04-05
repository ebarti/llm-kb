---
title: "SentencePiece"
type: concept
sources: ["[[sources/huggingface-tokenization-algorithms]]", "[[sources/ali-tokenizer-choice-negligible-crucial]]", "[[sources/winder-token-count-practical-guide]]"]
related: ["[[concepts/byte-pair-encoding]]", "[[concepts/unigram-tokenization]]", "[[concepts/subword-tokenization]]", "[[concepts/multilingual-tokenization]]"]
last_compiled: 2026-04-05
summary: "A language-agnostic tokenization library that applies BPE or Unigram directly on raw text streams — critical for languages like Chinese and Japanese that lack whitespace word boundaries."
---

## Overview

SentencePiece is a tokenization library (not an algorithm) developed by Taku Kudo and John Richardson (2018). It solves a fundamental limitation of standard BPE and WordPiece: those algorithms assume whitespace separates words, which fails for languages like Chinese, Japanese, Korean, and Thai that don't use spaces between words.

## Key Ideas

### Raw Text Processing

Standard BPE pre-tokenizes by splitting on whitespace, then applies merges within each word. SentencePiece skips this step entirely, treating the input as a **raw byte or character stream**. The space character itself becomes a regular token, represented as "▁" (U+2581, lower one-eighth block). This means "Hello world" becomes `["▁Hello", "▁world"]` — the leading space is part of the token.

### Algorithm Agnostic

SentencePiece is a library that can run **either BPE or Unigram** on the raw byte stream. It's the implementation, not the algorithm. The [[sources/ali-tokenizer-choice-negligible-crucial]] study found that even the choice of library (SentencePiece vs. HuggingFace Tokenizers) meaningfully affects downstream performance when running the same algorithm, suggesting implementation details matter.

### Multilingual Advantage

By treating all text as a byte stream without language-specific pre-tokenization rules, SentencePiece handles multilingual text more naturally. This makes it the preferred library for multilingual models and languages with complex morphology or no whitespace.

### Best Configuration

In the systematic study by Ali et al., BPE implemented in SentencePiece (BPE-SP) consistently outperformed BPE in HuggingFace Tokenizers at the same vocabulary sizes, for both monolingual English (BPE-SP-33k: 50.81%) and multilingual settings (BPE-SP-100k: 41.44%).

## Sources

- [[sources/huggingface-tokenization-algorithms]] — SentencePiece's role in handling non-whitespace languages
- [[sources/ali-tokenizer-choice-negligible-crucial]] — SentencePiece outperforms HuggingFace implementation
- [[sources/winder-token-count-practical-guide]] — practical usage for multilingual token counting

## Related Concepts

- [[concepts/byte-pair-encoding]] — one of two algorithms SentencePiece can run
- [[concepts/unigram-tokenization]] — the other algorithm SentencePiece supports
- [[concepts/multilingual-tokenization]] — SentencePiece's primary advantage
- [[concepts/subword-tokenization]] — the paradigm SentencePiece implements
