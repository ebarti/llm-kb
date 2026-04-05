---
title: "Source: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
type: source-summary
source: "[[raw/wei-chain-of-thought-prompting]]"
related: ["[[concepts/chain-of-thought]]", "[[concepts/llm-reasoning]]", "[[concepts/emergent-abilities]]", "[[entities/jason-wei]]"]
last_compiled: 2026-04-05
summary: "Foundational 2022 paper showing that providing step-by-step reasoning exemplars in prompts unlocks arithmetic, commonsense, and symbolic reasoning in 100B+ parameter LLMs."
---

## Key Points

- Chain-of-thought (CoT) prompting generates intermediate reasoning steps that significantly improve LLM performance on complex reasoning tasks.
- Few-shot CoT: provide exemplar problems with worked solutions. Zero-shot CoT: simply add "Let's think step by step."
- A 540B parameter model with 8 CoT exemplars achieved state-of-the-art on GSM8K, beating fine-tuned GPT-3 with verification.
- CoT is an [[concepts/emergent-abilities|emergent ability]] -- it only helps above ~100B parameters. Smaller models produce illogical chains that degrade performance.

## Detailed Summary

Wei et al. (2022) demonstrated that the simple technique of providing step-by-step reasoning demonstrations in a prompt could dramatically improve LLM performance on tasks requiring multi-step reasoning. The approach requires no fine-tuning, no architectural changes, and no specialized training data -- just carefully constructed prompts.

The paper evaluated CoT across three reasoning domains: arithmetic (GSM8K, SVAMP, ASDiv, AQuA, MAWPS), commonsense (CSQA, StrategyQA), and symbolic reasoning (last letter concatenation, coin flip). Improvements were consistent across all domains, with the most dramatic gains on arithmetic tasks.

A critical finding was the scale dependence: CoT prompting only helped models above approximately 100 billion parameters. Below that threshold, models generated illogical reasoning chains that actually hurt performance compared to standard prompting. This established CoT as an [[concepts/emergent-abilities|emergent ability]] -- one that appears suddenly at sufficient scale.

The paper spawned an entire field of research into reasoning via prompting, leading to [[concepts/tree-of-thought|Tree of Thoughts]], [[concepts/self-consistency|self-consistency]], and ultimately the development of dedicated [[concepts/reasoning-models|reasoning models]] like OpenAI's o1/o3 and DeepSeek R1.

## Notable Quotes

> "Generating a chain of thought -- a series of intermediate reasoning steps -- significantly improves the ability of large language models to perform complex reasoning."

## Related Concepts

- [[concepts/chain-of-thought]] -- the core technique introduced
- [[concepts/llm-reasoning]] -- the broader capability this paper investigates
- [[concepts/emergent-abilities]] -- CoT as an example of emergence at scale
- [[concepts/self-consistency]] -- follow-up technique using majority voting over multiple CoT samples
- [[concepts/tree-of-thought]] -- generalization of CoT to tree-structured exploration
