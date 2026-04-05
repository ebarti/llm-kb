---
title: "Predictive Coding"
type: concept
sources: ["[[sources/free-energy-principle-unified-brain-theory]]", "[[sources/neuroai-catalyzing-next-gen-ai]]"]
related: ["[[concepts/free-energy-principle]]", "[[concepts/active-inference]]", "[[concepts/bayesian-brain]]", "[[concepts/brain-inspired-ai]]", "[[entities/karl-friston]]"]
tags: [predictive-coding, neuroscience, perception, generative-models]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "A theory of brain function where the cortex continuously generates top-down predictions and only processes bottom-up prediction errors — the brain as a hierarchical prediction machine that minimizes surprise."
---

## Overview

Predictive coding is a leading theory of brain function proposing that the cortex operates as a hierarchical prediction machine. Rather than passively processing sensory input bottom-up, the brain continuously generates top-down predictions about incoming signals. Only the prediction errors — the difference between expected and actual input — are propagated upward for further processing. This makes the brain extraordinarily efficient: if you can predict what comes next, you only need to process what's surprising.

## Key Ideas

### The Prediction Hierarchy

The brain's cortical hierarchy operates through reciprocal connections:
- **Top-down (descending)**: Predictions from higher areas about what lower areas should be experiencing
- **Bottom-up (ascending)**: Prediction errors — the mismatch between predictions and actual input
- Each level tries to "explain away" the input from below by improving its predictions

### Mathematical Framework

Under the [[concepts/free-energy-principle]], predictive coding is formalized as gradient descent on variational free energy:
- **Predictions**: Internal model generates expected sensory input
- **Prediction errors**: Difference between expected and actual input, weighted by precision (inverse variance)
- **Precision weighting**: Corresponds to attention — high-precision errors are prioritized
- **Learning**: Hebbian plasticity optimizes model parameters to reduce long-term prediction error

### Connection to AI

Predictive coding has deep connections to modern AI:

| Neuroscience Concept | AI/ML Equivalent |
|---------------------|------------------|
| Prediction error minimization | Loss function minimization |
| Hierarchical predictions | Encoder-decoder architectures |
| Precision weighting | Attention mechanisms |
| Generative model | Variational autoencoder (VAE) |
| Free energy = negative ELBO | VAE training objective |
| Active inference | Model-based RL with world models |

The mathematical identity between variational free energy and the Evidence Lower Bound (ELBO) used in VAEs means that predictive coding and modern generative AI share the same mathematical foundation.

### Beyond Perception

Predictive coding extends beyond sensory perception to:
- **Motor control**: Descending motor predictions as "proprioceptive predictions" that the body fulfills
- **Attention**: Precision weighting determines which prediction errors get amplified
- **Learning**: Long-term prediction error minimization through synaptic plasticity
- **Emotion**: Interoceptive prediction errors about bodily states
- **Psychopathology**: Aberrant precision weighting may explain hallucinations (overly confident predictions) and delusions

## How It Connects

Predictive coding is the process theory instantiating the [[concepts/free-energy-principle]]. It extends into [[concepts/active-inference]] (prediction through action), connects to [[concepts/bayesian-brain]] (inference under uncertainty), and provides a theoretical foundation for [[concepts/brain-inspired-ai]] systems that process only surprises rather than full inputs. The efficiency principle directly parallels [[concepts/sparse-coding]] — both reduce the amount of information the brain needs to process.

## Open Questions

- Does the brain literally implement predictive coding, or is it a useful approximation?
- How does predictive coding handle the chicken-and-egg problem (predictions require a learned model)?
- Can predictive coding scale to explain all of cognition, including abstract thought and language?
- How should AI systems implement the precision-weighting / attention-like aspects?

## Sources

- [[sources/free-energy-principle-unified-brain-theory]] — the mathematical framework
- [[sources/neuroai-catalyzing-next-gen-ai]] — predictive coding as a NeuroAI research priority
