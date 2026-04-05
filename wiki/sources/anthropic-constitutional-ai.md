---
title: "Source: Constitutional AI - Harmlessness from AI Feedback"
type: source-summary
source: "[[raw/anthropic-constitutional-ai]]"
related: ["[[concepts/constitutional-ai]]", "[[concepts/rlaif]]", "[[concepts/rlhf]]", "[[entities/anthropic]]", "[[entities/claude]]"]
last_compiled: 2026-04-05
summary: "Anthropic's foundational paper on Constitutional AI: using a set of principles (a constitution) to enable AI self-critique and AI-generated preference labels, reducing reliance on human labelers while producing harmless yet non-evasive AI assistants."
---

## Key Points
- Constitutional AI uses a set of written principles (a "constitution") to guide AI self-improvement
- Two training phases: supervised self-critique/revision, then RL from AI feedback (RLAIF)
- Reduces reliance on human labelers while maintaining or improving harmlessness
- Produces non-evasive responses that explain reasoning rather than simply refusing
- Chain-of-thought reasoning improves the quality of AI-generated preference labels
- Later extended via Collective Constitutional AI with public input (~1,000 Americans)

## Detailed Summary

[[concepts/constitutional-ai]] addresses the fundamental scaling challenge of [[concepts/rlhf]]: as AI capabilities grow, human oversight becomes the bottleneck. CAI replaces human harmlessness labels with AI-generated feedback guided by explicit principles.

The supervised learning phase has the model critique its own harmful responses against constitutional principles, then revise them. The model is fine-tuned on these revised responses. In the RL phase, pairs of model responses are evaluated by another AI against constitutional principles, creating AI preference labels that train a [[concepts/reward-model]]. This reward model drives [[concepts/ppo-for-llms]] optimization -- a process called [[concepts/rlaif]].

The constitution includes principles like "choose the most helpful response," "choose the least harmful response," drawn from sources including the UN Declaration of Human Rights. The key result is an AI that engages with potentially problematic queries by explaining its reasoning and objections, rather than simply refusing -- harmless but non-evasive.

## Notable Quotes
> "Control AI behavior more precisely and with far fewer human labels" -- the core value proposition

## Related Concepts
- [[concepts/constitutional-ai]] -- the central concept
- [[concepts/rlaif]] -- the RL phase uses AI feedback
- [[concepts/scalable-oversight]] -- CAI as a solution to the oversight bottleneck
- [[entities/anthropic]] -- the organization behind this research
