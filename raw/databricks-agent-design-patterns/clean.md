---
title: "Agent System Design Patterns"
source: "https://docs.databricks.com/aws/en/generative-ai/guide/agent-system-design-patterns"
author: "Databricks"
date_published: 2025-06-01
date_ingested: 2026-04-05
tags: [agent-patterns, orchestration, multi-agent, single-agent, design-patterns]
type: article
status: raw
discovered_via: search
---

# Agent System Design Patterns

## Design Pattern Spectrum

### 1. LLM + Prompt
Simple standalone LLM. Good for generic Q&A and quick prototyping. Minimal complexity but limited customization and disconnected from business data.

### 2. Deterministic Chain (Hard-Coded Steps)
Predefined workflow for all requests — highly predictable. Best for well-defined tasks prioritizing consistency and auditability. Maximum predictability but inflexible for diverse requests.

Example: Basic RAG chains.

### 3. Single-Agent System
An LLM that orchestrates one coordinated flow of logic. Adaptively decides which tools to use, when to make more LLM calls, and when to stop. Best for moderate-to-complex queries within a single domain. Often optimal for enterprise — simpler than multi-agent yet allowing dynamic logic.

### 4. Multi-Agent System
Two or more specialized agents exchanging messages or collaborating. Each agent has domain or task expertise.

Best for large cross-functional domains, multiple specialized agents with separate logic, scenarios with numerous tools impractical for single-agent schemas.

A coordinator/supervisor (LLM-based or rule-based) directs requests to appropriate agents.

## Orchestration Patterns

### Orchestrator-Worker
Most deployed pattern in production. Central orchestrator:
1. Receives incoming tasks
2. Classifies intent
3. Decomposes complex requests into subtasks
4. Routes each subtask to specialized worker agent
5. Combines results into final response

### Supervisor
Supervisor agent coordinates multiple specialized agents. Each agent maintains its own scratchpad while supervisor orchestrates communication and delegates tasks.

### Router
Maps subtasks to best available worker agent based on capability match, current load, and historical accuracy. Advanced routers use multi-armed bandit algorithms.

## Four Core Orchestration Components
1. **Registry**: Available agents and their capabilities
2. **Router**: Maps tasks to best agent or sequence
3. **State store**: Shared context and conversation history
4. **Supervisor**: Monitors timeouts, retries, and escalations

## Best Practices
- Start with simplest pattern meeting requirements
- Maintain clear, minimal prompts
- Provide only essential tools and context
- Implement comprehensive logging
- Pin model versions to prevent behavioral drift
- Sandbox risky agent actions or enforce human approval
