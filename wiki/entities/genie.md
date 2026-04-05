---
title: "Genie (DeepMind)"
type: entity
entity_type: tool
url: "https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/"
related: ["[[concepts/world-models]]", "[[concepts/embodied-ai]]", "[[entities/google-deepmind]]"]
tags: [Genie, DeepMind, world-models, interactive-worlds, foundation-model]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "DeepMind's foundation world model series: Genie 1 (2D worlds), Genie 2 (interactive 3D from single images, Dec 2024), Genie 3 (real-time 24fps 720p, Aug 2025) — generating interactive environments for embodied AI agent training."
---

## Overview

Genie is Google DeepMind's foundation world model series for generating interactive environments. Genie 1 generated 2D worlds; Genie 2 (December 2024) expanded to 3D with keyboard/mouse interaction; Genie 3 (August 2025) achieved real-time 24fps generation at 720p with multi-minute consistency — called "the first real-time interactive general-purpose world model."

## Key Facts

- **Type**: tool (AI model)
- **Developer**: Google DeepMind
- **Architecture**: Autoregressive latent diffusion with transformer dynamics model
- **Genie 2**: Interactive 3D from single image, consistent for ~1 minute
- **Genie 3**: 24fps, 720p, several-minute consistency (August 2025)
- **Status**: Project Genie available to Google AI Ultra subscribers (U.S.); research preview expanding

## Technical Architecture

- Video processed through autoencoder → latent frames
- Large transformer dynamics model with causal mask (LLM-like)
- Autoregressive frame generation: actions + past latent frames → next frame
- Classifier-free guidance for action controllability
- Distilled version for real-time play (quality tradeoff)

## Emergent Capabilities

- Self-learned physics: gravity, water, smoke, lighting, reflections
- Object affordances: door opening, balloon bursting, explosions
- Long-horizon memory: accurate off-screen object rendering
- Counterfactual trajectories from identical starting points
- NPC behavior and multi-agent interaction
- Out-of-distribution generalization: concept art → interactive worlds

## Applications

- SIMA agent tested following natural-language instructions in Genie environments
- Unlimited diverse training environments for [[concepts/embodied-ai]]
- Rapid prototyping for concept artists and designers

## Mentions

- [[sources/deepmind-genie-2]] — full technical details
- [[sources/world-models-race-2026]] — competitive positioning
