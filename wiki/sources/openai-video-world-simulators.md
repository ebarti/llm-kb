---
title: "Source: Video Generation Models as World Simulators (OpenAI)"
type: source-summary
source: "[[raw/openai-video-world-simulators]]"
related: ["[[concepts/world-models]]", "[[concepts/video-generation-as-world-simulation]]", "[[entities/sora]]", "[[concepts/diffusion-models]]"]
tags: [Sora, video-generation, world-simulation, OpenAI, diffusion-transformers]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "OpenAI's technical report on Sora as a world simulator: spacetime patch architecture, emergent 3D consistency and world interaction at scale, plus Sora 2's physics improvements and eventual March 2026 discontinuation."
---

## Key Points

- Sora uses diffusion transformers (DiT) operating on spacetime patches — visual patches from videos/images at various resolutions and durations
- At scale, Sora exhibits emergent 3D consistency, long-range coherence, and ability to simulate world interactions
- Sora 2 (September 2025) achieved major physics improvements — balls rebound correctly, multi-shot narrative consistency
- OpenAI described Sora 2 as the "GPT-3.5 moment for video"
- Despite pioneering the paradigm, OpenAI discontinued Sora in March 2026 (app: April 2026, API: September 2026)
- Sora fell to #7 on Video Arena by early 2026, behind Runway Gen-4.5 and Google Veo 3

## Detailed Summary

OpenAI's February 2024 technical report framed video generation as a path toward building general-purpose simulators of the physical world. The core innovation was treating videos as sequences of spacetime patches — visual tokens extracted at variable resolutions, durations, and aspect ratios. This unified representation enabled training on diverse video and image data simultaneously.

The system demonstrated emergent capabilities at scale: 3D consistency with dynamic camera motion, consistent characters across frames, and the ability to simulate actions affecting world state. However, significant limitations remained — physics errors in basic interactions, object permanence failures, and implausible spatial relationships.

Sora 2 (September 2025) addressed many physics issues and introduced the ability to insert real people into generated environments. However, by March 2026, OpenAI announced Sora's discontinuation, signaling that the [[concepts/video-generation-as-world-simulation]] paradigm had shifted toward dedicated [[concepts/world-models]] rather than pure video generation.

## Concepts Introduced or Discussed

- [[concepts/video-generation-as-world-simulation]] — framing video models as physics simulators
- [[concepts/world-models]] — internal representations of reality
- [[concepts/diffusion-models]] — the underlying generative framework

## Quotes & Evidence

> "Scaling video generation models is a promising path towards building general purpose simulators of the physical world."

## Metadata

- **Author**: OpenAI
- **Date Published**: 2024-02-15
- **Format**: technical report
- **URL**: https://openai.com/index/video-generation-models-as-world-simulators/
