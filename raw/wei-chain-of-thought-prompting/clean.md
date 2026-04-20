---
title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
source: "https://arxiv.org/abs/2201.11903"
author: "Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou"
date_published: 2022-01-28
date_ingested: 2026-04-05
tags: [chain-of-thought, reasoning, prompting, few-shot, arithmetic, commonsense]
type: paper
status: raw
discovered_via: search
---

# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

## Key Findings

- Generating a chain of thought -- a series of intermediate reasoning steps -- significantly improves the ability of large language models to perform complex reasoning.
- The method works by providing a few chain of thought demonstrations as exemplars in prompting (few-shot CoT).
- Prompting a 540B parameter model (PaLM) with just eight exemplars achieved state-of-the-art on the GSM8K math benchmark, surpassing even fine-tuned GPT-3 with verification.
- Improvements demonstrated across three reasoning domains: arithmetic, commonsense, and symbolic reasoning.
- Chain-of-thought is an emergent ability -- it only helps at sufficient model scale (roughly 100B+ parameters). Smaller models produce illogical chains that hurt performance.

## Types of CoT

1. **Few-shot CoT**: Provide exemplar problems with step-by-step solutions in the prompt.
2. **Zero-shot CoT**: Simply add "Let's think step by step" to the prompt (discovered by Kojima et al., 2022).
3. **Automatic CoT**: Use the model itself to generate CoT exemplars.
4. **Multimodal CoT** (2024+): Extends CoT to incorporate visual data alongside language.

## Mechanism

CoT prompting leverages LLMs to articulate a succession of reasoning steps, guiding the model toward generating analogous reasoning chains for novel tasks. Users commonly add instructions like "describe your reasoning steps" or "explain your answer step-by-step."

## Significance

This paper is foundational to the field of LLM reasoning. It demonstrated that prompting alone -- without any fine-tuning -- could unlock substantial reasoning capabilities in large language models. It opened the door to subsequent work on tree-of-thought, self-consistency, and ultimately the development of dedicated reasoning models like o1 and R1.
