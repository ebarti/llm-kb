---
title: "Chain-of-Thought Prompting"
source: "https://www.promptingguide.ai/techniques/cot"
author: "DAIR.AI / Prompt Engineering Guide"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [prompt-engineering, chain-of-thought, reasoning, few-shot]
type: article
status: raw
discovered_via: search
---

# Chain-of-Thought Prompting: Comprehensive Overview

## Definition & Core Concept

Chain-of-Thought (CoT) prompting enables complex reasoning by decomposing problems into intermediate steps. As introduced by Wei et al. (2022), this technique "enables complex reasoning capabilities through intermediate reasoning steps" and can be combined with few-shot prompting for enhanced performance on demanding tasks.

## How It Works

CoT operates by encouraging models to articulate their reasoning process before providing final answers. The technique shows demonstrable improvements—in arithmetic examples, models correctly solve problems with step-by-step reasoning that they fail without it.

Key Finding: Even single demonstrations prove effective. The authors note this represents "an emergent ability that arises with sufficiently large language models."

## Zero-Shot CoT Prompting

Kojima et al. (2022) introduced a simpler variant requiring no examples. By appending "Let's think step by step" to prompts, models achieve comparable improvements. This approach proves especially valuable when demonstration examples are scarce.

## Automatic Chain-of-Thought (Auto-CoT)

Zhang et al. (2022) proposed automation for demonstration creation. Auto-CoT eliminates manual crafting through two stages:

1. Question clustering: partitioning dataset questions into clusters
2. Demonstration sampling: selecting representative questions per cluster and generating reasoning chains

The method uses heuristics like question length (60 tokens) and reasoning steps (5 steps) to ensure quality demonstrations.

## Effectiveness & Research

- CoT reasoning is possible even with invalid demonstrations - prompting with invalid reasoning steps can achieve over 80-90% of the performance obtained using CoT under various metrics
- Being relevant to the query and correctly ordering the reasoning steps are much more important for effective CoT reasoning
- CoT prompting is less effective with smaller models
- The practical sweet spot for most tasks is 150-300 words of prompt
- A 2025 Wharton study found reasoning models gain "only marginal benefits despite substantial time costs" (20-80% increase in cost), though CoT remains valuable for interpretability in high-stakes applications

## Key Variants

- Zero-shot CoT (Kojima et al. 2022): "Let's think step by step"
- Auto-CoT (Zhang et al. 2022): Automated demonstration creation
- Manual CoT: Hand-crafted reasoning chains as examples
- Self-Consistency + CoT: Multiple reasoning paths with majority voting
