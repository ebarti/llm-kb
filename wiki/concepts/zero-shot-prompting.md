---
title: "Zero-Shot Prompting"
type: concept
sources: ["[[sources/promptingguide-chain-of-thought]]", "[[sources/promptingguide-few-shot]]", "[[sources/lakera-prompt-engineering-guide]]"]
related: ["[[concepts/prompt-engineering]]", "[[concepts/few-shot-prompting]]", "[[concepts/chain-of-thought-prompting]]"]
last_compiled: 2026-04-05
summary: "Direct instruction to an LLM without any demonstration examples — the simplest prompting approach, and the recommended starting point before reaching for more complex techniques."
---

## Overview

Zero-shot prompting is the simplest form of [[concepts/prompt-engineering]]: giving an LLM a direct instruction without any examples. The model relies entirely on its pre-training knowledge and instruction-tuning to understand and execute the task.

Modern instruction-tuned models (Claude, GPT-4, Gemini) are remarkably capable in zero-shot settings. The practical recommendation is to always try zero-shot first, and only add examples ([[concepts/few-shot-prompting]]) or reasoning scaffolds ([[concepts/chain-of-thought-prompting]]) when zero-shot performance is insufficient.

## Zero-Shot CoT

A particularly powerful variant is Zero-Shot Chain-of-Thought, introduced by Kojima et al. (2022). Simply appending "Let's think step by step" to a zero-shot prompt dramatically improves performance on reasoning tasks without requiring any demonstration examples. This discovery showed that the reasoning capability is latent in the model and can be activated with a simple trigger phrase.

## When to Use

Zero-shot works well for:
- Simple, well-defined tasks (classification, summarization, translation)
- Tasks where the instruction is unambiguous
- General-purpose tasks the model has seen extensively in training
- Initial exploration before investing in example curation

Zero-shot may be insufficient for:
- Tasks requiring specific formatting patterns
- Domain-specific conventions the model hasn't seen
- Complex multi-step reasoning (though Zero-Shot CoT helps here)

## Sources
- [[sources/promptingguide-chain-of-thought]] — Zero-Shot CoT variant
- [[sources/promptingguide-few-shot]] — Contrasted with few-shot approaches
- [[sources/lakera-prompt-engineering-guide]] — Zero-shot in the technique taxonomy

## Related Concepts
- [[concepts/prompt-engineering]] — parent domain
- [[concepts/few-shot-prompting]] — the natural next step when zero-shot is insufficient
- [[concepts/chain-of-thought-prompting]] — Zero-Shot CoT as a powerful hybrid
