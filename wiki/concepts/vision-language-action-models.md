---
title: "Vision-Language-Action (VLA) Models"
type: concept
sources: ["[[sources/google-deepmind-rt2-vla-model]]", "[[sources/physical-intelligence-pi0-foundation-model]]", "[[sources/llms-for-robotics-survey-2025]]", "[[sources/nvidia-isaac-groot-n1-foundation-model]]", "[[sources/deloitte-physical-ai-humanoid-robots-2026]]"]
related: ["[[concepts/embodied-intelligence]]", "[[concepts/foundation-models-for-robotics]]", "[[concepts/flow-matching]]", "[[concepts/cross-embodiment-transfer]]", "[[concepts/language-grounding-for-robots]]"]
tags: [vla, robotics, foundation-models, rt-2, pi0, groot]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Neural architectures that unify visual perception, language understanding, and motor control in a single model — the core enabling technology for embodied AI, evolving from RT-2 (2023) through π0 and GR00T-N1 to general-purpose robot control."
---

## Overview

Vision-Language-Action (VLA) models are neural architectures that integrate computer vision, natural language processing, and motor control into a single system capable of perceiving the world, understanding instructions, and generating robot actions. They represent the critical bridge between the success of large language models in digital domains and the challenge of [[concepts/embodied-intelligence]] in the physical world.

The VLA paradigm was crystallized by [[entities/rt-2]] (Google DeepMind, July 2023), which showed that pre-trained vision-language models could be directly adapted for robotic control by encoding actions as text tokens. Since then, the field has rapidly evolved through [[entities/pi0]] (Physical Intelligence, flow matching at 50Hz), [[entities/nvidia-groot]] (dual System 1/2), OpenVLA (10x parameter efficiency), and [[entities/helix-vla]] (Figure AI's proprietary system).

## Key Ideas

### Architecture Patterns

VLA models extend vision-language models (VLMs) by adding action and robot state tokens:

| Aspect | VLM | VLA |
|--------|-----|-----|
| **Input** | Images + Text | Images + Text + Robot State |
| **Output** | Text / Multimodal | Motor Commands / Actions |
| **Purpose** | Understanding | Understanding + Physical Control |
| **Token types** | Image + Text | Image + Text + State + Action |

Three main approaches to action generation:

1. **Discrete action tokens** (RT-2): Actions encoded as text strings, processed by standard tokenizers. Simple but limited temporal resolution.
2. **Flow matching / diffusion** ([[entities/pi0]]): Continuous denoising from random noise to smooth action trajectories. Enables 50Hz control for [[concepts/dexterous-manipulation]].
3. **Autoregressive with FAST** (π0-FAST): DCT-based compression of action sequences into discrete tokens. 5x faster training than diffusion with lossless reconstruction.

### The Evolution of VLA Models

| Model | Year | Params | Key Innovation | Performance |
|-------|------|--------|---------------|-------------|
| RT-1 | 2022 | ~35M | End-to-end on 340K trajectories | Baseline |
| [[entities/rt-2]] | 2023 | 55B | Web-scale VLM pre-training + action tokens | 62% novel (vs 32% RT-1) |
| OpenVLA | 2024 | ~5.5B | 10x smaller, same performance | Parity with RT-2-X |
| [[entities/pi0]] | 2024 | 3B | Flow matching, 50Hz, 8 robot types | 0.971 bussing (others: 0) |
| [[entities/nvidia-groot]] N1 | 2025 | -- | Dual System 1/2, open-source | 780K synthetic trajectories in 11h |
| [[entities/helix-vla]] | 2025-26 | -- | Full-body autonomy, proprietary | Multi-robot simultaneous control |

### Training Paradigm

VLA training mirrors the LLM paradigm:

1. **Pre-training**: Large-scale vision-language data from the internet (knowledge, common sense, object recognition)
2. **Cross-embodiment training**: Diverse robot manipulation data (Open X-Embodiment: 800K trajectories from multiple platforms)
3. **Post-training / fine-tuning**: Task-specific demonstrations (π0 needs only 1-20 hours per task)

This mirrors [[concepts/domain-adaptive-pretraining]] in language models but for physical skills.

### Emergent Capabilities

Like LLMs exhibiting emergent abilities at scale, VLAs show emergent physical intelligence:
- **Symbol understanding**: Recognizing novel objects in unfamiliar contexts
- **Physical reasoning**: Using a rock as a hammer (knowledge from web data applied to manipulation)
- **Human awareness**: Selecting appropriate objects based on human state (e.g., energy drink for tired person)
- **Emergent behaviors**: π0 spontaneously stacking dishes and pre-cleaning plates during table bussing tasks

## How It Connects

- [[concepts/embodied-intelligence]] -- VLAs are the primary technical mechanism for embodied AI
- [[concepts/foundation-models-for-robotics]] -- VLAs are the specific model class implementing the foundation model paradigm for robots
- [[concepts/flow-matching]] -- the continuous action generation technique used by π0
- [[concepts/cross-embodiment-transfer]] -- VLAs enable a single model to control diverse robot morphologies
- [[concepts/language-grounding-for-robots]] -- VLAs provide end-to-end grounding without separate affordance functions
- [[concepts/dexterous-manipulation]] -- VLAs (especially π0) first achieved complex dexterous tasks
- [[concepts/sim-to-real-transfer]] -- training VLAs often requires synthetic data (780K trajectories in 11h for GR00T)

## Open Questions

- What is the minimum model size for effective VLA performance? (OpenVLA suggests 5.5B may suffice)
- Can VLAs handle safety-critical tasks (surgery, driving) where errors have severe consequences?
- How should VLAs handle out-of-distribution physical scenarios they have never trained on?
- Will a single universal VLA emerge, or will task-specific fine-tuning always be necessary?

## Sources

- [[sources/google-deepmind-rt2-vla-model]] -- the pioneering VLA work
- [[sources/physical-intelligence-pi0-foundation-model]] -- flow matching and dexterous manipulation breakthrough
- [[sources/llms-for-robotics-survey-2025]] -- comprehensive survey tracing VLA evolution
- [[sources/nvidia-isaac-groot-n1-foundation-model]] -- open foundation model with dual-system architecture
- [[sources/deloitte-physical-ai-humanoid-robots-2026]] -- industry perspective on VLA deployment
