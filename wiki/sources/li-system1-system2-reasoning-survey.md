---
title: "Source: From System 1 to System 2: A Survey of Reasoning LLMs"
type: source-summary
source: "[[raw/li-system1-system2-reasoning-survey]]"
related: ["[[concepts/system-1-system-2-thinking]]", "[[concepts/reasoning-models]]", "[[concepts/chain-of-thought]]", "[[concepts/test-time-compute]]"]
last_compiled: 2026-04-05
summary: "Comprehensive 2025 survey applying Kahneman's dual-process theory to LLMs: standard LLMs as System 1 (fast/intuitive), reasoning models (o1, R1) as System 2 (slow/deliberate), tracing the evolution through CoT, fine-tuning, and RL training."
---

## Key Points

- System 1 LLMs: direct output, fast, cheap, prone to errors on complex tasks.
- System 2 LLMs: intermediate reasoning steps, slower, more expensive, superior on structured tasks.
- Four training approaches: pure RL, RL+SFT, SFT+distillation, inference-time scaling.
- Hybrid toggle (like Claude 3.7) seen as promising -- choose System 1 or 2 per task.

## Detailed Summary

Li et al. (2025) provide the most comprehensive mapping of Kahneman's dual-process theory onto the LLM landscape. They trace a four-stage evolution:

1. **Pre-trained LLMs** (pure System 1): GPT-3, BERT-era models that respond immediately without deliberation.
2. **CoT prompting** (System 2 via prompting): [[concepts/chain-of-thought|Chain-of-thought]] prompts force models into step-by-step reasoning without changing weights.
3. **Fine-tuned reasoners** (System 2 via training): Models trained on reasoning traces to internalize step-by-step behavior.
4. **RL-trained reasoners** (System 2 via RL): [[concepts/reasoning-models|Models like o1 and R1]] that develop reasoning through reinforcement learning, the deepest form of System 2 internalization.

The survey catalogues training methodologies, benchmark performance, and identifies that System 2 models excel on arithmetic, symbolic reasoning, and competitive programming, while System 1 remains effective for intuitive/commonsense tasks.

## Related Concepts

- [[concepts/system-1-system-2-thinking]] -- the central framework
- [[concepts/reasoning-models]] -- the practical realization of System 2
- [[concepts/chain-of-thought]] -- the first System 2 technique
- [[concepts/test-time-compute]] -- the computational mechanism behind System 2
