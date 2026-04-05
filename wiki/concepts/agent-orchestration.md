---
title: "Agent Orchestration"
type: concept
sources: ["[[sources/databricks-agent-design-patterns]]", "[[sources/multi-agent-collaboration-survey]]", "[[sources/ng-agentic-design-patterns]]"]
related: ["[[concepts/multi-agent-systems]]", "[[concepts/llm-agent-architecture]]", "[[concepts/agentic-workflows]]", "[[concepts/agent-frameworks]]"]
last_compiled: 2026-04-05
summary: "Patterns for coordinating multiple LLM agents: orchestrator-worker (most common in production), supervisor, and router patterns with registry/state-store/supervisor components."
---

## Overview

Agent orchestration is the discipline of coordinating multiple LLM agents to work together on complex tasks. As individual agents become more capable, the challenge shifts from making one agent work to making many agents collaborate effectively. Orchestration patterns define how tasks are decomposed, assigned, monitored, and synthesized.

## Core Orchestration Patterns

### Orchestrator-Worker (Most Common in Production)

A central orchestrator agent:
1. Receives incoming tasks
2. Classifies intent
3. Decomposes complex requests into subtasks
4. Routes each subtask to a specialized worker agent
5. Combines results into a final response

This is the most widely deployed multi-agent pattern because it provides clear separation of concerns while maintaining centralized control.

### Supervisor

A supervisor agent coordinates specialized agents, each maintaining its own scratchpad. The supervisor orchestrates communication and delegates tasks based on agent capabilities. The supervisor can be either:
- **LLM-based**: A language model that reasons about task routing
- **Rule-based**: Deterministic routing logic based on task classification

### Router

Maps incoming tasks to the best available worker agent based on:
- **Capability match**: Which agent has the right tools and expertise
- **Current load**: Which agent is available
- **Historical accuracy**: Which agent performs best on similar tasks

Advanced routers use multi-armed bandit algorithms to balance exploration (trying different agents) and exploitation (using the proven best agent).

### Peer-to-Peer

Agents communicate directly without a central coordinator. Each agent decides when to pass work to another based on its own assessment. More flexible but harder to debug and monitor.

## Four Core Components

Any robust orchestration system needs:

1. **Registry**: A catalog of available agents with their capabilities, tools, and specializations
2. **Router**: Logic that maps incoming tasks to the best agent or sequence of agents
3. **State Store**: Shared context and conversation history accessible to all agents
4. **Supervisor**: Monitoring for timeouts, retries, escalations, and quality control

## Collaboration Typology

The 2025 survey (arXiv:2501.06322) identifies three collaboration types:

- **Cooperation**: Agents work toward shared goals using complementary skills
- **Competition**: Agents debate or compete, improving output quality through adversarial feedback
- **Coopetition**: Mixed mode — competing on some aspects while cooperating on others

## Five-Dimensional Taxonomy

Multi-agent systems can be characterized across:
1. **Actors**: Which agents participate and their roles
2. **Types**: Cooperation, competition, or coopetition
3. **Structures**: Peer-to-peer, centralized, or distributed
4. **Strategies**: Role-based vs. model-based approaches
5. **Coordination Protocols**: Rules governing interaction

## Production Considerations

From Databricks' practical guidance:
- **Start simple**: A single-agent system is often sufficient for enterprise use cases
- **Add complexity gradually**: Move to multi-agent only when the tool space or domain complexity demands it
- **Monitor carefully**: Multi-agent systems have increased debugging and tracing overhead
- **Prevent loops**: Risk of agents bouncing tasks indefinitely — implement maximum iteration limits
- **Sandbox risky actions**: Human approval gates for irreversible operations

## Sources

- [[sources/databricks-agent-design-patterns]] — orchestration patterns with production guidance
- [[sources/multi-agent-collaboration-survey]] — academic taxonomy of collaboration mechanisms
- [[sources/ng-agentic-design-patterns]] — multi-agent as fourth design pattern

## Related Concepts

- [[concepts/multi-agent-systems]] — the broader multi-agent paradigm
- [[concepts/llm-agent-architecture]] — single-agent architecture that orchestration coordinates
- [[concepts/agentic-workflows]] — orchestration enables complex workflows
- [[concepts/agent-frameworks]] — frameworks that implement orchestration
