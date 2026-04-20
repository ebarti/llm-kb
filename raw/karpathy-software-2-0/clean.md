---
title: "Software 2.0"
source: "https://karpathy.medium.com/software-2-0-a64152b37c35"
author: "Andrej Karpathy"
date_published: 2017-11-11
date_ingested: 2026-04-05
tags: [software-2.0, neural-networks, ai-programming, paradigm-shift]
type: article
status: raw
discovered_via: search
---

# Software 2.0

Andrej Karpathy proposes that neural networks represent a fundamental shift in software development, not merely another machine learning tool. He contrasts Software 1.0 -- traditional explicit code written in languages like Python and C++ -- with Software 2.0, where programs are defined by neural network weights learned through optimization rather than hand-coded instructions.

## The Paradigm Shift

In Software 1.0, programmers write explicit instructions. In Software 2.0, developers instead specify desired behavior, provide training data, design an architecture, and allow computational processes to discover the weights. As Karpathy explains, the "source code comprises 1) the dataset that defines the desirable behavior and 2) the neural net architecture" that provides the rough skeleton, with training "compiling the dataset into the binary."

This represents a revolutionary change in how teams structure themselves: data labelers become the primary "2.0 programmers," while infrastructure specialists maintain training systems.

## Real-World Examples

Karpathy documents the transition across multiple domains:

- **Visual Recognition**: Evolution from hand-engineered features to ConvNets trained on ImageNet, now progressing toward automated architecture search
- **Speech Recognition**: Displacement of Gaussian mixture models and hidden Markov models with neural approaches
- **Speech Synthesis**: WaveNet systems replacing stitching-based mechanisms
- **Machine Translation**: Neural networks dominating phrase-based statistical methods
- **Games**: AlphaGo Zero surpassing hand-coded Go programs
- **Databases**: Learned index structures outperforming traditional B-Trees

## Key Benefits

Software 2.0 offers distinctive advantages:

- **Computational homogeneity**: Neural networks rely primarily on matrix multiplication and ReLU operations, unlike heterogeneous classical software
- **Silicon-friendly**: Simplified instruction sets enable custom ASICs and neuromorphic chips
- **Predictable performance**: Constant running time and memory usage without dynamic allocation
- **Portability**: Matrix operations run across diverse computational architectures
- **Agility**: Adjusting network capacity through channel modifications enables speed-performance trade-offs
- **Integration**: Separate modules can backpropagate together, enabling system-wide optimization
- **Superiority**: Neural networks exceed human-written code across vision, audio, and speech domains

## Critical Limitations

Karpathy acknowledges significant drawbacks:

- **Interpretability crisis**: Large networks function effectively but remain opaque regarding internal mechanisms
- **Unintuitive failures**: Systems exhibit embarrassing errors, silently adopt training data biases, and remain difficult to analyze
- **Adversarial vulnerabilities**: The existence of adversarial examples highlights fundamental misunderstandings about these systems' properties

## Infrastructure Gaps

Karpathy identifies missing tooling for Software 2.0 development. Traditional IDEs support 1.0 programming through syntax highlighting and debuggers. Software 2.0 requires new infrastructure for dataset curation, visualization, cleaning, labeling, and versioning. He questions: "Who is going to develop the first Software 2.0 IDEs?" He envisions tools that identify mislabeled examples through per-example loss analysis.

Similarly, while GitHub succeeds for code repositories, no equivalent exists for datasets where "commits are made up of additions and edits of the labels." Package managers like pip and conda lack Software 2.0 equivalents for deploying and sharing trained models.

## Future Vision

Karpathy predicts Software 2.0 will dominate "any domain where repeated evaluation is possible and cheap, and where the algorithm itself is difficult to design explicitly." He emphasizes that AGI development will certainly utilize Software 2.0 approaches, suggesting this paradigm represents not a temporary trend but the fundamental future of programming itself.
