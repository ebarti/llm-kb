---
title: "Source: A Practical Guide to Domain-Adaptive Pretraining"
type: source-summary
source: "[[raw/domain-adaptive-pretraining-dapt]]"
related: ["[[concepts/domain-adaptive-pretraining]]", "[[concepts/fine-tuning]]", "[[concepts/continued-pretraining]]"]
last_compiled: 2026-04-05
summary: "DAPT adds an intermediate domain-specific pretraining step between general pretraining and task fine-tuning; operates on unlabeled data; combined with TAPT yields best results."
reading_time: "2 min"
---

## Key Points

- DAPT inserts domain-specific pretraining between general pretraining and task fine-tuning
- Uses unlabeled domain text — no annotation required (medical journals, legal docs, financial filings)
- DAPT + TAPT (task-adaptive pretraining) outperforms either alone
- Four benefits: no labeling needed, enhanced downstream fine-tuning, linguistic authenticity, reduced hallucination
- Well-adapted smaller models frequently outperform poorly adapted larger ones
- Three-stage implementation: foundational knowledge → domain specialization → task optimization
- Foundational paper: "Don't Stop Pretraining" (Gururangan et al., ACL 2020)

## Detailed Summary

DAPT represents a middle path between expensive full pretraining and narrow task-specific fine-tuning. By continuing pretraining on large volumes of unlabeled domain text, models internalize terminology, structural patterns, and contextual nuances before seeing any labeled examples. This is particularly valuable in domains where labeled data is scarce but raw text is abundant (medical literature, legal filings, industrial manuals).

The key practical insight: the DAPT pipeline (General Pretraining → Domain-Specific Pretraining → Task Fine-Tuning) consistently outperforms skipping the middle step, and combining DAPT with task-adaptive pretraining (TAPT) yields the best results across all tested domains.

## Related Concepts

- [[concepts/domain-adaptive-pretraining]] — the core methodology
- [[concepts/continued-pretraining]] — DAPT is a form of continued pretraining
- [[concepts/fine-tuning]] — DAPT precedes and enhances fine-tuning
- [[concepts/parameter-efficient-fine-tuning]] — LoRA can be used for efficient DAPT
