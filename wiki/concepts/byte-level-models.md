---
title: "Byte-Level Models (Tokenization-Free)"
type: concept
sources: ["[[sources/evabyte-tokenization-free-model]]", "[[sources/kamali-tokenization-killing-multilingual]]", "[[sources/karpathy-minbpe-lecture]]"]
related: ["[[concepts/tokenization]]", "[[concepts/multilingual-tokenization]]", "[[concepts/vocabulary-size-tradeoffs]]", "[[concepts/subword-tokenization]]", "[[entities/evabyte]]"]
last_compiled: 2026-04-05
summary: "Language models that process raw UTF-8 bytes instead of subword tokens, eliminating tokenization entirely — exemplified by EvaByte (6.5B) and Byte Latent Transformer, now matching tokenized models at scale."
---

## Overview

Byte-level language models (BLMs) represent a fundamental rethinking of the [[concepts/tokenization]] pipeline. Instead of converting text to subword tokens via [[concepts/byte-pair-encoding]] or similar algorithms, they process raw UTF-8 bytes directly. This eliminates the tokenizer entirely, along with all its associated problems: vocabulary limitations, [[concepts/multilingual-tokenization]] inequality, morphological incoherence, and inconsistent handling of numbers, whitespace, and special characters.

[[entities/andrej-karpathy]] has argued that someone should ideally find a way to delete tokenization entirely. Byte-level models are the primary research direction pursuing this goal.

## Key Ideas

### How They Work

Byte-level models use a vocabulary of just 256 byte values (plus a few special tokens). Every possible text is automatically in-vocabulary. The model sees the raw byte stream of UTF-8 encoded text and learns to predict the next byte(s).

The fundamental challenge: byte sequences are **3.8x longer** than tokenized equivalents on average. A text that takes 1,000 BPE tokens requires ~3,800 bytes, making standard transformer attention (quadratic in sequence length) prohibitively expensive.

### Key Models

**[[entities/evabyte]]** (2025): 6.5B parameters, trained on 1.5T bytes. The first open-source byte-level model matching modern tokenizer-based LMs. Uses 320 tokens (256 bytes + 64 special). Key innovations:
- **Multibyte prediction**: 8 heads predict multiple future bytes simultaneously, enabling self-speculative decoding
- **EVA attention**: Linear-complexity attention via chunked key-value pairs with separate linearization
- Achieves 5-10x faster decoding vs. vanilla byte architectures; up to 2x faster than some token-based models

**Byte Latent Transformer (BLT)** (Meta, 2025): Groups bytes into variable-length patches, processing patch-level representations with a global transformer. Matches Llama 3 at scale but requires patchification as an intermediate step.

**ByT5** (Google, 2022): Earlier byte-level model that demonstrated the concept but at significant efficiency cost.

### Advantages

- **No OOV problem**: Every possible byte sequence is valid input
- **Script-agnostic**: All writing systems encoded equally — no [[concepts/multilingual-tokenization]] penalty
- **Noise-robust**: Typos, spacing changes, diacritics don't cause catastrophic tokenization failures
- **Consistent number handling**: No arbitrary splits like "677" → " 6"+"77"
- **Multimodal potential**: [[entities/evabyte]] treats images as JPEG byte streams, enabling seamless text-image interleaving without architectural changes
- **Eliminates prompt boundary problem**: Token-based models produce different tokenizations depending on context boundaries; byte-level processing eliminates this

### Challenges

- **Sequence length**: 3.8x longer sequences require novel attention mechanisms (EVA, linear attention, patchification)
- **Training stability**: EvaByte experienced "byte-level collapses" with unusual character substitutions, requiring careful hyperparameter tuning
- **Training cost**: More bytes to process per unit of semantic content (though EvaByte matches token models with less data)
- **Inference latency**: Even with multibyte prediction, generating one byte at a time is fundamentally slower per semantic unit than generating one token

### Current State of the Art

As of 2025, byte-level models have crossed the threshold from research curiosity to practical viability. [[entities/evabyte]] matches modern tokenizer-based models on standard benchmarks and even outperforms on coding tasks. The gap is closing rapidly, and byte-level approaches may become standard within a few years, especially for multilingual and multimodal applications.

## Sources

- [[sources/evabyte-tokenization-free-model]] — the strongest evidence for practical byte-level models
- [[sources/kamali-tokenization-killing-multilingual]] — byte-level as solution to multilingual inequality
- [[sources/karpathy-minbpe-lecture]] — the argument for eliminating tokenization

## Related Concepts

- [[concepts/tokenization]] — the process byte-level models eliminate
- [[concepts/multilingual-tokenization]] — the problem byte-level models solve most cleanly
- [[concepts/vocabulary-size-tradeoffs]] — byte-level is the extreme: 256 tokens, no tradeoff
- [[concepts/subword-tokenization]] — the paradigm byte-level models replace
