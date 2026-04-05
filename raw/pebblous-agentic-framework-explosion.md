---
title: "Agentic Framework Big Bang - 3 Paths in Autonomous AI"
source: "https://blog.pebblous.ai/blog/agentic-framework-explosion/en/"
author: "Pebblous Data Communication Team"
date_published: 2026-04-01
date_ingested: 2026-04-05
tags: [agent-frameworks, autonomous-ai, reinforcement-learning, self-improvement, tdd]
type: article
status: raw
discovered_via: search
---

# Agentic Framework Big Bang — 3 Paths in Autonomous AI

## Three Stages of Agent Evolution
- **Stage 1 (2022-2023)**: Single-shot inference, model capability focus
- **Stage 2 (2023-2024)**: Tool-calling agents, integration reliability
- **Stage 3 (2025-present)**: Autonomous operating agents, learning and self-verification

## Three Major Frameworks of 2025

### 1. agent-lightning (Microsoft, June 2025)
- **Core**: Reinforcement learning — agents receive reward signals based on outcomes
- **Stars**: 16,372 | License: MIT
- **Best for**: AI research teams, advanced MLOps
- **Limitation**: Reward function accuracy is critical; noisy signals cause "reward hacking"

### 2. hermes-agent (NousResearch, July 2025)
- **Core**: Self-improvement through three mechanisms:
  1. Skill Generation: Successfully completed tasks generate reusable skills
  2. User Modeling: Develops personalized understanding of preferences
  3. Multi-channel Interface: Learning across Slack, email, webhooks
- **Stars**: 21,017 | License: MIT
- **Best for**: Product teams building customer-facing AI assistants

### 3. superpowers (obra, October 2025)
- **Core**: Test-Driven Development for autonomous code generation
- **Stars**: 129,443
- **Best for**: Software developers — resonates with code quality anxiety
- **Method**: Write tests first, then develop code to satisfy them

## Framework Comparison

| Dimension | agent-lightning | hermes-agent | superpowers |
|-----------|-----------------|--------------|-------------|
| Core Question | Train agents better | Enable self-improvement | Ensure code trustworthiness |
| Foundation | Reinforcement Learning | Skill accumulation | TDD methodology |
| Implementation Difficulty | High | Medium | Low |
| Primary Users | AI researchers | Product teams | Developers |

## Data Quality as Fundamental Bottleneck

"The more autonomous the agent, the less human oversight there is — and the more the quality of the underlying data sets the ceiling on results."

- RL agents: reward function accuracy determines everything
- Self-improving agents: flawed skills replicate and compound
- Autonomous coding: test coverage completeness limits reliability
- Framework sophistication cannot compensate for corrupted inputs
