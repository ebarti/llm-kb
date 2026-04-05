---
title: "RT-2 vs π0 vs GR00T N1: Robot Foundation Models Compared"
type: comparison
subjects: ["[[entities/rt-2]]", "[[entities/pi0]]", "[[entities/nvidia-groot]]"]
sources: ["[[sources/google-deepmind-rt2-vla-model]]", "[[sources/physical-intelligence-pi0-foundation-model]]", "[[sources/nvidia-isaac-groot-n1-foundation-model]]", "[[sources/llms-for-robotics-survey-2025]]"]
related: ["[[concepts/vision-language-action-models]]", "[[concepts/foundation-models-for-robotics]]", "[[concepts/cross-embodiment-transfer]]"]
tags: [vla, foundation-models, comparison, robotics]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Comparison of three leading robot foundation models: RT-2 (pioneering VLA, 55B params, emergent reasoning), π0 (3B params, flow matching, dexterous manipulation), and GR00T N1 (open platform, dual System 1/2, massive synthetic data)."
---

## Overview

Three models represent the evolution and diversification of [[concepts/foundation-models-for-robotics]]: Google DeepMind's [[entities/rt-2]] (the pioneer), Physical Intelligence's [[entities/pi0]] (the dexterous specialist), and NVIDIA's [[entities/nvidia-groot]] (the open platform). Each reflects a different philosophy and set of trade-offs.

## Comparison Matrix

| Dimension | RT-2 | π0 | GR00T N1 |
|-----------|------|-----|----------|
| **Organization** | Google DeepMind | Physical Intelligence | NVIDIA |
| **Date** | Jul 2023 | Oct 2024 | Mar 2025 |
| **Parameters** | Up to 55B | 3B (full), 470M (small) | Not disclosed |
| **Backbone** | PaLM-E / PaLI-X | PaliGemma | Custom (Cosmos Reason in N1.6) |
| **Action Generation** | Discrete text tokens | Flow matching (50Hz) | Dual System 1/2 |
| **Action Rate** | Low (token rate) | 50Hz continuous | Adaptive (System 1 fast, System 2 slow) |
| **Training Data** | RT-1 demos + web VLM | Open X-Embodiment + π Dataset (8 robots) | Human demos + 780K synthetic trajectories |
| **Cross-Embodiment** | Limited (kitchen robots) | 7-8 robot types, 68 tasks | Designed for diverse humanoids |
| **Open Source** | No | Yes (Hugging Face LeRobot) | Yes (GitHub, Hugging Face) |
| **Key Strength** | Emergent reasoning from web data | Dexterous manipulation | Ecosystem and synthetic data |
| **Key Limitation** | Closed, large, slow inference | Smaller web knowledge than RT-2 | Focused on humanoids |
| **Dexterous Tasks** | Not demonstrated | Laundry folding (1.0), box assembly | Material handling, grasping |

## Analysis

### RT-2: The Pioneer

RT-2 proved the VLA concept: web-scale VLM pre-training transfers to robotic control. Its emergent capabilities (using rocks as hammers, understanding human needs) demonstrated deep knowledge transfer. However, at 55B parameters it is too large for on-robot deployment, it remains closed-source, and it was not designed for dexterous manipulation.

### π0: The Dexterous Generalist

π0 made the opposite bet: smaller model (3B), richer action representation ([[concepts/flow-matching]] at 50Hz), and deeper investment in cross-embodiment training data. The result is unprecedented dexterous capability -- tasks where RT-2 and other models score literally zero. The open-source release via Hugging Face makes it the most accessible research platform.

### GR00T N1: The Open Platform

NVIDIA's approach is infrastructure-centric: provide the model, the simulation platform (Omniverse), the physics engine (Newton), and the synthetic data pipeline as an integrated ecosystem. The dual System 1/2 architecture is unique -- separating reflexive motor control from deliberate reasoning. The ability to generate 780K trajectories in 11 hours makes data scaling almost trivially cheap.

## When to Use Each

| Scenario | Best Choice | Reason |
|----------|-------------|--------|
| Research on web knowledge transfer | RT-2 concepts (replicate with OpenVLA) | Emergent reasoning paradigm |
| Dexterous manipulation tasks | [[entities/pi0]] | Flow matching at 50Hz, proven results |
| Building humanoid products | [[entities/nvidia-groot]] | Open platform, partner ecosystem, synthetic data |
| Academic research (budget) | π0 (open source, 3B params) | Accessible model and code |
| Industrial deployment | GR00T N1 + NVIDIA ecosystem | Simulation pipeline, enterprise support |

## Sources

- [[sources/google-deepmind-rt2-vla-model]] -- RT-2 details
- [[sources/physical-intelligence-pi0-foundation-model]] -- π0 architecture and results
- [[sources/nvidia-isaac-groot-n1-foundation-model]] -- GR00T N1 platform
- [[sources/llms-for-robotics-survey-2025]] -- comparative analysis
