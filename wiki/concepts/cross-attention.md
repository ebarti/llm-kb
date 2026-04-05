---
title: "Cross-Attention"
type: concept
sources: ["[[sources/raschka-self-attention-coding]]", "[[sources/illustrated-transformer-jalammar]]", "[[sources/retro-illustrated-retrieval-transformer]]", "[[sources/attention-mechanisms-comprehensive-survey]]"]
related: ["[[concepts/self-attention]]", "[[concepts/transformer-architecture]]", "[[concepts/multimodal-transformers]]", "[[concepts/attention-mechanisms]]", "[[concepts/memory-augmented-neural-networks]]", "[[entities/retro]]", "[[comparisons/self-attention-vs-cross-attention]]"]
last_compiled: 2026-04-05
summary: "Attention mechanism where queries come from one sequence and keys/values from another, enabling encoder-decoder models and multimodal fusion."
---

## Overview

Cross-attention (also called encoder-decoder attention) is the mechanism that connects two different sequences in a [[concepts/transformer-architecture]]. Unlike [[concepts/self-attention]] where queries, keys, and values all derive from the same sequence, cross-attention sources queries from one representation (typically the decoder) and keys/values from another (typically the encoder output).

## How It Works

Given decoder hidden states X_dec and encoder output X_enc:
- Q = X_dec W_q (queries from decoder)
- K = X_enc W_k (keys from encoder)
- V = X_enc W_v (values from encoder)
- Output = softmax(QK^T / sqrt(d_k)) V

This allows each decoder position to attend to all encoder positions, learning which parts of the input are most relevant for generating each output token.

## Applications

- **Original Transformer**: Decoder cross-attends to encoder for machine translation
- **[[concepts/multimodal-transformers]]**: Language decoder cross-attends to vision encoder output
- **Speech models**: Text decoder cross-attends to audio encoder features
- **Diffusion models**: Denoising network cross-attends to text encoder for conditional generation

## Decline in Pure Language Models

Modern language models have largely abandoned cross-attention in favor of decoder-only architectures with [[concepts/causal-attention]]. However, cross-attention remains essential for multimodal architectures where different modalities need to interact.

## Sources

- [[sources/raschka-self-attention-coding]] — implementation showing Q/K/V from different sources
- [[sources/illustrated-transformer-jalammar]] — encoder-decoder attention in the original Transformer

## Related Concepts

- [[concepts/self-attention]] — same-sequence attention
- [[concepts/multimodal-transformers]] — primary modern use case for cross-attention
- [[concepts/transformer-architecture]] — the architecture containing cross-attention
