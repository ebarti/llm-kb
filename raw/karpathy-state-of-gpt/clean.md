---
title: "State of GPT — Andrej Karpathy (Microsoft Build 2023)"
source: "https://community.openai.com/t/build-talk-state-of-gpt-andrej-karpathy/226110"
author: "Andrej Karpathy"
date_published: 2023-05-23
date_ingested: 2026-04-05
tags: [karpathy, GPT, training-pipeline, RLHF, Microsoft-Build, LLM]
type: article
status: raw
discovered_via: search
---

# State of GPT — Microsoft Build 2023 Keynote

## Overview
Andrej Karpathy presented at Microsoft Build 2023, explaining the full pipeline used to train GPT assistants like ChatGPT.

## Part 1: Training GPT

### Training Pipeline Stages
1. **Pretraining**: Main computational phase — thousands of GPUs, months of training, millions of dollars. Uses publicly available data from CommonCrawl, Wikipedia, GitHub, etc.
2. **Tokenization**: Converting text into integer sequences before training
3. **Supervised Fine-Tuning (SFT)**: Training on curated instruction-response pairs
4. **Reinforcement Learning from Human Feedback (RLHF)**: Human raters rank model outputs, creating a reward model, then using PPO to optimize against it

### Key Insight
Pretraining is where all the computational work happens. SFT and RLHF are comparatively lightweight but critical for alignment and usability.

## Part 2: Practical Use

### Prompting Strategies
- LLMs can have "bad luck" with sampling — try multiple attempts
- Ask reflective questions — models know when they make mistakes
- Use retrieval augmentation for grounding
- Chain-of-thought prompting for complex reasoning

### Ecosystem
- Plugins and tool use
- Fine-tuning for domain specialization
- Ensemble methods for reliability
- Retrieval augmentation for grounding

## Impact
The talk became one of the most widely referenced introductions to the GPT training pipeline, cited extensively in educational contexts for its clarity in explaining the pretraining → SFT → RLHF pipeline.
