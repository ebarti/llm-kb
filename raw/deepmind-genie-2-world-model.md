---
title: "Genie 2: A Large-Scale Foundation World Model"
source: "https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/"
author: "Google DeepMind"
date_published: 2024-12-04
date_ingested: 2026-04-05
tags: [Genie, DeepMind, world-models, interactive-worlds, diffusion]
type: article
status: raw
discovered_via: search
---

# Genie 2: A Large-Scale Foundation World Model

## Core Architecture
- Diffusion-based world model using autoregressive latent diffusion
- Autoencoder processes video; latent frames passed to large transformer dynamics model
- Trained with causal mask similar to LLMs
- Inference: autoregressive, taking actions and past latent frames frame-by-frame
- Classifier-free guidance for action controllability
- Distilled version for real-time play (with quality reduction)

## Key Capabilities
- Generates 3D environments from single image prompts (including Imagen 3 or real-world photos)
- Consistent worlds for up to one minute (most demos 10-20s)
- Physics: gravity, water effects, smoke, lighting, reflections, bloom
- Object affordances: door opening, balloon bursting, explosive interactions
- Multiple camera perspectives: first-person, isometric, third-person
- Long-horizon memory: renders off-screen content accurately when revisited
- Counterfactual trajectories from identical starting frames
- NPC behavior and multi-agent interaction
- Out-of-distribution generalization: concept art to interactive worlds

## Genie 1 vs Genie 2
- Genie 1: 2D world generation
- Genie 2: Full 3D world generation — fundamental expansion

## Genie 3 (August 2025)
- 24fps real-time, 720p
- Several-minute consistency
- "First real-time interactive general-purpose world model" (Shlomi Fruchter)

## Applications
- SIMA agent tested in Genie 2 environments following natural-language instructions
- "Unlimited diverse training environments" for embodied AI agents
- Rapid prototyping for concept artists and designers

## Current Status
- Project Genie available to Google AI Ultra subscribers (U.S.)
- Genie 2: Limited research preview
