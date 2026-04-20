---
title: "RAFT: Adapting Language Model to Domain Specific RAG"
source: "https://gorilla.cs.berkeley.edu/blogs/9_raft.html"
author: "Tianjun Zhang, Shishir G. Patil (UC Berkeley)"
date_published: 2024-03-15
date_ingested: 2026-04-05
tags: [raft, rag, fine-tuning, domain-adaptation, retrieval]
type: paper
status: raw
discovered_via: search
---

# RAFT: Retrieval Augmented Fine-Tuning

## Core Concept

RAFT is a fine-tuning methodology designed to optimize language models for domain-specific retrieval-augmented generation. The technique trains models to disregard any retrieved documents that do not contribute to answering a given question, using chain-of-thought reasoning with direct quotations from relevant source material.

## Training Methodology

The RAFT training recipe employs a distinctive data preparation strategy:

- **P% of training data**: Questions paired with oracle documents (containing answers) plus distractor documents
- **(1-P)% of training data**: Questions with only distractor documents, forcing knowledge memorization

This mixed approach compels the model to internalize domain knowledge while remaining robust to irrelevant retrieved documents.

## Training Data Structure

The framework requires:
- Questions (Q)
- Document collections (Dk) with oracle documents (D*) and distractors (Di)
- Chain-of-thought style answers with explicit quotation markers (##begin_quote## and ##end_quote##)

The quotation mechanism prevents hallucination by anchoring responses to source material.

## Evaluation Results

- **HotpotQA**: Up to 35.25% improvement over instruction-tuned baselines
- **TorchHub**: 76.35% improvement when combined with RAG
- **HuggingFace datasets**: 31.41% gain over domain-specific fine-tuning alone

RAFT consistently outperformed comparable approaches across all tested domains including PubMed QA, Natural Questions, TriviaQA, HotpotQA, and Gorilla API Bench.

## Technical Implementation

Base model: Llama2-7B, chosen for balance of reasoning capability, reasonable latency, and deployment feasibility on standard hardware (4 A100-40G GPUs for training; single GPU deployment).

## Key Insight

Standard approaches resemble studying without the textbook or practicing without access to reference materials you'll actually have during the test. RAFT teaches models to intelligently evaluate document relevance and extract meaningful content while filtering noise.
