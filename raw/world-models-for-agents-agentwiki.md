---
title: "World Models for AI Agents"
source: "https://agentwiki.org/world_models_for_agents"
author: "AgentWiki"
date_published: 2025-10-01
date_ingested: 2026-04-05
tags: [world-models, agents, planning, DreamerV3, Voyager, reinforcement-learning]
type: article
status: raw
discovered_via: search
---

# World Models for AI Agents

## Core Architecture (Four Components)
1. Transition Model: p(s_{t+1} | s_t, a_t) — predicts state changes
2. Observation Model: p(o_t | s_t) — maps states to perceptions
3. Reward Predictor: r̂(s_t, a_t) — estimates expected rewards
4. Latent Encoder: compresses observations into compact representations

## DreamerV3 (2025, Nature)
- Recurrent State-Space Model: deterministic (h_t) + stochastic (z_t) states
- Actor/critic trained entirely within imagined trajectories
- Mastery across 150+ diverse tasks with unified configuration
- First to mine diamond in Minecraft from scratch (30M steps ≈ 17 days playtime)
- Composite loss: reconstruction + reward prediction + KL regularization

## Alternative Approaches
- Voyager (2023): LLMs as world models/planners in Minecraft; automatic curriculum, skill library
- LLM-based World Models (2025-2026): fine-tuned Qwen2.5/Llama-3.1 >99% accuracy on ALFWorld; Claude Sonnet 77% with minimal examples

## Planning Methods
1. Forward rollout: simulate sequences, select highest cumulative reward
2. Model Predictive Control: replan at each timestep
3. Tree search: MCTS-style branching futures
4. Latent planning: gradient-based optimization in latent space

## Applications
- Sim-to-real transfer for robotics
- Multi-agent collaborative belief modeling
- Synthetic environment generation (Genie 3)
- Reduced environment interaction costs
