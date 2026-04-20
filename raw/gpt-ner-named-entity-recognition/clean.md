---
title: "GPT-NER: Named Entity Recognition via Large Language Models"
source: "https://arxiv.org/abs/2304.10428"
author: "Shuhe Wang, Xiaofei Sun, Xiaoya Li, Rongbin Ouyang, Fei Wu, Dayiheng Liu, Tianwei Lan, Jiwei Li"
date_published: 2023-04-20
date_ingested: 2026-04-05
tags: [named-entity-recognition, NER, LLM, few-shot-learning, sequence-labeling]
type: paper
status: raw
discovered_via: search
---

# GPT-NER: Named Entity Recognition via Large Language Models

Published at NAACL 2025 Findings (ACL Anthology: 2025.findings-naacl.239).

## Problem Statement

Despite LLMs achieving SOTA performances on a variety of NLP tasks, their performance on NER remains significantly below supervised baselines. This is due to a fundamental gap: NER is a sequence labeling task in nature, while LLMs are text-generation models.

## Methodology

GPT-NER bridges this gap by transforming the sequence labeling task into a generation task that can be easily adapted by LLMs. For example, the task of finding location entities in "Columbus is a city" is transformed to generate "@@Columbus## is a city," where special tokens @@## mark the entity to extract.

### Self-Verification Strategy

To combat LLM hallucination — where models over-confidently label empty inputs as entities — GPT-NER implements a self-verification strategy. This prompts the LLM to confirm whether extracted entities correspond to labeled entity categories.

## Key Results

- Achieves performance comparable to fully supervised baselines on five NER datasets (first-time achievement for LLM-based NER)
- Demonstrates superior performance in low-resource and few-shot scenarios
- When labeled training data is extremely scarce, GPT-NER performs significantly better than supervised models

## Significance for Information Extraction

GPT-NER proves that LLMs can match supervised NER systems with appropriate task reformulation. The sequence-to-generation transformation pattern is generalizable to other sequence labeling tasks. The self-verification strategy addresses a core challenge in LLM-based extraction: hallucinated entities.

## Related Work: Nested NER

Nested Named Entity Recognition (entities within entities) poses an additional challenge. Research at EMNLP 2024 explores specific reasoning techniques and instructions to improve LLM efficacy for nested NER, where traditional flat NER approaches fail.
