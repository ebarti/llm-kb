---
title: "Knowledge Base Index"
type: index
last_updated: 2026-04-05
---

# Knowledge Base Index

## Sources

- [[sources/karpathy-llm-knowledge-bases]] — Karpathy's workflow for LLM-maintained personal knowledge bases (Twitter thread, 2026-04-02)
- [[sources/dairai-llm-knowledge-bases-architecture]] — DAIR.AI Academy: four-phase operational cycle of Karpathy's LLM-KB system
- [[sources/glenrhodes-karpathy-workflow]] — Glen Rhodes: technical walkthrough emphasizing the filing loop and product gap
- [[sources/antigravity-post-code-ai-workflow]] — Antigravity Codes: broadest analysis — 6-step workflow, developer role transformation, 7 use cases
- [[sources/pebblous-cheap-ontology]] — Pebblous: Cheap Ontology framing, 50-year ontology history, RAG vs. fine-tuning vs. KB comparison
- [[sources/karma-multi-agent-knowledge-graph]] — KARMA (NeurIPS 2025): 9-agent LLM framework for automated knowledge graph enrichment
- [[sources/gallagher-second-brain-knowledge-graphs]] — Sam Gallagher: SQLite + ChromaDB knowledge graph kit, structure-first vs. text-first PKM
- [[sources/storm-automated-wiki-creation]] — STORM: multi-perspective automated Wikipedia-style article creation with LLMs
- [[sources/decodingai-second-brain-rag]] — Decoding AI: production-grade FTI architecture for second-brain RAG with Llama fine-tuning
- [[sources/hn-vector-database-debate]] — HN debate: pgvector/FAISS suffice for most cases; vector DBs only justified at billion-vector scale
- [[sources/graphiti-temporal-knowledge-graphs]] — Graphiti (Zep): temporal context graph framework with time-windowed facts for AI agents

## Concepts

### Core System
- [[concepts/llm-knowledge-base]] — Core system: LLM authors and maintains all wiki content from raw ingested sources
- [[concepts/wiki-compilation]] — Pipeline: raw ingested documents → structured cross-linked markdown wiki
- [[concepts/obsidian-as-ide]] — Using Obsidian as a read-only viewing frontend for LLM-written wikis
- [[concepts/llm-qa-over-documents]] — Answering complex questions over a compiled wiki via index navigation, no vector DB
- [[concepts/linting-and-health-checks]] — LLM-driven wiki health checks: inconsistencies, broken links, orphans, new article suggestions

### Retrieval & Infrastructure
- [[concepts/rag-vs-index-based-retrieval]] — Why simple index-based retrieval beats RAG at small-to-medium scale
- [[concepts/vector-databases]] — When vector DBs are actually needed vs. pgvector/FAISS/index-based navigation
- [[concepts/temporal-knowledge]] — Graphiti's temporal validity windows for facts that change over time

### Risks & Quality
- [[concepts/hallucination-contamination]] — LLM-generated errors that propagate through wiki and fine-tuning pipelines
- [[concepts/data-quality-bottleneck]] — Data quality > model scale; low-quality raw input cascades into contaminated KB
- [[concepts/vault-separation]] — Steph Ango's recommendation: separate AI-generated from human-curated Obsidian vaults

### Knowledge Representation
- [[concepts/knowledge-graph]] — Formal node/edge knowledge graphs: KARMA, Graphiti, and Gallagher's Kit compared
- [[concepts/multi-agent-systems]] — Multi-agent LLM pipelines for knowledge extraction (KARMA, STORM)
- [[concepts/automated-wiki-creation]] — STORM's single-shot multi-perspective Wikipedia article generation
- [[concepts/cheap-ontology]] — LLM wikis as $10M→API-cost ontology democratization

### Human & Workflow
- [[concepts/second-brain]] — Personal AI knowledge assistant: markdown wiki, graph DB, or production RAG
- [[concepts/personal-knowledge-management]] — PKM evolution from manual notes to AI-maintained wikis
- [[concepts/markdown-as-universal-interface]] — Why markdown is the optimal knowledge substrate
- [[concepts/post-code-ai-workflow]] — Karpathy's shift: from code generation to knowledge compilation
- [[concepts/knowledge-base-product-gap]] — "Hacky scripts" → product opportunity for accessible LLM-KB tooling

## Statistics

- Total sources: 11
- Total concepts: 20
- Total raw files: 9
