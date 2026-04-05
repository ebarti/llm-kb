---
title: "Source: Differentiable Neural Computers (DeepMind)"
type: source-summary
source: "[[raw/differentiable-neural-computers-deepmind]]"
related: ["[[concepts/memory-augmented-neural-networks]]", "[[entities/neural-turing-machine]]", "[[concepts/attention-mechanisms]]"]
tags: [DNC, neural-turing-machine, memory-augmented, differentiable-memory, DeepMind]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "DeepMind's overview of Differentiable Neural Computers: neural network controllers coupled to external read/write memory via differentiable attention, extending Neural Turing Machines with temporal linking and dynamic allocation — capable of learning graph navigation, multi-step reasoning, and algorithmic tasks."
---

## Key Points

- DNCs combine neural networks (pattern matching) with addressable memory (data storage)
- Extend Neural Turing Machines (2014) with temporal linking and dynamic memory allocation
- Memory operations (read, write, free) are fully differentiable via soft attention
- Content-based addressing finds similar memories; temporal linking enables sequential traversal
- Learns to use memory entirely from examples — no explicit programming of memory strategies
- Demonstrated: graph navigation (London Underground), multi-step logical reasoning (family relations), reinforcement learning (block puzzles)
- NTMs can infer simple algorithms (copying, sorting, associative recall) from examples

## Detailed Summary

Alex Graves and colleagues at DeepMind introduced the Differentiable Neural Computer as an extension of their earlier Neural Turing Machine work. The core architecture has a **neural network controller** (analogous to a CPU) coupled to an **external memory matrix** (analogous to RAM) through differentiable read and write operations.

The controller never accesses memory through hard addresses. Instead, all memory operations use **soft attention**: write operations distribute information across locations weighted by an attention vector, and read operations aggregate information from multiple locations using a similar attention-weighted mechanism. Because everything is differentiable, the entire system trains end-to-end via backpropagation.

The DNC adds three capabilities beyond the original NTM:
1. **Temporal links**: Record the order in which memory locations were written, enabling sequential traversal (forward and backward) through stored information
2. **Dynamic memory allocation**: Free and reallocate memory locations as needed, preventing memory exhaustion
3. **Content-based + temporal addressing**: Navigate memory either by similarity (like attention) or by sequential order (like a linked list)

The demonstrations are compelling: a DNC trained on London Underground graph data learned to find routes between stations without ever being explicitly programmed with graph search algorithms. In family reasoning tasks, it correctly inferred "Freya's maternal great uncle" from elementary parent-child relationships, demonstrating multi-step compositional reasoning.

## Concepts Introduced or Discussed

- [[concepts/memory-augmented-neural-networks]] — the architecture family
- [[concepts/attention-mechanisms]] — attention as the interface between controller and memory
- [[concepts/knowledge-storage-in-transformers]] — contrasting parametric storage with external memory

## Metadata

- **Author**: DeepMind (Alex Graves et al.)
- **Date Published**: 2016-10-12
- **Format**: blog post
- **URL**: https://deepmind.google/blog/differentiable-neural-computers/
