---
title: "Autoregressive Image Generation"
type: concept
sources: ["[[sources/autoregressive-vision-models-survey]]"]
related: ["[[concepts/diffusion-models]]", "[[concepts/visual-tokenization]]", "[[concepts/image-generation]]", "[[concepts/flow-matching]]"]
tags: [autoregressive, image-generation, visual-tokens, next-token-prediction]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Image generation via next-token prediction over visual tokens -- resurgent with LlamaGen and VAR (NeurIPS 2024 Best Paper) matching diffusion quality, and NextStep-1 (ICLR 2026 Oral, 14B) achieving state-of-the-art via continuous tokens with a flow matching head."
---

## Overview

Autoregressive image generation applies the same next-token prediction paradigm that powers LLMs to visual content. Images are first encoded into sequences of discrete or continuous tokens via [[concepts/visual-tokenization]], then an autoregressive transformer predicts tokens sequentially, conditioned on text or other inputs. The decoded token sequence is then transformed back into an image.

After being overshadowed by [[concepts/diffusion-models]] in 2022-2024, autoregressive approaches have re-emerged as serious competitors. LlamaGen (2024) demonstrated that "Autoregressive Model Beats Diffusion" on standard benchmarks, Visual Autoregressive Modeling (VAR) won NeurIPS 2024 Best Paper, and NextStep-1 (ICLR 2026 Oral) achieved state-of-the-art for autoregressive text-to-image generation.

## Key Ideas

### Visual Tokenization Evolution

The quality of autoregressive image generation depends critically on the visual tokenizer:

| Era | Method | Approach |
|-----|--------|----------|
| 2017 | VQ-VAE | Discrete representation learning via vector quantization |
| 2019 | VQ-VAE-2 | Hierarchical quantization for improved diversity |
| 2021 | VQGAN | Transformers + adversarial training for sharper tokens |
| 2023 | MAGVIT-v2 | "Language Model Beats Diffusion -- Tokenizer is Key" |
| 2024 | FSQ | Finite Scalar Quantization -- simplified VQ-VAE design |
| 2025 | Continuous tokens | MAR, TokenFlow, NextStep-1 -- no quantization loss |
| 2025 | 1D latent | ResTok -- hierarchical residual in 1D space |

The major trend is moving from discrete to continuous tokens, preserving richer visual information that quantization would destroy.

### Scale-wise Prediction (VAR)

Visual Autoregressive Modeling (VAR) reconceives generation as hierarchical scale prediction rather than sequential token prediction. Instead of predicting tokens left-to-right, VAR predicts progressively finer image scales (coarse to fine). This matches human visual perception and won NeurIPS 2024 Best Paper. Variants include M-VAR, FlowAR (integrating [[concepts/flow-matching]]), and FlexVAR.

### NextStep-1: Continuous AR State of the Art

NextStep-1 (ICLR 2026 Oral) combines a 14B autoregressive model with a 157M [[concepts/flow-matching]] head. Instead of predicting discrete tokens, it predicts continuous image representations and uses a small flow matching decoder to generate final images. This hybrid approach achieves state-of-the-art for autoregressive text-to-image.

### Next-X Prediction

The xAR model extends next-token prediction to "next-X" prediction, where X can be larger units (cells, regions) rather than individual tokens. Cells as prediction entities outperform both tokens and whole images, suggesting the optimal prediction granularity is somewhere between.

### Unified Multimodal Models

A key advantage of autoregressive approaches: they naturally unify vision and language in a single architecture. Models like Chameleon, Liquid, and Wallaroo handle both text understanding and image generation with the same next-token prediction framework. This unification is much harder with [[concepts/diffusion-models]], which require fundamentally different architectures for text and images.

### Comparison with Diffusion

| Property | Autoregressive | Diffusion |
|----------|---------------|-----------|
| Generation paradigm | Sequential token prediction | Iterative denoising |
| Inference scaling | Superior (more tokens = better quality) | Fixed (more steps = better quality) |
| Unified multimodal | Natural | Requires separate architectures |
| Training | Standard cross-entropy | Specialized noise/velocity prediction |
| Current quality | Matching diffusion | Slightly ahead |
| Ecosystem maturity | Growing | Dominant |

## How It Connects

Autoregressive image generation bridges [[concepts/image-generation]] with the LLM paradigm that dominates text generation. It enables unified models that handle text understanding, image generation, and image editing in a single architecture -- a direction that [[concepts/diffusion-models]] cannot easily match. The [[concepts/visual-tokenization]] layer is analogous to [[concepts/byte-pair-encoding]] in text LLMs.

## Open Questions

- Will continuous tokens fully replace discrete tokens?
- Can autoregressive models match diffusion quality at the highest resolutions (4K+)?
- Will unified multimodal AR models subsume specialized diffusion models?
- What is the optimal prediction granularity (token, cell, scale)?

## Sources

- [[sources/autoregressive-vision-models-survey]] -- comprehensive TMLR 2025 survey
