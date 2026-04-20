---
title: "Hierarchical Navigable Small Worlds (HNSW)"
source: "https://www.pinecone.io/learn/series/faiss/hnsw/"
author: "Pinecone"
date_published: 2023-06-15
date_ingested: 2026-04-05
tags: [HNSW, ANN, vector-search, approximate-nearest-neighbor, FAISS, algorithm]
type: article
status: raw
discovered_via: search
---

# HNSW: Complete Technical Analysis — Pinecone

## Algorithm Structure

HNSW is a graph-based ANN search method combining probability skip lists (1990) and navigable small world graphs (2011-2014). Uses hierarchical multi-layer architecture where top layers have longer-range connections for rapid traversal, lower layers have shorter, more precise connections.

## Layers and Entry Points

Vectors assigned to layers using probability function. Distribution: vectors heavily concentrate at layer 0, with exponential decay at higher layers. Single entry point at highest layer. Probability of layer assignment uses formula normalized by level multiplier mL ≈ 1/ln(M).

Example (1M vectors): Layer 0: ~968,746 vectors; Layer 1: ~30,276; Layer 2: ~951; Layer 3+: <100 each.

## Search Process

Two phases:
1. "Zoom-out": Traverse through low-degree vertices at higher layers
2. "Zoom-in": Process through high-degree vertices at lower layers

Begin at top layer with ef=1, move to closest connected vertex iteratively, descend to next layer at local minimum.

## Construction Process

Phase One (upper layers): Greedy traversal with ef=1.
Phase Two (insertion layer): Increase ef to efConstruction, select M neighbors from candidates. Faiss: M_max = M, M_max0 = M × 2 for layer 0.

## Critical Parameters

| Parameter | Function | Impact |
|-----------|----------|--------|
| M | Neighbors per vertex (non-layer-0) | Higher M = better recall, more memory |
| M_max | Max connections per vertex | Limits graph density; M_max0 = 2×M for layer 0 |
| efConstruction | Search candidates during building | Improves recall; minimal effect on search time |
| efSearch | Candidates evaluated at query time | Controls recall vs. speed tradeoff |
| mL | Layer assignment probability | Optimal: 1/ln(M) |

## Performance (Sift1M)

- Low params (M=4, efSearch=40): 80% recall at 1ms
- High params (M=32, efSearch=200): 99% recall at 50ms
- efConstruction has negligible effect on single-query search time

## Memory Usage

M=2: >0.5GB for 1M vectors; M=512: ~5GB. Linear scaling with M.

## Complexity

Search: (poly/)logarithmic. Space: O(M × n). Unlike IVF (quantization), HNSW stores full vector connections = higher memory footprint.
