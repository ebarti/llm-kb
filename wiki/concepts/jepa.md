---
title: "JEPA (Joint Embedding Predictive Architecture)"
type: concept
sources: ["[[sources/jepa-deep-dive]]", "[[sources/meta-v-jepa-2]]", "[[sources/world-models-race-2026]]"]
related: ["[[concepts/world-models]]", "[[concepts/self-supervised-learning]]", "[[entities/yann-lecun]]", "[[entities/ami-labs]]", "[[concepts/latent-world-models]]", "[[concepts/embodied-ai]]"]
tags: [JEPA, self-supervised-learning, energy-based-models, world-models, representation-learning]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Yann LeCun's Joint Embedding Predictive Architecture: predicts representations rather than pixels using energy-based models, avoiding both generative intractability and contrastive dimensionality curse — the foundation for I-JEPA, V-JEPA, V-JEPA 2, H-JEPA, and LeWorldModel."
---

## Overview

JEPA (Joint Embedding Predictive Architecture) is [[entities/yann-lecun]]'s proposed foundation for next-generation AI systems — a [[concepts/self-supervised-learning]] framework that predicts latent representations rather than raw data. First outlined in LeCun's 2022 position paper "A Path Towards Autonomous Machine Intelligence," JEPA represents a fundamental departure from both autoregressive language models (which predict tokens) and generative image/video models (which predict pixels).

The core insight: "predicting exactly what will happen is intractable" but understanding "what is possible and what is not" remains feasible. By operating in representation space rather than pixel space, JEPA sidesteps the intractability that plagues generative approaches while learning physically meaningful world structure.

## Key Ideas

### Mathematical Foundation

JEPA is formalized as an energy-based model (EBM):

- **Energy function**: E_w(x, y, z) where z are latent variables
- **Inference**: F_w(x,y) = min_{z} E_w(x,y,z)
- Low energy = compatible (x,y) pairs; high energy = incompatible

Four training criteria (crucially, without contrastive loss):
1. Maximize information in current-state representation: -I(s_x)
2. Maximize information in future-state representation: -I(s_y)
3. Minimize prediction error between representations: D(s_y, predicted_y)
4. Regularize latent variable capacity: R(z)

### The Collapse Problem and Its Solution

The central technical challenge is representational collapse — encoders that output constant values, achieving zero prediction error without learning anything meaningful. JEPA avoids contrastive methods (which need exponentially many negative samples) in favor of regularization:

- **I-JEPA/V-JEPA**: Exponential Moving Average (EMA) target encoder (like BYOL)
- **LeWorldModel**: Isotropic Gaussian Regularization (15M params, first end-to-end from raw pixels)

### The JEPA Family

| Variant | Domain | Architecture | Key Innovation |
|---------|--------|-------------|----------------|
| I-JEPA | Images | ViT + masked patches | Predict masked region representations |
| V-JEPA | Video | ViT + spatiotemporal patches | Dual short/long-range masks |
| V-JEPA 2 | Video + robotics | ViT-g/16 (1.2B params) | Action-conditioned training, zero-shot robot planning |
| H-JEPA | Hierarchical | Two-tier JEPA | Short-term detail + long-horizon abstraction |
| MC-JEPA | Motion + content | PWC-Net + multitask | Optical flow + SSL fusion |
| VL-JEPA | Vision-language | Cross-modal | Joint vision-language embeddings |
| LeWorldModel | Raw pixels | End-to-end JEPA | Isotropic Gaussian regularization, 15M params |

### Key Distinction from Other Approaches

- **Generative models** (GPT, diffusion): predict the actual output y from input x — intractable for complex physical futures
- **Contrastive learning** (CLIP, SimCLR): push apart negative pairs — requires exponentially many negatives at scale
- **JEPA**: learns encoders g_x, g_y producing representations s_x, s_y — prediction happens in compact, abstract space

### V-JEPA 2: The State of the Art

The most complete JEPA realization (June 2025):
- 1.2B params, trained on 22M videos (1M+ hours) + 1M images
- Progressive-resolution training (16 frames → 64 frames)
- SOTA on action anticipation (Epic-Kitchens-100: 39.7 recall-at-5)
- Zero-shot robot planning with only 62 hours of robot data
- 65-80% success on novel pick-and-place operations

## How It Connects

JEPA is the architectural philosophy underlying [[entities/ami-labs]] (LeCun's $1B startup). It connects to [[concepts/world-models]] as the prediction mechanism — learning how the world will change without generating explicit images of that change. It extends [[concepts/self-supervised-learning]] from static data to temporal dynamics, enabling [[concepts/embodied-ai]] applications. The V-JEPA 2 line demonstrates that JEPA-based [[concepts/latent-world-models]] can transfer from internet video to real-world robotics.

## Open Questions

- Can JEPA scale to match LLM-level general capabilities, or is it limited to perceptual domains?
- How does H-JEPA compare to planning approaches like MuZero's learned dynamics?
- Is the representation space sufficient for complex multi-step reasoning, or does it need integration with language models?
- Will LeWorldModel's Isotropic Gaussian approach supersede EMA-based collapse prevention?

## Sources

- [[sources/jepa-deep-dive]] — comprehensive technical walkthrough of the full JEPA family
- [[sources/meta-v-jepa-2]] — V-JEPA 2 with robotic planning results
- [[sources/world-models-race-2026]] — AMI Labs and JEPA in the competitive landscape
