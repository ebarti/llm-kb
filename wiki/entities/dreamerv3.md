---
title: "DreamerV3"
type: entity
entity_type: paper
url: "https://danijar.com/project/dreamerv3/"
related: ["[[concepts/world-models]]", "[[concepts/model-based-reinforcement-learning]]", "[[concepts/latent-world-models]]", "[[entities/google-deepmind]]"]
tags: [DreamerV3, world-models, reinforcement-learning, Minecraft, Nature]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "DeepMind's general RL algorithm published in Nature (2025): masters 150+ diverse tasks with a single configuration via learned world model imagination; first to mine a diamond in Minecraft from scratch without human data (30M steps, ~17 days)."
---

## Overview

DreamerV3 is a general reinforcement learning algorithm by Danijar Hafner et al. (Google DeepMind / University of Toronto), published in Nature in April 2025. It learns a [[concepts/world-models]] of the environment and improves behavior by imagining future scenarios within that model. Using a single fixed configuration, DreamerV3 outperforms specialized methods across over 150 diverse tasks.

## Key Facts

- **Type**: paper/algorithm
- **Authors**: Danijar Hafner, Jurgis Pasukonis, Timothy Lillicrap, Jimmy Ba
- **Published**: Nature, April 2025 (arXiv: January 2023)
- **Achievement**: First algorithm to mine a diamond in Minecraft from sparse rewards, without expert demonstrations or curricula
- **Scale**: 30 million environment steps (~17 days of playtime) to first diamond

## Technical Architecture

- **Recurrent State-Space Model (RSSM)**: Combines deterministic (h_t) and stochastic (z_t) states
- **Categorical latents**: Discrete latent representations (vs. Gaussian in earlier Dreamer versions)
- **Symlog predictions**: Normalization technique enabling stable learning across reward scales
- **Actor-critic**: Trained entirely within imagined trajectories — no real environment needed during policy learning
- **Loss**: Composite of reconstruction, reward prediction, and KL regularization

## Key Results

- Mastery across 150+ tasks with single configuration (Atari, DMC, Minecraft, BSuite, Crafter)
- Substantially outperforms PPO and specialized methods
- Favorable scaling properties: larger models improve both performance and data-efficiency
- Minecraft diamond: sequential challenge requiring exploration, navigation, crafting, and combat

## Significance

DreamerV3 validates the [[concepts/model-based-reinforcement-learning]] hypothesis at unprecedented scale: a single general algorithm that learns a world model and plans through imagination can outperform task-specific approaches. It demonstrates that [[concepts/latent-world-models]] enable long-horizon sequential reasoning, establishing the practical case for [[concepts/world-models]] in complex decision-making.

## Mentions

- [[sources/ha-schmidhuber-world-models]] — the foundational work DreamerV3 extends
- [[sources/world-models-race-2026]] — broader world models landscape
