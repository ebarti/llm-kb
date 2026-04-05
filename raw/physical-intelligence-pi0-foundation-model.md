---
title: "π0: A Vision-Language-Action Flow Model for General Robot Control"
source: "https://www.pi.website/blog/pi0"
author: "Physical Intelligence"
date_published: 2024-10-31
date_ingested: 2026-04-05
tags: [pi0, physical-intelligence, vla, foundation-models, robotics, flow-matching, dexterous-manipulation]
type: article
status: raw
discovered_via: search
---

# π0: Vision-Language-Action Flow Model — Physical Intelligence

π0 (pi-zero) is a general-purpose robot foundation model developed by Physical Intelligence. The company raised more than $400 million and subsequently open-sourced the model.

## Architecture

- 3 billion parameter VLM built on PaliGemma (Google's 3B parameter VLM)
- Uses flow matching (variant of diffusion models) to produce smooth, real-time action trajectories at 50Hz
- Augments pre-trained VLMs with continuous action outputs

## Training Data

Three sources:
1. Open X-Embodiment Dataset (open-source robot manipulation data)
2. Internet-scale pre-training (visual semantic knowledge)
3. π Dataset: Multi-robot dexterous tasks from 8 distinct robots (UR5e, Franka, bimanual, mobile)

Multi-stage training: pre-training on diverse tasks, post-training for downstream specialization. Between 1-20 hours of data sufficient to tune to new tasks.

## Performance Results

| Task | π0 | π0-small | OpenVLA | Octo |
|------|-----|----------|---------|------|
| Bussing Easy | 0.971 | 0.443 | 0 | 0.043 |
| Bussing Hard | 0.875 | 0.333 | 0 | 0 |
| Shirt Folding | 1.0 | 0.5 | 0 | 0 |
| Grocery Bagging | 0.786 | 0.271 | 0 | 0 |
| Toast from Toaster | 0.75 | 0 | 0 | 0 |

## π0-FAST Variant

- Autoregressive variant with FAST (Frequency-space Action Sequence Tokenization)
- 5x faster training than diffusion-based VLAs
- Uses DCT compression: raw actions → quantile normalization → DCT → coefficient pruning → BPE
- All operations invertible for lossless reconstruction

## Open Source

Released via Hugging Face LeRobot ecosystem. Checkpoints available for ALOHA, DROID platforms. Fine-tuning supported for custom tasks.

## Demonstrated Tasks

Laundry folding, table bussing, box assembly, grocery bagging, coffee preparation, egg placement, food packing. Shows emergent behaviors like stacking dishes and pre-cleaning plates.
