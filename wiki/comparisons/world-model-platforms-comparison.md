---
title: "World Model Platforms: AMI Labs vs Genie vs Cosmos vs World Labs"
type: comparison
subjects: ["[[entities/ami-labs]]", "[[entities/genie]]", "[[entities/nvidia-cosmos]]", "[[entities/world-labs]]"]
sources: ["[[sources/world-models-race-2026]]", "[[sources/deepmind-genie-2]]", "[[sources/nvidia-cosmos-world-foundation]]", "[[sources/meta-v-jepa-2]]"]
related: ["[[concepts/world-models]]", "[[concepts/physical-ai]]", "[[concepts/embodied-ai]]"]
tags: [world-models, platform-comparison, AMI-Labs, Genie, Cosmos, World-Labs, 2026]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Four major world model platforms compared: AMI Labs (JEPA, general intelligence), Genie 3 (interactive environments, agent training), NVIDIA Cosmos (physical AI infrastructure), World Labs Marble (creative 3D generation) — each targeting different applications with distinct architectures."
---

## Overview

By early 2026, four major platforms define the [[concepts/world-models]] landscape, each with distinct technical approaches, target applications, and business models. Together they represent over $1.5B in dedicated funding and signal a paradigm shift from language-only AI toward physically grounded intelligence.

## Comparison Matrix

| Dimension | AMI Labs | Genie 3 (DeepMind) | NVIDIA Cosmos | World Labs Marble |
|-----------|---------|-------------------|---------------|------------------|
| **Architecture** | [[concepts/jepa]] | Autoregressive latent diffusion | Diffusion + autoregressive WFM | 4D generation |
| **Focus** | General world understanding | Interactive environment generation | Physical AI infrastructure | Creative 3D content |
| **Funding** | $1.03B seed | Google internal | NVIDIA internal | $230M |
| **Valuation** | $3.5B | N/A | N/A | N/A |
| **Key person** | [[entities/yann-lecun]] | Shlomi Fruchter | Jensen Huang | [[entities/fei-fei-li]] |
| **Model size** | 15M (LeWorldModel) to 1.2B (V-JEPA 2) | Undisclosed | 4B-14B | Undisclosed |
| **Training data** | 1M+ hours video | Large video dataset | 20M hours / 100M clips | Undisclosed |
| **Real-time** | No (research stage) | Yes (24fps, 720p) | Near-real-time (with optimization) | No |
| **Interactive** | No (representation learning) | Yes (keyboard/mouse) | No (prediction only) | Limited |
| **Physics** | Representation-based | Self-learned, emergent | Trained on physical domains | 3D geometric |
| **Open/closed** | TBD | Research preview | Open model license | SaaS (freemium) |
| **Applications** | AGI research | Agent training, gaming | AV, robotics, industrial | Gaming, VFX, VR |
| **VR support** | No | No | No | Vision Pro, Quest 3 |
| **Export formats** | N/A | N/A | N/A | Unreal, Unity |

## Analysis

### AMI Labs: The Purist Play
Builds directly on [[concepts/jepa]] — predicting representations rather than pixels. The most theoretically ambitious: aiming to replace LLMs entirely. Currently at the earliest stage (LeWorldModel is 15M params), but V-JEPA 2 at Meta demonstrated the architecture at 1.2B params. The $1.03B seed provides runway to scale dramatically.

### Genie 3: The Interactivity Leader
The only platform generating fully interactive environments at real-time speeds. Genie 3's 24fps 720p with multi-minute consistency is a genuine technical breakthrough. Primary value: generating unlimited training environments for [[concepts/embodied-ai]] agents, removing the environment bottleneck for RL research.

### NVIDIA Cosmos: The Infrastructure Play
Positioned as the platform layer that all others build on — tokenizers, models at multiple scales, data processing pipelines. Already adopted by major robotics and AV companies. The open model license and 2M+ downloads create ecosystem lock-in through standardization.

### World Labs Marble: The Creative Tool
Makes 3D world generation accessible to non-technical users through text/image prompts. VR support and game engine export target creative applications. Less focused on AI understanding, more on democratizing 3D content creation.

## When to Use Each

| Use Case | Best Platform |
|----------|--------------|
| General world understanding research | AMI Labs / V-JEPA 2 |
| RL agent training environments | Genie 3 |
| Autonomous driving simulation | NVIDIA Cosmos |
| Robotic manipulation training | NVIDIA Cosmos + V-JEPA 2 |
| Creative 3D content | World Labs Marble |
| VR/gaming prototyping | World Labs Marble |
| Academic research (open weights) | NVIDIA Cosmos |

## Sources

- [[sources/world-models-race-2026]] — competitive landscape overview
- [[sources/deepmind-genie-2]] — Genie architecture and capabilities
- [[sources/nvidia-cosmos-world-foundation]] — Cosmos technical details
- [[sources/meta-v-jepa-2]] — V-JEPA 2 (AMI Labs' technical foundation)
