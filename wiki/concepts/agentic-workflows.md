---
title: "Agentic Workflows"
type: concept
sources: ["[[sources/ng-agentic-design-patterns]]", "[[sources/claude-code-agentic-coding]]", "[[sources/databricks-agent-design-patterns]]", "[[sources/pebblous-agentic-framework-explosion]]"]
related: ["[[concepts/llm-agent-architecture]]", "[[concepts/reflection-pattern]]", "[[concepts/tool-use]]", "[[concepts/agent-planning]]", "[[concepts/multi-agent-systems]]", "[[concepts/agentic-coding]]"]
last_compiled: 2026-04-05
summary: "The paradigm of prompting LLMs iteratively through multi-step workflows with reflection, tool use, planning, and multi-agent collaboration — architecture matters more than model size."
---

## Overview

Agentic workflows represent a paradigm shift from single-shot LLM prompting to iterative, multi-step processes where AI systems plan, execute, observe, and refine. Rather than asking an LLM to generate a final answer in one pass, agentic workflows prompt the model multiple times, enabling step-by-step improvements toward higher-quality results.

The term was popularized by [[entities/andrew-ng]], who argues that agentic workflows will "drive massive AI progress — perhaps even more than the next generation of foundation models." His central insight: an older model running inside an agentic workflow can outperform a more advanced model using zero-shot prompting. This means the architecture of how you use an LLM matters as much as — or more than — which LLM you use.

## The Four Design Patterns

Ng identifies four core patterns that compose agentic workflows:

### 1. Reflection

The [[concepts/reflection-pattern]] automates self-critique. The LLM generates output, evaluates it, and iteratively improves. This is the simplest pattern to implement and delivers "surprising performance gains" in code generation, writing, and question-answering. It can be implemented with a single model (self-critique) or two models (generator + critic).

### 2. Tool Use

[[concepts/tool-use]] extends the LLM beyond text generation. By calling external functions — code execution, web search, database queries, API calls — the agent can ground its reasoning in real-world information and take concrete actions. The [[concepts/model-context-protocol]] standardizes this integration.

### 3. Planning

[[concepts/agent-planning]] enables the LLM to decompose complex goals into sequential or parallel subtasks, allocate them to appropriate tools or sub-agents, and synthesize results. Planning transforms a single-step operation into a multi-step strategy.

### 4. Multi-Agent Collaboration

[[concepts/multi-agent-systems]] involve multiple specialized agents working together, each handling a different aspect of a complex task. A planner agent might decompose a problem while specialized worker agents execute subtasks in parallel.

## From Zero-Shot to Agentic

The evolution from traditional LLM use to agentic workflows:

| Approach | Process | Quality |
|----------|---------|---------|
| Zero-shot | Single prompt → single response | Baseline |
| Few-shot | Single prompt with examples → single response | Better |
| Chain-of-Thought | Single prompt with reasoning steps → single response | Better still |
| Agentic | Multiple prompts → plan → execute → observe → reflect → iterate | Significantly better |

The key difference is iteration. Agentic workflows accept that the first draft is imperfect and systematically improve it through repeated cycles of generation and evaluation.

## Three Stages of Agent Evolution

Pebblous traces a clear historical progression:

1. **Stage 1 (2022-2023)**: Single-shot inference — focused on model capability alone
2. **Stage 2 (2023-2024)**: Tool-calling agents — focused on integration reliability
3. **Stage 3 (2025-present)**: Autonomous operating agents — focused on learning and self-verification

Stage 3 represents the current frontier, where agents not only use tools but learn from experience, generate reusable skills, and verify their own outputs.

## Enterprise Strategy

Ng's advice for enterprises is pragmatic: stop chasing model leaderboards and start building applications. Model API costs are decreasing ~80% year-over-year, making experimentation cheap. The hard part is not finding the best model but designing workflows that produce reliable value. Start with the best available model, build a working application, and optimize for cost only after you have proven value.

## Impact in 2026

By 2026, agentic workflows have moved from research to production at scale:
- Anthropic reports developers use AI in ~60% of work but fully delegate only 0-20%
- [[entities/claude-code]] reached $2.5B annualized revenue
- Zapier deployed 800+ internal agents with 89% organization-wide AI adoption
- The shift is from "coding" to "coordination" — engineers orchestrate agents rather than write code

## Sources

- [[sources/ng-agentic-design-patterns]] — foundational four-pattern framework
- [[sources/claude-code-agentic-coding]] — 2026 production impact and trends
- [[sources/databricks-agent-design-patterns]] — design pattern spectrum for enterprise
- [[sources/pebblous-agentic-framework-explosion]] — three-stage evolution of agent frameworks

## Related Concepts

- [[concepts/llm-agent-architecture]] — the architecture that implements agentic workflows
- [[concepts/reflection-pattern]] — first and most accessible pattern
- [[concepts/tool-use]] — external integration pattern
- [[concepts/agent-planning]] — task decomposition pattern
- [[concepts/multi-agent-systems]] — collaboration pattern
- [[concepts/agentic-coding]] — agentic workflows applied to software development
