---
title: "The AI Scaling Paradigm Shift: From Pre-Training to Post-Training and Test-Time Compute"
source: "https://www.hec.edu/en/dare/tech-ai/ai-beyond-scaling-laws"
author: "Multiple sources (HEC Paris, Epoch AI, Introl)"
date_published: 2026-01-01
date_ingested: 2026-04-05
tags: [scaling-laws, test-time-compute, post-training, reasoning-models, deepseek, inference]
type: article
status: raw
discovered_via: search
---

# The AI Scaling Paradigm Shift: Pre-Training to Post-Training and Test-Time Compute

## The Scaling Wall

For over a year, frontier models appear to have reached their ceiling. The scaling laws that powered exponential LLM progress have started showing diminishing returns. Simply adding more data and compute no longer produces proportional improvements.

Evidence of plateau:
- GPT-5 delayed significantly beyond initial timelines
- Gemini Ultra improvements marginal over Gemini Pro at enormous cost increase
- Industry insiders acknowledge diminishing returns privately while maintaining public optimism

## Three Eras of Scaling

### Era 1: Pre-Training Scaling (2018-2023)
The Kaplan/Chinchilla scaling laws: more compute + more data = better models, predictably.
Dominated by increasing parameter count and training data.
GPT-2 → GPT-3 → GPT-4 progression demonstrated reliable scaling.

### Era 2: Post-Training Scaling (2023-2025)
RLHF, instruction tuning, DPO — improving model behavior without larger pre-training runs.
DeepSeek-R1 proved pure reinforcement learning can produce reasoning capabilities matching o1.

### Era 3: Test-Time Compute / Inference Scaling (2024-present)
Spending more compute at generation time via longer deliberation and search-like strategies.
Models like OpenAI o1/o3, Gemini 2.0 Flash represent this paradigm.
DeepSeek-R1 proved this at scale: matching o1 by generating 10-100x more tokens per query.

## The Paradigm Shift

From 2020-2024: frontier advances dominated by training scale.
Over 2024-2025: field added second axis — inference scale (test-time compute).
As of early 2026: the question shifts from "does scaling reduce loss?" to "which scaling metrics translate into durable economic utility?"

The field increasingly resembles an industrial phase rather than a discovery phase.

## Sutskever's Framing

"We're moving from the age of scaling to the age of research."
Bigger GPTs will still improve, but next breakthroughs depend on new learning methods, not more GPUs.
"It is back to the age of research again, just with big computers."

## Competing Narratives

Optimists (Satya Nadella): Post-training represents "emergence of new scaling laws" — scaling isn't dead, it's evolved.
Skeptics (Apple ML Research): Reasoning models may be an "illusion of thinking" — potentially a narrative to justify continued massive investment.

## Key Models in Test-Time Scaling

- OpenAI o1 (Sept 2024): First major test-time compute model
- OpenAI o3 (Dec 2024): Significant improvement
- DeepSeek-R1 (Jan 2025): Open-source, proved RL alone produces reasoning
- Gemini 2.0 Flash Thinking: Google's entry
- Claude 3.7 Sonnet: Anthropic's reasoning model

## Data Wall

Current consumption patterns suggest exhaustion of public text data by 2028.
Potentially accelerated to 2026 through overtraining (excessive data reuse).
Epoch AI: ~300 trillion tokens of high-quality language data will be fully utilized between 2026-2032.
Synthetic data as solution: Gartner projects 75% of businesses using synthetic data by 2026.
Risks: model collapse from training on AI-generated data, loss of nuance and complexity.
Microsoft's SynthLLM: Attempting to break the data wall with scalable synthetic data anchored in human truth.
