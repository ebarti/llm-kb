---
title: "Bayesian Brain"
type: concept
sources: ["[[sources/free-energy-principle-unified-brain-theory]]"]
related: ["[[concepts/free-energy-principle]]", "[[concepts/predictive-coding]]", "[[concepts/active-inference]]", "[[entities/karl-friston]]", "[[concepts/brain-inspired-ai]]"]
tags: [bayesian-brain, neuroscience, probabilistic-inference, perception]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The hypothesis that the brain represents and processes information as probability distributions, performing approximate Bayesian inference to combine prior beliefs with sensory evidence — the theoretical foundation for predictive coding and the free energy principle."
---

## Overview

The Bayesian brain hypothesis proposes that the brain represents information as probability distributions and processes it through approximate Bayesian inference. Rather than processing raw sensory data directly, the brain combines prior beliefs (expectations based on experience) with incoming evidence (sensory input) to form posterior beliefs (perceptions). This framework, rooted in Helmholtz's 19th-century "unconscious inference," has become one of the dominant theories in computational neuroscience and a key bridge to AI.

## Key Ideas

### Bayesian Inference in the Brain

At its core: **Posterior ∝ Likelihood × Prior**
- **Prior**: What the brain expects based on experience and context
- **Likelihood**: How well the sensory input matches each possible state of the world
- **Posterior**: The brain's updated belief about the world — perception

The brain does not compute exact Bayesian inference (computationally intractable for high-dimensional spaces) but uses efficient approximations, potentially through [[concepts/predictive-coding]] as proposed under the [[concepts/free-energy-principle]].

### Evidence from Neuroscience

- **Perceptual illusions**: Priors override sensory evidence (e.g., the hollow face illusion)
- **Multisensory integration**: Cues combined according to Bayesian reliability weighting
- **Motor learning**: Movement adaptation follows Bayesian optimal estimation
- **Decision making**: Choices incorporate prior probabilities in ways predicted by Bayes' theorem
- **Attention**: Precision weighting (inverse variance) maps to Bayesian confidence

### Connection to AI

The Bayesian brain provides theoretical grounding for several AI techniques:

| Brain Concept | AI Implementation |
|---------------|-------------------|
| Prior beliefs | Prior distributions in Bayesian neural networks |
| Posterior inference | Variational inference, MCMC sampling |
| Precision weighting | Attention mechanisms, confidence calibration |
| Bayesian updating | Online learning, continual learning |
| Generative models | VAEs, diffusion models, GANs |
| ELBO (= negative free energy) | VAE training objective |

## How It Connects

The Bayesian brain is the theoretical foundation for [[concepts/predictive-coding]] (perception as Bayesian inference), the [[concepts/free-energy-principle]] (minimizing surprise = maximizing Bayesian evidence), and [[concepts/active-inference]] (acting to confirm predictions). It connects to [[concepts/brain-inspired-ai]] as one of the most mathematically rigorous bridges between neuroscience and AI, and to [[concepts/neuroai]] as a core research direction.

## Open Questions

- Does the brain literally compute Bayesian probabilities, or is this a useful metaphor?
- What specific neural mechanisms implement approximate Bayesian inference?
- How are priors learned and represented in neural circuits?
- Can Bayesian AI systems match deep learning's practical performance?

## Sources

- [[sources/free-energy-principle-unified-brain-theory]] — Bayesian brain as the foundation of the FEP
