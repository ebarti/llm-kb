---
title: "Sora"
type: entity
entity_type: tool
url: "https://openai.com/sora"
related: ["[[concepts/video-generation-as-world-simulation]]", "[[concepts/world-models]]", "[[concepts/diffusion-models]]", "[[concepts/video-generation]]", "[[concepts/diffusion-transformer]]", "[[entities/veo]]", "[[entities/runway]]", "[[entities/kling]]"]
tags: [Sora, OpenAI, video-generation, world-simulation, diffusion-transformer]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "OpenAI's text-to-video model that pioneered the 'video generation as world simulation' thesis; Sora 2 (Sep 2025) improved physics and controllability; discontinued March 2026 after falling to #7 on Video Arena behind Runway and Google."
---

## Overview

Sora is OpenAI's text-to-video generation model, first unveiled in February 2024 with a technical report framing video generation as a path to building "general purpose simulators of the physical world." The model uses a diffusion transformer (DiT) architecture operating on spacetime patches — visual tokens extracted from videos at variable resolutions, durations, and aspect ratios.

## Key Facts

- **Type**: tool (AI model)
- **Developer**: OpenAI
- **Architecture**: Diffusion Transformer (DiT) on spacetime patches
- **Sora 2**: Released September 2025 with improved physics and controllability
- **Discontinued**: March 2026 (app shutdown April 2026, API shutdown September 2026)
- **Video Arena Ranking**: Fell to #7 by early 2026

## Technical Capabilities

- Variable resolution, duration, and aspect ratio generation
- Emergent 3D consistency and long-range coherence at scale
- Sora 2: Physics compliance (basketball rebounds correctly), multi-shot narrative consistency
- Could insert people into generated environments with accurate appearance and voice

## Significance

Sora pioneered the [[concepts/video-generation-as-world-simulation]] thesis, demonstrating that scaling video generation models produces emergent world understanding. However, its discontinuation in 2026 suggests OpenAI concluded that pure video generation is not the optimal path to [[concepts/world-models]], or that the commercial opportunity shifted.

## Economic Failure (2026)

Sora's shutdown is a cautionary tale for the generative AI industry:
- **Compute costs**: ~$15 million per day
- **Lifetime revenue**: $2.1 million total
- **Per-clip cost**: ~$1.30 (unsustainable at any consumer price point)
- **User decline**: Downloads fell 67% from November 2025 to February 2026; active users below 500,000
- **Partnership loss**: Disney withdrew a planned $1 billion partnership
- **Lesson**: Raw capability without sustainable unit economics is insufficient

The post-Sora market consolidated around [[entities/kling]] ($0.07/sec), [[entities/veo]] ($0.05-0.50/sec), and [[entities/runway]] (~$0.12/sec), all of which prioritized sustainable unit economics from the start.

## Mentions

- [[sources/openai-video-world-simulators]] — the original Sora technical report
- [[sources/world-models-race-2026]] — competitive landscape and decline
- [[sources/ai-video-market-2026]] — post-shutdown market analysis and economics
