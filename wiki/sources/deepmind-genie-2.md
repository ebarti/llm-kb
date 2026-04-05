---
title: "Source: Genie 2 — A Large-Scale Foundation World Model"
type: source-summary
source: "[[raw/deepmind-genie-2-world-model]]"
related: ["[[concepts/world-models]]", "[[entities/genie]]", "[[entities/google-deepmind]]", "[[concepts/embodied-ai]]"]
tags: [Genie, DeepMind, world-models, interactive-worlds, diffusion, foundation-model]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "DeepMind's Genie 2: diffusion-based autoregressive world model generating interactive 3D environments from single images; supports keyboard/mouse control, long-horizon memory, counterfactual trajectories, and NPC behavior modeling."
---

## Key Points

- Autoregressive latent diffusion model with transformer dynamics and causal masking
- Generates interactive 3D worlds from a single image prompt (including Imagen 3 or real-world photos)
- Consistent worlds for up to one minute; keyboard/mouse interaction in real-time (distilled version)
- Emergent capabilities: gravity, water, smoke, lighting, object affordances, NPC behavior
- Long-horizon memory: off-screen objects rendered accurately when revisited
- Out-of-distribution generalization: concept art and drawings become interactive environments
- Genie 3 (August 2025) achieved 24fps real-time at 720p with multi-minute consistency

## Detailed Summary

Genie 2 represents DeepMind's vision for [[concepts/world-models]] as interactive environments for training [[concepts/embodied-ai]] agents. The architecture processes video through an autoencoder, passes latent frames to a large transformer dynamics model trained with causal masking (similar to LLMs), and generates new frames autoregressively based on actions and past latent frames.

The system demonstrates remarkable emergent physics — not hard-coded but learned from data. Objects obey gravity, water flows realistically, smoke disperses naturally, and lighting/reflections behave consistently. Object affordances emerge naturally: doors can be opened, balloons burst, and explosions interact with environments.

A particularly notable capability is long-horizon memory: when an agent moves away from objects and later returns, the model renders previously off-screen content accurately. The model also generates counterfactual trajectories — given identical starting frames, different action sequences produce different but consistent futures.

DeepMind's SIMA agent was tested in Genie 2 environments, following natural-language instructions like "Open the blue door" and "Go behind the house," demonstrating the potential for generating unlimited diverse training environments. Genie 3 (August 2025) expanded to real-time 24fps at 720p with multi-minute consistency, called "the first real-time interactive general-purpose world model."

## Concepts Introduced or Discussed

- [[concepts/world-models]] — AI systems that simulate interactive environments
- [[concepts/embodied-ai]] — agents learning through world interaction
- [[concepts/latent-world-models]] — operating in compressed representation space
- [[concepts/physical-ai]] — understanding physical dynamics

## Metadata

- **Author**: Google DeepMind
- **Date Published**: 2024-12-04
- **Format**: research blog
- **URL**: https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/
