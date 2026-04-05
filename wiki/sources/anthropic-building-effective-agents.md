---
title: "Source: Building Effective AI Agents (Anthropic)"
type: source-summary
source: "[[raw/anthropic-building-effective-agents]]"
related: ["[[concepts/agentic-workflow-patterns]]", "[[concepts/tool-use-standards]]", "[[concepts/augmented-llm]]", "[[concepts/multi-agent-systems]]"]
last_compiled: 2026-04-05
summary: "Anthropic's definitive guide to agent design: augmented LLM as basic building block, five workflow patterns (chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer), tool engineering as first-class concern, and simplicity-first philosophy."
---

## Key Points
- The augmented LLM (retrieval + tools + memory) is the basic building block of all agentic systems
- Distinguishes **workflows** (predefined code paths) from **agents** (LLM-directed dynamic processes)
- Five workflow patterns: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer
- Tool engineering deserves "equivalent care to overall prompt engineering" — includes poka-yoke design principles
- Core philosophy: start simple, add complexity only when it demonstrably improves outcomes
- Frameworks (Claude Agent SDK, AWS Strands, etc.) can obscure underlying behavior — start with raw APIs

## Detailed Summary

This Anthropic research article establishes the canonical framework for building AI agents. The foundational concept is the [[concepts/augmented-llm]]: an LLM enhanced with retrieval, [[concepts/tool-use-standards|tool integration]], and memory. Modern models can independently generate search queries, select tools, and manage information retention.

The article draws a critical distinction between **workflows** (deterministic orchestration through predefined code paths) and **agents** (dynamic, model-directed processes). It then details five [[concepts/agentic-workflow-patterns]]: prompt chaining (sequential steps with validation gates), routing (input classification to specialized handlers), parallelization (concurrent execution via sectioning or voting), orchestrator-workers (dynamic task decomposition), and evaluator-optimizer (generation with iterative feedback).

A major contribution is elevating tool engineering to a first-class design concern. Good tool definitions include example usage, clear input formats, distinct boundaries between similar tools, and poka-yoke principles that prevent misuse. The format of tool specifications significantly impacts LLM execution quality.

The overarching philosophy is simplicity: begin with single LLM calls, add multi-step complexity only when simpler approaches fail, and always prefer transparency over abstraction.

## Notable Quotes
> "Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs."

## Related Concepts
- [[concepts/augmented-llm]] — the core building block described
- [[concepts/agentic-workflow-patterns]] — the five patterns catalogued
- [[concepts/tool-use-standards]] — tool engineering as design discipline
- [[concepts/multi-agent-systems]] — orchestrator-workers and evaluator-optimizer patterns
