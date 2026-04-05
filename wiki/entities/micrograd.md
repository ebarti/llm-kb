---
title: "micrograd"
type: entity
entity_type: tool
url: "https://github.com/karpathy/micrograd"
sources: ["[[sources/karpathy-educational-projects]]"]
related: ["[[entities/andrej-karpathy]]", "[[entities/nanogpt]]", "[[entities/minbpe]]", "[[concepts/ai-native-education]]"]
tags: [karpathy, autograd, backpropagation, education, open-source]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Karpathy's educational autograd engine: ~100 lines of Python implementing backpropagation over a dynamically built DAG, with a ~50-line neural net library — the most accessible introduction to how deep learning actually works."
---

## Overview

micrograd is a tiny scalar-valued automatic gradient engine written by [[entities/andrej-karpathy]] in approximately 100 lines of Python, with a ~50-line neural network library on top featuring a PyTorch-like API. It implements reverse-mode automatic differentiation (backpropagation) over a dynamically constructed directed acyclic graph (DAG).

## Key Facts

- **Type**: Educational open-source library
- **Author**: [[entities/andrej-karpathy]]
- **Language**: Python (~150 total lines)
- **License**: MIT
- **URL**: https://github.com/karpathy/micrograd

## Design Philosophy

micrograd operates at **scalar-level granularity** — each neuron is decomposed into individual additions and multiplications. This eliminates tensor complexity while maintaining the exact same mathematical principles that power PyTorch. The pedagogical insight is that understanding backpropagation at the scalar level makes the tensor-level version trivially obvious.

## Features

- Reverse-mode automatic differentiation
- Dynamic DAG construction
- PyTorch-like API (`.backward()`, parameter iteration)
- Graphviz visualization of computational graphs
- Binary classification with SVM-style margin loss
- Unit tests verified against PyTorch

## Educational Impact

The accompanying YouTube lecture ("The Spelled-Out Intro to Neural Networks and Backpropagation," 2h25m) is widely considered the best-ever explanation of backpropagation. It serves as the foundation of the Neural Networks: Zero to Hero series, establishing the from-scratch implementation pedagogy that carries through to [[entities/nanogpt]], [[entities/minbpe]], and [[entities/llm-c]].

## Mentioned In

- [[sources/karpathy-educational-projects]] — project catalog
- [[sources/karpathy-wikipedia-biography]] — career context
