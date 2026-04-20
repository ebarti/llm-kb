---
title: "Hybrid Search Explained"
source: "https://weaviate.io/blog/hybrid-search-explained"
author: "Weaviate"
date_published: 2023-11-20
date_ingested: 2026-04-05
tags: [hybrid-search, BM25, vector-search, RRF, Weaviate, retrieval]
type: article
status: raw
discovered_via: search
---

# Hybrid Search Explained — Weaviate

## Core Concept

Hybrid search merges sparse vectors (keyword-based, BM25) with dense vectors (semantic-based) to improve search accuracy.

## BM25 Algorithm

BM25 is a keyword scoring method that builds on TF-IDF by incorporating the Binary Independence Model and a document-length normalization penalty. Uses static parameters k1 and b for performance calibration.

## BM25F Variant

Introduced in Weaviate v1.17, BM25F allows assigning different weights to multiple text fields within objects (e.g., prioritizing titles over abstracts).

## Dense Vector Search

Dense embeddings from ML models capture contextual meaning. These vectors consist mostly of non-zero values and are indexed in vector databases. Similarity measured using distance metrics.

## Reciprocal Rank Fusion (RRF)

RRF combines results by calculating: sum(1/(k + r(d))) for each document across both ranked lists. Example: a document ranked first in BM25 and third in dense search scores 1/(0+1) + 1/(0+3) = 1.33.

## Alpha Parameter

Controls the balance:
- alpha = 0: pure keyword search
- alpha = 0.5: equal weighting
- alpha = 1: pure vector search
- Default: 0.75

## Weaviate Implementation (v1.17+)

Required parameters: hybrid, query. Optional: alpha, vector, score, fusionType. Two fusion algorithms: rankedFusion (default) and relativeScoreFusion.
