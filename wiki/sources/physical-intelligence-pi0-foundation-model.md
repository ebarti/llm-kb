---
title: "Source: π0 Vision-Language-Action Flow Model (Physical Intelligence)"
type: source-summary
source: "[[raw/physical-intelligence-pi0-foundation-model]]"
related: ["[[concepts/vision-language-action-models]]", "[[concepts/foundation-models-for-robotics]]", "[[concepts/dexterous-manipulation]]", "[[concepts/flow-matching]]", "[[entities/physical-intelligence]]", "[[entities/pi0]]"]
tags: [pi0, physical-intelligence, vla, flow-matching, robotics]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Physical Intelligence's π0 is a 3B-parameter VLA model using flow matching for 50Hz continuous robot control; trained on 8 robots and 68 tasks; achieves near-perfect scores on dexterous tasks (laundry folding, box assembly) where prior models score zero; open-sourced via Hugging Face."
---

## Key Points

- π0 is a 3B parameter [[concepts/vision-language-action-models]] built on PaliGemma, using [[concepts/flow-matching]] for continuous action generation at 50Hz
- Trained on 7-8 robotic platforms across 68 unique tasks -- true [[concepts/cross-embodiment-transfer]]
- Dramatically outperforms prior models: scores 0.971 on table bussing and 1.0 on shirt folding where OpenVLA and Octo score 0
- π0-FAST autoregressive variant trains 5x faster using DCT-based action tokenization (FAST)
- Open-sourced via Hugging Face LeRobot; 1-20 hours of data sufficient for task fine-tuning
- Demonstrated unprecedented [[concepts/dexterous-manipulation]]: laundry folding, box assembly, grocery bagging

## Detailed Summary

π0 (pi-zero) from [[entities/physical-intelligence]] is a general-purpose robot [[concepts/foundation-models-for-robotics]] that, like LLMs provide a foundation for language, provides a foundation for physical intelligence. The company raised over $400M to develop it.

The architecture builds on Google's PaliGemma (3B VLM) and extends it with [[concepts/flow-matching]], a variant of diffusion models that produces smooth, real-time action trajectories. Unlike standard policies that output discrete actions, π0 generates continuous motor commands at 50Hz, enabling the precise, fluid movements required for [[concepts/dexterous-manipulation]].

The attention mechanism is carefully designed: prefix tokens (images + text) fully attend to each other; state tokens (joint angles, sensors) attend causally; action tokens have full visibility to all non-padding tokens. This custom block-sparse attention pattern is implemented efficiently via PyTorch FlexAttention.

Training uses three data sources: Open X-Embodiment (community dataset), internet-scale VLM pre-training, and Physical Intelligence's own multi-robot dataset from 8 distinct robots (UR5e, Franka, bimanual, mobile platforms). A multi-stage pipeline mirrors LLM training: broad pre-training followed by task-specific post-training with just 1-20 hours of demonstration data.

Performance results are striking. On five benchmark tasks, π0 achieves near-perfect scores where prior models (OpenVLA, Octo) fail entirely -- 0.971 on easy table bussing, 1.0 on shirt folding, 0.786 on grocery bagging. The model shows emergent behaviors like stacking dishes and pre-cleaning plates during bussing tasks.

The π0-FAST variant replaces flow matching with autoregressive generation using FAST (Frequency-space Action Sequence Tokenization): raw actions are quantile-normalized, transformed via DCT, pruned, and encoded with BPE. This achieves 5x faster training with better generalization and lossless reconstruction.

## Concepts Introduced or Discussed

- [[concepts/vision-language-action-models]] -- the VLA architecture
- [[concepts/flow-matching]] -- continuous action generation via denoising flows
- [[concepts/foundation-models-for-robotics]] -- general-purpose robot models
- [[concepts/cross-embodiment-transfer]] -- one model for many robot types
- [[concepts/dexterous-manipulation]] -- complex physical tasks

## Quotes & Evidence

> π0 demonstrates "unprecedented dexterity and physical capability" compared to prior robot learning approaches.

> Performance comparison: π0 scores 0.971 on table bussing where OpenVLA scores 0 and Octo scores 0.043.

## Metadata

- **Author**: Physical Intelligence
- **Date Published**: 2024-10-31
- **Format**: article (research blog + paper)
- **URL**: https://www.pi.website/blog/pi0
