---
title: "Source: World Models (Ha & Schmidhuber, 2018)"
type: source-summary
source: "[[raw/ha-schmidhuber-world-models-2018]]"
related: ["[[concepts/world-models]]", "[[concepts/latent-world-models]]", "[[entities/david-ha]]", "[[entities/jurgen-schmidhuber]]"]
tags: [world-models, VAE, MDN-RNN, reinforcement-learning, foundational-paper]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The foundational 2018 paper: VAE + MDN-RNN + minimal controller architecture enabling agents to learn world representations and train policies 'inside a dream'; solved CarRacing-v0 with only 867 controller parameters."
---

## Key Points

- Three-component architecture: V (VAE for vision), M (MDN-RNN for memory), C (linear controller)
- Controller uses only 867 parameters (CarRacing) — proves rich world models enable trivially simple policies
- CarRacing-v0 solved at 906 ± 21 (previous best 838; deep RL baselines 343-652)
- "Learning inside a dream": agents trained entirely in MDN-RNN generated environments, then transferred to real environments
- Temperature parameter τ controls dream stochasticity; higher τ (~1.15) prevents adversarial policy exploitation
- Revitalized the world models research program, inspiring Dreamer series, MuZero, JEPA, and modern foundation world models

## Detailed Summary

Ha and Schmidhuber's 2018 paper demonstrated that agents can develop effective policies by first learning a compressed world representation, then training a minimal controller within that learned model. The VAE compresses 64x64 RGB frames into 32-64 dimensional latent vectors. The MDN-RNN (LSTM + Mixture Density Network) learns transition dynamics in latent space as a mixture of Gaussians.

The most striking finding is the extreme simplicity of the controller — a single linear layer with under 1,000 parameters, optimized via CMA-ES evolutionary strategy. This proves that if the world model is rich enough, the decision-making layer can be trivially small.

The "learning inside a dream" experiments showed agents could be trained entirely within the MDN-RNN's hallucinated environments and transfer to the real environment. However, agents sometimes discovered "adversarial policies" — exploiting imperfections in the learned model. Increasing the temperature parameter to generate more uncertain/stochastic dreams prevented this exploitation and improved real-world transfer.

This paper established the modern research program for [[concepts/world-models]] and directly inspired [[entities/dreamerv3]], [[concepts/jepa]], and the current wave of foundation world models.

## Concepts Introduced or Discussed

- [[concepts/world-models]] — the core concept
- [[concepts/latent-world-models]] — compressing observations into latent spaces for prediction
- [[concepts/model-based-reinforcement-learning]] — learning environment dynamics for planning

## Metadata

- **Author**: David Ha, Jürgen Schmidhuber
- **Date Published**: 2018-03-01
- **Format**: paper (NeurIPS 2018)
- **URL**: https://worldmodels.github.io/
