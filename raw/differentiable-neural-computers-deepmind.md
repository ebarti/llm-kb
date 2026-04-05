---
title: "Differentiable Neural Computers"
source: "https://deepmind.google/blog/differentiable-neural-computers/"
author: "DeepMind (Alex Graves et al.)"
date_published: 2016-10-12
date_ingested: 2026-04-05
tags: [DNC, neural-turing-machine, memory-augmented, differentiable-memory, DeepMind]
type: article
status: raw
discovered_via: search
---

# Differentiable Neural Computers

## Core Architecture

Differentiable Neural Computers (DNCs) combine neural networks with memory systems to enable machines that "learn from examples like neural networks, but also store complex data like computers." The system centers on a neural network controller analogous to a computer processor.

## Relationship to Neural Turing Machines

DNCs extend Neural Turing Machines (NTMs), introduced by Alex Graves in 2014. NTMs combine fuzzy pattern matching with algorithmic programmability through a neural network controller coupled to external memory via attentional mechanisms. All memory interactions are differentiable end-to-end.

NTMs can infer simple algorithms such as copying, sorting, and associative recall from examples alone. DNCs add memory attention mechanisms controlling where memory is stored, temporal attention recording event order, and dynamic memory allocation.

## Memory System

The DNC memory consists of addressable locations, each storing information vectors.

**Write Operations:**
- Store new information at unused locations
- Update existing locations by overwriting
- Free unused memory locations for reallocation
- Create temporal links recording storage sequence

**Read Operations:**
- Content-based searches across memory locations
- Associative temporal link following (forward and backward)
- Sequential and reverse-order information recall

## Temporal Linking

The system maintains "links of association, which represent the order in which information was stored," enabling sequential memory traversal. Memory can be navigated through content similarity or temporal associations.

## Learning Mechanism

DNCs learn how to use memory and produce answers completely from scratch through optimization — comparing produced outputs against desired answers and iteratively improving. No explicit programming of memory use is required.

## Demonstrated Capabilities

1. **Structured Data Management**: Learn arbitrary graph representations and answer complex queries (London Underground navigation)
2. **Logical Reasoning**: Multi-step deduction (e.g., determining family relationships from parent/child data)
3. **Reinforcement Learning**: Execute learned subroutines stored in memory for block-puzzle tasks
4. **Generalization**: Solve novel problems beyond training examples using learned memory organization

## Implementation Challenges

The original NTM authors never released source code. First stable open-source implementation arrived in 2018. Other implementations faced gradient instability (NaN errors), slow convergence, or undocumented training speed issues.
