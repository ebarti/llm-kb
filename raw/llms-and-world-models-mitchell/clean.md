---
title: "LLMs and World Models, Part 1"
source: "https://aiguide.substack.com/p/llms-and-world-models-part-1"
author: "Melanie Mitchell"
date_published: 2024-03-15
date_ingested: 2026-04-05
tags: [world-models, LLMs, understanding, philosophy-of-AI, Othello-GPT]
type: article
status: raw
discovered_via: search
---

# LLMs and World Models (Melanie Mitchell)

## Arguments FOR World Models in LLMs
- Ilya Sutskever (OpenAI): LLMs develop "compressed, abstract, usable representation" of the world through next-word prediction
- Training on vast text allows extraction of patterns reflecting real-world structure
- Language inherently encodes causal relationships and world knowledge

## Arguments AGAINST
- Kambhampati (ASU) & LeCun: LLMs succeed through "approximate retrieval" not genuine understanding
- LeCun: "A system trained on language alone will never approximate human intelligence, even if trained from now until the heat death of the universe"
- No direct sensorimotor feedback or causal intervention
- Lack embodied understanding

## Community Split
- 2022 NLP researcher survey: near 50-50 on whether text-trained models could achieve genuine language understanding

## Pre-LLM Cautionary Examples
1. Skin lesion classification: learned "rulers indicate malignancy" not actual lesions
2. Sentence implication: exploited word-overlap shortcuts
3. Atari Breakout: moving paddle pixels broke performance

## Definitions of "World Models" (Three Characteristics)
1. Internal representations capturing external phenomena
2. Preservation of causal structure, not just statistical patterns
3. Algorithmic efficiency enabling prediction and counterfactual reasoning

## The Orrery Spectrum (Jacob Andreas)
- Lookup tables → Maps → Orreries → Simulators
- LLMs at most "orrery-like" (tracking narrative dynamics), not true causal simulators

## Unresolved Questions
- What constitutes genuine "understanding"?
- Can statistical pattern-matching produce causal models?
- What mechanism serves as the "user" of internal representations?
