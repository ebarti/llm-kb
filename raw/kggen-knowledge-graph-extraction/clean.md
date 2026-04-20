---
title: "KGGen: Extracting Knowledge Graphs from Plain Text with Language Models"
source: "https://arxiv.org/abs/2502.09956"
author: "Various (arXiv)"
date_published: 2025-02-14
date_ingested: 2026-04-05
tags: [knowledge-graph, llm, extraction, entity-resolution, benchmark]
type: paper
status: raw
discovered_via: search
---

# KGGen: Extracting Knowledge Graphs from Plain Text with Language Models

## Core Architecture

KGGen employs a three-stage modular pipeline implemented as a Python library: (1) entity and relation extraction, (2) aggregation across sources, and (3) iterative clustering. The system uses GPT-4o with the DSPy framework to ensure consistent JSON-formatted outputs.

## Stage 1: Generate Module (Extraction)

The extraction follows a two-step approach:
- First LLM call identifies key entities (nouns, verbs, adjectives)
- Second call extracts subject-predicate-object triples using the identified entities

This two-step method "works better to ensure consistency between entities."

## Stage 2: Aggregate Module

All extracted entities and edges are collected across documents, normalized to lowercase, and consolidated into a unified graph. This step requires no LLM involvement — pure data processing.

## Stage 3: Cluster Module (Entity Resolution)

KGGen's distinguishing feature is "iterative LLM-based clustering" inspired by crowd-sourcing strategies:

1. The LLM examines the complete entity list attempting to extract single clusters
2. Validation occurs via "LLM-as-a-Judge" binary confirmation
3. Successful clusters receive semantic labels and are removed from the working list
4. Process repeats until n iterations pass without successful clustering
5. Remaining entities checked batch-by-batch (size b) against existing clusters

Clustering handles variations in "tense, plurality, stemming, or capitalization" — for instance, "vulnerabilities" and "weaknesses" get merged.

## MINE Benchmark

The authors introduced MINE (Measure of Information in Nodes and Edges) — "the first benchmark that measures a knowledge-graph extractor's ability to capture and distill a body of text into a KG."

**MINE Methodology:**
- 100 Wikipedia-length articles (~1,000 words) across diverse topics
- 15 manually-verified facts extracted per article
- Extracted KGs queried using semantic similarity (all-MiniLM-L6-v2 embeddings)
- Results evaluated with binary LLM judgment: whether facts can be inferred from retrieved nodes and their two-hop neighborhood

## Performance Results

KGGen achieved 66.07% accuracy on MINE, substantially outperforming:
- GraphRAG: 47.80%
- OpenIE: 29.84%

This represents an 18% improvement over the nearest competitor.

**Qualitative advantages:**
- Denser, more coherent graphs with better interconnectivity
- Fewer redundant entities compared to OpenIE's verbose node labels
- More comprehensive information capture versus GraphRAG's minimal node sets
