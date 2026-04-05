---
title: "Source: A Survey on Temporal Knowledge Graph — Representation Learning and Applications"
type: source-summary
source: "[[raw/temporal-knowledge-graphs-survey]]"
related: ["[[concepts/temporal-knowledge]]", "[[concepts/temporal-knowledge-graphs]]", "[[concepts/knowledge-graph-embeddings]]"]
last_compiled: 2026-04-05
summary: "Comprehensive survey of temporal KG representation learning: 10 method categories from TTransE to LLM-based approaches, covering interpolation, extrapolation, entity alignment, and temporal QA."
reading_time: "2 min"
---

## Key Points

- TKGs extend triples to quadruples (h, r, t, τ) with explicit timestamps
- 10 method categories: translation-based, decomposition, GNN, capsule networks, autoregression, temporal point processes, interpretability, LLM integration, few-shot learning, and novel approaches
- Interpolation (filling missing past facts) vs. extrapolation (predicting future facts) as two core tasks
- Key datasets: ICEWS14 (90K facts), ICEWS18 (468K), GDELT (2.2M facts)
- LLM integration via few-shot prompting, semantic enrichment, fine-tuning, and RAG

## Detailed Summary

This survey (March 2024) provides the most comprehensive taxonomy of temporal knowledge graph methods to date. TKGs add temporal context to static KGs, representing facts as quadruples like (Barack Obama, make_statement, Iran, 2014-06-19).

The ten method categories range from classical translation-based approaches (TTransE extending TransE with temporal concatenation, HyTE projecting onto temporal hyperplanes) through tensor decomposition methods (DE-SimplE, TComplEx), GNN-based approaches (TEA-GNN, TREA), autoregressive models treating TKGs as temporal snapshots (RE-NET, RE-GCN), temporal point processes modeling continuous-time event sequences (Know-Evolve, EvoKG), and emerging LLM-based methods.

The LLM integration section is particularly relevant: ICLTKG uses few-shot prompting for temporal reasoning without fine-tuning, ECOLA jointly optimizes knowledge-text prediction with temporal embeddings, and GenTKG applies retrieval-augmented generation with historical fact retrieval. These represent the frontier of combining structured temporal reasoning with language model capabilities.

## Related Concepts

- [[concepts/temporal-knowledge-graphs]] — the central topic
- [[concepts/temporal-knowledge]] — broader temporal representation concept
- [[concepts/knowledge-graph-embeddings]] — foundation methods extended temporally
