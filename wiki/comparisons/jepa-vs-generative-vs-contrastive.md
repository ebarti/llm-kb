---
title: "JEPA vs Generative vs Contrastive Learning"
type: comparison
subjects: ["[[concepts/jepa]]", "[[concepts/self-supervised-learning]]"]
sources: ["[[sources/jepa-deep-dive]]", "[[sources/meta-v-jepa-2]]"]
related: ["[[concepts/world-models]]", "[[concepts/latent-world-models]]", "[[entities/yann-lecun]]"]
tags: [JEPA, generative, contrastive, self-supervised-learning, representation-learning]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Three self-supervised learning paradigms compared: generative models predict raw data (pixel/token), contrastive models push apart negative pairs (exponential scaling), JEPA predicts representations without generation or negatives — each with distinct tradeoffs for world modeling."
---

## Overview

Three major paradigms compete for training [[concepts/world-models]] through [[concepts/self-supervised-learning]]: generative models (predict raw outputs), contrastive learning (distinguish similar from dissimilar), and [[concepts/jepa]] (predict representations). The choice of paradigm determines what the model learns, how efficiently it scales, and what applications it supports.

## Comparison Matrix

| Dimension | Generative | Contrastive | JEPA |
|-----------|-----------|-------------|------|
| **Prediction target** | Raw data (pixels, tokens) | Similarity scores | Latent representations |
| **Training signal** | Reconstruction loss | Positive/negative pairs | Prediction in embedding space |
| **Collapse risk** | None (explicit target) | Moderate (need negatives) | High (requires regularization) |
| **Negative samples** | Not needed | Required (exponential scaling) | Not needed |
| **Capacity waste** | High (predicting irrelevant details) | Low | Low |
| **Physical understanding** | Implicit (from generation quality) | Surface-level (similarity) | Deep (meaningful representations) |
| **Scalability** | O(d) per sample | O(n*d) for negatives | O(d) per sample |
| **Key examples** | GPT, Sora, MAE | CLIP, SimCLR, MoCo | I-JEPA, V-JEPA, V-JEPA 2 |
| **Best for** | Generation tasks | Retrieval, zero-shot | Understanding, planning |

## Analysis

### Generative Models
Predict exact future data (next token, next frame, reconstructed image). Strengths: no collapse risk, capture fine detail. Weakness: waste enormous capacity predicting irrelevant pixel-level details that don't matter for understanding. Sora demonstrates the limits — impressive video generation but incomplete physical understanding.

### Contrastive Learning
Learn by comparing positive pairs (augmented views of same input) against negative pairs (different inputs). Strengths: strong representations, excellent for retrieval. Weakness: need exponentially many negative samples as dimensionality increases ("the curse of dimensionality for contrastive methods").

### JEPA
Predict representations rather than raw data, without negative samples. Strengths: efficient, avoids pixel-level waste, learns physically meaningful structure. Weakness: collapse prevention is technically challenging — requires EMA target encoders (I-JEPA/V-JEPA) or Isotropic Gaussian regularization (LeWorldModel).

## When to Use Each

- **Generative**: When you need to produce output (images, video, text) — not just understand
- **Contrastive**: When building retrieval systems or cross-modal search (CLIP-style)
- **JEPA**: When building [[concepts/world-models]] for understanding, prediction, and planning — especially for [[concepts/embodied-ai]] and robotics

## Sources

- [[sources/jepa-deep-dive]] — detailed technical comparison with mathematical foundations
- [[sources/meta-v-jepa-2]] — V-JEPA 2 as JEPA applied to world modeling
