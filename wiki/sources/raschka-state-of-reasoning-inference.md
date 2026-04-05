---
title: "Source: The State of LLM Reasoning Model Inference"
type: source-summary
source: "[[raw/raschka-state-of-reasoning-inference]]"
related: ["[[concepts/test-time-compute]]", "[[concepts/reasoning-models]]", "[[concepts/self-consistency]]", "[[concepts/process-reward-models]]"]
last_compiled: 2026-04-05
summary: "Sebastian Raschka's 2025 survey of inference-time scaling methods: four implementation categories, sequential vs. parallel techniques, emerging approaches (latent reasoning, self-backtracking), and the practical tradeoff between reasoning quality and latency."
---

## Key Points

- Four categories: inference-time scaling, pure RL, RL+SFT, SFT+distillation.
- Sequential techniques: wait tokens, CoT prompting, budget forcing.
- Parallel techniques: majority voting, beam search, MCTS, PRM-based selection.
- Emerging: test-time preference optimization, thought switching penalty, self-backtracking, latent reasoning.
- A 1B parameter model with proper inference scaling can outperform unoptimized larger models.

## Detailed Summary

Raschka (2025) provides a practitioner-oriented overview of the rapidly evolving landscape of inference-time reasoning techniques, written shortly after DeepSeek R1's release galvanized the field.

The survey distinguishes between **sequential** approaches (extending reasoning chains: wait tokens, CoT, budget forcing) and **parallel** approaches (generating multiple solutions: [[concepts/self-consistency|majority voting]], beam search, [[concepts/process-reward-models|PRM selection]], MCTS). The most effective strategies combine both.

Emerging techniques point to the frontier: **latent reasoning** performs computation in hidden states without generating explicit tokens (more efficient but less interpretable), **self-backtracking** enables models to autonomously correct errors mid-generation, and **thought switching penalty** prevents models from jumping between reasoning approaches too quickly.

The practical insight is that no single technique dominates across all task types, and latency increases significantly with inference scaling. The future likely involves "thinking on demand" as a standard feature with configurable budgets.

## Related Concepts

- [[concepts/test-time-compute]] -- the overarching paradigm surveyed
- [[concepts/self-consistency]] -- a key parallel scaling technique
- [[concepts/process-reward-models]] -- used in verification-based search
- [[concepts/reasoning-models]] -- the practical systems that implement these techniques
- [[concepts/chain-of-thought]] -- the foundational sequential technique
