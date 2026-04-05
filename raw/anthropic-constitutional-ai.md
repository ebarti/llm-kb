---
title: "Constitutional AI: Harmlessness from AI Feedback"
source: "https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback"
author: "Anthropic (Yuntao Bai et al.)"
date_published: 2022-12-15
date_ingested: 2026-04-05
tags: [constitutional-ai, alignment, rlaif, anthropic, harmlessness, ai-feedback]
type: paper
status: raw
discovered_via: search
---

# Constitutional AI: Harmlessness from AI Feedback

## Overview
Constitutional AI (CAI) is Anthropic's approach to training AI systems that are both helpful and harmless with minimal human labeling. Uses a "constitution" of principles to guide AI self-improvement.

## Core Motivation
As AI capabilities increase, scaling human oversight becomes impractical. CAI enables AI systems to supervise other AI systems, reducing dependency on manual human labels while maintaining safety standards.

## Two-Phase Training Process

### Supervised Learning Phase (Critique and Revision)
1. Sample responses from initial model (including responses to harmful prompts)
2. Ask the model to critique its own response based on constitutional principles
3. Ask the model to revise the response based on the critique
4. Fine-tune the original model on the revised responses

### Reinforcement Learning Phase (RLAIF)
1. Sample pairs of responses from the SL-fine-tuned model
2. Use another AI model to evaluate which response better adheres to constitutional principles
3. Train a preference model on AI-generated preferences
4. Apply RL (PPO) using this preference model as reward signal

## Key Innovation: Chain-of-Thought Reasoning
Both phases leverage chain-of-thought reasoning to enhance performance transparency and decision-making quality. The AI explains why one response is preferred over another.

## The Constitution
A set of high-level normative principles such as:
- Choose the response that is most helpful
- Choose the response that is least harmful
- Choose the response that is most honest
- Principles drawn from UN Declaration of Human Rights, Apple's Terms of Service, and other documents

## Advantages
- Controls AI behavior more precisely with far fewer human labels
- Scales better than pure RLHF (AI feedback is cheaper than human feedback)
- Produces non-evasive harmless responses (explains reasoning rather than refusing)
- Transparent: constitution is inspectable and modifiable
- Reduces reliance on human labelers for harmlessness training

## Results
- Produces an AI that is harmless yet non-evasive
- Actively engages with potentially problematic queries by explaining reasoning
- Comparable or superior performance to RLHF with human harmlessness labels
- Chain-of-thought prompting improves AI label quality

## Connection to RLAIF
Constitutional AI pioneered the use of AI feedback for the harmlessness dimension while retaining human feedback for helpfulness. This partial automation demonstrated that AI supervision could be a viable substitute for human supervision in specific domains.

## Collective Constitutional AI
Later work (2023) extended CAI by allowing public input into the constitution, with ~1,000 Americans contributing to principles that guide Claude's behavior.
