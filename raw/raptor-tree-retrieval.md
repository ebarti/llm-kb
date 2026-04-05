---
title: "RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval"
source: "https://arxiv.org/abs/2401.18059"
author: "Sarthi, Abdullah et al."
date_published: 2024-01-31
date_ingested: 2026-04-05
tags: [raptor, retrieval, tree-structure, clustering, abstractive-summarization, rag]
type: paper
status: raw
discovered_via: search
---

# RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval

## Overview

RAPTOR introduces a novel approach to retrieval-augmented language models by constructing a hierarchical tree through recursive clustering and summarization, addressing limitations in traditional chunk-based retrieval.

## Core Methodology

### Tree Construction

1. Segment documents into 100-token chunks, embed using SBERT (leaf nodes)
2. Cluster semantically similar chunks using Gaussian Mixture Models (soft clustering)
3. Generate summaries of each cluster via language models (gpt-3.5-turbo)
4. Repeat iteratively upward, creating multiple abstraction levels

### Clustering Mechanism

RAPTOR employs soft clustering via GMMs, allowing text segments to belong to multiple clusters. Uses UMAP for dimensionality reduction and Bayesian Information Criterion for determining optimal cluster counts.

### Summarization

Approximately 4% of summaries contained minor hallucinations that "did not propagate to parent nodes and had no discernible impact on question-answering tasks."

## Retrieval Strategies

**Tree Traversal:** Starts at root, selects top-k nodes by cosine similarity, descends through child nodes layer-by-layer.

**Collapsed Tree:** Flattens entire structure and retrieves nodes across all layers simultaneously until reaching a token threshold. Testing showed collapsed tree performed consistently better.

## Experimental Results

- **QASPER:** 55.7% F-1 Match with GPT-4 (surpassing DPR by 2.7 points, BM25 by 5.5 points)
- **QuALITY:** 82.6% accuracy with GPT-4 (previous best: 62.3%) — 20% absolute improvement
- **NarrativeQA:** New METEOR score benchmark with UnifiedQA

Layer analysis: 18.5-57% of retrieved nodes came from non-leaf layers, demonstrating value of multi-layered summaries.

## Significance

RAPTOR scales linearly in token expenditure and build time. Effectively addresses "the limitation that most existing methods retrieve only short contiguous chunks," enabling holistic document understanding for complex, multi-step reasoning.
