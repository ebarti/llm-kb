---
title: "LLM Agent Architecture"
type: concept
sources: ["[[sources/superannotate-llm-agents-guide]]", "[[sources/martinfowler-function-calling-llm]]", "[[sources/databricks-agent-design-patterns]]", "[[sources/ng-agentic-design-patterns]]"]
related: ["[[concepts/agent-memory]]", "[[concepts/agent-planning]]", "[[concepts/tool-use]]", "[[concepts/react-pattern]]", "[[concepts/agentic-workflows]]", "[[concepts/agent-orchestration]]"]
last_compiled: 2026-04-05
summary: "The four-component architecture of LLM agents (brain, memory, planning, tools) and the design pattern spectrum from simple LLM+prompt to multi-agent systems."
---

## Overview

An LLM agent is an AI system that combines a language model with memory, planning, and tool-use capabilities to autonomously perform complex, multi-step tasks. Unlike basic LLMs that respond to single prompts, or RAG systems that retrieve and generate, agents can decompose problems, execute actions in the real world, observe results, and adapt their approach dynamically.

The term "agent" in this context means an AI system with agency — the ability to take actions that affect its environment, rather than merely generating text. This distinction is fundamental: an agent does things, while a chatbot says things.

## The Four-Component Architecture

The consensus architecture across sources identifies four core components:

### 1. Brain (The LLM Foundation)

The language model serves as the reasoning engine. It processes natural language inputs, maintains conversational context through its prompt, and generates structured outputs (reasoning traces, action decisions, tool calls). The brain is configured through system prompts that establish the agent's role, constraints, and available capabilities.

Different models bring different strengths: Claude excels at agentic coding and tool use, GPT-4 at broad reasoning, and smaller models can be effective within well-designed [[concepts/agentic-workflows]] (as [[entities/andrew-ng]] demonstrated — GPT-3.5 with agentic architecture outperforms GPT-4 zero-shot).

### 2. Memory

[[concepts/agent-memory]] provides contextual continuity. Short-term memory holds the current conversation and intermediate reasoning steps. Long-term memory persists across sessions, enabling the agent to learn preferences, recall past interactions, and build accumulated knowledge. The AgeMem framework (2026) unifies both as tool-based actions the agent can invoke autonomously.

### 3. Planning

[[concepts/agent-planning]] enables the agent to decompose complex goals into executable steps. This operates at two levels: formulation (breaking objectives into subtasks via Chain of Thought, Tree of Thought, or task decomposition) and reflection (evaluating and improving plans via [[concepts/react-pattern]], [[concepts/reflection-pattern]], or Reflexion).

### 4. Tool Use

[[concepts/tool-use]] extends the agent beyond text generation into real-world action. Through function calling and the [[concepts/model-context-protocol]], agents can invoke APIs, query databases, execute code, browse the web, and interact with external systems. This is what transforms an LLM from a language processor into an autonomous actor.

## Design Pattern Spectrum

Databricks identifies a useful spectrum of increasing complexity:

| Pattern | Complexity | Best For |
|---------|-----------|----------|
| LLM + Prompt | Minimal | Generic Q&A, prototyping |
| Deterministic Chain | Low | Well-defined, auditable workflows |
| Single Agent | Medium | Dynamic single-domain tasks (often optimal for enterprise) |
| Multi-Agent System | High | Cross-functional domains, many specialized tools |

The key insight is to start with the simplest pattern that meets requirements. Single-agent systems are often the sweet spot for enterprise: complex enough for dynamic decision-making but without multi-agent orchestration overhead.

## The Agent Loop

At runtime, most agents follow a variation of this loop:

1. **Receive** input (user message, trigger event, or observation from previous action)
2. **Reason** about what to do next (the LLM generates a plan or selects an action)
3. **Act** by invoking a tool, generating output, or requesting more information
4. **Observe** the result of the action
5. **Repeat** or **terminate** based on whether the goal is achieved

This loop — formalized as [[concepts/react-pattern]] (Thought → Action → Observation) — is the fundamental execution pattern for autonomous agents.

## Challenges

Key operational challenges facing LLM agents in 2025-2026:

- **Context window limits**: Constrains how much information the agent can reason over simultaneously
- **Planning horizon**: Difficulty maintaining coherent multi-step plans over many actions
- **Output reliability**: Natural language outputs can be inconsistent, requiring structured output formats
- **Cost and latency**: Multi-step reasoning with tool calls incurs significant API costs and time
- **Security**: Prompt injection, unauthorized actions, and data exfiltration risks require layered defenses
- **Evaluation**: Measuring agent quality is harder than measuring single-turn LLM quality (see [[concepts/swe-bench]])

## Sources

- [[sources/superannotate-llm-agents-guide]] — defines the four-component model with detailed capabilities and challenges
- [[sources/martinfowler-function-calling-llm]] — practical agent scaffold architecture and security considerations
- [[sources/databricks-agent-design-patterns]] — design pattern spectrum from simple to multi-agent
- [[sources/ng-agentic-design-patterns]] — four design patterns and architecture-over-model-size insight

## Related Concepts

- [[concepts/agent-memory]] — memory component deep-dive
- [[concepts/agent-planning]] — planning component deep-dive
- [[concepts/tool-use]] — tool use component deep-dive
- [[concepts/react-pattern]] — the foundational agent execution loop
- [[concepts/agentic-workflows]] — the broader paradigm
- [[concepts/agent-orchestration]] — multi-agent coordination patterns
