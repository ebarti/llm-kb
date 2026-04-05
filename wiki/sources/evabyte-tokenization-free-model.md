---
title: "Source: EvaByte — Efficient Byte-Level Language Models at Scale"
type: source-summary
source: "[[raw/evabyte-tokenization-free-model]]"
related: ["[[concepts/byte-level-models]]", "[[concepts/tokenization]]", "[[entities/evabyte]]"]
last_compiled: 2026-04-05
summary: "EvaByte is a 6.5B tokenization-free byte-level LM matching token-based models, using multibyte prediction and EVA attention to achieve 2x faster inference with 320-token vocabulary."
---

## Key Points

- 6.5B parameter model processing raw UTF-8 bytes instead of tokens
- Trained on 1.5 trillion bytes; matches modern tokenizer-based models with less training data
- Vocabulary of just 320 tokens (256 byte values + 64 special tokens) vs. typical 32k-128k
- Multibyte prediction: 8 heads simultaneously predict multiple future bytes
- EVA attention: distributes state across local memory slots for linear complexity
- 5-10x faster decoding vs. vanilla byte-level architectures; up to 2x faster than token-based models
- Naturally extends to multimodal by treating images as JPEG byte streams
- Byte sequences are 3.8x longer than tokenized equivalents — the key challenge
- Outperforms Byte Latent Transformers (BLTs) with 3-4x fewer training bytes

## Detailed Summary

[[entities/evabyte]] represents the strongest evidence yet that [[concepts/byte-level-models]] can match tokenizer-based models at practical scale. The key innovations are multibyte prediction (8 heads predict future bytes simultaneously, enabling Medusa-like self-speculative decoding at inference) and EVA attention (splits key-value pairs into chunks with separate linearized attention, achieving linear complexity while remaining hardware-compatible). The model excels at coding tasks, possibly because byte-level processing eliminates domain-specific tokenizer biases. Training revealed stability challenges including "byte-level collapses" requiring careful hyperparameter tuning. The multimodal angle is provocative: treating images as JPEG byte streams enables unified text-image processing without architectural changes.

## Related Concepts

- [[concepts/byte-level-models]] — the paradigm EvaByte validates at scale
- [[concepts/tokenization]] — the process EvaByte eliminates
- [[concepts/vocabulary-size-tradeoffs]] — EvaByte's extreme: 320 vs. 100k+ tokens
- [[concepts/multilingual-tokenization]] — byte-level processing inherently eliminates multilingual tokenization issues
