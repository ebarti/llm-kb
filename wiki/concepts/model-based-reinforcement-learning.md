---
title: "Model-Based Reinforcement Learning"
type: concept
sources: ["[[sources/ha-schmidhuber-world-models]]", "[[sources/deepmind-genie-2]]"]
related: ["[[concepts/world-models]]", "[[concepts/latent-world-models]]", "[[entities/dreamerv3]]"]
tags: [reinforcement-learning, model-based-RL, planning, world-models, sample-efficiency]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "RL that learns an explicit environment model for planning through imagination — from Dyna (Sutton, 1990) through Ha & Schmidhuber's dream training to DreamerV3's 150+ task mastery — enabling 10-100x better sample efficiency than model-free approaches."
---

## Overview

Model-based reinforcement learning (MBRL) learns an explicit model of environment dynamics — a [[concepts/world-models]] — and uses it for planning by simulating future trajectories. Unlike model-free RL (which learns value functions or policies directly from experience), MBRL separates "understanding the world" from "deciding what to do," enabling imagination-based planning, sample-efficient learning, and transfer across tasks.

The field's trajectory runs from Sutton's Dyna architecture (1990) through Ha and Schmidhuber's dream training (2018) to [[entities/dreamerv3]]'s mastery of 150+ diverse tasks with a single algorithm (Nature 2025).

## Key Ideas

### The MBRL Loop

1. **Observe**: Collect experience from the environment
2. **Model**: Update the world model with new observations
3. **Imagine**: Simulate future trajectories within the world model
4. **Plan**: Select actions that maximize predicted reward
5. **Act**: Execute the planned action in the real environment

### Dream Training

Ha and Schmidhuber demonstrated that step 5 can be optional — agents can be trained entirely within the model's "dreams." The MDN-RNN generates synthetic rollouts, and the controller is optimized via evolution (CMA-ES) within these dreams. Temperature control (τ ~1.15) prevents agents from exploiting model imperfections.

### DreamerV3's Achievement

The single most impressive MBRL result: [[entities/dreamerv3]] (Nature 2025) uses a Recurrent State-Space Model (RSSM) combining deterministic and stochastic states, training actor-critic networks entirely within imagined trajectories. It masters 150+ tasks with a single fixed configuration — including being the first algorithm to mine a diamond in Minecraft from scratch (30M steps, ~17 days of playtime), without expert demonstrations or curricula.

### Planning Strategies

- **Forward rollout**: Simulate and select best trajectory
- **Model Predictive Control**: Re-plan at every step
- **Monte Carlo Tree Search**: Branch search (MuZero)
- **Gradient-based optimization**: Backprop through the model

## How It Connects

MBRL is the original application domain for [[concepts/world-models]]. [[concepts/latent-world-models]] emerged as the practical approach for MBRL at scale. The DreamerV3 line connects to [[concepts/embodied-ai]] through robotic applications. The MuZero line connects to game-playing and planning. The modern foundation world model era (Cosmos, Genie) extends MBRL principles to internet-scale data.

## Sources

- [[sources/ha-schmidhuber-world-models]] — dream training paradigm
- [[sources/deepmind-genie-2]] — generating training environments for MBRL agents
