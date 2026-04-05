---
title: "Claimify: Extracting High-Quality Claims from Language Model Outputs"
source: "https://www.microsoft.com/en-us/research/blog/claimify-extracting-high-quality-claims-from-language-model-outputs/"
author: "Microsoft Research"
date_published: 2025-05-01
date_ingested: 2026-04-05
tags: [claim-extraction, fact-checking, verification, LLM, information-extraction]
type: paper
status: raw
discovered_via: search
---

# Claimify: Extracting High-Quality Claims from Language Model Outputs

Accepted at ACL 2025.

## Problem

When language models produce complex outputs, breaking them into verifiable statements enables more effective fact-checking than evaluating entire texts at once. Traditional claim extraction methods suffer from four issues:

1. **Non-verifiable Content**: Extracting opinions and subjective statements alongside factual claims
2. **Incomplete Claims**: Omitting critical context or nuance
3. **Inaccurate Extraction**: Misrepresenting the source material's meaning
4. **Contextual Ambiguity**: Creating claims that lack sufficient context for independent verification

## Five Guiding Principles

- Claims must capture all verifiable content while excluding unverifiable material
- Each claim must be fully supported by source text
- Claims should be independently understandable
- Critical context must be preserved
- Ambiguous cases should be flagged rather than arbitrarily resolved

## Four-Stage Pipeline

### Stage 1 — Sentence Splitting
Breaks answers into sentences with surrounding context.

### Stage 2 — Selection
An LLM identifies non-verifiable sentences and rewrites mixed sentences to retain only verifiable components.

### Stage 3 — Disambiguation
Detects ambiguity and determines if context resolves it, labeling unresolvable cases.

### Stage 4 — Decomposition
Creates standalone claims while preserving essential context.

## Results

- 99% of claims extracted by Claimify are entailed by their source sentence
- Best balance between including verifiable content and excluding unverifiable material
- Least likely to omit context critical to fact-checking verdicts
- First system to identify multiple possible interpretations and extract claims only with high confidence

## Evaluation Metrics for Claim Extraction

Six metrics: Atomicity, Fluency, Decontextualization, Faithfulness, Focus, and Coverage.

## Applications Beyond Fact-Checking

Claimify is being used to evaluate LLM output quality, including assessing comprehensiveness and diversity in systems like GraphRAG.
