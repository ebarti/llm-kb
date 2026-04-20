---
title: "NVIDIA Isaac GR00T N1: Open Humanoid Robot Foundation Model"
source: "https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks"
author: "NVIDIA"
date_published: 2025-03-18
date_ingested: 2026-04-05
tags: [nvidia, groot, isaac, foundation-models, humanoid-robots, simulation, robotics]
type: article
status: raw
discovered_via: search
---

# NVIDIA Isaac GR00T N1

World's first open, fully customizable foundation model for generalized humanoid reasoning and skills. Released March 2025.

## Dual-System Architecture

Inspired by human cognition (Kahneman System 1/System 2):

- **System 1 (Fast Thinking)**: Action model mirroring reflexes. Translates high-level plans into precise continuous robot movements. Trained on human demonstration + massive synthetic data from NVIDIA Omniverse.
- **System 2 (Slow Thinking)**: Vision language model for deliberate reasoning about environment and instructions.

## Training & Data

- Generated 780,000 synthetic trajectories (equivalent to 9 months of continuous human demonstration) in 11 hours
- 40% performance improvement when synthetic + real data combined
- Fully customizable: developers post-train with real or synthetic data specific to their robot/task

## Version History

- **N1** (March 2025): Initial release
- **N1.6** (September 2025): Integrates NVIDIA Cosmos Reason (reasoning VLM). Simultaneous movement + object handling. More torso/arm freedom.

## Capabilities

- Single and dual-arm manipulation
- Object grasping and transfer
- Material handling, packaging, inspection
- Multi-step tasks requiring long context

## Supporting Technologies

- **Newton Physics Engine**: Open-source, co-developed with Google DeepMind and Disney Research. Optimized for robot learning. Compatible with MuJoCo and Isaac Lab.
- **Isaac GR00T Blueprint**: Synthetic manipulation motion generation
- **NVIDIA Cosmos Transfer**: World foundation models
- Open-source physical AI dataset on Hugging Face

## Partner Robots

1X Technologies (NEO Gamma), Agility Robotics, Boston Dynamics, Mentee Robotics, NEURA Robotics, Franka Robotics, LG Electronics, Techman Robot, and others.
