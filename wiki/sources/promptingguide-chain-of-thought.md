---
title: "Source: Chain-of-Thought Prompting (Prompt Engineering Guide)"
type: source-summary
source: "[[raw/promptingguide-chain-of-thought]]"
related: ["[[concepts/chain-of-thought-prompting]]", "[[concepts/zero-shot-prompting]]", "[[concepts/prompt-engineering]]"]
last_compiled: 2026-04-05
summary: "DAIR.AI overview of CoT prompting: Wei et al. (2022) technique enabling complex reasoning via intermediate steps, plus Zero-Shot CoT and Auto-CoT variants."
reading_time: "2 min"
---

## Key Points
- CoT prompting decomposes problems into intermediate reasoning steps before providing final answers
- Introduced by Wei et al. (2022) as an "emergent ability that arises with sufficiently large language models"
- Zero-Shot CoT (Kojima et al. 2022) requires only appending "Let's think step by step"
- Auto-CoT (Zhang et al. 2022) automates demonstration creation via clustering and sampling
- Even invalid demonstrations achieve 80-90% of full CoT performance — relevance and step ordering matter more

## Detailed Summary
Chain-of-thought prompting is arguably the single most impactful [[concepts/prompt-engineering]] technique for reasoning tasks. By encouraging models to "show their work," CoT transforms tasks that LLMs fail at (arithmetic, logic, commonsense reasoning) into tasks they can handle reliably. The technique works by providing few-shot examples that include reasoning chains, which the model then mimics for novel problems.

The practical sweet spot for prompt length is 150-300 words. A 2025 Wharton study found diminishing returns for reasoning-heavy models, but CoT remains valuable for interpretability in high-stakes applications.

## Notable Quotes
> "An emergent ability that arises with sufficiently large language models." — Wei et al. (2022)

## Related Concepts
- [[concepts/chain-of-thought-prompting]] — the core technique
- [[concepts/zero-shot-prompting]] — CoT's simpler variant
- [[concepts/self-consistency-prompting]] — builds on CoT with majority voting
- [[concepts/tree-of-thoughts-prompting]] — generalizes CoT into search trees
