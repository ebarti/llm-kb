---
title: "NVIDIA Isaac GR00T"
type: entity
entity_type: framework
url: "https://developer.nvidia.com/isaac/gr00t"
related: ["[[concepts/foundation-models-for-robotics]]", "[[concepts/humanoid-robots]]", "[[concepts/sim-to-real-transfer]]", "[[entities/nvidia]]"]
tags: [nvidia, groot, isaac, foundation-models, humanoid-robots]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "NVIDIA's open humanoid robot foundation model with dual System 1 (reflexive) / System 2 (deliberative) architecture; generated 780K synthetic trajectories in 11h; adopted by Boston Dynamics, 1X, Agility; N1.6 integrates Cosmos Reason VLM for step-by-step planning."
---

## Overview

NVIDIA Isaac GR00T (Generalist Robot 00 Technology) is the world's first open, fully customizable [[concepts/foundation-models-for-robotics]] for [[concepts/humanoid-robots]]. Released in March 2025, it brings human-like reasoning to robots through a dual-system architecture inspired by Kahneman's System 1 / System 2 cognitive framework.

## Key Facts

- **Type**: framework / model
- **Organization**: [[entities/nvidia]]
- **Released**: March 2025 (N1); September 2025 (N1.6)
- **Architecture**: Dual System 1 (fast reflexive actions) / System 2 (slow deliberate VLM reasoning)
- **Open Source**: Yes (GitHub, Hugging Face)
- **Notable for**: 780K synthetic trajectories in 11 hours; adopted by major robotics companies

## Version History

- **N1** (March 2025): Initial release. Dual-system architecture. Open and customizable.
- **N1.6** (September 2025): Integrates NVIDIA Cosmos Reason VLM. Simultaneous locomotion + manipulation. More torso/arm freedom.

## Supporting Technologies

- **Newton Physics Engine**: Co-developed with [[entities/google-deepmind]] and Disney Research
- **NVIDIA Omniverse**: Digital twin simulation platform
- **Isaac GR00T Blueprint**: Synthetic data generation for manipulation
- **Cosmos Transfer**: World foundation models

## Adoption

1X Technologies (NEO Gamma), Agility Robotics, [[entities/boston-dynamics]], Mentee Robotics, NEURA Robotics, Franka Robotics, LG Electronics, Techman Robot.

## Mentions

- [[sources/nvidia-isaac-groot-n1-foundation-model]] -- primary source
- [[sources/llms-for-robotics-survey-2025]] -- in VLA evolution survey
