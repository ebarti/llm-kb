---
title: "Video Generation Models as World Simulators"
source: "https://openai.com/index/video-generation-models-as-world-simulators/"
author: "OpenAI"
date_published: 2024-02-15
date_ingested: 2026-04-05
tags: [Sora, video-generation, world-simulation, diffusion-transformers]
type: article
status: raw
discovered_via: search
---

# Video Generation Models as World Simulators (OpenAI Sora Technical Report)

## Core Architecture
Sora is a diffusion model trained on spacetime patches — visual patches extracted from videos and images at various resolutions, durations, and aspect ratios. Videos and images are compressed into a lower-dimensional latent space, then decomposed into spacetime patches that serve as transformer tokens.

## Key Design Choices
- Unified visual representation: spacetime patches enable training on diverse video/image data
- Variable duration, resolution, and aspect ratio training
- Diffusion transformer (DiT) architecture
- Language conditioning via DALL-E 3 recaptioning pipeline

## Emergent Capabilities at Scale
- 3D consistency: dynamic camera motion with people/scenes moving through 3D space
- Long-range coherence: consistent characters and visual style across frames
- World interaction: simulating simple actions that affect world state
- Digital world simulation: rendering video game environments (e.g., Minecraft)

## Limitations
- Does not accurately model physics in many basic interactions
- Object permanence failures
- Difficulty with exact spatial relationships
- Interactions between objects sometimes physically implausible

## Sora 2 (September 2025)
- Better physics compliance (basketball rebounds off backboard)
- "GPT-3.5 moment for video" — major controllability leap
- Can insert people into generated environments with accurate appearance/voice
- Multi-shot narrative following with consistent world state

## Sora Discontinuation (March 2026)
- OpenAI announced discontinuing Sora in both mobile app and API
- App shutdown: April 26, 2026; API shutdown: September 24, 2026
- Reflects broader strategic shift in video model landscape
