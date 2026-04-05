---
title: "Agent Frameworks"
type: concept
sources: ["[[sources/pebblous-agentic-framework-explosion]]", "[[sources/superannotate-llm-agents-guide]]", "[[sources/databricks-agent-design-patterns]]"]
related: ["[[concepts/llm-agent-architecture]]", "[[concepts/agent-orchestration]]", "[[concepts/model-context-protocol]]", "[[concepts/agentic-workflows]]"]
last_compiled: 2026-04-05
summary: "The landscape of LLM agent development frameworks: LangChain/LangGraph, AutoGen, CrewAI, and 2025 newcomers (agent-lightning, hermes-agent, superpowers), consolidating around distinct use cases."
---

## Overview

Agent frameworks provide the scaffolding for building [[concepts/llm-agent-architecture]]-based applications: managing the [[concepts/react-pattern]] execution loop, [[concepts/tool-use]] integration, [[concepts/agent-memory]] persistence, and [[concepts/agent-orchestration]] for multi-agent systems. The landscape has evolved rapidly from experimental libraries (2023) through a Cambrian explosion of options (2024) to consolidation around distinct use-case segments (2025-2026).

## Major Frameworks (2025-2026)

### LangChain / LangGraph
The most widely adopted ecosystem. LangChain provides the foundational primitives (chains, prompts, memory), while LangGraph adds stateful, multi-step workflow orchestration through a graph-based architecture. LangGraph won the stateful, multi-step workflow segment. However, 45% of developers who experimented with LangChain never deployed to production, and 23% eventually removed it.

### AutoGen (Microsoft)
Enables flexible multi-agent conversations. Agents can be configured with different LLMs, tools, and communication patterns. Strong for research and complex multi-agent coordination.

### CrewAI
Task-oriented multi-agent orchestration with a focus on role-based collaboration. Agents are defined with roles, goals, and backstories, creating natural team dynamics.

### OpenAI Agents SDK (March 2025)
The "native SDK" counter-movement — built directly into OpenAI's platform. Represents a shift toward simpler, framework-less agent development using the model provider's own tools.

### LlamaIndex Workflows
Event-driven agent execution where each step emits events triggering downstream steps. Natural for RAG-heavy agents.

## 2025 Autonomous Framework Wave

Three major open-source frameworks emerged representing distinct approaches:

| Framework | Developer | Approach | Best For |
|-----------|-----------|----------|----------|
| agent-lightning | Microsoft | Reinforcement learning | AI research, MLOps |
| hermes-agent | NousResearch | Self-improvement + skill accumulation | Customer-facing AI assistants |
| superpowers | obra | Test-driven development | Software development |

## Framework Selection Criteria

The 57.3% of teams with agents in production (per LangChain's 2025 survey) face these selection factors:

- **Complexity of task**: Simple tasks need simple frameworks; multi-agent only when justified
- **Production readiness**: Some frameworks excel at prototyping but struggle in production
- **Model flexibility**: Over 75% of teams use multiple models; frameworks must be model-agnostic
- **Observability**: Production agents need comprehensive logging and tracing
- **Community and ecosystem**: MCP compatibility, pre-built integrations, active maintenance

## The Framework Debate

A persistent tension exists between framework-heavy and framework-light approaches. The OpenAI Agents SDK represents the latter: "Why add a framework layer when the model provider gives you everything?" Meanwhile, LangGraph represents the former: complex stateful workflows need explicit graph-based orchestration. The answer depends on use case complexity.

## Sources

- [[sources/pebblous-agentic-framework-explosion]] — 2025 framework wave analysis
- [[sources/superannotate-llm-agents-guide]] — framework overview
- [[sources/databricks-agent-design-patterns]] — framework selection guidance

## Related Concepts

- [[concepts/llm-agent-architecture]] — what frameworks implement
- [[concepts/agent-orchestration]] — multi-agent coordination within frameworks
- [[concepts/model-context-protocol]] — standardized tool integration across frameworks
- [[concepts/agentic-workflows]] — the patterns frameworks enable
