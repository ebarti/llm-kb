---
title: "Domain-Adaptive Pretraining (DAPT)"
type: concept
sources: ["[[sources/domain-adaptive-pretraining-dapt]]"]
related: ["[[concepts/fine-tuning]]", "[[concepts/continued-pretraining]]", "[[concepts/parameter-efficient-fine-tuning]]"]
last_compiled: 2026-04-05
summary: "Intermediate pretraining step on unlabeled domain text between general pretraining and task fine-tuning — requires no labeled data and consistently improves downstream performance."
---

## Overview

Domain-Adaptive Pretraining (DAPT) is a training strategy that adds an intermediate step between general pretraining and task-specific [[concepts/fine-tuning]]: continuing pretraining on large volumes of unlabeled, domain-specific text. This allows models to internalize domain terminology, structural patterns, and contextual nuances before seeing any labeled task data.

DAPT is foundational to the emerging three-layer architecture for domain LLM deployment:
1. **DAPT** — broad domain knowledge from unlabeled text
2. **Task fine-tuning** — specific skills from labeled examples
3. **RAG** — dynamic, traceable knowledge at inference time

## The Pipeline

**Traditional:** General Pretraining → Task Fine-Tuning

**With DAPT:** General Pretraining → Domain-Specific Pretraining → Task Fine-Tuning

The "Don't Stop Pretraining" paper (Gururangan et al., ACL 2020) demonstrated this pipeline consistently outperforms skipping DAPT across biomedical, computer science, news, and review domains.

## Key Properties

- **No labeled data required** — uses raw domain documents (medical journals, legal filings, technical manuals)
- **Enhances downstream fine-tuning** — models require less labeled data and achieve higher accuracy
- **Linguistic authenticity** — outputs match professional conventions and terminology
- **Reduced hallucination** — grounding in authentic domain materials decreases fabrication
- **Composable with TAPT** — combining DAPT with task-adaptive pretraining (TAPT) yields best results

## Relationship to [[concepts/continued-pretraining]]

DAPT is a specific form of continued pretraining with a domain focus. Continued pretraining is the broader category that includes:
- **DAPT**: Domain-specific unlabeled text
- **TAPT**: Task-specific unlabeled text (e.g., customer reviews for sentiment analysis)
- **Instruction pretraining**: Continued pretraining with instruction-format data

## Practical Considerations

- Well-adapted smaller models frequently outperform poorly adapted larger ones
- [[concepts/parameter-efficient-fine-tuning|LoRA]] can be used for compute-efficient DAPT
- Data pipeline quality directly determines DAPT effectiveness
- Typical implementation: ~12,500 training steps on domain materials with RoBERTa-scale models; more for larger models
- Risk of [[concepts/catastrophic-forgetting]] is lower than task fine-tuning because DAPT uses the same training objective as original pretraining

## Sector Applications

| Domain | Training Data | Downstream Tasks |
|--------|--------------|-----------------|
| Legal | Contracts, case law, compliance | Contract analysis, research |
| Healthcare | Clinical notes, medical literature | Diagnostics, documentation |
| Finance | Annual reports, regulatory filings | Risk assessment, fraud detection |
| Industrial | Technical manuals, SOPs | Troubleshooting, maintenance |

## Sources

- [[sources/domain-adaptive-pretraining-dapt]] — practical guide and sector applications

## Related Concepts

- [[concepts/fine-tuning]] — DAPT precedes and enhances task fine-tuning
- [[concepts/continued-pretraining]] — DAPT is a specific form
- [[concepts/parameter-efficient-fine-tuning]] — LoRA enables efficient DAPT
- [[concepts/catastrophic-forgetting]] — less risk during DAPT than task fine-tuning
