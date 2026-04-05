---
title: "Neural Turing Machine"
type: entity
entity_type: paper
url: "https://arxiv.org/abs/1410.5401"
related: ["[[concepts/memory-augmented-neural-networks]]", "[[concepts/attention-mechanisms]]", "[[entities/retro]]"]
tags: [NTM, neural-turing-machine, memory-augmented, differentiable-memory, DeepMind]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Alex Graves et al. (2014) architecture coupling a neural network controller with external memory via differentiable soft attention — the foundational work connecting attention mechanisms to external memory, enabling networks to learn algorithmic tasks like copy, sort, and associative recall."
---

## Overview

The Neural Turing Machine (NTM), introduced by Alex Graves et al. at Google DeepMind in 2014, is the foundational architecture for [[concepts/memory-augmented-neural-networks]]. It couples an RNN/LSTM controller with an external memory matrix, using soft [[concepts/attention-mechanisms]] for both reading and writing — making all operations differentiable and trainable via backpropagation.

## Key Facts

- **Type**: Paper / architecture
- **URL**: https://arxiv.org/abs/1410.5401
- **Notable for**: First architecture to combine neural networks with differentiable external memory
- **Authors**: Alex Graves, Greg Wayne, Ivo Danihelka (Google DeepMind)
- **Published**: October 2014

## Architecture

The NTM consists of:
1. **Controller**: An LSTM network that processes inputs and decides memory operations
2. **Memory matrix**: An N x M external memory bank (N locations, M-dimensional vectors)
3. **Read heads**: Soft attention over memory locations for content retrieval
4. **Write heads**: Soft attention combined with erase/add vectors for memory modification

### Addressing Mechanisms
- **Content-based**: Cosine similarity between a query vector and each memory location (like attention)
- **Location-based**: Shift operations for sequential memory traversal
- **Combined**: Content addressing followed by location-based refinement

## Demonstrated Capabilities

- Copy: Reproduce input sequences of arbitrary length
- Sort: Order sequences by priority
- Associative recall: Retrieve a value given its associated key
- All learned from examples, with no explicit algorithmic programming

## Historical Significance

The NTM is historically significant because:
1. It introduced differentiable memory access via soft attention — the same mechanism that would later define the Transformer
2. It proved neural networks could learn algorithmic behaviors when given appropriate memory structures
3. It established the research program that led to Differentiable Neural Computers (DNCs) and ultimately informed the design of attention-based architectures

## Implementation Challenges

The NTM proved notoriously difficult to implement in practice:
- Original authors never released code
- First stable open-source implementation arrived in 2018 (winning a best-paper award)
- Common issues: gradient instability (NaN errors), slow convergence, difficulty reproducing results

## Mentioned In

- [[sources/differentiable-neural-computers-deepmind]] — DNCs as NTM extension
- [[concepts/memory-augmented-neural-networks]] — NTM as Generation 1

## External References

- [arXiv Paper](https://arxiv.org/abs/1410.5401)
- [Wikipedia: Neural Turing Machine](https://en.wikipedia.org/wiki/Neural_Turing_machine)
