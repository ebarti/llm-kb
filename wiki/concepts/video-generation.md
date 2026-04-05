---
title: "Video Generation"
type: concept
sources: ["[[sources/ai-video-market-2026]]"]
related: ["[[concepts/diffusion-models]]", "[[concepts/diffusion-transformer]]", "[[concepts/image-generation]]", "[[concepts/audio-visual-generation]]", "[[entities/sora]]", "[[entities/runway]]", "[[entities/kling]]", "[[entities/veo]]"]
tags: [video-generation, text-to-video, generative-ai, creative-tools]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "AI systems generating video from text or image inputs -- a $847M market in 2026 growing at 34.2% CAGR, shaped by Sora's shutdown and the rise of Runway Gen-4, Kling 3.0, and Veo 3 with native audio generation."
---

## Overview

Video generation extends [[concepts/image-generation]] into the temporal dimension, synthesizing coherent sequences of frames from text prompts, reference images, or existing video. The field underwent a dramatic market correction in early 2026 when [[entities/sora]] shut down due to unsustainable compute costs ($15M/day), but the surviving platforms have established viable business models and continue advancing capabilities.

Modern video generation systems build on the [[concepts/diffusion-transformer]] architecture, treating video as sequences of spatiotemporal patches -- the same architectural principle that made DiT successful for images, extended with temporal attention mechanisms.

## Key Ideas

### Technical Architecture

Video generation models typically extend image [[concepts/diffusion-models]] with:
- **Temporal attention layers**: Self-attention across frames in addition to spatial attention within frames
- **Spatiotemporal patches**: Video treated as 3D patch sequences (height x width x time)
- **Motion modules**: Specialized components for learning coherent movement and physics
- **Character persistence**: Maintaining subject identity across shots and camera angles

### Market Tiers (2026)

The post-Sora market has consolidated into four tiers:

**Quality-First: [[entities/runway]] Gen-4**
Professional production tool with character persistence via reference imagery, Act-Two motion capture, in-video editing via Aleph interface. Maximum 1080p, 10-second clips. ~$0.12/second. The only platform designed for professional post-production workflows.

**Cost-Efficiency: [[entities/kling]] 3.0**
ByteDance's model leads on economics at $0.07/second (65% cheaper than Sora). Technical breakthroughs include multi-shot sequences (2-6 scenes) with automatic transitions and camera logic, native audio with character dialogue and lip synchronization, and character lock consistency.

**Ecosystem: [[entities/veo]] 3**
Google DeepMind's model introduced native synchronized audio generation -- effects, dialogue, and ambient sound from a single text prompt. This eliminates entire post-production steps. Veo 3.1 Lite at $0.05/second is the most affordable option. Deep integration with YouTube and Vertex AI.

**Creative: Pika 2.5**
Specializes in expressive short-form content with Pikaformance (voice/image to performance) and Pikaswaps for viral social applications.

### The Sora Lesson

[[entities/sora]]'s failure is a cautionary tale for the industry. Despite producing cinema-quality output, the platform burned ~$15M daily on compute against only $2.1M in total lifetime revenue. Disney withdrew a planned $1B partnership. The lesson: in generative video, sustainable unit economics matter more than raw capability. Successful platforms prioritized efficiency from the start.

### Capability Progression

| Capability | 2024 | 2025 | 2026 |
|-----------|------|------|------|
| Maximum duration | 5-10 sec | 10-30 sec | Up to 3 min (Kling) |
| Resolution | 720p | 1080p | Up to 4K (Veo) |
| Native audio | None | Emerging | Standard (Veo, Kling) |
| Multi-shot | None | None | Available (Kling 3.0) |
| Character consistency | Poor | Improving | Good (Runway, Kling) |
| Cost per second | $0.50+ | $0.15-0.30 | $0.05-0.15 |

### Market Economics

- AI video market: $847M in 2026, projected $3.35B by 2034
- VC investment: $4.7B in 2025 (189% YoY increase)
- Growth rate: 34.2% CAGR
- 87% of creative professionals use AI video tools (Artlist AI Trend Report 2026)
- Teams report 5-10x content production with same resources

## How It Connects

Video generation builds on [[concepts/image-generation]] foundations (same [[concepts/diffusion-transformer]] architectures) and increasingly converges with [[concepts/audio-generation]] via [[concepts/audio-visual-generation]]. The [[concepts/diffusion-models]] that power video generation share theoretical foundations with those for images and 3D content ([[concepts/3d-generation]]).

## Open Questions

- When will 5+ minute coherent narratives become reliable?
- Will native audio-video generation eliminate the need for separate audio models?
- How will pricing compress as competition intensifies?
- What governance frameworks will address deepfake concerns?

## Sources

- [[sources/ai-video-market-2026]] -- comprehensive market analysis
