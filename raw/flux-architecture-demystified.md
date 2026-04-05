---
title: "Demystifying Flux Architecture"
source: "https://arxiv.org/html/2507.09595v1"
author: "Or Greenberg"
date_published: 2025-07-12
date_ingested: 2026-04-05
tags: [flux, architecture, dit, mmdit, flow-matching, transformer]
type: paper
status: raw
discovered_via: search
---

# FLUX.1 Architecture: Technical Overview

## Core Architecture
Fully transformer-based architecture operating in latent space, replacing traditional U-Net designs. Processes text and image tokens through two distinct block types.

## Dual-Stream Transformer Blocks (19 blocks)
Maintain separate weights for text and image tokens. Apply different weights for text and latent embeddings while performing joint attention over concatenated tokens. Sequential processing: attention output feeds into feedforward layer. AdaLN modulation: each stream uses Adaptive Layer Normalization with dynamic scaling and shifting based on conditioning vectors. Mixed attention: concatenated Q/K matrices undergo rotation via Rotary Positional Embeddings (RoPE).

## Single-Stream Transformer Blocks
Follow the 19 double-stream blocks. Process concatenated text and image embeddings using shared weights. Parallel computation: attention and feedforward layers computed simultaneously from same input. Trade-off: efficiency and integration vs. domain specialization.

## Text Encoding Strategy
Dual text encoders: T5 encoder produces dense per-token embeddings for fine-grained semantic representation. CLIP encoder generates pooled embeddings for high-level semantic alignment. This enables superior prompt adherence vs. single-encoder models.

## Rotary Positional Embeddings (RoPE)
Rotates query and key vectors according to token positions. Preserves relative positional relationships. Supports extrapolation beyond training sequence lengths.

## Flow Matching Training
Employs rectified flow training: model predicts velocity vectors rather than noise (epsilon-objective). Minimizes difference between predicted velocity and actual vector pointing from noise x0 to data x1 along straight interpolation path. Enables faster, more stable image synthesis.

## Multimodal Attention
Both block types implement joint self-attention over concatenated modalities, enabling bidirectional text-image interactions.

## Comparison with SD3
SD3 pioneered the mm-DiT design used in FLUX's double-stream blocks. FLUX adds single-stream blocks for enhanced capacity in a lightweight manner.
