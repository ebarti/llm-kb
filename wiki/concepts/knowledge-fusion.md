---
title: "Knowledge Fusion"
type: concept
sources: ["[[sources/llm-kg-construction-survey]]", "[[sources/kggen-knowledge-graph-extraction]]", "[[sources/karma-multi-agent-knowledge-graph]]"]
related: ["[[concepts/knowledge-graph-construction]]", "[[concepts/knowledge-extraction]]", "[[concepts/knowledge-graph]]"]
last_compiled: 2026-04-05
summary: "The process of merging, deduplicating, and reconciling extracted knowledge from multiple sources into a unified knowledge graph — addressing entity alignment, schema reconciliation, and conflict resolution."
---

## Overview

Knowledge fusion is the final stage of [[concepts/knowledge-graph-construction]], where separately extracted entities, relations, and facts are merged into a unified, consistent knowledge graph. This stage addresses three core challenges: entity alignment (recognizing that different mentions refer to the same entity), schema reconciliation (aligning different ontological frameworks), and conflict resolution (handling contradictory information).

Traditional fusion pipelines "continue to struggle with semantic heterogeneity, large-scale integration, and dynamic knowledge updating" — LLMs are increasingly addressing these gaps.

## Entity Alignment Methods

### LLM-Based Approaches

- **[[entities/kggen]] iterative clustering**: LLM examines entity list, proposes clusters, validates via LLM-as-a-Judge, iterates until convergence. Handles tense, plurality, stemming, and synonym variations.
- **LLM-Align**: Treats alignment as constrained multiple-choice problems using contextual reasoning
- **EntGPT**: Two-phase refinement — candidate generation followed by targeted reasoning
- **COMEM**: Cascades smaller and larger LLMs in multi-stage pipelines, combining lightweight filtering with fine-grained reasoning

### Traditional Approaches

- Embedding-based similarity matching
- String matching with edit distance thresholds
- Graph structure-based alignment (matching neighborhood patterns)

## Schema-Level Fusion

Evolution across three generations:

1. **Ontology-driven**: Using explicit ontologies as global constraints for consistency
2. **Data-driven**: LKD-KGC uses embedding-based schema integration and vector clustering
3. **LLM-enabled**: EDC generates semantic definitions and compares via vector similarity

## Comprehensive Fusion Frameworks

- **[[entities/karma-framework]]**: Multi-agent design with specialized agents handling schema alignment and conflict resolution across the full pipeline
- **ODKE+**: Ontology-guided workflows coupling schema supervision with instance-level corroboration
- **Graphusion**: Unified prompt-based paradigm performing all fusion subtasks in single generative cycles

## Key Challenges

1. **Scale**: Quadratic complexity of pairwise entity comparison at large scale
2. **Semantic heterogeneity**: Same concepts described in fundamentally different ways across domains
3. **Temporal conflicts**: Facts that were true at different times may appear contradictory
4. **Cross-lingual fusion**: Aligning entities across languages

## Sources

- [[sources/llm-kg-construction-survey]] — detailed taxonomy of fusion approaches
- [[sources/kggen-knowledge-graph-extraction]] — iterative clustering for entity resolution
- [[sources/karma-multi-agent-knowledge-graph]] — multi-agent fusion framework

## Related Concepts

- [[concepts/knowledge-graph-construction]] — the end-to-end process
- [[concepts/knowledge-extraction]] — the preceding pipeline stage
- [[concepts/ontology-engineering]] — schema that guides fusion
