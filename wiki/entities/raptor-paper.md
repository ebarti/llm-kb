---
title: "RAPTOR Paper (ICLR 2024)"
type: entity
entity_type: paper
sources: ["[[sources/raptor-tree-retrieval]]"]
related: ["[[concepts/raptor]]", "[[concepts/hierarchical-retrieval]]", "[[concepts/retrieval-augmented-generation]]"]
last_compiled: 2026-04-05
summary: "ICLR 2024 paper by Sarthi, Abdullah et al. introducing RAPTOR — recursive tree construction via GMM clustering and abstractive summarization for multi-level retrieval, achieving 20% improvement on QuALITY."
---

## Overview

"RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval" is a paper presented at ICLR 2024 by Parth Sarthi, Salman Abdullah, and colleagues. It introduces a novel retrieval method that constructs hierarchical trees of summaries via recursive clustering and abstractive summarization, enabling retrieval at multiple levels of abstraction.

## Key Results

- 20% absolute improvement on QuALITY benchmark (82.6% vs 62.3% previous best)
- Surpassed DPR by 2.7 points and BM25 by 5.5 points on QASPER
- Demonstrated that 18.5-57% of useful retrieved nodes come from summary layers

## Implementation

Open-source implementation available at `github.com/parthsarthi03/raptor`.

## Mentioned In

- [[sources/raptor-tree-retrieval]] — full paper summary
