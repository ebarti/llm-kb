---
title: "Source: Autoregressive Models in Vision Survey (TMLR 2025)"
type: source-summary
source: "[[raw/autoregressive-vision-models-survey]]"
related: ["[[concepts/autoregressive-image-generation]]", "[[concepts/visual-tokenization]]", "[[concepts/diffusion-models]]"]
tags: [autoregressive, image-generation, visual-tokens, survey]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "TMLR 2025 survey cataloging 200+ papers on autoregressive vision models: from VQ-VAE to continuous tokens, scale-wise VAR (NeurIPS 2024 Best Paper), and the convergence of AR models with diffusion -- showing AR approaches now match or beat diffusion on inference-time scaling."
---

## Key Points

- [[concepts/visual-tokenization]] evolved from VQ-VAE (2017) through VQGAN (2021) to continuous tokens (MAR, NextStep-1) and 1D latent representations (ResTok)
- Visual Autoregressive Modeling (VAR) predicts image scales hierarchically, winning NeurIPS 2024 Best Paper
- LlamaGen (2024) demonstrated "Autoregressive Model Beats Diffusion" on standard benchmarks
- NextStep-1 (ICLR 2026 Oral): 14B AR model with 157M [[concepts/flow-matching]] head, state-of-the-art for AR text-to-image
- [[concepts/autoregressive-image-generation]] now matches diffusion quality while offering superior inference-time scaling
- Two dominant paradigms emerging (late 2025): unified multimodal models and autoregressive diffusion-forcing for video
- Key trend: discrete tokens giving way to continuous tokens, preserving richer visual information

## Detailed Summary

This comprehensive TMLR 2025 survey documents the resurgence of [[concepts/autoregressive-image-generation]] as a serious competitor to [[concepts/diffusion-models]]. The field has evolved through multiple tokenization paradigms: VQ-VAE's discrete codes, VQGAN's adversarially-trained codebooks, and now continuous token representations that preserve richer visual information.

The most significant development is Visual Autoregressive Modeling (VAR), which reconceives image generation as predicting progressively finer scales rather than sequential tokens. This approach won NeurIPS 2024 Best Paper and spawned variants including FlowAR (integrating [[concepts/flow-matching]]) and FlexVAR (residual-free).

Leading models like LlamaGen demonstrated that autoregressive approaches can match diffusion models on standard benchmarks, while NextStep-1 (ICLR 2026 Oral) achieved state-of-the-art by combining a 14B autoregressive model with a small flow matching head for continuous token generation.

The xAR model introduced next-X prediction, where prediction units larger than individual tokens (cells) outperform both token-level and image-level prediction.

By late 2025, the field converged on two paradigms: unified multimodal models (Chameleon, Liquid, Lumina-Image 2.0) that handle both understanding and generation, and autoregressive diffusion-forcing for coherent video generation.

## Concepts Introduced or Discussed

- [[concepts/autoregressive-image-generation]] -- the survey's subject
- [[concepts/visual-tokenization]] -- VQ-VAE to continuous tokens
- [[concepts/diffusion-models]] -- the primary comparison baseline
- [[concepts/flow-matching]] -- used in hybrid AR approaches

## Metadata

- **Author**: Chaofan Tao et al.
- **Date Published**: 2025-01-15
- **Format**: paper (survey)
- **URL**: https://github.com/ChaofanTao/Autoregressive-Models-in-Vision-Survey
