---
title: "RLHF and Alternatives: Comprehensive Overview"
source: "https://argilla.io/blog/mantisnlp-rlhf-part-9/"
author: "MantisNLP / Argilla"
date_published: 2024-06-01
date_ingested: 2026-04-05
tags: [rlhf, dpo, kto, ipo, orpo, spin, alignment, comparison]
type: article
status: raw
discovered_via: search
---

# RLHF and Alternatives: Comprehensive Overview

## Methods Covered

### DPO (Direct Preference Optimization)
Simplifies RLHF by aligning the LLM with human preferences without requiring RL. Treats preference learning as a classification problem.

### IPO (Identity Preference Optimization)
Replaces logit functions with identity functions, works better when preferences are deterministic. Adds regularization to avoid overfitting.

### KTO (Kahneman-Tversky Optimization)
Based on prospect theory. Directly maximizes utility of generations instead of log-likelihood of preferences. Only requires binary signals (desirable/undesirable).

### ORPO (Odds Ratio Preference Optimization)
Combines instruction tuning and preference alignment in a single process. Reference model-free and computationally efficient.

### SPIN (Self-Play Fine-Tuning)
Model competes against its previous version without direct supervision, creates its own training data.

### CoH (Chain of Hindsight)
Converts all feedback types into sequences, enabling learning from detailed comparisons.

### RLAIF (Reinforcement Learning from AI Feedback)
Eliminates human feedback by leveraging another LLM guided by constitutional principles.

### SimPO (Simple Preference Optimization)
Aligns reward and generative models more intuitively.

## Data Requirements Comparison

| Method | Data Format | Paper Scale | Min Scale | Compute |
|--------|------------|-------------|-----------|---------|
| RLHF | Prompt + chosen/rejected + reward | 10K | - | High |
| DPO | Prompt + chosen/rejected | 170K | 12K | Medium |
| KTO | Prompt + response + binary label | 600K | 12K | Medium/Low |
| ORPO | Prompt + chosen/rejected | 200K | 7K | Low |
| SPIN | Prompt + chosen (auto-generates rejected) | 50K | 1.8K | High |
| RLAIF | Prompt + responses | 125K | - | High |
| IPO | Prompt + chosen/rejected | - | - | Medium |
| CoH | Conversational feedback format | 300K | - | Medium |
| SimPO | Prompt + chosen/rejected | 200K | - | Low |

## Key Findings
- Well-curated data enhances results and allows dataset size reduction
- SPIN achieved comparable results with 1.8K vs original 50K prompts
- ORPO showed success with only 7K instances
- Using AI feedback to generate preference datasets is now widely accepted
- No single method addresses all aspects effectively
- HuggingFace TRL supports SFT, DPO, IPO, KTO, and ORPO

## Pipeline Stages
- Traditional RLHF: 3 stages (SFT, Reward Model, PPO)
- Newer approaches consolidate: ORPO combines instruction tuning + preference alignment in one step
- DPO and related methods eliminate the reward model stage
