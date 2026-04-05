---
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
source: "https://www.promptingguide.ai/techniques/react"
author: "Yao et al. (2022)"
date_published: 2022-10-06
date_ingested: 2026-04-05
tags: [react, reasoning, acting, llm-agents, prompting]
type: article
status: raw
discovered_via: search
---

# ReAct Prompting: Reasoning and Acting Framework

## Overview

ReAct, introduced by Yao et al. (2022), is a prompting framework that enables language models to generate both reasoning traces and task-specific actions in an interleaved manner. This approach addresses limitations in purely reasoning-based or action-based systems by combining their strengths.

## Core Mechanism

The framework operates through a cyclical process:
- **Reasoning Traces**: Models articulate their thought process, helping them induce, track, and update action plans while handling exceptions
- **Actions**: Models interface with external sources like knowledge bases or search engines
- **Observations**: Results from actions inform subsequent reasoning steps

The typical ReAct loop: Thought → Action → Observation → (repeat)

## Key Advantages Over Alternatives

**vs. Chain-of-Thought (CoT)**
CoT struggles with fact hallucination and cannot update knowledge based on external information. ReAct mitigates these issues through information retrieval.

**vs. Action-Only Approaches**
Without reasoning, systems fail to decompose complex goals into manageable subgoals. ReAct's interleaved approach maintains strategic planning.

## Performance Results

### Knowledge-Intensive Tasks
ReAct outperforms action-only methods on question-answering and fact-verification benchmarks. ReAct + Reflexion significantly outperforms ReAct by completing 130/134 tasks.

### Decision-Making Tasks
On ALFWorld and WebShop, ReAct significantly outperforms action-only baselines.

## Hybrid Approaches
Combining ReAct with Chain-of-Thought and self-consistency yields optimal performance, leveraging both internal knowledge and external information retrieval.

## Implementation
Modern implementations use frameworks like LangChain to configure: an LLM as the reasoning engine, tools for actions, and an agent that orchestrates the reasoning-action cycle.
