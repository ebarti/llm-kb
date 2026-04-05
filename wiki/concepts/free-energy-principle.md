---
title: "Free Energy Principle"
type: concept
sources: ["[[sources/free-energy-principle-unified-brain-theory]]"]
related: ["[[concepts/predictive-coding]]", "[[concepts/active-inference]]", "[[concepts/bayesian-brain]]", "[[entities/karl-friston]]", "[[concepts/brain-inspired-ai]]"]
tags: [free-energy-principle, bayesian-brain, neuroscience, generative-models]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Karl Friston's mathematical framework proposing that all adaptive systems minimize variational free energy — an upper bound on surprise — unifying perception, action, learning, and attention under one principle with direct links to VAEs and generative AI."
---

## Overview

The Free Energy Principle (FEP) is the most ambitious attempt at a unified theory of brain function. Proposed by [[entities/karl-friston]], it states that all adaptive biological systems — from single cells to brains — minimize variational free energy, an information-theoretic quantity that upper-bounds surprise (negative log evidence). In plain language: living systems maintain themselves by building internal models of the world and acting to confirm their predictions.

## Key Ideas

### The Mathematical Core

Variational free energy (F) decomposes into:
- **Accuracy**: How well the model predicts observations
- **Complexity**: How much the model diverges from prior expectations
- Minimizing F means finding the simplest model that best explains observations

The crucial mathematical identity: **negative free energy equals the Evidence Lower Bound (ELBO)** — the same objective used to train variational autoencoders in modern AI. This is not analogy; it is the same mathematics.

### Markov Blankets

The FEP uses the concept of a Markov blanket to partition any system into:
- **Internal states**: The system's model of the world
- **External states**: The actual world
- **Sensory states**: Information flowing in
- **Active states**: Information flowing out (actions)

Any system that persists must minimize free energy with respect to its Markov blanket.

### Key Terminology

| Term | Meaning |
|------|---------|
| Surprisal | Negative log probability of observations |
| Precision | Inverse variance; encodes confidence in predictions |
| Generalized coordinates | Position + velocity + acceleration of states |
| Complexity | KL divergence between posterior and prior |

### What the FEP Unifies

The FEP subsumes multiple theories:
- **Perception**: [[concepts/predictive-coding]] — minimizing prediction errors
- **Action**: [[concepts/active-inference]] — changing the world to match predictions
- **Learning**: Long-term free energy minimization = Hebbian plasticity
- **Attention**: Precision weighting = optimizing the gain on prediction errors
- **Curiosity**: Epistemic foraging = reducing expected free energy about uncertain states

### Criticisms

1. The FEP itself is unfalsifiable — it's a mathematical principle (like the principle of least action in physics), not an empirical claim
2. Only specific process theories (like predictive coding) that implement the FEP can be tested
3. Critics argue it risks being vacuously true — any persisting system trivially "minimizes free energy"
4. The ergodicity assumption may oversimplify living systems
5. Some argue it obscures the distinctive features of biological self-organization

## How It Connects

The FEP provides the theoretical umbrella for [[concepts/predictive-coding]] (perception), [[concepts/active-inference]] (action), and the [[concepts/bayesian-brain]] hypothesis. Its mathematical equivalence with the ELBO creates a direct bridge to modern generative AI, making it the most important theoretical link between neuroscience and AI. It connects to [[concepts/brain-inspired-ai]] as a guiding theoretical framework and to [[concepts/neuroai]] as a key research direction.

## Open Questions

- Is the FEP truly a theory of everything biological, or is it too general to be useful?
- Can FEP-based AI systems compete with conventional deep learning at scale?
- Does the FEP have implications for [[concepts/ai-consciousness]]?
- How does the FEP relate to other unifying theories (integrated information theory, global workspace theory)?

## Sources

- [[sources/free-energy-principle-unified-brain-theory]] — comprehensive overview of the principle
