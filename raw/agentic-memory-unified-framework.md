---
title: "Agentic Memory: Unified Long-Term and Short-Term Memory Management for LLM Agents"
source: "https://arxiv.org/abs/2601.01885"
author: "Various"
date_published: 2026-01-03
date_ingested: 2026-04-05
tags: [agent-memory, long-term-memory, short-term-memory, reinforcement-learning]
type: paper
status: raw
discovered_via: search
---

# Agentic Memory (AgeMem): Unified Memory Management for LLM Agents

## Abstract

LLM agents struggle with long-horizon reasoning due to context window limitations. This paper proposes integrating long-term and short-term memory management directly into agent policy through tool-based actions that enable autonomous decision-making about storing, retrieving, updating, summarizing, or discarding information.

## Key Contributions

1. **Unified Framework (AgeMem)**: Single system managing both LTM and STM as integrated agent actions, eliminating need for separate heuristic-based controllers
2. **Progressive Training Strategy**: Three-stage reinforcement learning for sparse and discontinuous reward signals from memory operations
3. **Novel Optimization Method**: Step-wise GRPO algorithm for memory operation training challenges
4. **Empirical Validation**: Testing across five long-horizon benchmarks shows consistent improvements over memory-augmented baselines

## Core Innovation

Memory operations exposed as callable tools within the agent's action space. The LLM autonomously determines what information to preserve and when to perform memory operations — shifting from fixed heuristics to learned, adaptive behavior optimized through reinforcement learning.

## Memory Types

### Short-Term Memory (STM)
Working memory holding information relevant to current context. Analogous to human conscious thoughts or computer RAM. Maintains conversation flow, tracks immediate task goals, stores intermediate results.

### Long-Term Memory (LTM)
Persists across conversations. Allows agents to learn from feedback and adapt to user preferences over time.

## The Memory Challenge
LLMs are stateless at their core — the model doesn't retain information between API calls. Products like ChatGPT and Claude layer memory systems on top. When building custom agents, developers must implement memory layers themselves.
