# Wiki Changelog

> Auto-generated on 2026-04-06 00:55 from git history.

## 2026-04-05

### New Concept Articles
- [[concepts/automated-wiki-creation]] — STORM's approach: single-shot, multi-perspective Wikipedia-style article generation from web search using simulated expe
- [[concepts/cheap-ontology]] — Pebblous framing: LLM wikis replace $10M–$20M enterprise knowledge graphs using only markdown files, LLM APIs, and natur
- [[concepts/data-quality-bottleneck]] — In LLM knowledge base pipelines, data quality at the raw input stage — not model capability — is the decisive factor: lo
- [[concepts/hallucination-contamination]] — The risk that LLM-generated errors written into a wiki propagate into future queries and fine-tuning, corrupting the kno
- [[concepts/knowledge-base-product-gap]] — Karpathy's own acknowledgment that the current LLM-KB is 'a hacky collection of scripts' — and the product opportunity t
- [[concepts/knowledge-graph]] — Formal representation of knowledge as nodes (entities) and edges (relationships), with three distinct modern approaches:
- [[concepts/linting-and-health-checks]] — LLM-driven health checks over the compiled wiki to find inconsistencies, fill data gaps, detect broken links, identify o
- [[concepts/llm-knowledge-base]] — A personal knowledge base where an LLM authors and maintains all wiki content from raw ingested sources, with humans int
- [[concepts/llm-qa-over-documents]] — Using an LLM agent to answer complex questions over a compiled wiki by reading index files and summaries to navigate to 
- [[concepts/markdown-as-universal-interface]] — The observation that markdown is simultaneously human-readable, LLM-friendly, version-controllable, tool-agnostic, and f
- [[concepts/multi-agent-systems]] — Using networks of specialized LLM agents (rather than a single LLM) to build and maintain knowledge systems — exemplifie
- [[concepts/obsidian-as-ide]] — Using Obsidian as a read-only frontend IDE to view LLM-maintained wikis, raw sources, and generated visualizations — wit
- [[concepts/personal-knowledge-management]] — The practice of capturing, organizing, and retrieving personal knowledge — transformed by LLMs from manual note-taking (
- [[concepts/post-code-ai-workflow]] — Karpathy's framing of a shift in AI-augmented developer work: from code generation as the primary token use, to knowledg
- [[concepts/rag-vs-index-based-retrieval]] — At small-to-medium scale (~100 articles, ~400K words), LLM-maintained index files and one-line summaries can replace vec
- [[concepts/second-brain]] — A personal AI system that stores, organizes, and retrieves the user's own knowledge — implemented either as a markdown w
- [[concepts/temporal-knowledge]] — Graphiti's core contribution: representing knowledge with temporal validity windows (when a fact became true and when it
- [[concepts/vault-separation]] — Steph Ango's (Obsidian CEO) recommendation to maintain a clean human-curated Obsidian vault separately from agent-genera
- [[concepts/vector-databases]] — Specialized databases for approximate nearest-neighbor (ANN) search over embedding vectors, necessary at billion-vector 
- [[concepts/wiki-compilation]] — The LLM-driven pipeline that converts raw ingested documents into a structured, cross-linked markdown wiki with source s

### New Sources Ingested
- [[sources/antigravity-post-code-ai-workflow]] — Broadest analysis of Karpathy's LLM KB shift: the 6-step workflow, developer role transformation, real-world application
- [[sources/dairai-llm-knowledge-bases-architecture]] — DAIR.AI Academy deep-dive on the four-phase operational cycle (ingest, compile, query, maintain) of Karpathy's LLM knowl
- [[sources/decodingai-second-brain-rag]] — Production-grade second brain using the FTI (Feature/Training/Inference) architecture: Notion → ETL → MongoDB vector sea
- [[sources/gallagher-second-brain-knowledge-graphs]] — Practitioner account of building the Knowledge Graph Kit (MCP server): SQLite + ChromaDB graph with four node types, con
- [[sources/glenrhodes-karpathy-workflow]] — Technical walkthrough of Karpathy's workflow emphasizing the 'filing loop' where query results compound the knowledge ba
- [[sources/graphiti-temporal-knowledge-graphs]] — Graphiti: open-source temporal graph framework for AI agents with time-windowed facts, incremental updates, hybrid retri
- [[sources/hn-vector-database-debate]] — Hacker News practitioner debate: pgvector and Elasticsearch handle most cases; specialized vector DBs only justified at 
- [[sources/karma-multi-agent-knowledge-graph]] — NeurIPS 2025 Spotlight paper: nine-agent LLM framework for automated KG enrichment achieving 83.1% accuracy on 1,200 Pub
- [[sources/karpathy-llm-knowledge-bases]] — Karpathy describes using LLMs to build and maintain personal markdown wikis from raw ingested sources, with Obsidian as 
- [[sources/pebblous-cheap-ontology]] — Deep analysis placing Karpathy's markdown wiki within 50 years of ontology history, quantifying the RAG vs. fine-tuning 
- [[sources/storm-automated-wiki-creation]] — STORM system: multi-perspective question-asking + retrieval → automated Wikipedia-style article generation with FreshWik

### Other New Files
- [[_index]]
- [[_meta/links]]
- [[_meta/manifest]]
- [[_meta/summaries]]
- [[log]]

