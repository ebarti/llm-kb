---
title: "Autoregressive Models in Vision: A Survey (TMLR 2025)"
source: "https://github.com/ChaofanTao/Autoregressive-Models-in-Vision-Survey"
author: "Chaofan Tao et al."
date_published: 2025-01-15
date_ingested: 2026-04-05
tags: [autoregressive, image-generation, visual-tokens, vqgan, survey]
type: paper
status: raw
discovered_via: search
---

# Autoregressive Models in Vision Survey (TMLR 2025)

## Generation Categories
Image: unconditional, class-conditioned, text-to-image, image editing.
Video: unconditional/conditional, embodied AI.
3D/Multimodal: motion, point cloud, 3D medical, unified multimodal understanding and generation.

## Visual Tokenization Evolution
VQ-VAE (2017): discrete representation learning.
VQ-VAE-2 (2019): hierarchical quantization.
VQGAN (2021): transformers + adversarial training.
FSQ (Finite Scalar Quantization): simplified VQ-VAE.
MAGVIT-v2: "Language Model Beats Diffusion -- Tokenizer is Key."
Titok, OmniTokenizer: joint image-video tokenization.
Continuous approaches: MAR, TokenFlow, Lumina-mGPT.
1D latent space representations: ResTok (hierarchical residual).

## Scale-wise Autoregressive (VAR)
Visual Autoregressive Modeling: predicts image scales hierarchically rather than individual tokens. NeurIPS 2024 Best Paper. Variants: M-VAR (decoupled), FlowAR (+ flow matching), FlexVAR (residual-free).

## Leading Models
Image: LlamaGen ("AR Model Beats Diffusion," 2024), Infinity (bitwise scaling), OmniGen (unified, CVPR 2025).
Multimodal: Chameleon (unified understanding + generation), Liquid (scalable multi-modal), Lumina-Image 2.0.

## Continuous vs Discrete Tokens
NextStep-1 (ICLR 2026 Oral): 14B AR model + 157M flow matching head, continuous image tokens. State-of-the-art for AR text-to-image.
TokenBridge: bridges continuous/discrete via post-training quantization.

## Novel Prediction Strategies
xAR: next-X prediction (cells as entities outperform tokens or images).
ImageFolder: folded tokens for efficiency.

## Comparison with Diffusion
AR approaches now match or exceed diffusion quality while offering superior inference-time scaling. "Visual Autoregressive Models Beat Diffusion Models on Inference Time Scaling" (NeurIPS 2025). Two dominant paradigms (late 2025): unified multimodal models; autoregressive diffusion-forcing for video.
