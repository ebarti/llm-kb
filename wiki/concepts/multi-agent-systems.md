---
title: "Multi-Agent Systems"
type: concept
sources: ["[[sources/karma-multi-agent-knowledge-graph]]", "[[sources/storm-automated-wiki-creation]]", "[[sources/multi-agent-collaboration-survey]]", "[[sources/ng-agentic-design-patterns]]"]
related: ["[[concepts/knowledge-graph]]", "[[concepts/automated-wiki-creation]]", "[[concepts/llm-knowledge-base]]", "[[concepts/agent-orchestration]]", "[[concepts/agentic-workflows]]", "[[concepts/agent-frameworks]]", "[[concepts/agent-to-agent-protocol]]", "[[concepts/agentic-workflow-patterns]]"]
last_compiled: 2026-04-05
summary: "Networks of specialized LLM agents collaborating through cooperation, competition, or coopetition — from KARMA's 9-agent KG pipeline to general-purpose orchestrator-worker architectures."
reading_time: "2 min"
---

## Overview

Multi-agent approaches to knowledge management divide the pipeline into specialized roles, each handled by a distinct LLM agent. This improves quality through specialization and enables conflict resolution between agents.

## KARMA's 9-Agent Architecture

Roles in KARMA's knowledge graph enrichment pipeline:
1. Document parser
2. Entity discoverer
3. Relation extractor
4. Schema aligner
5. Conflict detector
6. Conflict resolver
7. Knowledge integrator
8. Verifier
9. Schema validator

Each agent focuses on one task; agents pass results to each other and can challenge each other's outputs. The conflict resolution mechanism (18.6% edge conflict reduction) is only possible because distinct agents independently assess the same facts.

## STORM's Perspective-Simulating Agents

STORM uses a different multi-agent pattern: each agent role-plays a distinct *perspective* (identified from Wikipedia ToC analysis). These agents conduct simulated expert conversations, asking questions from their viewpoint. This produces more balanced, comprehensive coverage than a single-perspective research pass.

## When Multi-Agent > Single LLM

- **Conflict detection**: When two agents disagree, that's a signal worth surfacing
- **Scale**: Large document collections that exceed single context windows
- **Specialization**: When entity extraction, relation extraction, and schema validation have different requirements
- **Quality assurance**: Verification agent checks the primary extraction agent's work

## Contrast with Karpathy's Single-LLM Approach

Karpathy's system uses a single LLM in each phase (compilation, Q&A, linting) — simpler architecture, sufficient at personal scale (~100 articles). Multi-agent systems become justified at research-paper scale (thousands of documents) or when formal schema validation is required.

## Collaboration Taxonomy (2025 Survey)

A comprehensive survey (arXiv:2501.06322) taxonomizes multi-agent collaboration across five dimensions:

1. **Actors**: Which agents participate and their roles
2. **Types**: Cooperation (shared goals), competition (adversarial improvement), or coopetition (mixed)
3. **Structures**: Peer-to-peer, centralized, or distributed
4. **Strategies**: Role-based or model-based approaches
5. **Coordination Protocols**: Rules governing agent interactions

Natural language serves as the universal coordination medium, enabling unprecedented flexibility and emergent behaviors.

## Multi-Agent as Agentic Design Pattern

[[entities/andrew-ng]] identifies multi-agent collaboration as the fourth [[concepts/agentic-workflows]] design pattern. Multiple specialized agents decompose complex tasks through prompting and data feeding, mirroring the "Society of Mind" concept where intelligence emerges from many simple agents working together.

## General-Purpose Orchestration

Beyond knowledge management, multi-agent systems are deployed via [[concepts/agent-orchestration]] patterns:
- **Orchestrator-Worker**: Central agent decomposes tasks and routes to specialists
- **Supervisor**: Monitors and coordinates specialized agents
- **Router**: Maps tasks to agents based on capability, load, and historical accuracy

See [[concepts/agent-orchestration]] for detailed pattern descriptions.

## Sources
- [[sources/karma-multi-agent-knowledge-graph]] — 9-agent KG enrichment (NeurIPS 2025 Spotlight)
- [[sources/storm-automated-wiki-creation]] — perspective-based article creation agents
- [[sources/multi-agent-collaboration-survey]] — five-dimension taxonomy of collaboration mechanisms
- [[sources/ng-agentic-design-patterns]] — multi-agent as fourth agentic design pattern

## Related Concepts
- [[concepts/knowledge-graph]] — what KARMA builds
- [[concepts/automated-wiki-creation]] — STORM's output
- [[concepts/llm-knowledge-base]] — the single-LLM alternative
- [[concepts/agent-orchestration]] — coordination patterns for multi-agent systems
- [[concepts/agentic-workflows]] — the broader paradigm
- [[concepts/agent-frameworks]] — frameworks implementing multi-agent coordination

## Related Entities

- [[entities/karma]] — nine-agent KG enrichment pipeline
- [[entities/storm]] — perspective-simulating article creation

## Agent-to-Agent Protocol (A2A)

Google's [[concepts/agent-to-agent-protocol]] provides a standardized protocol layer for multi-agent collaboration. Agents publish "Agent Cards" describing their capabilities, enabling dynamic discovery and task delegation at runtime. A2A complements [[concepts/model-context-protocol]] (tool access) by addressing inter-agent communication — see [[sources/google-ai-agent-protocols]] and [[sources/zilliz-function-calling-vs-mcp-vs-a2a]] for details.

## Anthropic's Workflow Patterns

[[sources/anthropic-building-effective-agents]] defines the orchestrator-workers pattern as a key [[concepts/agentic-workflow-patterns|agentic workflow pattern]]: a central LLM dynamically decomposes tasks and delegates to worker instances, then synthesizes results. This is a practical multi-agent pattern distinct from the more complex A2A-style autonomous agent collaboration.

## Related Comparisons

- [[comparisons/single-agent-vs-multi-agent]] — single-LLM vs. multi-agent approaches
