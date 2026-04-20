---
title: "LLM-Empowered Knowledge Graph Construction: A Survey"
source: "https://arxiv.org/abs/2510.20345"
author: "Various (arXiv)"
date_published: 2025-10-27
date_ingested: 2026-04-05
tags: [knowledge-graph, llm, survey, ontology, knowledge-extraction, knowledge-fusion]
type: paper
status: raw
discovered_via: search
---

# LLM-Empowered Knowledge Graph Construction: A Survey

## Core Framework

This survey systematizes how Large Language Models reshape knowledge graph (KG) construction across three traditional pipeline stages: ontology engineering, knowledge extraction, and knowledge fusion. The work emphasizes the paradigm shift from "rule-based and statistical pipelines to language-driven and generative frameworks."

## Taxonomy of Approaches

The survey presents a dual-paradigm architecture:

**Schema-Based Methods** prioritize structural consistency and normalization through predefined ontologies, while **schema-free methods** emphasize flexibility and open discovery without predetermined templates.

## Ontology Engineering

### Top-Down Construction (LLMs as Assistants)

- Competency Question (CQ)-based methods translate user requirements into formal OWL ontologies
- Notable systems: Ontogenia (incorporating metacognitive prompting and design patterns), CQbyCQ framework
- Natural language-based approaches extract semantic structures directly from unstructured text
- Systems like NeOn-GPT and LLMs4Life enable end-to-end workflows for complex domains

### Bottom-Up Construction (KGs for LLMs)

- Data-driven schema induction from instance-level graphs
- The Extract-Define-Canonicalize (EDC) framework normalizes automatically induced schemas
- AdaKGC addresses dynamic schema evolution without model retraining
- AutoSchemaKG integrates schema-based and schema-free paradigms for enterprise-scale deployment

## Knowledge Extraction Methods

### Schema-Based Extraction

**Static Schema-Driven:** Early approaches used fully predefined ontologies ensuring high consistency but limited adaptability. The KARMA framework employs multi-agent architecture for schema-guided task execution. ODKE+ introduces ontology snippets — dynamically selected subsets — enabling context-aware prompt construction.

**Dynamic Schema-Based:** AutoSchemaKG induces schemas from large corpora via unsupervised clustering. AdaKGC implements Schema-Enriched Prefix Instruction (SPI) for context-aware prompting and Schema-Constrained Dynamic Decoding (SDD) for runtime adaptation without retraining.

### Schema-Free Methods

**Structured Generative Extraction:**
- Chain-of-Thought (CoT) prompting enables stepwise reasoning without external schemas
- AutoRE introduces an RHF (Relation-Head-Facts) pipeline via instruction fine-tuning
- Retrieval-Augmented prompting dynamically enriches context windows with relevant exemplars
- ChatIE reformulates extraction as multi-turn dialogue for iterative refinement
- KGGEN decomposes extraction into sequential entity detection then relation generation phases

**Open Information Extraction (OIE):**
The EDC framework uses few-shot prompting to generate comprehensive natural-language triples, creating raw open knowledge graphs that subsequently undergo definition and canonicalization steps.

## Knowledge Fusion Approaches

### Schema-Level Fusion

Evolution from ontology-driven consistency (using explicit ontologies as global constraints) to data-driven unification (LKD-KGC uses embedding-based schema integration and vector clustering) to LLM-enabled canonicalization (EDC generates semantic definitions comparing via vector similarity).

### Instance-Level Fusion

**Entity Alignment Progression:**
- KGGEN employs iterative LLM-guided clustering for semantic entity merging
- LLM-Align treats alignment as constrained multiple-choice problems using contextual reasoning
- EntGPT introduces two-phase refinement: candidate generation followed by targeted reasoning
- COMEM combines lightweight filtering with fine-grained reasoning, cascading smaller and larger LLMs in multi-stage pipelines

### Comprehensive Frameworks

- KARMA: Multi-agent design with specialized agents handling schema alignment and conflict resolution
- ODKE+: Ontology-guided workflows coupling schema supervision with instance-level corroboration
- Graphusion: Unified prompt-based paradigm performing all fusion subtasks in single generative cycles

## Key Findings on LLM Performance

The survey documents that LLMs achieve performance approaching junior human modelers in autonomous ontology generation. Empirical evaluations reveal LLMs can independently identify classes, object properties, and data properties while generating logically consistent axioms. However, the research emphasizes that "traditional fusion pipelines continue to struggle with semantic heterogeneity, large-scale integration, and dynamic knowledge updating."

Few-shot prompting with GPT-4 or Claude achieves accuracy roughly equivalent to — and sometimes superior to — fully supervised traditional models, but without requiring thousands of labeled training examples. LTNER reaches 91.91% on CoNLL2003.

## Identified Limitations of Traditional Approaches

Pre-LLM pipelines faced three primary constraints:
1. Scalability challenges from rule-based systems failing across domains
2. Expert dependency requiring substantial human intervention
3. Pipeline fragmentation causing cumulative error propagation across stages

## Future Research Directions

1. **Knowledge Graph-Based Reasoning:** Integrating structured KGs into LLM reasoning mechanisms for enhanced logical consistency and interpretability
2. **Dynamic Knowledge Memory for Agents:** KGs as evolving memory substrates supporting persistent, structured information across finite context windows
3. **Multimodal Knowledge Graph Construction:** VaLiK cascades Vision-Language Models translating visual features into textual form; KG-MRI employs multimodal embeddings
4. **Beyond RAG:** KGs functioning as cognitive middle layers for querying, planning, and decision-making rather than mere retrieval mechanisms

## Methodological Trends

The survey identifies three overarching trajectories:
1. Evolution from static schemas toward dynamic induction
2. Integration of modular pipelines into generative unified frameworks
3. Transition from symbolic rigidity to semantic adaptability

These shifts reposition KGs as "living, cognitive infrastructures that blend language understanding with structured reasoning."
