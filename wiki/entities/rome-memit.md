---
title: "ROME and MEMIT"
type: entity
entity_type: paper
sources: ["[[sources/rome-memit-knowledge-editing]]"]
related: ["[[concepts/knowledge-editing]]", "[[concepts/catastrophic-forgetting]]"]
last_compiled: 2026-04-05
summary: "Pioneering knowledge editing methods: ROME makes rank-one MLP modifications for single fact edits; MEMIT scales to thousands of simultaneous edits across transformer layers."
---

## Overview

ROME (Rank-One Model Editing) and MEMIT (Mass-Editing Memory in a Transformer) are research systems from David Bau's lab that pioneered the field of [[concepts/knowledge-editing]] — precisely modifying factual associations stored in language model weights without full retraining.

## ROME

**Paper**: "Locating and Editing Factual Associations in GPT" (Meng, Bau et al.)

ROME's two-step approach:
1. **Causal tracing**: Identify where factual knowledge is stored by corrupting inputs and selectively restoring hidden states → facts concentrate in MLP modules at middle layers
2. **Rank-one editing**: Treat MLP as key-value store; make a rank-one matrix modification to insert a new key-value pair

**Key result**: Edits both generalize (work across paraphrases) and maintain specificity (don't affect unrelated facts).

## MEMIT

**Paper**: "Mass-Editing Memory in a Transformer"

MEMIT extends ROME to batch-edit thousands of facts by modifying MLP weights across multiple critical layers simultaneously. Enables large-scale knowledge updates in a single operation.

## Evaluation Dataset

**CounterFact**: Dataset of thousands of counterfactual statements with paraphrases, enabling quantitative measurement of edit specificity and generalization.

## Follow-up Work (2025)

- **MAKE**: Memory-Associated Knowledge Editing — accounts for associated knowledge transfer
- **NAMET**: Noise-injection variant of MEMIT (one-line modification)
- **EasyEdit2**: Open-source framework unifying multiple editing methods

## Limitations

Sequential ROME edits cause progressive degradation: gradual forgetting → loss of specificity → catastrophic failure. This fundamentally limits knowledge editing as a continuous update strategy.

## Mentioned In

- [[sources/rome-memit-knowledge-editing]] — primary source
- [[concepts/knowledge-editing]] — the methodology these systems pioneer
