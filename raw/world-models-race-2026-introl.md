---
title: "World Models Race 2026: How LeCun, DeepMind, and NVIDIA Are Building the Next AI Paradigm"
source: "https://introl.com/blog/world-models-race-agi-2026"
author: "Introl"
date_published: 2026-01-15
date_ingested: 2026-04-05
tags: [world-models, JEPA, AMI-Labs, Genie, NVIDIA-Cosmos, World-Labs, AGI]
type: article
status: raw
discovered_via: search
---

# World Models Race 2026

## AMI Labs (Yann LeCun)
- Founded late 2025, headquartered Paris
- €500M raise at €3B valuation (pre-product); later $1.03B seed at $3.5B valuation (March 2026, largest European seed ever)
- Executive Chairman: Yann LeCun (Turing Award, former Meta FAIR director)
- CEO: Alex LeBrun (ex-Nabla medical AI)
- Meta partnership maintained; no direct investment
- LeCun describes world models as "your mental model of how the world behaves," enabling systems to simulate action sequences and predict environmental consequences
- Core capabilities: planning through outcome simulation, causal reasoning, persistent memory, spatial relationship comprehension
- Builds on I-JEPA (Image Joint Embedding Predictive Architecture)

## DeepMind Genie 3
- Released August 2025
- 24 fps real-time, 720p resolution, several-minute consistency, ~1 minute lookback memory
- Auto-regressive frame generation with visual memory integration
- Physics self-learned (not hard-coded)
- Shlomi Fruchter: "the first real-time interactive general-purpose world model"
- Limitations: limited agent action spaces, consistency degradation beyond several minutes

## World Labs Marble
- Founded by Fei-Fei Li, launched November 2025
- $230M funding
- Accepts text, photos, videos, 3D layouts, panoramic images
- Outputs persistent, downloadable 3D environments
- Export to Unreal Engine, Unity; VR support (Vision Pro, Quest 3)
- Pricing: Free ($0, 4/mo) to Max ($95, 75/mo)

## NVIDIA Cosmos
- Launched CES 2025, 2M downloads by Jan 2026
- Training: 9,000 trillion tokens, 20M hours real-world footage
- Model tiers: Nano (edge), Super (baseline), Ultra (max quality)
- Model types: Cosmos-Predict (future state), Cosmos-Transfer (spatial control), Cosmos-Reason (reasoning)
- Industrial adoption: 1X, Agility, Figure AI, Waabi, XPENG, Uber

## LLM Limitations (Mathematical)
- 2024 proof: LLMs cannot learn all computable functions, ensuring inevitable hallucination
- LeCun: "LLMs are too limiting...Scaling them up will not allow us to reach AGI"

## Competitive Video Generation
- Gen-4.5 (Runway): #1 Video Arena, explicit world model framing
- Veo 3 (Google): #2 Video Arena
- Sora 2 Pro (OpenAI): #7 Video Arena

## Infrastructure Requirements
- World model inference: 8-32 GPUs/request (vs 1-8 for LLMs)
- World model training: thousands-tens of thousands GPUs
- Single video hour = ~100GB uncompressed; petabyte-scale storage needed
