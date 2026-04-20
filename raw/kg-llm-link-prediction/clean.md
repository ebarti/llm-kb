---
title: "Knowledge Graph Large Language Model (KG-LLM) for Link Prediction"
source: "https://arxiv.org/abs/2403.07311"
author: "Various (arXiv)"
date_published: 2024-03-11
date_ingested: 2026-04-05
tags: [knowledge-graph, llm, link-prediction, knowledge-graph-completion, fine-tuning]
type: paper
status: raw
discovered_via: search
---

# KG-LLM: Knowledge Graph Large Language Model for Link Prediction

## Architecture and Framework

The KG-LLM framework operates in two stages:
1. Knowledge graph paths undergo preprocessing to transform into chain-of-thought prompts
2. Three LLMs — Flan-T5-Large, LLaMA2-7B, and Gemma-7B — undergo instruction fine-tuning

For LLaMA2 and Gemma, 4-bit quantized LoRA modification applies minimal parameter adjustments for efficiency.

## Knowledge Graph to Natural Language Conversion

The system converts structured triples into natural language statements. For instance, a path like (Node1, relation_x, Node2) becomes: "Node [node_id1] has relation [relation_id] with node [node_id2]." This representation enables LLMs to reason through multi-hop relationships step-by-step.

## Fine-Tuning Methodology

The framework employs instruction fine-tuning with cross-entropy loss across output token sequences. Two prompt variants were tested:

- **KG-LLM prompt**: Structured format with explicit instructions and binary/multi-choice options
- **Ablation prompt**: Simplified format without instructional guidance

Training utilized 2 epochs on A40 GPU with maximum 10-node complexity and 512-token limits for Flan-T5 compatibility.

## Evaluation on Benchmarks

Two datasets were tested: WN18RR (40,943 entities) and NELL-995 (75,492 entities).

**Multi-hop Link Prediction (without ICL):**
- Gemma-7B (KG-LLM): F1=0.84 (WN18RR), F1=0.82 (NELL-995)
- Traditional methods (TransE, ComplEx, DistMult): F1 ranges 0.25-0.61

**Multi-hop Link Prediction (with ICL):**
- Gemma-7B (KG-LLM): F1=0.98 (WN18RR), F1=0.95 (NELL-995)

## Comparison with Traditional Methods

Traditional embedding approaches demonstrated significantly lower performance. The paper notes that "the performance of traditional models is not ideal," attributing this to complexity challenges in multi-hop reasoning requiring consideration of intermediate entities beyond direct pairwise links.

## Key Results

The KG-LLM framework substantially outperformed both traditional embedding methods and ablation variants. In-context learning integration produced dramatic gains, particularly for relation prediction tasks on unseen prompts, achieving 76% accuracy for Gemma-7B on NELL-995 when augmented with ICL examples.
