---
title: "Visual Tokenization"
type: concept
sources: ["[[sources/autoregressive-vision-models-survey]]"]
related: ["[[concepts/autoregressive-image-generation]]", "[[concepts/byte-pair-encoding]]", "[[concepts/image-generation]]"]
tags: [visual-tokens, vq-vae, vqgan, tokenization, image-generation]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Methods for converting images into discrete or continuous token sequences for autoregressive generation -- evolving from VQ-VAE (2017) through VQGAN (2021) to continuous tokens (2025), with MAGVIT-v2 showing 'the tokenizer is the key' to matching diffusion quality."
---

## Overview

Visual tokenization converts images into sequences of tokens that can be processed by autoregressive transformers -- the visual equivalent of [[concepts/byte-pair-encoding]] for text. The quality of the tokenizer is the primary bottleneck for [[concepts/autoregressive-image-generation]], as MAGVIT-v2 demonstrated with its claim that "Language Model Beats Diffusion -- Tokenizer is Key."

## Key Ideas

### Discrete Tokenization

**VQ-VAE (2017)**: Introduced vector quantization for discrete image representation. An encoder maps image patches to the nearest vector in a learned codebook, producing a sequence of discrete indices. A decoder reconstructs the image from these codes.

**VQ-VAE-2 (2019)**: Added hierarchical quantization with multiple codebook levels for improved diversity and quality.

**VQGAN (2021)**: Combined the VQ-VAE framework with adversarial training (a GAN discriminator) and transformer-based generation. Produced much sharper reconstructions and became the standard tokenizer for autoregressive image generation.

**FSQ (Finite Scalar Quantization)**: Simplified the VQ-VAE design by quantizing each dimension independently, avoiding codebook collapse issues.

**MAGVIT-v2**: Achieved quality sufficient for autoregressive models to match [[concepts/diffusion-models]], demonstrating the critical role of the tokenizer.

### Continuous Tokenization

The major 2025 trend is moving from discrete to continuous tokens:

- **MAR (Masked Autoregressive)**: Uses continuous latent representations
- **TokenFlow**: Bridges VQ tokens with continuous representations
- **NextStep-1**: 14B AR model working directly with continuous image tokens and a [[concepts/flow-matching]] head
- **ResTok**: Hierarchical residual tokenizer producing 1D latent sequences

Continuous tokens avoid the information loss inherent in vector quantization, preserving richer visual detail. This is analogous to the difference between character-level (discrete) and embedding-level (continuous) representations in language models.

### Joint Image-Video Tokenization

Newer tokenizers like Titok and OmniTokenizer handle both images and video frames, enabling unified generation systems.

### Evaluation Tradeoffs

Tokenizers face a reconstruction-generation tradeoff: tokens optimized for faithful reconstruction may not be optimal for autoregressive generation, and vice versa. Recent work (RandAR, Randomized AR) addresses this by training tokenizers that balance both objectives.

## How It Connects

Visual tokenization is the bridge between [[concepts/image-generation]] and language modeling techniques. It enables [[concepts/autoregressive-image-generation]] by converting the continuous pixel domain into sequences processable by transformers. The quality of the tokenizer determines the ceiling for generation quality, making it as fundamental to visual generation as [[concepts/byte-pair-encoding]] is to text generation.

## Sources

- [[sources/autoregressive-vision-models-survey]] -- comprehensive tokenization evolution
