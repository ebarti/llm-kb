---
title: "A Review of Embodied Intelligence Systems: Three-Layer Framework"
source: "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1668910/full"
author: "Frontiers in Robotics and AI"
date_published: 2025-11-01
date_ingested: 2026-04-05
tags: [embodied-AI, world-models, robotics, perception, planning]
type: paper
status: raw
discovered_via: search
---

# Three-Layer Framework for Embodied Intelligence (DP-TA)

## Layer 1: Perception & Alignment
- Integrates multimodal inputs (vision, language, touch)
- Feature-Conditioned Modal Alignment (F-CMA) mechanism
- Unified state representations through cross-modal fusion
- Addresses uncertainty modeling and semantic alignment

## Layer 2: World Modeling & Structure Prediction
- Internal environmental understanding through latent state learning
- Causal relationship models and task graphs
- "Simulate potential future states and model causal relationships" (Ha & Schmidhuber, 2018)
- Knowledge transfer across tasks and domains

## Layer 3: Policy Generation & Adaptation
- Transforms environmental models into executable control actions
- Prompt encoders and policy decoders
- Tokenized state representations

## Key Integration
"Perception-modeling-decision" loop: world models bridge semantic understanding from perception with concrete policy execution. Enables generalization beyond training scenarios and Sim-to-Real transfer.

## Evolution of World Model Architectures
RNN encoders → latent state space modeling → multimodal Transformers with structural awareness and causal reasoning. Now accelerating with generative world models learning controllable dynamics from internet videos.

## Challenges
- Sim-to-Real gap as core challenge
- Requires structural identity mapping between policy inputs, state representations, and trajectory generation logic
