---
title: "ROME and MEMIT: Locating and Editing Factual Associations in LLMs"
source: "https://rome.baulab.info/"
author: "Kevin Meng, David Bau et al."
date_published: 2022-12-01
date_ingested: 2026-04-05
tags: [knowledge-editing, model-editing, rome, memit, factual-associations]
type: paper
status: raw
discovered_via: search
---

# ROME and MEMIT: Knowledge Editing in LLMs

## ROME: Rank-One Model Editing

### Core Methodology — Causal Tracing
The researchers developed causal tracing to identify where factual information flows through a network. This technique involves running a network multiple times, introducing corruptions to frustrate the computation, and then restoring individual states to pinpoint critical computations. The analysis reveals that factual retrieval concentrates in specific MLP modules at middle layers, particularly during processing of the final subject token.

### Factual Localization
Three key dimensions for fact storage:
- **Location type**: MLP module parameters rather than attention mechanisms
- **Layer depth**: Middle layers of the transformer
- **Processing stage**: During the last token of the subject entity

### The ROME Algorithm
ROME treats MLP modules as key-value stores. The method makes a rank-one modification of the MLP weights to directly write in a new key-value pair. Rather than modifying individual neurons, ROME updates entire parameter matrices using low-rank changes, preserving model stability.

### Knowledge vs. Surface Learning
- **Specificity**: Changes to one fact should not affect unrelated facts
- **Generalization**: Modified knowledge should apply across paraphrases and contextually different prompts

### Key Results
ROME demonstrated superior performance: high efficacy on counterfactual statements, excellent specificity leaving neighboring facts unchanged, and strong generalization to paraphrased queries. Editing attention mechanisms at later layers achieved fair efficacy and specificity but completely failed to generalize.

## MEMIT: Mass-Editing Memory in a Transformer

MEMIT extends ROME to insert thousands of memories by modifying the MLP weights of a range of critical layers. It enables thousands of edits without significant influence on editing accuracy.

## Limitations

Sequential ROME edits induce gradual forgetting of prior facts and degrade downstream performance, leading to an abrupt catastrophic forgetting phase with neighborhood specificity gradually being lost.

## Recent Developments (2025)

- **MAKE (Memory-Associated Knowledge Editing)**: Takes into account the transfer of associated knowledge
- **NAMET**: Introduces noise during memory extraction via one-line modification to MEMIT
- **EasyEdit2**: Framework for editing LLMs with precision and flexibility
- **RelEdit**: Evaluating conceptual knowledge editing

## Dataset
CounterFact: dataset of thousands of counterfactual statements with associated paraphrases for evaluating editing specificity and generalization.
