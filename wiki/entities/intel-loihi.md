---
title: "Intel Loihi"
type: entity
entity_type: tool
url: "https://www.intel.com/content/www/us/en/research/neuromorphic-computing.html"
related: ["[[concepts/neuromorphic-computing]]", "[[concepts/sparse-coding]]", "[[concepts/brain-inspired-ai]]", "[[entities/ibm-northpole]]"]
tags: [neuromorphic-computing, intel-loihi, spiking-neural-networks, hardware]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Intel's family of neuromorphic processors — from Loihi 1 (2018, 130K neurons, research-only) through Loihi 3 (2025, 8M neurons, first commercial neuromorphic chip), achieving 100-1000x GPU energy efficiency for sensory and robotic AI tasks."
---

## Overview

Intel Loihi is a family of neuromorphic processors that mimic the structure and function of biological neurons using spiking neural networks. The third generation, Loihi 3, unveiled in June 2025, represents the first commercially available Intel neuromorphic chip, marking the transition from research to market.

## Key Facts

- **Type**: tool (neuromorphic processor family)
- **Developer**: Intel Labs
- **Notable for**: First commercial-grade neuromorphic chip family
- **URL**: https://www.intel.com/content/www/us/en/research/neuromorphic-computing.html

## Generations

### Loihi 1 (2018)
- 128 neuromorphic cores, 3 x86 cores
- 130,000 synthetic neurons, 130 million synapses
- 14nm process, 60mm²
- Power: below 1.5W
- 5,000x better energy-delay product vs conventional solutions
- Research-only (end of life)

### Loihi 2
- Intel 4 process node
- 10x faster processing vs Loihi 1
- Hala Point system: 1,152 Loihi 2 processors in data center chassis

### Loihi 3 (2025-2026)
- 8 million digital neurons, 64 billion synapses
- 4nm process
- 1.2 watts peak load
- 100x GPU energy efficiency for specific AI tasks
- First commercially available Intel neuromorphic chip
- Commercial deployment planned for Q3 2026
- Target sectors: healthcare, autonomous vehicles, industrial automation

## Technical Architecture

- **Neuron model**: Leaky integrate-and-fire with dendritic compartments
- **Learning**: On-chip reward-modulated spike-timing-dependent plasticity (STDP)
- **Communication**: Asynchronous event-driven spike communication
- **Temporal features**: Axonal delays, refractory periods
- **Software**: nxSDK framework, Lava open-source framework

## Real-World Applications

- **ANYmal D Neuro**: Quadruped inspection robot, 72 hours on single charge (9x vs GPU)
- **Mercedes-Benz / BMW**: Neuromorphic vision for sub-millisecond autonomous braking
- **Robotics**: Adaptive control, few-shot learning, planning under uncertainty

## Mentioned In

- [[sources/neuromorphic-computing-mainstream-2026]] — commercial deployment in 2026
- [[sources/neuro-inspired-dynamic-sparsity-efficiency]] — neuromorphic hardware for sparse AI

## External References

- Intel Neuromorphic Research: https://www.intel.com/content/www/us/en/research/neuromorphic-computing.html
- Open Neuromorphic: https://open-neuromorphic.org/
