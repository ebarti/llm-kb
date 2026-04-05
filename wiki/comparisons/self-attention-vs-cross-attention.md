---
title: "Self-Attention vs Cross-Attention"
type: comparison
subjects: ["[[concepts/self-attention]]", "[[concepts/cross-attention]]"]
sources: ["[[sources/attention-mechanisms-comprehensive-survey]]", "[[sources/retro-illustrated-retrieval-transformer]]"]
related: ["[[concepts/attention-mechanisms]]", "[[concepts/multi-head-attention]]", "[[concepts/transformer-architecture]]", "[[entities/retro]]"]
tags: [self-attention, cross-attention, encoder-decoder, comparison]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Self-attention captures within-sequence relationships (Q, K, V from same source) while cross-attention connects two sequences (Q from decoder, K/V from encoder) — self-attention dominates decoder-only LLMs, cross-attention remains essential for multimodal, retrieval-augmented, and encoder-decoder tasks."
---

## Overview

Self-attention and cross-attention are the two fundamental modes of the attention mechanism. They differ in the source of their queries, keys, and values, and consequently serve different purposes: self-attention models relationships within a single sequence, while cross-attention aligns and transfers information between two different sequences or modalities.

## Comparison Matrix

| Dimension | Self-Attention | Cross-Attention |
|-----------|---------------|-----------------|
| **Q source** | Same sequence | Different sequence (decoder) |
| **K, V source** | Same sequence | Different sequence (encoder) |
| **Purpose** | Intra-sequence relationships | Inter-sequence alignment |
| **Symmetry** | Symmetric (any position can attend to any) | Asymmetric (decoder queries encoder) |
| **Used in** | All transformer models | Encoder-decoder, multimodal, retrieval |
| **Causal variant** | [[concepts/causal-attention]] (masked) | Typically not masked |
| **Complexity** | O(N^2) where N = sequence length | O(N_q * N_kv) |
| **Dominant in LLMs?** | Yes (decoder-only models) | No (mostly multimodal/retrieval) |

## Analysis

### Self-Attention: Within a Sequence

Self-attention allows each position in a sequence to attend to all other positions, capturing:
- **Syntactic dependencies**: Subject-verb agreement across clauses
- **Semantic relationships**: Coreference resolution ("he" -> "John")
- **Long-range interactions**: Relating a question to an answer far away
- **Structural patterns**: Code syntax, document formatting

In decoder-only models (GPT, Llama, Claude), causal self-attention is the sole attention mechanism — there is no separate encoder, so all processing happens through self-attention with a causal mask preventing attention to future tokens.

### Cross-Attention: Between Sequences

Cross-attention connects two different representations, enabling:
- **Translation**: Source language encoder -> target language decoder
- **Multimodal fusion**: Vision encoder -> language decoder (GPT-4V, Claude vision)
- **Retrieval augmentation**: Retrieved document encoder -> generation decoder ([[entities/retro]])
- **Conditional generation**: Text encoder -> image decoder (Stable Diffusion, DALL-E)
- **Speech**: Audio encoder -> text decoder (Whisper)

In cross-attention, queries come from the representation being generated (decoder), while keys and values come from the conditioning input (encoder). This allows the decoder to "look up" relevant information in the encoder output.

### The Decline of Cross-Attention in Language Models

Modern language models have largely moved from encoder-decoder (T5, BART) to decoder-only architectures (GPT, Llama). This eliminates cross-attention from pure language modeling. However, cross-attention remains essential in:

1. **Multimodal models**: Vision encoders connect to language decoders via cross-attention
2. **Retrieval-augmented models**: [[entities/retro]] uses chunked cross-attention to integrate retrieved text
3. **Diffusion models**: Text conditioning in image generation relies on cross-attention
4. **Speech models**: Audio encoder to text decoder

### RETRO: Cross-Attention for Retrieval

[[entities/retro]] provides a compelling example of cross-attention's power. Every third decoder block from layer 9 onward includes a Chunked Cross-Attention (CCA) layer where:
- Queries: Decoder hidden states (what the model is generating)
- Keys/Values: Encoded retrieved text chunks (external factual knowledge)

This allows the model to condition generation on retrieved facts, effectively externalizing factual memory via cross-attention.

## When to Use Each

| Scenario | Recommended |
|----------|-------------|
| Autoregressive language modeling | Self-attention (causal) |
| Machine translation | Both (encoder: self; decoder: self + cross) |
| Multimodal understanding | Both (vision self-attention; cross-attention for fusion) |
| Retrieval augmentation | Both (self for generation; cross for integrating retrieved docs) |
| Image generation from text | Cross-attention (text conditions denoising) |
| Document understanding | Self-attention only (decoder-only models) |

## Sources

- [[sources/attention-mechanisms-comprehensive-survey]] — mathematical formulation of both types
- [[sources/retro-illustrated-retrieval-transformer]] — cross-attention for retrieval augmentation
