---
title: "EvaByte"
type: entity
entity_type: tool
sources: ["[[sources/evabyte-tokenization-free-model]]"]
related: ["[[concepts/byte-level-models]]", "[[concepts/tokenization]]", "[[concepts/multilingual-tokenization]]"]
last_compiled: 2026-04-05
summary: "A 6.5B open-source tokenization-free byte-level language model from HKU/SambaNova that matches tokenizer-based models, using multibyte prediction and EVA linear attention."
---

## Overview

EvaByte is a 6.5 billion parameter language model developed collaboratively by the University of Hong Kong and SambaNova Systems. It is the first open-source [[concepts/byte-level-models|byte-level model]] to match the performance of modern tokenizer-based language models, demonstrating that efficient byte-level processing at scale is practically viable.

## Key Specifications

- **Parameters**: 6.5B
- **Training data**: 1.5 trillion bytes of text, math, and code
- **Vocabulary**: 320 tokens (256 byte values + 64 special tokens)
- **Architecture**: Transformer with EVA attention + multibyte prediction heads

## Key Innovations

### Multibyte Prediction
Eight prediction heads simultaneously predict multiple future bytes. At inference, combined via Medusa-like tree attention for self-speculative decoding — predicting several bytes per forward pass instead of one.

### EVA (Efficient Visual Attention)
Distributes computational state across multiple local memory slots with chunked key-value pairs and separate linearization per chunk. Achieves linear complexity while remaining compatible with optimized standard attention kernels.

### Performance
- 5-10x faster decoding vs. vanilla byte-level architectures
- Up to 2x faster than some token-based models on H800 GPU
- Outperforms similarly-sized models on coding benchmarks (HumanEval, MBPP)
- Beats Byte Latent Transformers with 3-4x fewer training bytes

### Multimodal Extension
Treats images as JPEG byte streams, enabling text-image interleaving without architectural changes. Demonstrates basic image captioning after fine-tuning on ~3M images.

## Availability

Open-source: model weights on HuggingFace (Phase1, base, SFT versions), code on GitHub.

## Mentioned In

- [[sources/evabyte-tokenization-free-model]] — detailed architecture and benchmark analysis
