---
title: "Building Effective AI Agents"
source: "https://www.anthropic.com/research/building-effective-agents"
author: "Anthropic"
date_published: 2024-12-01
date_ingested: 2026-04-05
tags: [agents, tool-use, workflows, patterns, augmented-llm, anthropic]
type: article
status: raw
discovered_via: search
---

# Building Effective AI Agents: A Comprehensive Guide

## Core Philosophy

Anthropic's approach prioritizes simplicity over complexity. The most successful agent implementations use "simple, composable patterns" rather than elaborate frameworks. The fundamental principle: only add complexity when it demonstrably improves outcomes.

## Foundational Architecture

### The Augmented LLM
The basic building block combines an LLM with:
- **Retrieval capabilities** for accessing external information
- **Tool integration** for external system interaction
- **Memory systems** for information retention

Modern models can independently generate search queries, select appropriate tools, and determine what information to preserve. Implementations should prioritize clear, well-documented interfaces tailored to specific use cases.

## Pattern Classifications

Anthropic distinguishes between two structural approaches:

**Workflows**: Systems where "LLMs and tools are orchestrated through predefined code paths" — deterministic and predictable.

**Agents**: Systems where "LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks" — flexible and model-driven.

## Workflow Patterns

### Prompt Chaining
Decompose tasks into sequential steps where each LLM call processes previous output. Add programmatic validation gates between steps. Ideal for fixed subtasks requiring accuracy over speed.

### Routing
Classify inputs and direct them to specialized downstream handlers. Enables separation of concerns and prompt optimization for distinct categories.

### Parallelization
Two implementation variations:
- **Sectioning**: Independent subtasks execute simultaneously.
- **Voting**: Identical tasks run multiple times for diverse perspectives.

### Orchestrator-Workers
A central LLM dynamically decomposes tasks and delegates to worker instances, synthesizing results. Unlike parallelization, subtasks aren't pre-defined but determined by the orchestrator based on input specifics.

### Evaluator-Optimizer
One LLM generates responses while another provides iterative feedback. Most effective with clear evaluation criteria where refinement demonstrably improves quality.

## Autonomous Agents

True agents operate independently after receiving initial instructions, making decisions across multiple turns. They require:
- Capacity for reasoning and planning
- Reliable tool usage
- Error recovery mechanisms
- Access to "ground truth" feedback from environmental responses
- Defined stopping conditions (iteration limits, checkpoint reviews, blocker resolution)

## Framework Guidance

While frameworks like the Claude Agent SDK, AWS Strands, Rivet, and Vellum simplify implementation, they introduce abstraction layers that can obscure underlying prompts and responses. Recommendation: "start by using LLM APIs directly: many patterns can be implemented in a few lines of code."

## Tool Engineering (Agent-Computer Interface)

Tool design deserves equivalent care to overall prompt engineering.

**Format principles**:
- Provide sufficient token space for reasoning before execution
- Maintain formats naturally occurring in internet text
- Minimize formatting overhead (avoid line counting, complex escaping)

**Good tool definition practices**:
- Include example usage and edge cases
- Clearly define input format requirements
- Establish distinct boundaries between similar tools
- Apply poka-yoke principles (design preventing mistakes)

## Three Core Implementation Principles

1. **Simplicity**: Maintain straightforward agent design
2. **Transparency**: Explicitly display agent planning steps
3. **Documentation and Testing**: Rigorously craft tool specifications

## Success Strategy

Begin with optimized single LLM calls enhanced by retrieval and contextual examples. Progress to multi-step agentic systems only when simpler approaches prove insufficient. The ultimate insight: "Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs."
