---
title: "Multi-Agent Collaboration Mechanisms: A Survey of LLMs"
source: "https://arxiv.org/abs/2501.06322"
author: "Various (6 authors)"
date_published: 2025-01-10
date_ingested: 2026-04-05
tags: [multi-agent, collaboration, cooperation, competition, survey]
type: paper
status: raw
discovered_via: search
---

# Multi-Agent Collaboration Mechanisms: A Survey of LLMs

## Overview

This survey examines how groups of LLM-based intelligent agents can work together to tackle complex problems at scale, shifting from single-model approaches to collaboration-centric systems.

## Taxonomy of Collaboration

Five key dimensions:
1. **Actors**: The specific agents participating
2. **Types**: Cooperation, competition, or coopetition
3. **Structures**: Peer-to-peer, centralized, or distributed
4. **Strategies**: Role-based or model-based approaches
5. **Coordination Protocols**: Rules governing agent interactions

## Collaboration Types

### Cooperation
Agents leverage individual specialties (writing, translation, research) to achieve shared goals.

### Competition
Agents compete and debate against each other for their own goals — useful for improving output quality through adversarial feedback.

### Coopetition
Agents compromise, competing on one aspect while agreeing on another.

## Communication Patterns

LLM-based systems use natural language as a universal coordination medium, enabling unprecedented flexibility and emergent behaviors.

Common pattern: planner-worker architectures where a planner decomposes tasks into subgoals and assigns them to worker agents.

## Five Essential Components of Multi-Agent Systems
1. **Profile**: How agents are created with personalized characteristics
2. **Perception**: Environmental information acquisition
3. **Self-action**: Memory, reasoning, and planning capabilities
4. **Mutual interaction**: Inter-agent communication
5. **Evolution**: Self-reflection and progressive enhancement

## Practical Frameworks
- **CAMEL**: Role-playing framework for role-based conversations
- **AutoGen**: Flexible agent behaviors and communication patterns
- **CrewAI**: Task-oriented multi-agent orchestration

## Applications
5G/6G networks, Industry 5.0, question answering systems, social and cultural applications.
