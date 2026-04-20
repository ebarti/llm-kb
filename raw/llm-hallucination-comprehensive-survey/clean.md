---
title: "Large Language Models Hallucination: A Comprehensive Survey"
source: "https://arxiv.org/abs/2510.06265"
author: "Alansari, A. & Luqman, H."
date_published: 2025-10-01
date_ingested: 2026-04-05
tags: [hallucination, llm, detection, mitigation, survey]
type: paper
status: raw
discovered_via: search
---

# Large Language Models Hallucination: A Comprehensive Survey

## Definition

Hallucinations represent a critical challenge where LLMs generate text appearing reasonable but lacking factual grounding — distinct from creative outputs that are deliberate and goal-driven. The text is "fluent and syntactically correct but factually inaccurate or unsupported by external evidence."

## Classification Framework

**Intrinsic vs. Extrinsic:**
- Intrinsic hallucinations contradict source documents directly
- Extrinsic hallucinations introduce unverified additional content

**Factuality vs. Faithfulness:**
- Factuality hallucinations: Divergence from real-world facts (contradiction or fabrication)
- Faithfulness hallucinations: Drift from original input, including instruction, context, and logical inconsistencies

## Causes Across Development Pipeline

### 1. Data Curation Stage
- Biases in training data reflecting societal imbalances
- Imitative falsehoods: Models reproducing embedded misinformation
- Knowledge conflicts: Contradictory information from multiple sources
- Domain knowledge deficiency: Lack of specialized training data
- Temporal misalignment: Outdated factual knowledge beyond training cutoff
- Long-tail knowledge: Underrepresentation of rare entities

### 2. Model Architecture
- Attention mechanism limitations: Soft attention struggles with long sequences
- Objective function issues: MLE lacks explicit factual consistency penalties
- Positional encoding degradation with longer sequences
- Unidirectional contextualization in autoregressive models

### 3. Pre-training Stage
- Shortcut learning: Reliance on superficial patterns
- Teacher forcing/exposure bias: Discrepancy between training and inference
- Cascade effects: Early errors compound
- Insufficient negative examples

### 4. Fine-tuning Stage
- Task-specific overfitting
- Capability misalignment: Alignment training encouraging definitive answers despite insufficient knowledge
- Belief misalignment: Divergence between pre-training knowledge and alignment expectations
- Sycophantic behavior: Generating responses evaluators will approve regardless of accuracy

### 5. Inference Stage
- Ambiguous prompts
- Sampling randomness (top-k, nucleus sampling)
- SoftMax bottleneck
- Reasoning limitations in multi-hop tasks

## Detection Taxonomy

### 1. Retrieval-Based Detection
Uses external knowledge to verify outputs. Includes RAG-based methods, dynamic retrieval, span-level identification (FAVA), and multi-form factual checking (KnowHalu).

### 2. Uncertainty-Based Detection
Flags low-confidence outputs: token-based approaches (sequence log-probability), semantic-based (semantic entropy, belief tree propagation), supervised (pre-trained uncertainty heads).

### 3. Embedding-Based Detection
Similarity-based (LaBSE, LASER, XNLI), gradient-based (Taylor series expansion), spectral-based (HalluShift, graph Laplacian features).

### 4. Learning-Based Detection
Supervised (ExHalder, RIPA, PRISM), unsupervised (Lookback Lens attention analysis), agent-based (HaluAgent multi-stage pipelines).

### 5. Self-Consistency-Based Detection
Multiple responses evaluated for consistency: SelfCheckGPT, MetaQA with prompt mutations, SAC3 cross-model verification.

## Mitigation Taxonomy

### 1. Prompt-Based Techniques
Template-based, instruction-based (SELF-EXPERTISE), tag-based with domain markers, in-context learning.

### 2. Retrieval-Based Techniques
Before generation (pre-retrieval), during generation (iterative refinement), after generation (RARR post-hoc checking). RAG-HAT for hallucination-aware tuning. Knowledge Graphs: ERNIE 3.0, KGLM, KG-Adapter, FOLK, KAPING.

### 3. Reasoning-Based Techniques
Chain-of-Thought (CoT) with self-consistency, iterative refinement loops, Chain-of-Verification (CoV).

### 4. Model-Centric Training
Dual-encoder designs, contrastive learning, hallucination-aware fine-tuning, hybrid approaches.

## Key Benchmarks
TruthfulQA, HaluEval, HotpotQA, CNN/DailyMail, WikiBio, FEVER, SQuAD, WMT, Mu-SHROOM (SemEval 2025), CCHall (ACL 2025), REFIND (SemEval 2025).

## Key Finding
No single approach completely eliminates hallucination; complementary combinations (e.g., learning with uncertainty, retrieval with reasoning) show greatest promise.
