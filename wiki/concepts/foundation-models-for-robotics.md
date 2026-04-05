---
title: "Foundation Models for Robotics"
type: concept
sources: ["[[sources/llms-for-robotics-survey-2025]]", "[[sources/google-deepmind-rt2-vla-model]]", "[[sources/physical-intelligence-pi0-foundation-model]]", "[[sources/nvidia-isaac-groot-n1-foundation-model]]", "[[sources/deloitte-physical-ai-humanoid-robots-2026]]"]
related: ["[[concepts/vision-language-action-models]]", "[[concepts/embodied-intelligence]]", "[[concepts/cross-embodiment-transfer]]", "[[concepts/sim-to-real-transfer]]", "[[concepts/robot-learning-from-demonstration]]"]
tags: [foundation-models, robotics, generalist-robots, pre-training]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The application of the foundation model paradigm (large-scale pre-training → task-specific fine-tuning) to robotics — enabling generalist robot policies that transfer across tasks, environments, and robot morphologies; key models include RT-2, π0, GR00T-N1, and OpenVLA."
---

## Overview

Foundation models for robotics apply the same paradigm that transformed NLP and vision -- large-scale pre-training on diverse data followed by task-specific fine-tuning -- to robot control. Just as GPT-4 provides a foundation for language tasks and CLIP for vision, models like [[entities/rt-2]], [[entities/pi0]], and [[entities/nvidia-groot]] aim to provide a foundation for physical interaction. The goal is a single model that can control diverse robots across diverse tasks, rather than training a separate policy for each robot-task combination.

VC investment in robotics reached $7.2B in 2025 (up from $3.1B in 2023), with foundation models a primary driver. IEEE Robotics and Automation Society has a special issue on the topic expected July 2026.

## Key Ideas

### The Foundation Model Paradigm for Robots

The paradigm mirrors LLM development:

| Phase | LLMs | Robot Foundation Models |
|-------|------|----------------------|
| **Pre-training data** | Internet text (trillions of tokens) | Internet images/text + robot trajectories (Open X-Embodiment: 800K) |
| **Pre-training** | Next-token prediction | Vision-language pre-training + action prediction |
| **Fine-tuning** | Task-specific instruction tuning | 1-20 hours of task demonstrations (π0) |
| **Deployment** | API / local inference | On-robot inference at 50Hz (π0) or with cloud fallback |

### Key Models

**[[entities/rt-2]]** (Google DeepMind, 2023): First major VLA. Built on PaLM-E/PaLI-X. Encodes actions as text tokens. Showed emergent reasoning from web pre-training. 55B parameters.

**OpenVLA** (2024): Achieved parity with RT-2-X at 10x fewer parameters (~5.5B), demonstrating that scaling is not the only path to performance.

**[[entities/pi0]]** (Physical Intelligence, 2024): 3B parameter model using [[concepts/flow-matching]] for 50Hz continuous control. Trained on 8 robots, 68 tasks. First to achieve complex dexterous tasks (laundry folding, box assembly). Open-sourced.

**[[entities/nvidia-groot]]** N1 (NVIDIA, 2025): Open foundation model with dual System 1 (reflexive) / System 2 (deliberative) architecture. Generated 780K synthetic trajectories in 11 hours. Adopted by Boston Dynamics, 1X, Agility Robotics.

**[[entities/helix-vla]]** (Figure AI, 2025-26): Proprietary VLA enabling full-body humanoid autonomy. Pivoted from OpenAI partnership to focus on "high rate robot control."

### Cross-Embodiment Transfer

One of the most striking capabilities is [[concepts/cross-embodiment-transfer]]: a model trained on data from many robot types can deploy on an entirely new robot without retraining. π0 was trained on 7-8 distinct robot platforms and OpenX-Embodiment spans hundreds. This parallels how LLMs generalize across tasks.

### The Data Challenge

Robot foundation models face a unique data problem: real-world robot data is expensive and scarce compared to internet text. Solutions include:
- **Synthetic data**: NVIDIA's GR00T generated 780K trajectories in 11 hours via Omniverse simulation
- **Cross-embodiment pooling**: Open X-Embodiment aggregates 800K trajectories from diverse platforms
- **Human video data**: Learning from human demonstration videos (no robot needed)
- **Efficient fine-tuning**: π0 requires only 1-20 hours of demonstration data per new task

## How It Connects

- [[concepts/vision-language-action-models]] -- the specific model architecture
- [[concepts/embodied-intelligence]] -- the broader paradigm these models serve
- [[concepts/cross-embodiment-transfer]] -- key capability of foundation models
- [[concepts/sim-to-real-transfer]] -- critical for generating training data at scale
- [[concepts/robot-learning-from-demonstration]] -- primary fine-tuning mechanism
- [[concepts/dexterous-manipulation]] -- the frontier task these models are tackling

## Open Questions

- Is there a "scaling law" for robot foundation models analogous to Chinchilla for LLMs?
- Can foundation models trained primarily in simulation match those trained on real data?
- What is the right granularity of action representation (discrete tokens vs continuous flows)?
- Will a single universal robot foundation model emerge or will specialization persist?

## Sources

- [[sources/llms-for-robotics-survey-2025]] -- comprehensive taxonomy and evolution
- [[sources/google-deepmind-rt2-vla-model]] -- pioneering VLA work
- [[sources/physical-intelligence-pi0-foundation-model]] -- open-source generalist policy
- [[sources/nvidia-isaac-groot-n1-foundation-model]] -- open foundation model platform
- [[sources/deloitte-physical-ai-humanoid-robots-2026]] -- market and deployment context
