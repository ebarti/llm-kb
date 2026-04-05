---
title: "Deep Dive into Yann LeCun's JEPA Architecture"
source: "https://rohitbandaru.github.io/blog/JEPA-Deep-Dive/"
author: "Rohit Bandaru"
date_published: 2025-06-01
date_ingested: 2026-04-05
tags: [JEPA, I-JEPA, V-JEPA, H-JEPA, MC-JEPA, self-supervised-learning, energy-based-models]
type: article
status: raw
discovered_via: search
---

# Deep Dive into JEPA Architecture

## Core Concept
JEPA is an energy-based model predicting future representations rather than raw pixels. Energy = error in predicting future features from current features.

## Mathematical Foundation
- Energy-Based Model: E_w(x, y, z) with F_w(x,y) = min_{z ∈ Z} E_w(x,y,z)
- Four training criteria (without contrastive loss):
  1. Maximize information in current state: -I(s_x)
  2. Maximize information in future state: -I(s_y)
  3. Predict future from current: D(s_y, ỹ_y)
  4. Regularize latent variable capacity: R(z)

## Key Distinction from Generative Models
- Generative: directly predict y from x
- JEPA: learn encoders g_x and g_y producing representations s_x and s_y
- "Predicting exactly what will happen is intractable" but understanding "what is possible and what is not" is feasible
- Avoids curse of dimensionality affecting contrastive methods

## Hierarchical JEPA (H-JEPA)
- Two-tier: lower JEPA for short-term (detailed), upper for longer horizons (abstract)
- Enables hierarchical planning through sampling/search in reduced latent spaces

## I-JEPA (Image)
- Input split into N non-overlapping patches via target encoder f_θ
- M overlapping blocks as prediction targets
- Context block predicts target block representations
- Collapse prevention: EMA weights in target encoder (like BYOL, data2vec)

## V-JEPA (Video)
- 64 frames (~2.1s at 30fps) → 16×224×224×3
- Spatiotemporal patches (16×16×2)
- Two masks: short-range (discontinuous) and long-range
- L1 distance loss between predicted and ground-truth masked representations
- Limitation: predicts spatial gaps, not temporal progression

## V-JEPA 2 Advances
- ViT-H/16 (630M) → ViT-g/16 (1B params)
- Dataset: 2M → 22M videos (YT-Temporal-1B)
- Progressive-resolution training: 16 frames → 64 frames cooldown
- Post-training: attentive probing, LLM conditioning, action-conditioned training
- Robotics: teacher-forcing + rollout losses; Cross Entropy Method for planning

## MC-JEPA
- Combines optical flow (motion) + general SSL (content) via multitask learning
- Hierarchical PWC-Net architecture at multiple resolutions
- Potentially first H-JEPA instantiation

## Collapse Prevention
- Contrastive: increase energy on negatives (exponential scaling needed)
- Regularized: minimize low-energy region (JEPA's approach) — less affected by dimensionality
