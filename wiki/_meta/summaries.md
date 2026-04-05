---
title: "Article Summaries"
type: meta
last_updated: 2026-04-05
---

# Article Summaries

One-line summaries of all wiki articles. Used for quick navigation and Q&A context loading.

## Sources

- [[sources/karpathy-llm-knowledge-bases]] — Karpathy describes using LLMs to build and maintain personal markdown wikis from raw ingested sources, with Obsidian as the viewing IDE and LLM-driven Q&A, output generation, and linting.
- [[sources/dairai-llm-knowledge-bases-architecture]] — DAIR.AI Academy deep-dive on the four-phase LLM-KB cycle (ingest → compile → query → maintain) emphasizing no vector infrastructure needed at ~100-article personal scale.
- [[sources/glenrhodes-karpathy-workflow]] — Technical walkthrough emphasizing the "filing loop" where query results compound the KB over time, and Karpathy's acknowledgment of a significant product gap for non-technical users.
- [[sources/antigravity-post-code-ai-workflow]] — Broadest analysis: 6-step workflow, 7 use cases, developer role transformation from coders to curators, hallucination contamination risk, and vault separation recommendation from Obsidian CEO.
- [[sources/pebblous-cheap-ontology]] — Places Karpathy's markdown wiki in 50 years of ontology history; introduces "Cheap Ontology" framing; quantifies RAG vs. fine-tuning vs. KB tradeoffs; identifies data quality (not model scale) as the decisive bottleneck.
- [[sources/karma-multi-agent-knowledge-graph]] — NeurIPS 2025 Spotlight: KARMA uses 9 collaborative LLM agents to enrich knowledge graphs from unstructured text, achieving 83.1% accuracy and 38,230 new entities from 1,200 PubMed papers.
- [[sources/gallagher-second-brain-knowledge-graphs]] — Practitioner account of building Knowledge Graph Kit (SQLite + ChromaDB MCP server); argues structure-first graph approach over text-first markdown for personal task/relationship management.
- [[sources/storm-automated-wiki-creation]] — STORM system: multi-perspective question-asking + retrieval → automated Wikipedia-style articles; introduces FreshWiki evaluation dataset; contrasts single-shot creation vs. Karpathy's accumulating KB.
- [[sources/decodingai-second-brain-rag]] — Production-grade FTI architecture (Feature/Training/Inference): Notion → ETL → MongoDB vector search + Llama 3.1 8B fine-tuning + ZenML orchestration; scalable but less auditable than markdown approach.
- [[sources/hn-vector-database-debate]] — HN practitioner debate: pgvector/Elasticsearch handle most use cases; dedicated vector DBs only justified at billion-vector scale; real question is "do you need ANN search?"
- [[sources/graphiti-temporal-knowledge-graphs]] — Graphiti (Zep): open-source temporal context graph with time-windowed facts, hybrid retrieval (semantic + BM25 + graph), and full provenance — middle ground between markdown wikis and enterprise KGs.

## Concepts

- [[concepts/llm-knowledge-base]] — A personal knowledge base where an LLM authors and maintains all wiki content from raw ingested sources, with humans interacting only via natural language.
- [[concepts/wiki-compilation]] — The LLM-driven pipeline that converts raw ingested documents into a structured, cross-linked markdown wiki with source summaries and concept articles.
- [[concepts/obsidian-as-ide]] — Using Obsidian as a read-only frontend IDE to view LLM-maintained wikis, raw sources, and generated visualizations — with the LLM as the actual author.
- [[concepts/llm-qa-over-documents]] — Using an LLM agent to answer complex questions over a compiled wiki by reading index files and summaries to navigate to relevant full articles, without needing a vector database.
- [[concepts/linting-and-health-checks]] — LLM-driven health checks over the compiled wiki to find inconsistencies, fill data gaps, detect broken links, identify orphan articles, and suggest new content.
- [[concepts/rag-vs-index-based-retrieval]] — At small-to-medium scale (~100 articles, ~400K words), LLM-maintained index files and one-line summaries can replace vector database RAG for document Q&A.
- [[concepts/vector-databases]] — Specialized ANN search databases: justified at billion-vector scale; pgvector/FAISS/index-based navigation suffice for personal or team-scale knowledge bases.
- [[concepts/temporal-knowledge]] — Graphiti's approach: representing facts with validity time windows so AI agents can track what was true when, and identify superseded information.
- [[concepts/hallucination-contamination]] — The risk that LLM errors written into a wiki propagate through future queries and fine-tuning, permanently corrupting the knowledge base.
- [[concepts/data-quality-bottleneck]] — Data quality > model scale in LLM-KB pipelines: low-quality raw inputs cascade into contaminated wiki and flawed fine-tuning datasets.
- [[concepts/vault-separation]] — Steph Ango's recommendation: keep AI-generated wiki content in a separate Obsidian vault from human-curated personal notes to prevent hallucination contamination.
- [[concepts/knowledge-graph]] — Formal node/edge knowledge representation: KARMA (automated enrichment, NeurIPS 2025), Graphiti (temporal), and Gallagher's Kit (personal SQLite) compared against Karpathy's markdown alternative.
- [[concepts/multi-agent-systems]] — Networks of specialized LLM agents for knowledge management: KARMA's 9-agent KG enrichment pipeline and STORM's perspective-simulating article creation.
- [[concepts/automated-wiki-creation]] — STORM's single-shot multi-perspective Wikipedia-style article generation, contrasting with Karpathy's persistent accumulating KB approach.
- [[concepts/cheap-ontology]] — Pebblous framing: LLM wikis replace $10M–$20M enterprise KGs via markdown + LLM API + natural-language schema, enabled by 1,000-fold context window expansion.
- [[concepts/second-brain]] — Personal AI knowledge assistant implemented as markdown wiki (Karpathy), graph DB (Gallagher), or production RAG (Decoding AI) — all using LLMs as the intelligence layer.
- [[concepts/personal-knowledge-management]] — PKM evolution: manual notes (Notion/Obsidian) → AI-augmented → AI-maintained wikis with humans as curators rather than authors.
- [[concepts/markdown-as-universal-interface]] — Markdown satisfies all requirements for LLM-KB substrate: human-readable, LLM-friendly, version-controllable, tool-agnostic, and future-proof.
- [[concepts/post-code-ai-workflow]] — Karpathy's shift from code generation to knowledge compilation: "manipulating knowledge, not code" as the next developer competitive advantage.
- [[concepts/knowledge-base-product-gap]] — The gap between Karpathy's "hacky scripts" and a polished product accessible to non-technical users — significant market opportunity in a $62B enterprise KM sector.
