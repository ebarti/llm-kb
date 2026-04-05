---
title: "A Recipe for Training Neural Networks — Andrej Karpathy"
source: "https://karpathy.github.io/2019/04/25/recipe/"
author: "Andrej Karpathy"
date_published: 2019-04-25
date_ingested: 2026-04-05
tags: [karpathy, training, neural-networks, best-practices, deep-learning]
type: article
status: raw
discovered_via: search
---

# A Recipe for Training Neural Networks

Published April 25, 2019 on Karpathy's blog.

## Core Principles

**Neural nets as leaky abstractions**: Unlike plug-and-play libraries, neural networks require deep understanding. Batch normalization, RNNs, and RL don't work magically.

**Silent failures**: "Neural net training fails silently" — syntactically correct code may produce degraded performance without exceptions.

## The Six-Stage Recipe

### Stage 1: Become One with the Data
Spend extensive time examining thousands of examples. Understand distributions, identify patterns, duplicates, corrupted entries. Look for imbalances, biases, spurious variations. Visualize outliers — they "almost always uncover some bugs in data quality."

### Stage 2: Establish Infrastructure
Create a complete training/evaluation pipeline using simple models (linear classifiers, tiny ConvNets):
- Fixed random seeds for reproducibility
- Disabled data augmentation initially
- Loss verification at initialization
- Proper final layer initialization
- Human baseline comparisons
- Batch overfitting tests
- Input visualization before the network

### Stage 3: Overfit
Build model capacity to achieve low training loss. Key advice: "Don't be a hero" — copy architectures from related papers rather than inventing novel designs. Use Adam optimizer at learning rate 3e-4 initially. Add complexity one component at a time.

### Stage 4: Regularize
Improve validation performance through:
- Collecting more real data (primary method)
- Data augmentation
- Pretraining
- Reducing input dimensionality
- Decreasing model size
- Batch size reduction
- Dropout and weight decay
- Early stopping

### Stage 5: Tune
Use random search over grid search for hyperparameters. Neural networks show varying sensitivity to different parameters.

### Stage 6: Squeeze Performance
Apply ensembles and extended training periods — networks often improve longer than expected.

## Key Takeaway
"Patience and attention to detail" correlate most strongly with deep learning success. Systematic, hypothesis-driven approach prevents accumulating unverified complexity.
