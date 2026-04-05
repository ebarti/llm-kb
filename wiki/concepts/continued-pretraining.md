---
title: "Continued Pretraining"
type: concept
sources: ["[[sources/domain-adaptive-pretraining-dapt]]", "[[sources/textbooks-are-all-you-need-phi]]"]
related: ["[[concepts/domain-adaptive-pretraining]]", "[[concepts/fine-tuning]]", "[[concepts/catastrophic-forgetting]]"]
last_compiled: 2026-04-05
summary: "Extending a model's pretraining phase on new corpora (domain text, synthetic data, or instruction data) to broaden or specialize its knowledge before task-specific fine-tuning."
---

## Overview

Continued pretraining (CPT) is the practice of resuming the original pretraining process of a foundation model on new data. Unlike [[concepts/fine-tuning]], which trains on labeled task-specific examples with a supervised objective, continued pretraining typically uses the same self-supervised objective (next-token prediction or masked language modeling) as the original pretraining.

This is the deepest way to inject new knowledge into model weights — short of training from scratch — and is the mechanism behind [[concepts/domain-adaptive-pretraining]] (DAPT).

## Variants

| Variant | Data Source | Purpose |
|---------|------------|---------|
| [[concepts/domain-adaptive-pretraining\|DAPT]] | Unlabeled domain text | Domain expertise |
| TAPT | Unlabeled task-specific text | Task-relevant language patterns |
| Instruction CPT | Instruction-format data | Instruction following during pretraining |
| Synthetic CPT | [[concepts/synthetic-data-generation\|Synthetic]] textbooks/exercises | "Textbook quality" knowledge (Phi models) |

## When to Use

Continued pretraining is appropriate when:
- The target domain has substantially different vocabulary and patterns from web text
- Large volumes of unlabeled domain text are available
- Downstream fine-tuning alone yields insufficient quality
- You need the model to "speak the language" of a domain natively

## Risks

- Higher compute cost than fine-tuning (many more tokens processed)
- [[concepts/catastrophic-forgetting]] of general capabilities if overfit to narrow domain
- Requires careful learning rate scheduling to avoid destabilizing pretrained representations

## Sources

- [[sources/domain-adaptive-pretraining-dapt]] — DAPT as continued pretraining
- [[sources/textbooks-are-all-you-need-phi]] — synthetic data continued pretraining for Phi models

## Related Concepts

- [[concepts/domain-adaptive-pretraining]] — most common form of CPT
- [[concepts/fine-tuning]] — task-specific training that follows CPT
- [[concepts/catastrophic-forgetting]] — risk during CPT if not carefully managed
