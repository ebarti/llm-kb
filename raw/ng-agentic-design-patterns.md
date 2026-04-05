---
title: "Andrew Ng on Agentic Design Patterns and Enterprise AI"
source: "https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/"
author: "Andrew Ng"
date_published: 2024-03-27
date_ingested: 2026-04-05
tags: [agentic-workflows, reflection, tool-use, planning, multi-agent, andrew-ng]
type: article
status: raw
discovered_via: search
---

# Andrew Ng on Agentic Design Patterns

## Four Core Design Patterns

Andrew Ng identifies four agentic AI design patterns that drive massive AI progress:

### 1. Reflection
The reflection pattern automates the feedback process. Instead of manually critiquing an LLM's output, the system prompts the model to automatically criticize its own output and improve its response.

**How it works:**
1. Initial Generation: Prompt the LLM to produce output
2. Self-Criticism: Request the model evaluate its work
3. Refinement: Have the model rewrite using the feedback
4. Iteration: Repeat the cycle

Extends through tool integration—running code against unit tests or web searches to validate output. Can use two agents: one generates, another critiques.

Described as "relatively quick to implement" with "surprising performance gains" across code generation, writing, and Q&A.

### 2. Tool Use
Integrating LLMs with specialized external tools to create more capable systems. An LLM might generate code while another tool compiles and executes it.

### 3. Planning
Multiple LLM agents working collaboratively to decompose complex problems. One model functions as a coder while a separate agent takes on a reviewer role.

### 4. Multi-Agent Collaboration
Networks of specialized agents working together, each handling different subtasks through prompting and data feeding.

## Key Insight: Architecture > Model Size

GPT-3.5 with an agentic workflow can outperform GPT-4 using a zero-shot approach. This reframes the competitive landscape — the architecture matters as much as the model.

## Enterprise Strategy

Ng argues enterprises should prioritize building practical applications using agentic workflows rather than chasing the most advanced foundational models:
- Focus on application development, not model competition
- Cost of model usage decreasing ~80% year-over-year
- "The hardest thing is just building something that works"
- Start with best available model, optimize later

## Recommended Papers
- Self-Refine: Iterative Refinement with Self-Feedback (Madaan et al., 2023)
- Reflexion: Language Agents with Verbal Reinforcement Learning (Shinn et al., 2023)
- CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing (Gou et al., 2024)
