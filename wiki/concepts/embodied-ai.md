---
title: "Embodied AI"
type: concept
sources: ["[[sources/meta-v-jepa-2]]", "[[sources/deepmind-genie-2]]", "[[sources/world-models-race-2026]]"]
related: ["[[concepts/world-models]]", "[[concepts/physical-ai]]", "[[concepts/jepa]]", "[[concepts/model-based-reinforcement-learning]]", "[[concepts/latent-world-models]]"]
tags: [embodied-AI, robotics, sim-to-real, world-models, perception]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "AI agents with physical instantiation that learn through interaction with the world — requiring the perception-modeling-decision loop where world models bridge multimodal sensing with executable actions; advancing via sim-to-real transfer and self-supervised video pretraining."
---

## Overview

Embodied AI is the subfield where AI systems exist as physical agents — robots, autonomous vehicles, drones — that learn through direct interaction with the real world. Unlike disembodied AI (chatbots, image classifiers), embodied systems must close the perception-action loop: sensing the environment, building an internal model, planning actions, executing them, and learning from the results.

[[concepts/world-models]] have become the central enabling technology for embodied AI. They provide the internal "mental simulation" that allows agents to plan before acting, predict consequences of actions, and transfer skills from simulation to reality.

## Key Ideas

### The Three-Layer Framework

A 2025 Frontiers survey formalizes embodied intelligence as three interconnected layers:

1. **Perception & Alignment**: Integrating multimodal inputs (vision, language, touch) into unified state representations via cross-modal fusion
2. **World Modeling & Structure Prediction**: Building internal environmental understanding through [[concepts/latent-world-models]], causal relationship models, and task graphs
3. **Policy Generation & Adaptation**: Transforming environmental models into executable control actions via prompt encoders and policy decoders

### The Sim-to-Real Gap

The fundamental challenge: simulated environments differ from reality in physics, visual appearance, sensor noise, and dynamics. Bridging this requires:

- **Domain randomization**: Train across many visual/physical variations
- **Progressive finetuning**: Simulation pretraining → real-world adaptation
- **Self-supervised pretraining**: V-JEPA 2 demonstrates that internet video pretraining transfers to real robots with only 62 hours of robot-specific data
- **Structural consistency**: Maintaining identity mapping between simulation and reality

### Key Demonstrations

- **V-JEPA 2-AC**: Zero-shot robot planning on Franka arms in unseen labs; 65-80% pick-and-place success
- **DreamerV3**: First to mine diamonds in Minecraft from scratch — long-horizon sequential decision-making
- **Genie 2/3**: Generating unlimited diverse training environments for embodied agents
- **SIMA agent**: Following natural-language instructions in Genie-generated worlds

### The Architectural Evolution

RNN encoders (2018) → latent state-space models (2020) → multimodal Transformers (2024) → joint MLLM + world model architectures (2025). The trend is toward systems that combine high-level semantic reasoning (from language models) with physics-aware simulation (from world models).

## How It Connects

Embodied AI is where [[concepts/world-models]], [[concepts/physical-ai]], and [[concepts/jepa]] converge in practice. The perception layer connects to [[concepts/multimodal-ai]] and [[concepts/vision-language-models]]. The planning layer connects to [[concepts/model-based-reinforcement-learning]] and [[concepts/latent-world-models]]. The deployment connects to [[concepts/physical-ai]] applications in robotics and autonomous driving.

## Sources

- [[sources/meta-v-jepa-2]] — V-JEPA 2 for zero-shot robot planning
- [[sources/deepmind-genie-2]] — generating training environments
- [[sources/world-models-race-2026]] — the broader ecosystem
