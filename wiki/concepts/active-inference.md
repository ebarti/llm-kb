---
title: "Active Inference"
type: concept
sources: ["[[sources/free-energy-principle-unified-brain-theory]]"]
related: ["[[concepts/free-energy-principle]]", "[[concepts/predictive-coding]]", "[[concepts/bayesian-brain]]", "[[entities/karl-friston]]", "[[concepts/brain-inspired-ai]]"]
tags: [active-inference, free-energy-principle, embodied-ai, neuroscience]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "An extension of the free energy principle to action: organisms minimize surprise not only by updating internal models (perception) but by actively changing the world to match their predictions — with implications for robotics and embodied AI."
---

## Overview

Active inference is the action-oriented extension of the [[concepts/free-energy-principle]]. While [[concepts/predictive-coding]] explains how organisms minimize surprise through perception (updating internal models to match sensory input), active inference explains how organisms minimize surprise through action (changing the world to match their predictions). Together, they provide a unified account of perception, action, and learning.

## Key Ideas

### Two Pathways to Minimize Free Energy

1. **Perceptual inference**: Update internal model to better explain sensory input (the brain changes its mind)
2. **Active inference**: Change the environment through action so that sensory input matches predictions (the organism changes the world)

Example: If you predict it will be warm but feel cold, you can either (1) update your prediction (perceptual inference) or (2) put on a jacket (active inference). Biological organisms do both.

### Difference from Standard RL

| Dimension | Standard RL | Active Inference |
|-----------|-------------|-----------------|
| Objective | Maximize cumulative reward | Minimize expected free energy |
| Planning | Cost function over future states | Priors over preferred trajectories |
| Exploration | Epsilon-greedy, UCB | Epistemic foraging (reduce uncertainty) |
| Reward | Externally specified | Emerges from prior preferences |
| World model | Optional (model-free RL exists) | Required (inherently model-based) |

### Epistemic Actions

Active inference naturally accounts for curiosity and exploration. An agent seeks not just preferred outcomes but also information-gaining actions that reduce uncertainty about the world. This "epistemic foraging" emerges from the mathematics without requiring additional mechanisms — unlike RL, where exploration must be engineered separately.

### Applications in AI

- **Robotics**: Robots that plan actions to confirm predictions about their environment
- **Autonomous navigation**: Agents that balance goal-seeking with information-gathering
- **Adaptive systems**: AI that self-regulates by maintaining preferred internal states
- **Dialogue systems**: Agents that ask questions to reduce uncertainty (epistemic actions in language)

### Connection to World Models

Active inference is inherently model-based — the agent must have an internal generative model of how the world works and how actions affect observations. This connects to the "world model" paradigm in AI (Dreamer, IRIS, etc.), where agents learn environment models for planning.

## How It Connects

Active inference extends [[concepts/predictive-coding]] from perception to action, operationalizing the [[concepts/free-energy-principle]] for embodied agents. It connects to [[concepts/brain-inspired-ai]] as a theoretical framework for autonomous systems and to [[concepts/neuroai]] as a bridge between motor neuroscience and robotics AI. Its emphasis on embodiment and sensorimotor interaction addresses one of the key gaps identified in the NeuroAI research agenda.

## Open Questions

- Can active inference scale to the complexity of real-world robotics tasks?
- How does active inference compare to model-based RL in practice (not just theory)?
- Is active inference computationally tractable for high-dimensional action spaces?
- Could LLMs be understood as performing a form of active inference in language space?

## Sources

- [[sources/free-energy-principle-unified-brain-theory]] — the theoretical framework
