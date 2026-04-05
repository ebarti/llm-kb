---
title: "Chain-of-Thought Prompting"
type: concept
sources: ["[[sources/promptingguide-chain-of-thought]]", "[[sources/anthropic-claude-prompting-best-practices]]", "[[sources/lakera-prompt-engineering-guide]]"]
related: ["[[concepts/prompt-engineering]]", "[[concepts/self-consistency-prompting]]", "[[concepts/tree-of-thoughts-prompting]]", "[[concepts/zero-shot-prompting]]", "[[concepts/few-shot-prompting]]"]
last_compiled: 2026-04-05
summary: "Wei et al. (2022) technique that enables complex reasoning by having LLMs decompose problems into intermediate steps — the single most impactful prompting technique for reasoning tasks."
---

## Overview

Chain-of-Thought (CoT) prompting is arguably the single most transformative technique in [[concepts/prompt-engineering]]. Introduced by Wei et al. (2022), CoT enables large language models to solve complex reasoning problems by encouraging them to articulate intermediate steps before arriving at a final answer. Tasks that LLMs fail at with direct prompting — arithmetic, multi-step logic, commonsense reasoning — become solvable when the model "shows its work."

The core insight is deceptively simple: instead of asking for just an answer, ask for the reasoning process. This works because it forces the model to decompose complex problems, maintain intermediate state, and catch errors before they propagate to the final answer.

## How It Works

CoT prompting comes in several variants, all sharing the principle of explicit reasoning:

### Few-Shot CoT (Original)
Provide examples that include reasoning chains alongside the answer:

```
Q: Roger has 5 tennis balls. He buys 2 more cans of 3. How many does he have?
A: Roger started with 5 balls. 2 cans of 3 is 6 balls. 5 + 6 = 11. The answer is 11.

Q: The cafeteria had 23 apples. They used 20 and bought 6 more. How many?
A: [Model generates reasoning chain here]
```

### Zero-Shot CoT
Kojima et al. (2022) discovered that simply appending "Let's think step by step" to a prompt achieves comparable improvements without any examples. This is especially valuable when demonstration examples are scarce.

### Auto-CoT
Zhang et al. (2022) automated the creation of CoT demonstrations:
1. Cluster dataset questions by similarity
2. Select representative questions from each cluster
3. Generate reasoning chains automatically
4. Use heuristics (question length <= 60 tokens, reasoning <= 5 steps) for quality control

## Key Research Findings

**Emergent ability.** CoT is described as "an emergent ability that arises with sufficiently large language models." It is less effective with smaller models, and improvements scale with model size.

**Robustness to demonstration quality.** Surprisingly, even invalid demonstrations achieve 80-90% of the performance of correct CoT demonstrations. What matters most is:
- Relevance to the query
- Correct ordering of reasoning steps
- Having the right format/structure

Label accuracy is less critical than structure — echoing findings from [[concepts/few-shot-prompting]] research.

**Optimal prompt length.** Research finds the practical sweet spot for most tasks is 150-300 words. LLM reasoning performance starts degrading around 3,000 tokens.

**Diminishing returns for reasoning models.** A 2025 Wharton study found that for models with native reasoning capabilities (o1, Claude with extended thinking), explicit CoT adds only marginal benefits at 20-80% higher cost. However, CoT remains valuable for interpretability in high-stakes applications.

## Relationship to Other Techniques

CoT is the foundation for a family of increasingly sophisticated reasoning techniques:

- **[[concepts/self-consistency-prompting]]** — Generate multiple CoT paths, take majority vote
- **[[concepts/tree-of-thoughts-prompting]]** — Generalize CoT into a search tree with backtracking
- **[[concepts/prompt-chaining]]** — Externalize CoT into separate API calls for inspection

Anthropic's guide notes that for Claude 4.6, "Think thoroughly" as a general instruction often produces better reasoning than prescriptive step-by-step plans, because the model's internal reasoning can exceed what a human would prescribe.

## Practical Application to This KB

This knowledge base uses CoT-style reasoning implicitly in several operations:
- **COMPILE**: The LLM reasons through raw sources to identify concepts, entities, and relationships
- **Q&A**: The model reads summaries, navigates to relevant articles, then synthesizes answers
- **LINT**: Health checks require multi-step reasoning about consistency and completeness

Explicitly asking the LLM to "reason through" its compilation or Q&A process could improve quality.

## Sources
- [[sources/promptingguide-chain-of-thought]] — Foundational overview with all variants
- [[sources/anthropic-claude-prompting-best-practices]] — Claude-specific CoT guidance (adaptive thinking)
- [[sources/lakera-prompt-engineering-guide]] — CoT as core technique in the technique taxonomy

## Related Concepts
- [[concepts/prompt-engineering]] — parent domain
- [[concepts/self-consistency-prompting]] — multi-path extension of CoT
- [[concepts/tree-of-thoughts-prompting]] — tree-structured extension of CoT
- [[concepts/zero-shot-prompting]] — CoT's minimal variant
- [[concepts/few-shot-prompting]] — CoT's example-based variant
