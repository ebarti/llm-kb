---
title: "ReAct Pattern"
type: concept
sources: ["[[sources/react-prompting-framework]]", "[[sources/superannotate-llm-agents-guide]]", "[[sources/ng-agentic-design-patterns]]"]
related: ["[[concepts/llm-agent-architecture]]", "[[concepts/agent-planning]]", "[[concepts/reflection-pattern]]", "[[concepts/tool-use]]", "[[concepts/agentic-workflows]]"]
last_compiled: 2026-04-05
summary: "The Thought-Action-Observation loop that enables LLM agents to interleave reasoning with real-world actions, outperforming both pure reasoning (CoT) and action-only approaches."
---

## Overview

ReAct (Reasoning + Acting) is a foundational prompting framework introduced by Yao et al. (2022) that enables language models to generate both reasoning traces and task-specific actions in an interleaved manner. It is the dominant execution pattern for LLM agents, formalizing the loop that allows an agent to think about what to do, do it, observe the result, and adjust.

The pattern addresses a fundamental tension: pure reasoning approaches like Chain-of-Thought (CoT) can hallucinate facts because they lack access to external information, while pure action approaches (just calling tools) lack strategic planning to decompose complex goals. ReAct combines the strengths of both.

## The ReAct Loop

The cycle repeats until the task is complete:

1. **Thought**: The agent reasons about the current state, what information it needs, and what action to take next. This reasoning trace is explicit and observable.

2. **Action**: Based on its reasoning, the agent selects and invokes a tool — a search query, a database lookup, a code execution, or any available action.

3. **Observation**: The result of the action is returned to the agent as new information, which informs the next thought.

For example, answering "What is the elevation range for the eastern sector of the Colorado orogeny?" might require: (1) Think: I need to search for Colorado orogeny, (2) Act: Search "Colorado orogeny", (3) Observe: results mention sectors, (4) Think: I need the eastern sector specifically, (5) Act: Search "eastern sector Colorado orogeny elevation", (6) Observe: get the answer.

## Advantages Over Alternatives

**vs. Chain-of-Thought**: CoT generates reasoning but cannot access external information, leading to hallucinated facts. ReAct grounds reasoning in real-world data through tool use.

**vs. Action-Only**: Without reasoning traces, agents cannot decompose complex goals or handle exceptions. ReAct provides strategic planning capability.

**vs. Plan-then-Execute**: Static plans cannot adapt to unexpected observations. ReAct's interleaved approach adapts dynamically.

## Performance

- ReAct outperforms action-only methods on knowledge-intensive QA and fact verification
- On decision-making tasks (ALFWorld, WebShop), ReAct significantly outperforms action-only baselines
- **ReAct + Reflexion** achieves near-perfect performance: 130/134 tasks completed
- Hybrid ReAct + CoT + self-consistency yields optimal overall performance

## Implementation

Modern implementations typically use frameworks like LangChain or LangGraph that provide:
- An LLM as the reasoning engine
- A registry of available tools
- An orchestration loop that manages the Thought → Action → Observation cycle
- Termination conditions (max iterations, explicit "I have the answer" signals)

## Relationship to Other Patterns

ReAct is the foundational agent loop. Other patterns build on top of it:
- [[concepts/reflection-pattern]] adds self-critique after the ReAct loop completes
- [[concepts/agent-planning]] adds upfront task decomposition before ReAct execution
- [[concepts/agent-orchestration]] coordinates multiple ReAct agents working in parallel

## Sources

- [[sources/react-prompting-framework]] — original framework description and performance results
- [[sources/superannotate-llm-agents-guide]] — ReAct as a planning component within agent architecture
- [[sources/ng-agentic-design-patterns]] — ReAct within Ng's agentic workflow patterns

## Related Concepts

- [[concepts/llm-agent-architecture]] — ReAct is the core execution loop
- [[concepts/agent-planning]] — planning formulation and reflection
- [[concepts/reflection-pattern]] — extends ReAct with self-critique
- [[concepts/tool-use]] — actions in ReAct invoke tools
- [[concepts/agentic-workflows]] — ReAct is a building block
