---
title: "Claimify"
type: entity
entity_type: tool
sources: ["[[sources/claimify-claim-extraction]]"]
related: ["[[concepts/claim-extraction]]", "[[concepts/information-extraction]]", "[[concepts/hallucination-contamination]]"]
last_compiled: 2026-04-05
summary: "Microsoft Research's 4-stage claim extraction system (ACL 2025) that decomposes LLM outputs into atomic verifiable claims with 99% source entailment."
---

## Overview

Claimify is a claim extraction system developed by Microsoft Research, accepted at ACL 2025. It decomposes complex LLM-generated text into simple, independently verifiable factual claims.

## Four-Stage Pipeline

1. **Sentence Splitting**: Segments text while preserving surrounding context
2. **Selection**: LLM identifies and filters non-verifiable content (opinions, hedges)
3. **Disambiguation**: Detects ambiguity; flags unresolvable cases
4. **Decomposition**: Creates standalone atomic claims

## Key Results

- 99% of extracted claims are entailed by their source sentence
- Best balance between including verifiable content and excluding unverifiable material
- First system to handle multiple possible interpretations by flagging rather than guessing

## Applications

- Fact-checking LLM outputs
- Evaluating LLM quality (comprehensiveness, diversity)
- Quality assessment of systems like GraphRAG

## Mentioned In

- [[sources/claimify-claim-extraction]] — full methodology and results
