---
title: "World Models"
type: concept
sources: ["[[sources/ha-schmidhuber-world-models]]", "[[sources/world-models-race-2026]]", "[[sources/deepmind-genie-2]]", "[[sources/meta-v-jepa-2]]", "[[sources/openai-video-world-simulators]]", "[[sources/nvidia-cosmos-world-foundation]]", "[[sources/llms-and-world-models-mitchell]]"]
related: ["[[concepts/jepa]]", "[[concepts/latent-world-models]]", "[[concepts/video-generation-as-world-simulation]]", "[[concepts/physical-ai]]", "[[concepts/embodied-ai]]", "[[concepts/model-based-reinforcement-learning]]", "[[concepts/llm-world-understanding]]"]
tags: [world-models, AI-paradigm, simulation, prediction, planning, AGI]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "AI systems that build internal representations of reality to simulate, predict, and plan — the emerging paradigm challenging LLMs as the path to general intelligence, with $1.3B+ in 2026 funding across AMI Labs, DeepMind, NVIDIA, and World Labs."
---

## Overview

A world model is an AI system that maintains an internal representation of reality — enabling it to simulate future states, predict consequences of actions, and plan strategies without directly interacting with the real world. Where [[concepts/llm-world-understanding]] debate centers on whether LLMs implicitly learn world structure from text, dedicated world models explicitly construct these representations from visual, physical, and interactive data.

The concept has roots in cognitive science (humans navigate the world using internal mental models) and was formally introduced to modern AI by [[entities/david-ha]] and [[entities/jurgen-schmidhuber]] in their seminal 2018 paper. By 2026, world models have become a major AI paradigm with over $1.3 billion in dedicated funding, positioned by [[entities/yann-lecun]] and others as the necessary successor to LLMs for achieving general intelligence.

## Key Ideas

### The Four Components

A world model typically combines four elements:

1. **Transition Model**: Predicts how environmental state changes given an action — p(s_{t+1} | s_t, a_t)
2. **Observation Model**: Determines what the agent perceives in each state — p(o_t | s_t)
3. **Reward Predictor**: Estimates expected reward for state-action pairs — r(s_t, a_t)
4. **Latent Encoder**: Compresses high-dimensional observations into compact representations

### The Core Insight

If the world model is rich enough, the decision-making policy can be trivially simple. Ha and Schmidhuber demonstrated this dramatically: their CarRacing agent used a world model with 4.7M parameters but a controller with only 867 parameters — a single linear layer. The world model does the heavy lifting of understanding reality; the controller merely navigates within that understanding.

### Why World Models Matter for AGI

[[entities/yann-lecun]] argues that LLMs are fundamentally limited because they operate on language — a lossy, one-dimensional projection of multidimensional reality. World models, by contrast, learn directly from sensory data (video, interaction) and develop physical intuition, causal reasoning, and persistent spatial-temporal memory. The argument is not that language is unimportant, but that it is insufficient as the sole substrate for intelligence.

### The 2026 Landscape

| Organization | System | Architecture | Focus |
|-------------|--------|-------------|-------|
| [[entities/ami-labs]] | LeWorldModel | [[concepts/jepa]] | General world understanding |
| [[entities/google-deepmind]] | [[entities/genie]] 3 | Autoregressive latent diffusion | Interactive environment generation |
| [[entities/nvidia-cosmos]] | Cosmos | Diffusion + autoregressive WFMs | Physical AI infrastructure |
| [[entities/world-labs]] | Marble | 4D generation | Creative 3D world building |
| Meta AI | [[concepts/jepa]] (V-JEPA 2) | Joint embedding prediction | Self-supervised video understanding |
| Wayve | GAIA-2 | Latent diffusion | Autonomous driving simulation |

### Historical Evolution

1. **Sutton (1990)**: Conceptual framework separating real and imagined experience
2. **Ha & Schmidhuber (2018)**: VAE + MDN-RNN demonstrating "learning inside a dream"
3. **MuZero (2020)**: Planning via implicit dynamics without observation reconstruction
4. **Dreamer series (2020-2025)**: From Dreamer to [[entities/dreamerv3]] — single algorithm across 150+ tasks
5. **LeCun (2022)**: Proposes [[concepts/jepa]] as the architectural framework for world models
6. **Foundation era (2024-2026)**: Sora, Genie, Cosmos, V-JEPA 2 — scaling world models to foundation model size

## How It Connects

World models sit at the intersection of several major AI paradigms. They extend [[concepts/model-based-reinforcement-learning]] to richer representations. They provide the grounding layer that [[concepts/embodied-ai]] systems need. They offer a fundamentally different approach than [[concepts/llm-world-understanding]] — learning from interaction rather than text. And they enable [[concepts/physical-ai]] applications (robotics, autonomous driving) that require understanding physical dynamics.

The [[concepts/video-generation-as-world-simulation]] paradigm (Sora, Veo) represents one approach where video generation quality serves as a proxy for world understanding. [[concepts/jepa]] represents another where the goal is not to generate but to understand — learning representations rather than pixels.

## Open Questions

- Can world models and LLMs converge into a unified architecture, or are they fundamentally different paradigms?
- What is the minimum data requirement for a world model to develop robust physical intuition?
- How do we evaluate whether a model truly "understands" physics vs. pattern-matching visual statistics?
- Can world models trained on internet video transfer to real-world robotic applications at production quality?
- Is the 8-32 GPU inference requirement for world models an acceptable infrastructure cost at scale?

## Sources

- [[sources/ha-schmidhuber-world-models]] — the foundational paper (2018)
- [[sources/world-models-race-2026]] — the competitive landscape
- [[sources/deepmind-genie-2]] — interactive 3D world generation
- [[sources/meta-v-jepa-2]] — self-supervised world models for robotics
- [[sources/openai-video-world-simulators]] — video as world simulation
- [[sources/nvidia-cosmos-world-foundation]] — infrastructure for physical AI
- [[sources/llms-and-world-models-mitchell]] — the philosophical debate
