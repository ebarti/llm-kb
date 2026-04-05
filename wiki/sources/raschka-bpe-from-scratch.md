---
title: "Source: Implementing BPE Tokenizer From Scratch"
type: source-summary
source: "[[raw/raschka-bpe-from-scratch]]"
related: ["[[concepts/byte-pair-encoding]]", "[[concepts/tokenization]]", "[[concepts/subword-tokenization]]", "[[entities/sebastian-raschka]]"]
last_compiled: 2026-04-05
summary: "Sebastian Raschka's hands-on tutorial building a BPE tokenizer from scratch, covering the three-step algorithm (find pairs, merge, repeat), encoding/decoding, and GPT-2 compatibility."
---

## Key Points

- BPE converts text into integer token representations by iteratively merging the most frequent byte/character pairs
- The algorithm starts with 256 ASCII bytes as the base vocabulary and adds new merged tokens starting from ID 256
- A 17-character phrase like "This is some text" compresses from 17 character-level tokens to just 4 BPE tokens (GPT-2)
- The `BPETokenizerSimple` class implements training, encoding, decoding, and persistence
- GPT-2 uses "Ġ" notation for whitespace handling during encoding
- The algorithm originated from Philip Gage's 1994 compression paper

## Detailed Summary

Raschka walks through a complete BPE implementation in Python. The core algorithm has three steps repeated until the desired vocabulary size is reached: (1) scan text for the most frequent adjacent byte/character pair, (2) replace all occurrences of that pair with a new token ID and record the merge in a lookup table, (3) continue until saturation. The encoding process splits input text into words, applies whitespace handling, then iteratively merges adjacent tokens matching learned pairs prioritized by merge rank. Modern implementations like [[entities/tiktoken]] offer superior performance, but this educational version prioritizes clarity.

## Notable Quotes

> "A 17-character phrase requires 17 tokens using character-level encoding, but only 4 tokens with GPT-2's BPE approach."

## Related Concepts

- [[concepts/byte-pair-encoding]] — core algorithm explained step by step
- [[concepts/tokenization]] — broader context of text-to-token conversion
- [[concepts/subword-tokenization]] — BPE as one of the three main subword methods
- [[concepts/vocabulary-size-tradeoffs]] — vocabulary size affects BPE merge count
