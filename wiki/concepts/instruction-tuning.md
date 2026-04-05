---
title: "Instruction Tuning"
type: concept
sources: ["[[sources/rlhf-preference-data-collection]]", "[[sources/huggingface-rlhf-illustrated]]", "[[sources/argilla-rlhf-alternatives-overview]]"]
related: ["[[concepts/preference-data]]", "[[concepts/rlhf]]", "[[concepts/dpo]]", "[[concepts/kto]]", "[[concepts/orpo]]", "[[concepts/training-data-curation]]", "[[concepts/synthetic-data-generation]]", "[[entities/flan]]"]
last_compiled: 2026-04-05
summary: "Fine-tuning a pretrained LLM on instruction-response pairs to make it follow human instructions — the bridge between raw pretraining and RLHF alignment, with dataset choice critically affecting which skills emerge."
---

## Overview

Instruction tuning (also called supervised fine-tuning or SFT) is the process of training a pretrained base model on curated datasets of instruction-response pairs. This transforms a next-token predictor into a model that can follow human instructions, answer questions, and complete tasks.

In the standard LLM training pipeline, instruction tuning sits between pretraining (learning language from web data) and [[concepts/rlhf]] alignment (learning human preferences). It is the step where models learn the *format* of helpful interaction.

## Major Datasets

| Dataset | Size | Construction | Key Characteristics |
|---------|------|--------------|-------------------|
| **FLAN Collection** | 1,836 tasks, 15M examples | Templates transform existing NLP datasets | Broadest task coverage |
| **OpenAssistant** | 161K messages, 66K conversation trees | Community-generated, 35 languages | Multilingual, dialogue-focused |
| **Dolly** | 15K examples | Databricks employees, human-generated | English only, ChatGPT-style |
| **Alpaca** | 52K examples | GPT-3.5-generated (synthetic) | Stanford, self-instruct method |
| **ShareGPT** | Varies | User-shared ChatGPT conversations | Real user interactions |

## Dataset-Skill Relationship

Research comparing instruction datasets reveals that **no single dataset provides the best performance across all evaluations**. Different datasets "uncover or enhance specific skills":

- FLAN excels at structured task completion due to its breadth of NLP task templates
- OpenAssistant produces more natural conversational behavior
- Synthetic datasets (Alpaca) provide cheap scaling but may lack the nuance of human-generated data
- Dolly provides focused instruction-following but limited diversity

This suggests that instruction dataset selection should be guided by the target use case rather than by aggregate benchmark scores.

## Construction Approaches

### Template-Based (FLAN)
Transform existing NLP datasets into instruction format using templates. Scales well but may not capture the natural diversity of real user instructions.

### Human-Generated (Dolly, OpenAssistant)
Collect instructions and responses directly from humans. Higher quality per example but expensive and harder to scale. Quality depends heavily on annotator selection and guidelines.

### Synthetic/Distilled (Alpaca, WizardLM)
Use a strong LLM (GPT-4, Claude) to generate instruction-response pairs. Cheaply scalable but limited by the capabilities and biases of the teacher model. Self-instruct and Evol-Instruct are key generation methodologies.

## Relationship to Pretraining Data Curation

An important finding from [[sources/dclm-datacomp-language-models]]: the most effective training data for quality classifiers used in pretraining curation (fastText filtering) came from instruction-formatted data (OpenHermes 2.5, ELI5). This suggests that instruction tuning data can inform pretraining curation, creating a connection between these traditionally separate stages.

## SFT in the Alignment Pipeline

Most successful LLM deployments use a three-stage pipeline where SFT is the critical middle step:

1. **Pretraining**: Next-token prediction on large corpora
2. **SFT (Instruction Tuning)**: Fine-tune on curated demonstrations
3. **Preference Optimization**: [[concepts/rlhf]], [[concepts/dpo]], [[concepts/kto]], or alternatives

[[concepts/orpo]] is notable for combining SFT and preference alignment into a single step, eliminating the separate stages.

Without preference optimization after SFT, models follow instructions but may produce unhelpful, unsafe, or verbose outputs. [[concepts/kto]] research showed that without prior SFT, DPO models ramble and hallucinate, while KTO remains stable -- highlighting the different robustness properties of post-SFT methods ([[sources/argilla-kto-kahneman-tversky]]).

## Sources

- [[sources/rlhf-preference-data-collection]] — instruction tuning as context for preference data
- [[sources/huggingface-rlhf-illustrated]] — SFT as step 1 of the RLHF pipeline
- [[sources/argilla-rlhf-alternatives-overview]] — SFT's role across alignment methods

## Related Concepts

- [[concepts/preference-data]] — the next stage after instruction tuning
- [[concepts/rlhf]] — uses instruction-tuned model as starting point
- [[concepts/dpo]] — a popular preference optimization method applied after SFT
- [[concepts/kto]] — alternative that is more robust without prior SFT
- [[concepts/orpo]] — combines SFT and preference alignment in one step
- [[concepts/training-data-curation]] — instruction data informs pretraining curation
- [[concepts/synthetic-data-generation]] — synthetic instruction generation methods
