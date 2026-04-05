---
title: "Agentic Workflow Patterns"
type: concept
sources: ["[[sources/anthropic-building-effective-agents]]", "[[sources/google-ai-agent-protocols]]"]
related: ["[[concepts/augmented-llm]]", "[[concepts/multi-agent-systems]]", "[[concepts/model-context-protocol]]", "[[concepts/tool-use-standards]]"]
last_compiled: 2026-04-05
summary: "Five canonical workflow patterns for AI agents (Anthropic): prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer — plus the distinction between deterministic workflows and dynamic agents."
---

## Overview

Agentic workflow patterns describe how [[concepts/augmented-llm|augmented LLMs]] and tools are organized to accomplish complex tasks. [[entities/anthropic]]'s definitive guide distinguishes two fundamental approaches:

- **Workflows**: LLMs and tools orchestrated through **predefined code paths** — deterministic and predictable
- **Agents**: LLMs that **dynamically direct their own processes** and tool usage — flexible and model-driven

The key recommendation is to start with workflows and only graduate to agents when the added flexibility demonstrably improves outcomes.

## The Five Workflow Patterns

### 1. Prompt Chaining
Decompose a task into sequential steps where each LLM call processes the output of the previous one. Programmatic validation gates between steps catch errors early.

**Best for**: Fixed subtasks requiring accuracy over speed (e.g., generate outline → validate → write full document)

### 2. Routing
Classify inputs and direct them to specialized downstream handlers. Each handler has its own optimized prompt and potentially different model.

**Best for**: Separation of concerns (e.g., customer service triage: general / refund / technical); cost optimization by routing simple queries to smaller models.

### 3. Parallelization
Execute multiple tasks concurrently. Two variations:
- **Sectioning**: Independent subtasks run simultaneously (e.g., one model processes the query while another screens for safety)
- **Voting**: Identical tasks run multiple times for diverse perspectives (e.g., multiple code vulnerability reviews)

**Best for**: Tasks with independent subtasks or where multiple perspectives improve quality.

### 4. Orchestrator-Workers
A central LLM dynamically decomposes tasks and delegates to worker instances, then synthesizes results. Unlike parallelization, subtasks are determined at runtime by the orchestrator rather than predefined.

**Best for**: Complex tasks where subtasks can't be predicted in advance (e.g., multi-file code changes, comprehensive research).

### 5. Evaluator-Optimizer
One LLM generates responses while another provides iterative feedback in a loop. The generator refines its output based on the evaluator's critique.

**Best for**: Tasks with clear evaluation criteria where iterative refinement improves quality (e.g., translation refinement, multi-round search).

## From Workflows to Agents

True autonomous agents operate independently after receiving initial instructions, making decisions across multiple turns. Requirements:
- Capacity for reasoning and planning
- Reliable [[concepts/tool-use-standards|tool usage]]
- Error recovery mechanisms
- Access to ground truth feedback from environmental responses
- Defined stopping conditions (iteration limits, checkpoints, blocker resolution)

**Trade-offs**: Agents are more flexible but have higher costs, potential for cascading errors, and need for sandboxed testing with appropriate guardrails.

## Composable Patterns

The broader industry trend is toward composable agent architectures:
- Modular, specialized sub-agents that plug together
- Output of one agent becomes input for the next
- [[concepts/model-context-protocol]] provides the standardized tool layer
- [[concepts/agent-to-agent-protocol]] enables dynamic inter-agent discovery and delegation

## Sources
- [[sources/anthropic-building-effective-agents]] — canonical five-pattern framework
- [[sources/google-ai-agent-protocols]] — protocol-level support for agent workflows

## Related Concepts
- [[concepts/augmented-llm]] — the building block workflows orchestrate
- [[concepts/multi-agent-systems]] — multi-agent implementations of these patterns
- [[concepts/model-context-protocol]] — the tool access layer agents use
- [[concepts/agent-to-agent-protocol]] — the inter-agent collaboration layer
- [[concepts/tool-use-standards]] — the standards enabling reliable tool usage
