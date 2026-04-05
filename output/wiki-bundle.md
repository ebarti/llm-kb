# LLM Knowledge Base - Complete Bundle

*63 articles*

## Table of Contents


### Sources

- [Source: Karpathy's LLM Knowledge Bases: The Post-Code AI Workflow](#sources-antigravity-post-code-ai-workflow)
- [Source: Don't Do RAG — When Cache-Augmented Generation is All You Need](#sources-cache-augmented-generation)
- [Source: LLM Knowledge Bases: A System Architecture Overview](#sources-dairai-llm-knowledge-bases-architecture)
- [Source: Build Your Second Brain AI Assistant — LLMs and RAG](#sources-decodingai-second-brain-rag)
- [Source: Using LLMs as a Second Brain — From Notes to Knowledge Graphs](#sources-gallagher-second-brain-knowledge-graphs)
- [Source: Andrej Karpathy's LLM-Powered Knowledge Base Workflow](#sources-glenrhodes-karpathy-workflow)
- [Source: Graphiti — Temporal Context Graphs for AI Agents](#sources-graphiti-temporal-knowledge-graphs)
- [Source: Do You Need a Vector Database? (HN Discussion)](#sources-hn-vector-database-debate)
- [Source: Introduction to Matryoshka Embedding Models](#sources-huggingface-matryoshka-embeddings)
- [Source: KARMA — Multi-Agent LLM Framework for Knowledge Graph Enrichment](#sources-karma-multi-agent-knowledge-graph)
- [Source: Thread by @karpathy — LLM Knowledge Bases](#sources-karpathy-llm-knowledge-bases)
- [Source: LLMs That Compile Knowledge: The Karpathy Methodology and the Democratization of Ontology](#sources-pebblous-cheap-ontology)
- [Source: Choosing an Embedding Model](#sources-pinecone-embedding-models-rundown)
- [Source: RAFT — Adapting Language Model to Domain Specific RAG](#sources-raft-retrieval-augmented-fine-tuning)
- [Source: RAG vs Fine-tuning — Pipelines, Tradeoffs, and Agriculture Case Study](#sources-rag-vs-finetuning-agriculture)
- [Source: From RAG to Context — A 2025 Year-End Review](#sources-ragflow-rag-review-2025)
- [Source: STORM — Automating Wikipedia Article Creation with LLMs](#sources-storm-automated-wiki-creation)
- [Source: The Definitive Guide to Synthetic Data Generation Using LLMs](#sources-synthetic-data-generation-llms)
- [Source: Hybrid Search Explained](#sources-weaviate-hybrid-search-explained)

### Concepts

- [Automated Wiki Creation](#concepts-automated-wiki-creation)
- [Cheap Ontology](#concepts-cheap-ontology)
- [Data Quality Bottleneck](#concepts-data-quality-bottleneck)
- [Hallucination Contamination](#concepts-hallucination-contamination)
- [Knowledge Base Product Gap](#concepts-knowledge-base-product-gap)
- [Knowledge Graph](#concepts-knowledge-graph)
- [Linting and Health Checks](#concepts-linting-and-health-checks)
- [LLM Knowledge Base](#concepts-llm-knowledge-base)
- [LLM Q&A Over Documents](#concepts-llm-qa-over-documents)
- [Markdown as Universal Interface](#concepts-markdown-as-universal-interface)
- [Multi-Agent Systems for Knowledge Management](#concepts-multi-agent-systems)
- [Obsidian as IDE](#concepts-obsidian-as-ide)
- [Personal Knowledge Management (PKM)](#concepts-personal-knowledge-management)
- [Post-Code AI Workflow](#concepts-post-code-ai-workflow)
- [RAG vs. Index-Based Retrieval](#concepts-rag-vs-index-based-retrieval)
- [Second Brain](#concepts-second-brain)
- [Temporal Knowledge](#concepts-temporal-knowledge)
- [Vault Separation](#concepts-vault-separation)
- [Vector Databases](#concepts-vector-databases)
- [Wiki Compilation](#concepts-wiki-compilation)

### Entities

- [Andrej Karpathy](#entities-andrej-karpathy)
- [ChromaDB](#entities-chromadb)
- [DAIR.AI](#entities-dairai)
- [Dataview](#entities-dataview)
- [Elvis Saravia](#entities-elvis-saravia)
- [FAISS](#entities-faiss)
- [FreshWiki](#entities-freshwiki)
- [Graphiti](#entities-graphiti)
- [KARMA](#entities-karma)
- [Marp](#entities-marp)
- [Matplotlib](#entities-matplotlib)
- [Memex](#entities-memex)
- [Obsidian](#entities-obsidian)
- [pgvector](#entities-pgvector)
- [SQLite](#entities-sqlite)
- [Steph Ango](#entities-steph-ango)
- [STORM](#entities-storm)
- [Vannevar Bush](#entities-vannevar-bush)
- [Zep](#entities-zep)

### Other

- [Dashboard](#dashboard)
- [Graph Analysis](#graph)
- [Dataview Queries](#queries)
- [Tag Index](#tags)
- [Activity Log](#log)

---

## Source: Karpathy's LLM Knowledge Bases: The Post-Code AI Workflow {#sources-antigravity-post-code-ai-workflow}

***type:** source-summary | **source:** Antigravity Post Code Ai Workflow | **related:** Llm Knowledge Base, Wiki Compilation, Post Code Ai Workflow, Hallucination Contamination, Markdown As Universal Interface | **last_compiled:** 2026-04-05 | **summary:** Broadest analysis of Karpathy's LLM KB shift: the 6-step workflow, developer role transformation, real-world applications across 7 domains, hallucination contamination risk, and minimum viable setup.*

## Key Points
- Karpathy framing: "A large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge"
- The shift: Vibe Coding (Feb 2025) → Agentic Engineering (Jan 2026) → LLM Knowledge Bases (Apr 2026)
- 6 steps: ingest → compile → scale → query → multi-format output → health checks
- 7 real-world applications: competitive intelligence, due diligence, literature reviews, documentation, product research, compliance, personal learning
- Steph Ango (Obsidian CEO): use **vault separation** — clean personal vault separate from agent-generated content
- Markdown is the universal interface: human-readable, LLM-friendly, version-controllable, tool-agnostic

## Detailed Summary

This Antigravity Codes article is the most comprehensive analysis of what Karpathy's approach means for developers. It places the LLM KB within a broader intellectual trajectory: from "vibe coding" (accepting all AI-generated code without review) through agentic engineering to the current focus on knowledge orchestration.

The article documents community reactions: Steph Ango recommends vault separation to prevent AI-hallucinated content from contaminating human-curated personal wikis; Elvis Saravia confirms the pattern's effectiveness. The key risk — hallucination contamination propagating through the wiki — is addressed by tracing all claims back to `raw/` source files.

The minimum viable setup is refreshingly simple: `raw/`, `wiki/`, `output/`, `_meta/` directories + Obsidian + Web Clipper + LLM API.

The article concludes with a bold claim: "The developers who thrive will be those with the strongest knowledge systems."

## Notable Quotes
> "A large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge." — Karpathy
> "Developers become curators and questioners rather than coders or agent orchestrators."

## Related Concepts
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the system
- [Post Code Ai Workflow](#concepts-post-code-ai-workflow) — the broader shift
- [Markdown As Universal Interface](#concepts-markdown-as-universal-interface) — markdown as the format
- [Hallucination Contamination](#concepts-hallucination-contamination) — the main risk
- [Vault Separation](#concepts-vault-separation) — Steph Ango's recommendation


---

## Source: Don't Do RAG — When Cache-Augmented Generation is All You Need {#sources-cache-augmented-generation}

***type:** source-summary | **source:** Cache Augmented Generation | **related:** Cache Augmented Generation, Retrieval Augmented Generation, Rag Vs Cag | **last_compiled:** 2026-04-05 | **summary:** ArXiv paper proposing CAG as a RAG alternative that preloads all documents into KV cache — achieving 10x faster inference (0.85s vs 9.24s) with higher BERTScores, but limited to manageable knowledge base sizes.*

## Key Points

- CAG preloads all documents and caches KV parameters, eliminating retrieval entirely
- Three-phase framework: Preloading → Inference → Cache Reset
- 10x faster than RAG on HotPotQA-Small (0.85s vs 9.24s)
- Higher BERTScores across most test configurations on SQuAD and HotPotQA
- Limited to knowledge bases that fit within extended context windows (~128k tokens)
- Eliminates retrieval ranking errors — deterministic behavior

## Detailed Summary

This paper challenges the default assumption that RAG is always necessary for knowledge-intensive tasks. Cache Augmented Generation works by computing a KV cache from all documents once, then loading this cache alongside each query. The model processes all documents holistically, enabling multi-hop reasoning without the variability introduced by document ranking.

The approach excels when knowledge is bounded and relatively stable. As long-context LLMs continue expanding their context windows, CAG becomes viable for increasingly large knowledge bases. However, it remains impractical for dynamic or very large corpora where continuous updates are needed.

## Related Concepts

- Cache Augmented Generation — the core concept
- Retrieval Augmented Generation — the baseline being compared against
- Rag Vs Cag — when to use each


---

## Source: LLM Knowledge Bases: A System Architecture Overview {#sources-dairai-llm-knowledge-bases-architecture}

***type:** source-summary | **source:** Dairai Llm Knowledge Bases Architecture | **related:** Llm Knowledge Base, Wiki Compilation, Obsidian As Ide, Rag Vs Index Based Retrieval | **last_compiled:** 2026-04-05 | **summary:** DAIR.AI Academy deep-dive on the four-phase operational cycle (ingest, compile, query, maintain) of Karpathy's LLM knowledge base system, emphasizing no vector infrastructure needed at personal scale.*

## Key Points
- System treats the LLM as a "compiler" that transforms raw documents into a structured, cross-referenced wiki
- Four phases: **Ingestion** → **Compilation** → **Query & Enhancement** → **Maintenance & Validation**
- Index files plus context windows replace vector databases at ~100-article scale
- Every query result feeds back into the wiki (cumulative exploration)
- The author's own extension uses Obsidian + qmd CLI for semantic indexing of research papers

## Detailed Summary

This DAIR.AI Academy article by Elvis Saravia provides a thorough system-level description of Karpathy's knowledge base architecture. The core innovation is framing the LLM as a "compiler" rather than just a chatbot: raw materials enter through multiple channels (web clipper, papers, repos), land in `raw/`, then the LLM incrementally builds a structured wiki with index files, concept articles, backlinks, and derived artifacts.

At personal scale (~100 articles, ~400K words), vector databases are unnecessary—LLMs can maintain index files and read comprehensive material within context windows. This is a significant practical simplification: no embeddings, no vector DB infrastructure, just markdown files and an LLM API.

The maintenance phase includes LLM-driven health checks for consistency, missing information (filled via web search), cross-concept connections, and exploratory question generation. The author extends this with their own research indexing system using qmd and MCP tools for interactive visualization.

## Notable Quotes
> "The key innovation centers on the workflow pattern: having an LLM progressively construct and sustain a structured knowledge repository from unprocessed sources, with every interaction contributing to system growth."

## Related Concepts
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the core system described
- [Wiki Compilation](#concepts-wiki-compilation) — the compilation phase in detail
- [Obsidian As Ide](#concepts-obsidian-as-ide) — Obsidian as viewer and navigator
- [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval) — why vector DBs are skipped
- [Linting And Health Checks](#concepts-linting-and-health-checks) — the maintenance phase


---

## Source: Build Your Second Brain AI Assistant — LLMs and RAG {#sources-decodingai-second-brain-rag}

***type:** source-summary | **source:** Decodingai Second Brain Rag | **related:** Rag Vs Index Based Retrieval, Second Brain, Llm Knowledge Base, Data Quality Bottleneck | **last_compiled:** 2026-04-05 | **summary:** Production-grade second brain using the FTI (Feature/Training/Inference) architecture: Notion → ETL → MongoDB vector search + Llama 3.1 fine-tuning + ZenML orchestration — the enterprise-scale counterpart to Karpathy's personal approach.*

## Key Points
- FTI pattern: Feature stage → Training stage → Inference stage — clean separation of offline/online concerns
- Five major pipelines: data ETL → feature engineering → model training → inference (RAG) → observability
- Fine-tunes Llama 3.1 8B on summarization via distillation; deploys to Hugging Face Endpoints
- Advanced RAG: Contextual Retrieval + hybrid search (semantic + keyword) in MongoDB
- Tools: Crawl4AI, Unsloth, ZenML, Opik, smolagents
- Contrast: production-grade scalability vs. Karpathy's simplicity and auditability

## Detailed Summary

The Decoding AI course represents the professional-grade version of the "second brain" concept: a full MLOps stack with five pipeline stages, vector database storage, LLM fine-tuning, and observability. This is the approach to take when personal-scale markdown wikis won't suffice — when you have thousands of documents and need production reliability.

The architecture explicitly separates offline work (ingestion, feature engineering, fine-tuning — batch, scheduled) from online work (RAG inference, summarization — real-time, always-on). This separation is a key MLOps principle often missed in prototype systems.

Key tradeoffs vs. Karpathy's approach:
- **Scalability**: handles 1000s of documents (vs. ~100 for markdown wiki)
- **Infrastructure complexity**: MongoDB, Hugging Face, ZenML, Opik stack (vs. just markdown + LLM API)
- **Auditability**: low (vector chunks) vs. high (readable markdown)
- **Compounding**: none (static index) vs. yes (filing loop enriches the KB)

## Related Concepts
- [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval) — the RAG side of the comparison
- [Second Brain](#concepts-second-brain) — the shared goal
- [Data Quality Bottleneck](#concepts-data-quality-bottleneck) — ETL quality scoring via LLMs
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the simpler alternative


---

## Source: Using LLMs as a Second Brain — From Notes to Knowledge Graphs {#sources-gallagher-second-brain-knowledge-graphs}

***type:** source-summary | **source:** Gallagher Second Brain Knowledge Graphs | **related:** Second Brain, Knowledge Graph, Llm Knowledge Base, Personal Knowledge Management | **last_compiled:** 2026-04-05 | **summary:** Practitioner account of building the Knowledge Graph Kit (MCP server): SQLite + ChromaDB graph with four node types, contrasting structure-first (graph) vs. text-first (markdown) approaches to personal knowledge management.*

## Key Points
- Key insight: "an intelligent knowledge system can't just manipulate text, it must understand structure"
- Knowledge Graph Kit: SQLite storage + ChromaDB vectorization + four node types (Task, Note, Person, Project)
- Relationship labels: part_of, mentions, related_to
- Semantic search surfaces connections even when keywords don't overlap
- Data layer precedence: the underlying structure matters more than the interface
- Open-source MCP server — same patterns as Karpathy but with formal graph structure

## Detailed Summary

Sam Gallagher's journey from Notion/Obsidian failure to Knowledge Graph Kit documents a key architectural choice: markdown files are text that LLMs can manipulate, but graphs are structures that LLMs can reason over. His system stores notes as nodes with typed relationships in SQLite, with ChromaDB providing semantic vector search on top.

This approach contrasts with Karpathy's markdown-centric system:
- **Gallagher**: explicit graph structure + semantic search → better for personal tasks, projects, and people
- **Karpathy**: flat markdown + LLM index navigation → better for research synthesis and document Q&A

Both use LLMs as the intelligence layer but differ in the substrate: Gallagher stores structure in a database; Karpathy encodes structure implicitly in markdown wikilinks and LLM-maintained index files.

The MCP server packaging makes the Knowledge Graph Kit directly usable as a Claude Code/agent tool.

## Related Concepts
- [Second Brain](#concepts-second-brain) — the goal
- [Knowledge Graph](#concepts-knowledge-graph) — the approach
- [Personal Knowledge Management](#concepts-personal-knowledge-management) — the broader domain
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the contrasting text-first approach


---

## Source: Andrej Karpathy's LLM-Powered Knowledge Base Workflow {#sources-glenrhodes-karpathy-workflow}

***type:** source-summary | **source:** Glenrhodes Karpathy Workflow | **related:** Llm Knowledge Base, Wiki Compilation, Llm Qa Over Documents, Hallucination Contamination | **last_compiled:** 2026-04-05 | **summary:** Technical walkthrough of Karpathy's workflow emphasizing the 'filing loop' where query results compound the knowledge base, and the product gap for non-technical users.*

## Key Points
- The **filing loop**: query results get written back into the wiki — "his explorations accumulate, the knowledge base grows from use"
- At ~100 articles / 400K words, LLMs can maintain indexes and read comprehensively within context windows
- Current implementation is "a hacky collection of scripts" — significant product opportunity for polished tooling
- LLM health checks actively scan for inconsistencies and fill gaps via web search
- Synthetic data generation / fine-tuning is the future direction

## Detailed Summary

Glen Rhodes' walkthrough emphasizes the compounding nature of the system as its defining feature. Unlike traditional knowledge management tools where notes sit inert, Karpathy's system creates a feedback loop: every question asked enriches the knowledge base with a new filed answer. This transforms the wiki from a static repository into a living, growing resource.

The article identifies a key product gap: the current workflow requires significant technical expertise (CLI tooling, LLM API configuration, Obsidian customization). Karpathy himself acknowledges this as a "hacky collection of scripts," signaling opportunity for productized tooling.

The system architecture is straightforward: raw sources → LLM compilation → markdown wiki → Obsidian viewer → LLM Q&A → filed answers back to wiki.

## Notable Quotes
> "His explorations accumulate. The knowledge base grows from use."

## Related Concepts
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the system
- [Wiki Compilation](#concepts-wiki-compilation) — compilation process
- [Llm Qa Over Documents](#concepts-llm-qa-over-documents) — query/answer loop
- [Hallucination Contamination](#concepts-hallucination-contamination) — key risk
- [Knowledge Base Product Gap](#concepts-knowledge-base-product-gap) — the product opportunity


---

## Source: Graphiti — Temporal Context Graphs for AI Agents {#sources-graphiti-temporal-knowledge-graphs}

***type:** source-summary | **source:** Graphiti Temporal Knowledge Graphs | **related:** Knowledge Graph, Temporal Knowledge, Rag Vs Index Based Retrieval | **last_compiled:** 2026-04-05 | **summary:** Graphiti: open-source temporal graph framework for AI agents with time-windowed facts, incremental updates, hybrid retrieval (semantic + BM25 + graph), and full provenance — the middle ground between markdown wikis and enterprise KGs.*

## Key Points
- Context graph = temporal graph: entities + relationships + facts with validity windows (when true → when superseded)
- Four components: Entities (nodes), Facts/Relationships (edges with time windows), Episodes (raw provenance), Custom Types (Pydantic ontology)
- Hybrid retrieval: semantic + keyword (BM25) + graph-based search
- Incremental updates: no batch recomputation; old facts invalidated not deleted
- Full provenance: every derived fact traces to Episodes (source documents)
- Middle ground: more structured than markdown wiki, more accessible than KARMA

## Detailed Summary

Graphiti occupies the gap between Karpathy's simple markdown wiki and enterprise knowledge graph systems like KARMA. Its killer feature for AI agents: temporal validity windows. Rather than a static graph where facts are true or false, Graphiti tracks when facts became true and when they were superseded. This is critical for agents operating in changing environments (e.g., "what was the product roadmap last quarter vs. today?").

The Episodes concept mirrors Karpathy's `raw/` directory: all derived knowledge traces back to source documents, enabling auditability and correction. The hybrid retrieval combining semantic embeddings, BM25 keyword search, and graph traversal provides more robust retrieval than any single method alone.

The open-source/Zep split (Graphiti as engine, Zep as managed service) mirrors the pattern seen across knowledge management tools: open core for experimentation, managed service for production.

## Related Concepts
- [Knowledge Graph](#concepts-knowledge-graph) — the representation
- [Temporal Knowledge](#concepts-temporal-knowledge) — Graphiti's unique contribution
- [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval) — retrieval methods compared
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the simpler alternative


---

## Source: Do You Need a Vector Database? (HN Discussion) {#sources-hn-vector-database-debate}

***type:** source-summary | **source:** Hn Vector Database Debate | **related:** Rag Vs Index Based Retrieval, Vector Databases | **last_compiled:** 2026-04-05 | **summary:** Hacker News practitioner debate: pgvector and Elasticsearch handle most cases; specialized vector DBs only justified at billion-vector scale; FAISS/Vespa.ai as middle ground; real question is 'do you need ANN search?'*

## Key Points
- pgvector sufficient for most projects; Elasticsearch handles vector ops without new infrastructure
- pgvector limitation: IVF algorithm, nprobes=3 default → ~50% recall; HNSW support being added
- FAISS: billion-scale disk-based indexing, open-source, good middle ground
- Vespa.ai: underrated hybrid engine (vector + metadata, multi-vector indexing)
- Single vector per document loses nuance: "like making a movie poster the average of all frames"
- Real question: "do you actually need approximate nearest-neighbor search?"

## Detailed Summary

This HN thread provides honest practitioner perspectives rarely found in vendor documentation. The consensus: for most teams, adding a specialized vector database is premature infrastructure. PostgreSQL with pgvector handles typical workloads; Elasticsearch already does vector search.

Dedicated vector databases only justify their operational complexity at billion-vector scale (Wikipedia-scale datasets, social media content). For personal-scale or team-scale knowledge bases (~100K to ~10M documents), existing tools suffice.

This aligns directly with Karpathy's observation: at ~100 articles / 400K words, an LLM with a 1M-token context window can simply load the entire index rather than doing approximate retrieval — eliminating both the need for vector search AND the accuracy loss from approximate nearest-neighbor algorithms.

## Related Concepts
- [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval) — the central debate
- [Vector Databases](#concepts-vector-databases) — what's being evaluated


---

## Source: Introduction to Matryoshka Embedding Models {#sources-huggingface-matryoshka-embeddings}

***type:** source-summary | **source:** Huggingface Matryoshka Embeddings | **related:** Matryoshka Representation Learning, Text Embeddings, Sentence Transformers | **last_compiled:** 2026-04-05 | **summary:** Hugging Face tutorial on Matryoshka Representation Learning: training embeddings that can be truncated to any dimension with minimal quality loss, preserving 98.37% performance at just 8.3% of original size.*

## Key Points

- Matryoshka models frontload important information in earlier dimensions, enabling truncation without retraining
- Training applies the same loss function at multiple dimensions simultaneously (e.g., 768, 512, 256, 128, 64) with no notable training overhead
- At 64 dimensions (8.3% of 768), Matryoshka model preserves 98.37% of full-size performance vs 96.46% for standard models
- MRL consistently outperforms post-hoc PCA at equivalent compression ratios
- Inference speed for embedding generation is identical regardless of target dimension; downstream tasks (retrieval, clustering) are significantly faster
- Normalization must happen after truncation, not before

## Detailed Summary

The article provides a complete tutorial on Matryoshka Representation Learning, from theory through implementation with Sentence Transformers. The key innovation is that a single model produces embeddings usable at any dimension by training with `MatryoshkaLoss` — the loss function is applied to truncated versions of the embedding at each target dimension. This eliminates the need to train separate models for different deployment constraints. The practical implications are significant: teams can use shorter embeddings for fast retrieval and full-length embeddings for reranking, all from one model. Production-ready models like nomic-embed-text-v1.5 (10.5M downloads) already include Matryoshka training.

## Notable Quotes

> "Rather than applying a loss function on only the full-size embeddings, MRL also applies that same loss function on truncated portions of the embeddings."

## Related Concepts

- Matryoshka Representation Learning — the core technique
- Text Embeddings — the broader field
- Sentence Transformers — the library providing training support


---

## Source: KARMA — Multi-Agent LLM Framework for Knowledge Graph Enrichment {#sources-karma-multi-agent-knowledge-graph}

***type:** source-summary | **source:** Karma Multi Agent Knowledge Graph | **related:** Knowledge Graph, Multi Agent Systems, Llm Knowledge Base | **last_compiled:** 2026-04-05 | **summary:** NeurIPS 2025 Spotlight paper: nine-agent LLM framework for automated KG enrichment achieving 83.1% accuracy on 1,200 PubMed articles with 18.6% conflict reduction — the research-grade counterpart to markdown wikis.*

## Key Points
- Nine specialized collaborative LLM agents: entity discovery, relation extraction, schema alignment, conflict resolution
- Tested on 1,200 PubMed articles across 3 domains
- 38,230 new entities discovered; 83.1% LLM-verified correctness; 18.6% conflict edge reduction
- NeurIPS 2025 Spotlight paper
- Formal graph triplets (entity, relation, entity) vs. Karpathy's natural-language markdown

## Detailed Summary

KARMA is the research-grade automated approach to building and enriching knowledge graphs from unstructured text. Nine collaborative agents handle the full pipeline: parsing documents, verifying extractions against existing data, integrating new information, resolving conflicts, and maintaining schema adherence.

The key contrast with Karpathy's approach: KARMA builds formal graph structures (triplets with schema constraints), while Karpathy uses human-readable markdown with wikilinks. KARMA scales to thousands of scientific papers; Karpathy's approach targets ~100 articles with emphasis on auditability and human readability.

Both share the core architecture: raw documents → LLM extraction/compilation → structured knowledge → querying. KARMA adds formal conflict resolution and schema validation; Karpathy's system adds the "filing loop" (query outputs enrich the KB) and health check linting.

## Related Concepts
- [Knowledge Graph](#concepts-knowledge-graph) — the target representation
- [Multi Agent Systems](#concepts-multi-agent-systems) — the nine-agent architecture
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the contrasting personal approach


---

## Source: Thread by @karpathy — LLM Knowledge Bases {#sources-karpathy-llm-knowledge-bases}

***type:** source-summary | **source:** Karpathy Llm Knowledge Bases | **related:** Llm Knowledge Base, Wiki Compilation, Obsidian As Ide, Llm Qa Over Documents, Linting And Health Checks, Rag Vs Index Based Retrieval | **last_compiled:** 2026-04-05 | **summary:** Karpathy describes using LLMs to build and maintain personal markdown wikis from raw ingested sources, with Obsidian as the viewing IDE and LLM-driven Q&A, output generation, and linting.*

## Key Points

- LLMs are increasingly useful for **manipulating knowledge** (markdown/images), not just code
- Architecture: `raw/` directory → LLM compiles → `wiki/` of `.md` files with summaries, backlinks, and concept articles
- **Obsidian** serves as the frontend IDE to view raw data, the compiled wiki, and visualizations
- The LLM writes and maintains the wiki; the human rarely edits it directly
- **Q&A** works without fancy RAG at ~small scale (~100 articles, ~400K words): LLM auto-maintains index files and brief summaries to navigate efficiently
- **Outputs**: markdown reports, Marp slideshows, matplotlib images — all viewable in Obsidian; outputs get "filed back" into the wiki
- **Linting**: LLM health checks find inconsistencies, impute missing data via web search, suggest new article candidates
- **Extra tools**: custom CLI search engine handed off to LLM as a tool for larger queries
- **Future direction**: synthetic data generation + finetuning so the LLM "knows" the corpus in its weights
- Karpathy sees potential for a polished product rather than a collection of scripts

## Detailed Summary

Karpathy outlines a workflow where an LLM acts as the author and maintainer of a personal knowledge base. Source documents (articles, papers, repos, datasets) are ingested into a `raw/` directory using tools like the Obsidian Web Clipper. An LLM then incrementally "compiles" these into a structured wiki of markdown files, producing per-source summaries, concept articles with cross-links, and backlink graphs.

Obsidian is used purely as a viewer/IDE — the human does not write wiki content directly. Plugins like Marp allow viewing LLM-generated slide decks inside Obsidian.

For Q&A, Karpathy found that simple index files and one-line summaries maintained by the LLM were sufficient to navigate a ~400K word corpus without needing a vector database or RAG pipeline. The LLM reads the summaries index, selects relevant articles, and synthesizes answers.

Output formats include markdown reports, Marp slides, and matplotlib visualizations. These outputs are often filed back into the wiki, making the knowledge base self-reinforcing.

LLM-driven linting runs health checks: detecting inconsistencies, filling gaps with web searches, and proposing new concept articles based on observed gaps.

## Notable Quotes

> "You rarely ever write or edit the wiki manually, it's the domain of the LLM."

> "I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents."

> "I think there is room here for an incredible new product instead of a hacky collection of scripts."

> "My own explorations and queries always 'add up' in the knowledge base."

## Related Concepts

- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the core system described in this thread
- [Wiki Compilation](#concepts-wiki-compilation) — the raw→wiki compilation pipeline
- [Obsidian As Ide](#concepts-obsidian-as-ide) — use of Obsidian as a read-only frontend
- [Llm Qa Over Documents](#concepts-llm-qa-over-documents) — Q&A without RAG via index+summaries
- [Linting And Health Checks](#concepts-linting-and-health-checks) — LLM-driven wiki health checks
- [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval) — why simple indexing beats RAG at small scale


---

## Source: LLMs That Compile Knowledge: The Karpathy Methodology and the Democratization of Ontology {#sources-pebblous-cheap-ontology}

***type:** source-summary | **source:** Pebblous Cheap Ontology | **related:** Llm Knowledge Base, Cheap Ontology, Rag Vs Index Based Retrieval, Hallucination Contamination, Data Quality Bottleneck | **last_compiled:** 2026-04-05 | **summary:** Deep analysis placing Karpathy's markdown wiki within 50 years of ontology history, quantifying the RAG vs. fine-tuning vs. LLM-KB tradeoffs, and identifying data quality as the decisive bottleneck.*

## Key Points
- Traditional enterprise knowledge graphs: $10M–$20M upfront, 27% reach production — Karpathy's approach is "Cheap Ontology"
- Three-layer architecture: **raw/** (immutable) → **wiki/** (LLM-maintained) → **schema** (CLAUDE.md/AGENTS.md)
- Context windows expanded 1,000-fold in 5 years (GPT-3 2K → Gemini 2.0 Pro 2M tokens) — enabling full-wiki loading
- RAG accuracy: 87.5%; fine-tuning accuracy on new facts: only 50.4%; Karpathy = wiki-quality dependent
- Data quality > model scale (Microsoft phi-1 study); low-quality raw → contaminated wiki → flawed fine-tuning
- Knowledge graph market: $1.07B (2024) → $6.94B (2030) at 36.6% CAGR
- McKinsey: employees spend 1.8 hours/day (25% of workday) searching for information

## Detailed Summary

Pebblous provides the most historically grounded analysis, tracing the lineage from 1970s formal ontologies through Semantic Web (RDF/OWL/SPARQL), to Google-scale knowledge graphs, to LLM wikis. The key insight: context windows expanding 1,000-fold in five years made it feasible to load an entire personal wiki into a single LLM prompt, eliminating the need for vector database retrieval at personal scale.

The "Cheap Ontology" framing is particularly useful: what required $10–20M, specialized ontology engineers, and years of schema design now costs only API fees and takes days to prototype. The CLAUDE.md or AGENTS.md file replaces formal ontology axioms with natural-language rules.

The comparative table (RAG vs. fine-tuning vs. Karpathy) is quantitative and valuable: fine-tuning achieves only 50.4% accuracy on new facts (vs. RAG's 87.5%), making it a poor choice for knowledge that changes. Karpathy's approach offers a unique advantage: compounding knowledge via the filing loop, which neither RAG nor fine-tuning supports.

The article identifies data quality — not model capability — as the decisive bottleneck. Low-quality raw inputs cascade into contaminated wiki, then into polluted fine-tuning datasets.

## Notable Quotes
> "The bottleneck shifts from technical capability to data quality."
> "Every organization maintains raw directories of meeting notes, emails, and documents in uncompiled state."

## Related Concepts
- [Cheap Ontology](#concepts-cheap-ontology) — the core framing
- [Data Quality Bottleneck](#concepts-data-quality-bottleneck) — critical vulnerability
- [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval) — quantitative comparison
- [Hallucination Contamination](#concepts-hallucination-contamination) — cascading risk
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the methodology


---

## Source: Choosing an Embedding Model {#sources-pinecone-embedding-models-rundown}

***type:** source-summary | **source:** Pinecone Embedding Models Rundown | **related:** Text Embeddings, Bi Encoder Vs Cross Encoder, Openai Embeddings, Mteb | **last_compiled:** 2026-04-05 | **summary:** Pinecone's practical guide comparing OpenAI, Cohere, and E5 embedding models on speed, dimensions, asymmetric search, and MTEB benchmark interpretation.*

## Key Points

- Embedding models compress text into vector representations that capture semantic meaning
- OpenAI ada-002 (1536 dims) took 9:07 to embed ~42K chunks; E5-base-v2 (768 dims, GPU) took 3:53 — nearly 2.5x faster
- Cohere embed-english-v3.0 (1024 dims) sits in between at 5:32
- Asymmetric search requires different treatment for queries vs documents: Cohere uses `input_type` parameter; E5 uses text prefixes ("passage:" / "query:")
- Mean pooling converts token-level embeddings into single vectors by averaging (with padding mask)
- MTEB results are self-reported and some models may be benchmark-optimized

## Detailed Summary

The article walks through the practical mechanics of choosing and using embedding models for RAG. It demonstrates that open-source models like E5 can match or exceed proprietary options in speed when run on GPU, while proprietary models offer easier API integration. The key insight is that dimensionality directly impacts storage cost and speed — higher dimensions do not always mean better retrieval quality. The article warns that Mteb leaderboard scores should be interpreted cautiously because results are self-reported and some models appear fine-tuned specifically for benchmark tasks.

## Notable Quotes

> "Storage costs scale with dimensionality — higher dimensions increase infrastructure expenses."

## Related Concepts

- Text Embeddings — the core technology being compared
- Bi Encoder Vs Cross Encoder — the architectural distinction underlying all embedding models
- Mteb — the benchmark used for evaluation


---

## Source: RAFT — Adapting Language Model to Domain Specific RAG {#sources-raft-retrieval-augmented-fine-tuning}

***type:** source-summary | **source:** Raft Retrieval Augmented Fine Tuning | **related:** Raft, Fine Tuning, Rag Vs Index Based Retrieval | **last_compiled:** 2026-04-05 | **summary:** UC Berkeley paper combining RAG with fine-tuning: train models to ignore distractor documents and cite verbatim from oracle docs, achieving up to 76% improvement on domain-specific benchmarks.*

## Key Points

- RAFT trains models to ignore irrelevant retrieved documents (distractors) while citing verbatim from relevant ones
- Training mix: P% questions with oracle + distractor docs; (1-P)% with distractor-only docs (forces memorization)
- Chain-of-thought answers with explicit quotation markers prevent hallucination
- Results: +35.25% on HotpotQA, +76.35% on TorchHub, +31.41% on HuggingFace over baselines
- Base model: Llama2-7B on 4 A100-40G GPUs; deploys on single GPU
- Outperforms both RAG-only and fine-tuning-only approaches across all tested domains

## Detailed Summary

RAFT addresses a fundamental limitation in both RAG and fine-tuning: RAG alone doesn't train the model to handle domain-specific retrieval patterns, while fine-tuning alone ignores the reality that retrieved documents will be available at inference time. RAFT's analogy: traditional methods are like studying without the textbook you'll have during the exam.

The training recipe is elegantly simple: include distractor documents during training so the model learns to distinguish signal from noise, and require chain-of-thought explanations that quote source material verbatim. The dual-scenario design (sometimes with oracle docs, sometimes without) ensures the model both leverages retrieval and memorizes core domain knowledge.

## Notable Quotes

> "Standard approaches resemble studying without the textbook or practicing without access to reference materials you'll actually have during the test."

## Related Concepts

- Raft — the hybrid RAG + fine-tuning methodology
- Fine Tuning — one of the two approaches RAFT combines
- Synthetic Data Generation — RAFT's training data preparation is a form of synthetic data curation
- Catastrophic Forgetting — RAFT's distractor-only training mitigates by reinforcing domain memorization


---

## Source: RAG vs Fine-tuning — Pipelines, Tradeoffs, and Agriculture Case Study {#sources-rag-vs-finetuning-agriculture}

***type:** source-summary | **source:** Rag Vs Finetuning Agriculture | **related:** Retrieval Augmented Generation, Fine Tuning, Rag Vs Fine Tuning | **last_compiled:** 2026-04-05 | **summary:** ArXiv paper demonstrating RAG and fine-tuning are complementary: fine-tuning adds +6pp accuracy, RAG adds another +5pp, and combining both improved geographic knowledge transfer from 47% to 72% similarity.*

## Key Points

- RAG augments the prompt with external data at runtime; fine-tuning incorporates knowledge into model parameters
- Fine-tuning alone improved accuracy by 6+ percentage points on agricultural QA
- RAG added a further 5 percentage points on top of fine-tuning
- Geographic knowledge transfer improved from 47% to 72% answer similarity
- Tested on Llama2-13B, GPT-3.5, and GPT-4

## Detailed Summary

This research paper provides empirical evidence that Retrieval Augmented Generation and Fine Tuning are complementary rather than competing approaches. Using agriculture as a test domain — chosen for its limited AI adoption and need for location-specific knowledge — the authors implement a multi-stage pipeline covering PDF extraction, Q&A generation, fine-tuning, and GPT-4-based evaluation.

The key finding is cumulative benefit: each technique addresses different knowledge dimensions. Fine-tuning internalizes domain behavior, terminology, and reasoning patterns. RAG provides current factual grounding from external documents. The combination outperforms either alone.

## Notable Quotes

> "RAG augments the prompt with the external data, while fine-Tuning incorporates the additional knowledge into the model itself."

## Related Concepts

- Retrieval Augmented Generation — one of the two compared approaches
- Fine Tuning — the other compared approach
- Rag Vs Fine Tuning — detailed comparison article


---

## Source: From RAG to Context — A 2025 Year-End Review {#sources-ragflow-rag-review-2025}

***type:** source-summary | **source:** Ragflow Rag Review 2025 | **related:** Retrieval Augmented Generation, Context Engineering, Hybrid Search, Multimodal Rag, Ragflow | **last_compiled:** 2026-04-05 | **summary:** RAGFlow's year-end review arguing RAG is evolving from a retrieval pattern into a Context Engine — combining domain knowledge, tool retrieval, and memory into unified context platforms.*

## Key Points

- RAG solidified as "a cornerstone of data infrastructure" in enterprise AI during 2025, contrary to predictions of obsolescence
- Long context windows do not replace RAG — they complement it via "retrieval-first, long-context containment"
- TreeRAG decouples search and retrieval into different text granularities, addressing the "Lost in the Middle" problem
- Graphrag showed promise but revealed challenges: massive token consumption, quality gaps in extraction
- RAG is evolving into a **Context Engine** serving three data categories: domain knowledge, tool data, and conversation state
- Multimodal Rag stalled due to storage costs (512KB per page image with ColPali)
- 85% of production LLM applications now incorporate RAG (up from 30% in early 2024)

## Detailed Summary

The RAGFlow team's comprehensive 2025 review charts RAG's transformation from a simple retriever-generator pipeline into a sophisticated enterprise intelligence architecture. The article identifies four approaches to knowledge provision with roughly 100x cost differences between them, from full RAG to simple grep-based search.

A central thesis is that RAG's core capability — intelligent retrieval — is becoming the foundation for a broader discipline called Context Engineering. Rather than being replaced by [Multi Agent Systems](#concepts-multi-agent-systems), RAG provides the "fuel" that agents need to make good decisions. The article introduces a three-layered context model: domain knowledge (traditional RAG), tool retrieval (selecting which APIs/tools to use from hundreds of options), and conversation state (memory management).

The review also covers practical challenges with Graphrag, noting that while the approach is promising for relational discovery, real-world implementations consume several to dozens of times the original text in tokens, and extraction quality often falls short of expectations.

## Notable Quotes

> "No matter how intelligent an Agent is, the quality of its decisions and actions fundamentally depends on the quality and relevance of the Context it receives."

> RAG is "undergoing its own profound metamorphosis, evolving from the specific pattern of 'Retrieval-Augmented Generation' into a 'Context Engine' with 'intelligent retrieval' as its core capability."

## Related Concepts

- Retrieval Augmented Generation — the core topic
- Context Engineering — RAG's evolutionary destination
- Hybrid Search — combining retrieval strategies
- Multimodal Rag — extending beyond text
- Graphrag — graph-based RAG variant discussed


---

## Source: STORM — Automating Wikipedia Article Creation with LLMs {#sources-storm-automated-wiki-creation}

***type:** source-summary | **source:** Storm Automated Wiki Creation | **related:** Automated Wiki Creation, Llm Knowledge Base, Wiki Compilation | **last_compiled:** 2026-04-05 | **summary:** STORM system: multi-perspective question-asking + retrieval → automated Wikipedia-style article generation with FreshWiki evaluation dataset, contrasting single-shot creation vs. Karpathy's accumulating KB.*

## Key Points
- STORM = Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking
- Three phases: perspective discovery (from related Wikipedia ToCs) → multi-turn expert conversations → outline synthesis
- Introduced **FreshWiki** dataset: recent Wikipedia articles after LLM training cutoffs (prevents data leakage)
- Metrics: heading/entity recall for outlines; ROUGE + entity recall for articles; expert Wikipedia editor rubrics
- Remaining challenges: source bias, red herring fallacy, multi-modal content, balanced retrieval

## Detailed Summary

STORM tackles the pre-writing phase of Wikipedia article creation — research and outline generation — rather than just text production. By simulating conversations between LLMs playing different perspectives, it generates more comprehensive and balanced coverage.

The key innovation vs. naive retrieval: simulating N perspectives (identified from related Wikipedia ToCs) as distinct "expert" personas that ask different questions about the topic. This mirrors human research behavior (consulting multiple experts) and produces richer outlines.

FreshWiki addresses a critical evaluation problem: LLMs trained before a Wikipedia article was written can't have "leaked" knowledge of it, making it a fair test of generation quality.

**Contrast with Karpathy's approach:**
- STORM: single-shot article generation from web search, no persistent KB, produces one article per run
- Karpathy/LLM-KB: persistent, accumulating, incrementally updated knowledge base
- STORM: better for standalone reference articles; LLM-KB better for compounding research knowledge

## Related Concepts
- [Automated Wiki Creation](#concepts-automated-wiki-creation) — STORM's core contribution
- [Wiki Compilation](#concepts-wiki-compilation) — related process in LLM-KB
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the contrasting persistent approach


---

## Source: The Definitive Guide to Synthetic Data Generation Using LLMs {#sources-synthetic-data-generation-llms}

***type:** source-summary | **source:** Synthetic Data Generation Llms | **related:** Synthetic Data Generation, Data Quality Bottleneck, Fine Tuning | **last_compiled:** 2026-04-05 | **summary:** Five-step architecture for LLM-driven synthetic data generation (chunk → context → query → evolve → answer) with quality filtering at every stage.*

## Key Points

- Synthetic data generation replaces weeks of manual annotation with minutes of LLM-driven generation
- Two primary methods: **distillation** (strong model generates for weaker) and **self-improvement** (model iterates on own outputs)
- Five-step pipeline: document chunking → context generation → query generation → query evolution → expected output generation
- Query evolution uses three techniques: in-depth (complexity), in-breadth (diversity), elimination (pruning)
- Quality filtering applied at both context and input levels with multi-dimensional rubrics
- 250,000 instructions generated from 175 human queries demonstrates massive scaling potential

## Detailed Summary

The article presents a production-ready framework for synthetic data generation. The pipeline begins with document chunking (1024-character segments), proceeds through cosine-similarity-based context grouping, then reverses the typical retrieval operation by generating questions from contexts rather than finding contexts for questions.

The most novel contribution is the **query evolution** framework, which iteratively transforms simple questions into complex, diverse test cases. This mirrors the Evol-Instruct methodology used in WizardLM. Quality filtering uses multi-dimensional rubrics assessing clarity, depth, organization, relevance, accuracy, novelty, and efficiency.

A critical design principle: "mirror your application's retriever logic" — synthetic data must match production chunking, tokenization, and overlap settings to be useful for evaluation and training.

## Notable Quotes

> "Mirror your application's retriever logic to ensure synthetic data aligns with production expectations."

## Related Concepts

- Synthetic Data Generation — the core methodology described
- [Data Quality Bottleneck](#concepts-data-quality-bottleneck) — quality filtering is central to the pipeline
- Fine Tuning — synthetic data is a primary input for fine-tuning
- Knowledge Distillation — distillation approach to data generation


---

## Source: Hybrid Search Explained {#sources-weaviate-hybrid-search-explained}

***type:** source-summary | **source:** Weaviate Hybrid Search Explained | **related:** Hybrid Search, Bm25, Vector Search, Weaviate | **last_compiled:** 2026-04-05 | **summary:** Weaviate's technical explanation of hybrid search combining BM25 keyword scoring with dense vector search via Reciprocal Rank Fusion, including the alpha parameter for tuning the balance.*

## Key Points

- Hybrid search merges sparse (BM25) and dense (vector) results into a single ranked list
- BM25 builds on TF-IDF with Binary Independence Model and document-length normalization
- BM25F variant (Weaviate v1.17+) allows per-field weighting (e.g., title vs body)
- Reciprocal Rank Fusion: score = sum(1/(k + r(d))) across both ranked lists
- Alpha parameter: 0 = pure keyword, 0.5 = equal, 1 = pure vector; default 0.75
- Two fusion algorithms available: rankedFusion (default) and relativeScoreFusion

## Detailed Summary

The article explains how Weaviate implements Hybrid Search by running BM25 keyword search and dense vector search in parallel, then merging results. The Bm25 component handles exact-term matching while Vector Search captures semantic meaning. The key tunable is the alpha parameter — defaulting to 0.75 (favoring vector search) — which lets users balance precision of keyword matching against the recall of semantic understanding depending on their use case.

## Related Concepts

- Hybrid Search — the retrieval strategy
- Bm25 — the keyword scoring algorithm
- Vector Search — the semantic component
- Weaviate — the implementing database


---

## Automated Wiki Creation {#concepts-automated-wiki-creation}

***type:** concept | **sources:** Storm Automated Wiki Creation | **related:** Wiki Compilation, Llm Knowledge Base, Multi Agent Systems | **last_compiled:** 2026-04-05 | **summary:** STORM's approach: single-shot, multi-perspective Wikipedia-style article generation from web search using simulated expert conversations and outline-first synthesis — contrasting with Karpathy's incremental, accumulating KB model.*

## Overview

Automated wiki creation refers to systems that generate full structured articles from scratch, typically from web search or document corpora, without requiring human authoring. STORM is the primary research system; Karpathy's LLM-KB is the alternative persistent-KB model.

## STORM's Approach

**Core innovation**: Rather than retrieving and summarizing, STORM simulates the pre-writing research phase:
1. **Perspective discovery**: Analyze related Wikipedia ToCs to identify N distinct viewpoints on the topic
2. **Simulated expert conversations**: LLMs role-playing each perspective ask multi-turn questions, breaking down queries into searchable sub-questions
3. **Outline synthesis**: Refine a structured outline from the conversations before writing full content

**FreshWiki evaluation**: Dataset of recent Wikipedia articles created after LLM training cutoffs — ensures test articles couldn't have been memorized during training.

**Metrics**: Heading soft recall, entity recall (outline quality); ROUGE, entity recall (article quality); Wikipedia editor expert rubrics (interest, coherence, relevance, coverage, verifiability).

## STORM vs. Karpathy LLM-KB

| Dimension | STORM | Karpathy LLM-KB |
|-----------|-------|-----------------|
| Mode | Single-shot article generation | Persistent, accumulating KB |
| Input | Web search per topic | Curated raw/ sources |
| Output | One standalone article | Full wiki with cross-links |
| Compounding | None | Yes (filing loop) |
| Auditability | Source citations | raw/ provenance |
| Best for | Standalone reference articles | Research knowledge synthesis |

## Sources
- [Storm Automated Wiki Creation](#sources-storm-automated-wiki-creation) — full STORM description and evaluation

## Related Concepts
- [Wiki Compilation](#concepts-wiki-compilation) — the persistent-KB counterpart
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the accumulating approach
- [Multi Agent Systems](#concepts-multi-agent-systems) — multi-perspective agent architecture


---

## Cheap Ontology {#concepts-cheap-ontology}

***type:** concept | **sources:** Pebblous Cheap Ontology | **related:** Llm Knowledge Base, Knowledge Graph, Markdown As Universal Interface | **last_compiled:** 2026-04-05 | **summary:** Pebblous framing: LLM wikis replace $10M–$20M enterprise knowledge graphs using only markdown files, LLM APIs, and natural-language schema instructions — democratizing what was once exclusive ontology engineering expertise.*

## Overview

"Cheap Ontology" is the Pebblous framing for what Karpathy's LLM wiki approach represents historically: a 1000x cost reduction in building structured knowledge systems, achieved by replacing formal ontology engineering with LLM-maintained markdown files.

## Key Ideas

**The cost disruption:**
- Traditional enterprise knowledge graphs: $10M–$20M upfront investment, ontology engineers at $107K–$207K/year, only 27% reaching production
- Karpathy's approach: API costs only, setup in days, no specialized expertise required

**What gets replaced:**
- RDF/OWL/SPARQL formal ontologies → natural-language markdown with wikilinks
- Schema axioms → CLAUDE.md or AGENTS.md instructions in plain English
- Ontology engineers → developers who can write a system prompt
- Formal reasoners → LLM health checks (linting)

**Context window as enabler:** GPT-3 had 2K tokens; Gemini 2.0 Pro has 2M tokens — a 1,000-fold expansion in five years. This expansion is what made loading entire wikis into context feasible, eliminating the need for vector retrieval at personal scale.

**Historical phases:**
1. 1970s–2000: Expert-built formal ontologies (Description Logic, Closed World Assumption)
2. 2001–2007: Semantic Web (RDF, RDFS, OWL, SPARQL) — technically sound, expensive to deploy
3. 2007–2020: Knowledge graph maturation (DBpedia, Google's 570M-entity graph, Wikidata)
4. 2024–present: LLM wikis — Cheap Ontology era

## Limitations

Cheap Ontology trades rigor for accessibility:
- No formal query language (SPARQL) — just LLM natural-language navigation
- No closed-world reasoning — LLMs can confabulate
- Scale ceiling: ~100–400 articles; beyond this, LlamaIndex or GraphRAG needed
- No schema enforcement — the LLM must be prompted to maintain consistency

## Sources
- [Pebblous Cheap Ontology](#sources-pebblous-cheap-ontology) — coined the "Cheap Ontology" framing; provides full historical context

## Related Concepts
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the implementation of Cheap Ontology
- [Knowledge Graph](#concepts-knowledge-graph) — the expensive alternative
- [Markdown As Universal Interface](#concepts-markdown-as-universal-interface) — the substrate
- [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval) — retrieval implications


---

## Data Quality Bottleneck {#concepts-data-quality-bottleneck}

***type:** concept | **sources:** Pebblous Cheap Ontology, Decodingai Second Brain Rag | **related:** Llm Knowledge Base, Hallucination Contamination, Wiki Compilation | **last_compiled:** 2026-04-05 | **summary:** In LLM knowledge base pipelines, data quality at the raw input stage — not model capability — is the decisive factor: low-quality ingestion cascades into contaminated wiki content and flawed fine-tuning.*

## Overview

As LLM capability has grown, the bottleneck in knowledge management systems has shifted from "can the LLM understand this?" to "is the input data good enough for the LLM to build on?" Data quality at the pipeline entry point determines everything downstream.

## Key Ideas

**The cascade:**
Low-quality raw data → contaminated wiki entries → polluted synthetic Q&A generation → permanently flawed fine-tuned models

**Research evidence:**
- Microsoft phi-1 (2023): "data quality matters more than model scale" — a 1.3B parameter model trained on textbook-quality synthetic data achieved competitive results against far larger models
- Gretel (2024): +73.6% performance improvement using high-quality synthetic data vs. human-curated baseline
- Amazon Science (2024): small amounts of high-quality data consistently outperformed large quantities of low-quality data
- Hybrid approaches (real + synthetic data) outperformed either alone

**Practical implications for LLM-KB:**
- Curate sources aggressively before ingestion — don't just dump all web content into `raw/`
- Prefer primary sources (papers, official docs) over summaries of summaries
- Use LLM quality scoring during ETL (as in the Decoding AI FTI pipeline) to filter low-quality content
- Never ingest from sources you wouldn't trust as authoritative

**The "garbage in, garbage out" amplification:**
Unlike traditional databases where bad data is contained, in LLM-maintained wikis bad data gets synthesized, cross-linked, and potentially used to generate training data. The contamination amplifies rather than stays local.

## Sources
- [Pebblous Cheap Ontology](#sources-pebblous-cheap-ontology) — identifies data quality as the decisive bottleneck; cites phi-1, Gretel, Amazon Science studies
- [Decodingai Second Brain Rag](#sources-decodingai-second-brain-rag) — implements quality scoring via LLMs during ETL as practical mitigation

## Related Concepts
- [Hallucination Contamination](#concepts-hallucination-contamination) — the downstream consequence
- [Wiki Compilation](#concepts-wiki-compilation) — where quality determines output
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the system affected
- [Linting And Health Checks](#concepts-linting-and-health-checks) — detection mechanism


---

## Hallucination Contamination {#concepts-hallucination-contamination}

***type:** concept | **sources:** Antigravity Post Code Ai Workflow, Pebblous Cheap Ontology, Glenrhodes Karpathy Workflow | **related:** Llm Knowledge Base, Data Quality Bottleneck, Vault Separation, Linting And Health Checks | **last_compiled:** 2026-04-05 | **summary:** The risk that LLM-generated errors written into a wiki propagate into future queries and fine-tuning, corrupting the knowledge base over time.*

## Overview

Hallucination contamination is the primary systemic risk in LLM-maintained knowledge bases. When an LLM generates an incorrect fact or fabricated connection and writes it into the wiki, that error becomes part of the knowledge substrate used to answer future queries — and, critically, to generate fine-tuning training data.

## Key Ideas

**The contamination cascade:**
1. LLM hallucinates a connection or fact during compilation
2. The error is written into a wiki article
3. Future queries reference this wiki article, propagating the error
4. If the wiki is used to generate synthetic Q&A for fine-tuning, the error is baked into model weights permanently

**Research backing:** Tanwar et al. (2024) demonstrated that fine-tuning on hallucinated data causes "poor calibration," permanently embedding errors into model weights. This is qualitatively worse than a runtime retrieval error — it's an irreversible weight corruption.

**Why it's worse than RAG hallucinations:** In traditional RAG, a hallucinated retrieval result affects one query. In an LLM wiki, it affects all future queries that touch that article, plus any downstream fine-tuning.

## Mitigation Strategies

1. **Vault separation** (Steph Ango, Obsidian CEO): Maintain human-curated content in a separate Obsidian vault from agent-generated content. Never let AI-generated knowledge contaminate your personal knowledge base.

2. **Provenance tracing**: All wiki claims should trace back to `raw/` source files. Unsourced assertions in wiki articles are a red flag.

3. **Linting / health checks**: LLM agents periodically scan the wiki for contradictions, verify claims against source documents, and flag unsupported assertions.

4. **Incremental verification**: When ingesting new sources, explicitly check new content against existing wiki claims for contradictions before writing.

5. **Data quality gates**: Validate raw input quality before ingestion — garbage in, garbage out. Low-quality sources generate low-quality wiki content.

## Sources
- [Antigravity Post Code Ai Workflow](#sources-antigravity-post-code-ai-workflow) — identifies hallucination contamination as the main risk; documents vault separation recommendation
- [Pebblous Cheap Ontology](#sources-pebblous-cheap-ontology) — quantifies the risk cascade; cites Tanwar et al. on fine-tuning degradation
- [Glenrhodes Karpathy Workflow](#sources-glenrhodes-karpathy-workflow) — describes health checks as active mitigation

## Related Concepts
- [Data Quality Bottleneck](#concepts-data-quality-bottleneck) — contamination starts with bad raw inputs
- [Vault Separation](#concepts-vault-separation) — key mitigation strategy
- [Linting And Health Checks](#concepts-linting-and-health-checks) — active detection and correction
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the system at risk


---

## Knowledge Base Product Gap {#concepts-knowledge-base-product-gap}

***type:** concept | **sources:** Glenrhodes Karpathy Workflow, Antigravity Post Code Ai Workflow, Pebblous Cheap Ontology | **related:** Llm Knowledge Base, Personal Knowledge Management, Cheap Ontology | **last_compiled:** 2026-04-05 | **summary:** Karpathy's own acknowledgment that the current LLM-KB is 'a hacky collection of scripts' — and the product opportunity to build polished tooling that makes AI-maintained wikis accessible to non-technical users.*

## Overview

Despite the conceptual elegance of Karpathy's LLM knowledge base approach, the current state is explicitly "a hacky collection of scripts." This creates a significant product gap: the underlying idea is sound and desirable, but the UX is inaccessible to anyone without CLI/API/Obsidian expertise.

## The Gap

**Current barriers:**
- Requires CLI tooling and LLM API configuration
- Directory structure setup is manual
- Obsidian installation and Web Clipper configuration
- No automated ingestion from multiple source types (PDFs, YouTube, RSS, Slack)
- No quality scoring or deduplication at ingestion
- No scheduled compilation or health check alerts
- No UI for non-technical users

## The Opportunity

**What a polished product would provide:**
- One-click setup: directory structure + Obsidian configured automatically
- Multi-source ingestion: web clipper, PDF drag-and-drop, YouTube transcript, RSS feed, email
- LLM quality scoring at ingestion: filter low-quality sources before they enter the pipeline
- Automated compilation: scheduled incremental builds
- Proactive health checks: alerts when wiki content is stale or inconsistent
- Accessible UI: non-technical users can build and query their own LLM-maintained wikis

## Market Context

From Pebblous: the knowledge graph market is growing from $1.07B (2024) to $6.94B (2030) at 36.6% CAGR. McKinsey data shows employees spend 1.8 hours/day (25% of workday) searching for information. The "quality assurance layer" — validating raw material quality before pipeline entry — is identified as an independent business opportunity.

Every organization has a `raw/` directory equivalent: unsorted meeting notes, emails, Slack messages, documents. The product that compiles this into a queryable LLM wiki without technical setup is the gap.

## Current Alternatives

- **Notion AI**: knowledge assistant for Notion content, not a general-purpose KB compiler
- **Google NotebookLM**: closest product analog — upload documents, ask questions — but single-session, no persistent wiki
- **Mem.ai**: AI note-taking with automatic connections, but not a compilation-based wiki
- None of these implement the full Karpathy pipeline: raw → compile → wiki → Q&A → file back → lint

## Sources
- [Glenrhodes Karpathy Workflow](#sources-glenrhodes-karpathy-workflow) — Karpathy's "hacky scripts" acknowledgment
- [Antigravity Post Code Ai Workflow](#sources-antigravity-post-code-ai-workflow) — identifies the product gap explicitly
- [Pebblous Cheap Ontology](#sources-pebblous-cheap-ontology) — market sizing and "quality assurance layer" opportunity

## Related Concepts
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the underlying system
- [Personal Knowledge Management](#concepts-personal-knowledge-management) — the broader domain
- [Cheap Ontology](#concepts-cheap-ontology) — what the product would democratize


---

## Knowledge Graph {#concepts-knowledge-graph}

***type:** concept | **sources:** Karma Multi Agent Knowledge Graph, Gallagher Second Brain Knowledge Graphs, Graphiti Temporal Knowledge Graphs, Pebblous Cheap Ontology | **related:** Llm Knowledge Base, Cheap Ontology, Temporal Knowledge, Multi Agent Systems | **last_compiled:** 2026-04-05 | **summary:** Formal representation of knowledge as nodes (entities) and edges (relationships), with three distinct modern approaches: KARMA (automated multi-agent enrichment), Graphiti (temporal context graphs), and Gallagher's Knowledge Graph Kit (personal SQLite graph).*

## Overview

A knowledge graph represents information as a network of entities (nodes) and relationships (edges), enabling structured querying and reasoning that flat text doesn't support. LLMs have dramatically changed how knowledge graphs are built and maintained — shifting from expensive manual ontology engineering to automated extraction and enrichment.

## Three Modern LLM-Powered Approaches

### KARMA (Research-Grade Automated Enrichment)
- **Architecture**: 9 collaborative LLM agents (entity discovery, relation extraction, schema alignment, conflict resolution)
- **Input**: Unstructured scientific text (PubMed articles)
- **Output**: Formal graph triplets with schema validation
- **Performance**: 83.1% accuracy, 38,230 new entities from 1,200 papers, 18.6% conflict reduction
- **Best for**: Large-scale scientific literature domains
- **NeurIPS 2025 Spotlight**

### Graphiti (Temporal Context Graphs)
- **Architecture**: Open-source framework; episodes (raw) → entities/relationships (with time windows)
- **Key feature**: Facts have validity windows — when they became true and when superseded
- **Retrieval**: Hybrid (semantic + BM25 + graph traversal)
- **Best for**: AI agents operating in dynamic, changing environments
- **Open source** via Zep AI

### Knowledge Graph Kit (Personal Graph)
- **Architecture**: SQLite (nodes/edges) + ChromaDB (semantic search)
- **Node types**: Task, Note, Person, Project
- **Edge labels**: part_of, mentions, related_to
- **Best for**: Personal task/project/relationship management

## Knowledge Graphs vs. Markdown Wikis

| Dimension | Knowledge Graph | Markdown Wiki (Karpathy) |
|-----------|-----------------|--------------------------|
| Structure | Formal (triplets) | Implicit (wikilinks) |
| Queryability | Structured + semantic | LLM-mediated natural language |
| Temporality | Explicit (Graphiti) | Manual (file dates) |
| Auditability | Provenance to episodes | Provenance to raw/ files |
| Setup complexity | Higher | Lower |
| Scale | Enterprise to production | Personal |

## The Convergence

Both approaches share core principles: raw input preserved as source of truth, LLM-derived structured knowledge separate from raw, incremental enrichment from new sources, conflict detection. The difference is representation: formal graph triplets vs. human-readable markdown.

## Sources
- [Karma Multi Agent Knowledge Graph](#sources-karma-multi-agent-knowledge-graph) — automated KG enrichment at research scale
- [Graphiti Temporal Knowledge Graphs](#sources-graphiti-temporal-knowledge-graphs) — temporal context graphs for AI agents
- [Gallagher Second Brain Knowledge Graphs](#sources-gallagher-second-brain-knowledge-graphs) — personal SQLite graph approach
- [Pebblous Cheap Ontology](#sources-pebblous-cheap-ontology) — historical context; KGs as expensive alternative to markdown wikis

## Related Concepts
- [Cheap Ontology](#concepts-cheap-ontology) — LLM wikis as low-cost alternative to KGs
- [Temporal Knowledge](#concepts-temporal-knowledge) — Graphiti's temporal features
- [Multi Agent Systems](#concepts-multi-agent-systems) — KARMA's multi-agent architecture
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the markdown-based alternative


---

## Linting and Health Checks {#concepts-linting-and-health-checks}

***type:** concept | **sources:** Karpathy Llm Knowledge Bases | **related:** Llm Knowledge Base, Wiki Compilation | **last_compiled:** 2026-04-05 | **summary:** LLM-driven health checks over the compiled wiki to find inconsistencies, fill data gaps, detect broken links, identify orphan articles, and suggest new content.*

## Overview

Wiki linting is the process of running LLM-powered health checks over the compiled wiki to maintain data integrity, surface inconsistencies, and suggest improvements. It is an incremental, ongoing process rather than a one-time step.

## Key Ideas

- **Inconsistency detection**: The LLM compares claims across articles to find contradictions.
- **Missing data imputation**: Gaps in knowledge can be filled using web search tools during a lint pass.
- **Broken link detection**: Find `Wikilinks` pointing to non-existent files.
- **Orphan detection**: Identify wiki articles with no incoming links.
- **New article suggestions**: The LLM identifies concepts mentioned across sources that don't yet have dedicated articles.
- **Stale content detection**: Raw files not yet compiled into the wiki.
- **LLM-generated questions**: The LLM suggests further questions to explore and look into, driving future research directions.

## Output

Lint results are saved to `output/lint-report.md` and can be filed back into the wiki to track outstanding issues.

## Sources

- [Karpathy Llm Knowledge Bases](#sources-karpathy-llm-knowledge-bases) — Karpathy's description of LLM health checks over the wiki

## Related Concepts

- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the system being linted
- [Wiki Compilation](#concepts-wiki-compilation) — the pipeline that produces the wiki being checked


---

## LLM Knowledge Base {#concepts-llm-knowledge-base}

***type:** concept | **sources:** Karpathy Llm Knowledge Bases | **related:** Wiki Compilation, Obsidian As Ide, Llm Qa Over Documents, Linting And Health Checks, Rag Vs Index Based Retrieval | **last_compiled:** 2026-04-05 | **summary:** A personal knowledge base where an LLM authors and maintains all wiki content from raw ingested sources, with humans interacting only via natural language.*

## Overview

An LLM knowledge base is a system where source documents are ingested into a `raw/` directory and an LLM incrementally compiles them into a structured wiki of markdown files. The human owner interacts with the system only through natural language prompts — the LLM writes, updates, and maintains all wiki content directly.

## Key Ideas

- **LLM as author**: The LLM owns the wiki directory and writes all content. Humans rarely edit wiki files manually.
- **Incremental compilation**: New raw sources are compiled into the wiki without rewriting unchanged articles.
- **Structured output**: The wiki contains source summaries, concept articles with cross-links, backlink graphs, and index files.
- **Self-reinforcing**: Queries and explorations produce outputs (reports, slides, images) that get filed back into the wiki, compounding knowledge over time.
- **Scalable without RAG**: At ~small scale (~100 articles, ~400K words), LLM-maintained index files and one-line summaries are sufficient for effective Q&A without a vector database.
- **Product opportunity**: Karpathy notes this workflow could become a polished product rather than a collection of scripts.

## Architecture

```
raw/          ← ingested source documents (source of truth)
wiki/         ← LLM-compiled and maintained
  _index.md   ← master article index
  _meta/      ← summaries, link graph, manifest
  sources/    ← per-source summary articles
  concepts/   ← cross-source concept articles
output/       ← reports, slides, images (filed back into wiki)
```

## Sources

- [Karpathy Llm Knowledge Bases](#sources-karpathy-llm-knowledge-bases) — original description of the workflow by Andrej Karpathy

## Related Concepts

- [Wiki Compilation](#concepts-wiki-compilation) — the pipeline from raw → wiki
- [Obsidian As Ide](#concepts-obsidian-as-ide) — the viewing frontend
- [Llm Qa Over Documents](#concepts-llm-qa-over-documents) — Q&A over the compiled wiki
- [Linting And Health Checks](#concepts-linting-and-health-checks) — maintaining wiki integrity
- [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval) — why simple indexing can beat RAG


---

## LLM Q&A Over Documents {#concepts-llm-qa-over-documents}

***type:** concept | **sources:** Karpathy Llm Knowledge Bases | **related:** Llm Knowledge Base, Rag Vs Index Based Retrieval, Wiki Compilation | **last_compiled:** 2026-04-05 | **summary:** Using an LLM agent to answer complex questions over a compiled wiki by reading index files and summaries to navigate to relevant full articles, without needing a vector database.*

## Overview

Once a wiki is compiled and large enough, an LLM agent can answer complex research questions by navigating the wiki's index and summary files to find relevant articles, reading them in full, and synthesizing answers.

## Key Ideas

- **Index-first navigation**: The LLM reads `_meta/summaries.md` (one-line summaries of all articles) to identify relevant documents before reading full articles.
- **No vector DB required**: At ~small scale (~100 articles, ~400K words), LLM-maintained summaries and indexes are sufficient — no RAG pipeline needed.
- **Self-improving**: Query outputs (reports, slides, images) are filed back into the wiki, so every Q&A session enhances the knowledge base for future queries.
- **CLI tool integration**: Custom search tools can be handed to the LLM via CLI for larger or more complex queries.
- **Output formats**: Answers are rendered as markdown reports, Marp slide decks, or matplotlib visualizations — not just text in a terminal.

## Workflow

1. User asks a question in natural language
2. LLM reads `_meta/summaries.md` to find relevant articles
3. LLM reads full relevant articles from `wiki/`
4. LLM synthesizes answer, citing sources with `Wikilinks`
5. (Optional) LLM saves substantial answers to `output/reports/` or files them into the wiki

## Sources

- [Karpathy Llm Knowledge Bases](#sources-karpathy-llm-knowledge-bases) — Karpathy's description of Q&A over a compiled wiki

## Related Concepts

- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the system this Q&A operates over
- [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval) — comparison of index-based vs. vector retrieval approaches
- [Wiki Compilation](#concepts-wiki-compilation) — the compilation process that makes Q&A possible


---

## Markdown as Universal Interface {#concepts-markdown-as-universal-interface}

***type:** concept | **sources:** Antigravity Post Code Ai Workflow, Karpathy Llm Knowledge Bases | **related:** Llm Knowledge Base, Obsidian As Ide, Cheap Ontology | **last_compiled:** 2026-04-05 | **summary:** The observation that markdown is simultaneously human-readable, LLM-friendly, version-controllable, tool-agnostic, and future-proof — making it the optimal substrate for LLM-maintained knowledge bases.*

## Overview

Karpathy's system and its derivatives rely entirely on markdown as the storage and interchange format. This isn't incidental — markdown uniquely satisfies all the competing requirements of a personal knowledge system.

## Why Markdown Works

**Human-readable**: Anyone can open a `.md` file in any text editor and read it. No schema to understand, no database to query.

**LLM-friendly**: Markdown is heavily represented in training data. LLMs generate well-structured markdown natively. Headers, bullets, wikilinks, code blocks — all map naturally to LLM output.

**Version-controllable**: Plain text files work perfectly with Git. Full history, diffing, rollback. Enterprise use cases add version control as a governance mechanism.

**Tool-agnostic**: Obsidian, VS Code, Zed, Cursor, Vim — any editor works. No vendor lock-in to a specific knowledge management platform.

**Future-proof**: `.md` files will be readable in 50 years. Proprietary database formats won't be.

**Wikilinks for structure**: `Concept Name` provides implicit graph structure without a graph database. LLMs can follow wikilinks during compilation to build coherent concept articles.

## The Markdown Workflow

```
raw/source.md          → LLM reads (immutable source of truth)
wiki/concepts/foo.md   → LLM writes (concept articles with Wikilinks)
wiki/sources/bar.md    → LLM writes (source summaries)
wiki/_index.md         → LLM writes (master index)
output/report.md       → LLM writes (generated artifacts)
```

All human-readable. All versionable. All processable by any LLM.

## Limitations

- No formal query language (unlike SPARQL for knowledge graphs)
- Implicit structure depends on LLM following conventions consistently
- Wikilinks require filename matching to resolve — broken links are silent failures until linting
- No built-in temporal tracking (unlike Graphiti's time windows)

## Sources
- [Antigravity Post Code Ai Workflow](#sources-antigravity-post-code-ai-workflow) — articulates "markdown as universal interface" explicitly
- [Karpathy Llm Knowledge Bases](#sources-karpathy-llm-knowledge-bases) — the system that embodies this principle

## Related Concepts
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — uses markdown as substrate
- [Obsidian As Ide](#concepts-obsidian-as-ide) — the viewer/navigator for the markdown files
- [Cheap Ontology](#concepts-cheap-ontology) — markdown replacing formal ontology schemas
- [Knowledge Graph](#concepts-knowledge-graph) — the structured alternative


---

## Multi-Agent Systems for Knowledge Management {#concepts-multi-agent-systems}

***type:** concept | **sources:** Karma Multi Agent Knowledge Graph, Storm Automated Wiki Creation | **related:** Knowledge Graph, Automated Wiki Creation, Llm Knowledge Base | **last_compiled:** 2026-04-05 | **summary:** Using networks of specialized LLM agents (rather than a single LLM) to build and maintain knowledge systems — exemplified by KARMA's 9-agent KG enrichment pipeline and STORM's perspective-simulating article creation system.*

## Overview

Multi-agent approaches to knowledge management divide the pipeline into specialized roles, each handled by a distinct LLM agent. This improves quality through specialization and enables conflict resolution between agents.

## KARMA's 9-Agent Architecture

Roles in KARMA's knowledge graph enrichment pipeline:
1. Document parser
2. Entity discoverer
3. Relation extractor
4. Schema aligner
5. Conflict detector
6. Conflict resolver
7. Knowledge integrator
8. Verifier
9. Schema validator

Each agent focuses on one task; agents pass results to each other and can challenge each other's outputs. The conflict resolution mechanism (18.6% edge conflict reduction) is only possible because distinct agents independently assess the same facts.

## STORM's Perspective-Simulating Agents

STORM uses a different multi-agent pattern: each agent role-plays a distinct *perspective* (identified from Wikipedia ToC analysis). These agents conduct simulated expert conversations, asking questions from their viewpoint. This produces more balanced, comprehensive coverage than a single-perspective research pass.

## When Multi-Agent > Single LLM

- **Conflict detection**: When two agents disagree, that's a signal worth surfacing
- **Scale**: Large document collections that exceed single context windows
- **Specialization**: When entity extraction, relation extraction, and schema validation have different requirements
- **Quality assurance**: Verification agent checks the primary extraction agent's work

## Contrast with Karpathy's Single-LLM Approach

Karpathy's system uses a single LLM in each phase (compilation, Q&A, linting) — simpler architecture, sufficient at personal scale (~100 articles). Multi-agent systems become justified at research-paper scale (thousands of documents) or when formal schema validation is required.

## Sources
- [Karma Multi Agent Knowledge Graph](#sources-karma-multi-agent-knowledge-graph) — 9-agent KG enrichment (NeurIPS 2025 Spotlight)
- [Storm Automated Wiki Creation](#sources-storm-automated-wiki-creation) — perspective-based article creation agents

## Related Concepts
- [Knowledge Graph](#concepts-knowledge-graph) — what KARMA builds
- [Automated Wiki Creation](#concepts-automated-wiki-creation) — STORM's output
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the single-LLM alternative


---

## Obsidian as IDE {#concepts-obsidian-as-ide}

***type:** concept | **sources:** Karpathy Llm Knowledge Bases | **related:** Llm Knowledge Base, Wiki Compilation | **last_compiled:** 2026-04-05 | **summary:** Using Obsidian as a read-only frontend IDE to view LLM-maintained wikis, raw sources, and generated visualizations — with the LLM as the actual author.*

## Overview

In the LLM knowledge base workflow, Obsidian serves as the human-facing IDE: a viewer for raw data, the compiled wiki, and generated outputs. Crucially, the human uses Obsidian primarily to *read* — the LLM writes all content.

## Key Ideas

- **Read-only for humans**: The LLM writes and maintains wiki content; humans rarely edit files directly in Obsidian.
- **Web Clipper**: The Obsidian Web Clipper browser extension converts web articles to markdown for ingestion into `raw/`.
- **Image downloads**: A hotkey workflow downloads referenced images locally so the LLM can reference them during compilation.
- **Plugin ecosystem**: Plugins like Marp enable rendering of LLM-generated slide decks directly in Obsidian.
- **Unified view**: Raw sources, wiki articles, reports, slides, and matplotlib images are all viewable within the same Obsidian vault.

## Why Obsidian

Obsidian's native support for markdown, `Wikilinks`, and backlink graphs makes it a natural fit for a wiki structured around interconnected `.md` files. The graph view and backlinks panel expose the link structure the LLM builds during compilation.

## Sources

- [Karpathy Llm Knowledge Bases](#sources-karpathy-llm-knowledge-bases) — Karpathy's description of Obsidian as the frontend IDE

## Related Concepts

- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the broader system
- [Wiki Compilation](#concepts-wiki-compilation) — the pipeline that produces the wiki Obsidian displays


---

## Personal Knowledge Management (PKM) {#concepts-personal-knowledge-management}

***type:** concept | **sources:** Gallagher Second Brain Knowledge Graphs, Glenrhodes Karpathy Workflow, Antigravity Post Code Ai Workflow | **related:** Second Brain, Llm Knowledge Base, Obsidian As Ide | **last_compiled:** 2026-04-05 | **summary:** The practice of capturing, organizing, and retrieving personal knowledge — transformed by LLMs from manual note-taking (Notion/Obsidian) to AI-compiled, queryable wikis with automatic synthesis and gap-filling.*

## Overview

Personal Knowledge Management (PKM) refers to systematic approaches for managing what you know. Traditional tools (Notion, Obsidian, Roam, Logseq) require humans to write, tag, and link notes manually. LLMs have fundamentally changed this: instead of human-authored notes, an LLM can compile raw sources into structured, interlinked knowledge — with humans acting as curators and questioners rather than authors.

## Evolution: Manual → AI-Augmented → AI-Maintained

**Manual PKM (pre-2024):**
- Tools: Notion, Obsidian, Roam, Logseq, Evernote
- Human writes notes, creates tags, builds links manually
- Knowledge stays where you put it — no synthesis
- Problem: management overhead grows with scale; systems become unmaintainable

**AI-augmented PKM (2023–2024):**
- Tools: Notion AI, Obsidian Copilot, etc.
- Human still authors; AI helps with writing, search, Q&A
- Knowledge grows faster but structure is still human-maintained

**AI-maintained PKM (2025–present, Karpathy approach):**
- Human curates *what* to ingest; LLM handles *everything else*
- Compilation, linking, concept synthesis, Q&A, health checks — all automated
- Human role: curator, questioner, validator

## The Unsustainability Problem

Gallagher's experience with Notion/Obsidian is representative: elaborate systems become unmaintainable as priorities shift. "Complex structures became unmaintainable as priorities shifted. Management overhead quickly outweighed benefits." The LLM-maintained approach addresses this directly by removing the human from the compilation and maintenance loop.

## The Product Gap

Karpathy noted the current state is "a hacky collection of scripts." The PKM product landscape is wide open for tools that:
- Abstract the technical setup (LLM API, directory structure, Obsidian)
- Provide quality scoring and deduplication at ingestion
- Offer scheduled compilation, health checks, and alerts
- Enable non-technical users to run LLM-maintained wikis

## Sources
- [Gallagher Second Brain Knowledge Graphs](#sources-gallagher-second-brain-knowledge-graphs) — practitioner journey from Notion/Obsidian to graph-based LLM KB
- [Glenrhodes Karpathy Workflow](#sources-glenrhodes-karpathy-workflow) — Karpathy's system as PKM evolution
- [Antigravity Post Code Ai Workflow](#sources-antigravity-post-code-ai-workflow) — identifies the product gap

## Related Concepts
- [Second Brain](#concepts-second-brain) — the LLM-powered version
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — Karpathy's specific approach
- [Obsidian As Ide](#concepts-obsidian-as-ide) — current tooling
- [Knowledge Base Product Gap](#concepts-knowledge-base-product-gap) — the market opportunity


---

## Post-Code AI Workflow {#concepts-post-code-ai-workflow}

***type:** concept | **sources:** Antigravity Post Code Ai Workflow | **related:** Llm Knowledge Base, Wiki Compilation | **last_compiled:** 2026-04-05 | **summary:** Karpathy's framing of a shift in AI-augmented developer work: from code generation as the primary token use, to knowledge compilation and orchestration — 'manipulating knowledge, not code.'*

## Overview

The "post-code" framing describes Karpathy's observation that, as LLMs become capable at code generation, the remaining bottleneck for developers shifts from writing code to understanding the problem domain deeply. The answer: structured, queryable knowledge systems.

## The Trajectory

| Period | Concept | Shift |
|--------|---------|-------|
| Feb 2025 | Vibe Coding | Accept all AI-generated code without review |
| Dec 2025 | "Never felt this behind" | Recognition of the magnitude shift in AI capabilities |
| Jan 2026 | Agentic Engineering | Orchestrate AI agents with human oversight |
| Apr 2026 | LLM Knowledge Bases | Move beyond code to knowledge orchestration |

## The Core Claim

"A large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge."

If AI can write code adequately, the competitive advantage shifts to the quality of your knowledge about *what to build* — domain context, competitive landscape, technical constraints, user needs. A structured, LLM-maintained wiki is how you operationalize that advantage.

## Developer Role Transformation

- **From**: Writing code, reviewing AI code suggestions
- **To**: Curating knowledge inputs, asking high-quality questions, validating wiki content

The developers who thrive will be those who build strong knowledge systems — structured, maintained, queryable repositories that give AI agents the context to do exceptional work.

## Sources
- [Antigravity Post Code Ai Workflow](#sources-antigravity-post-code-ai-workflow) — primary source for this framing

## Related Concepts
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the tool for the post-code workflow
- [Wiki Compilation](#concepts-wiki-compilation) — the maintenance activity


---

## RAG vs. Index-Based Retrieval {#concepts-rag-vs-index-based-retrieval}

***type:** concept | **sources:** Karpathy Llm Knowledge Bases | **related:** Llm Qa Over Documents, Llm Knowledge Base | **last_compiled:** 2026-04-05 | **summary:** At small-to-medium scale (~100 articles, ~400K words), LLM-maintained index files and one-line summaries can replace vector database RAG for document Q&A.*

## Overview

Retrieval-Augmented Generation (RAG) uses vector embeddings and similarity search to retrieve relevant document chunks for LLM Q&A. However, at small-to-medium scale, a simpler approach — LLM-maintained index files and concise summaries — can be equally or more effective.

## Key Ideas

- **RAG**: Chunks documents, embeds them into a vector database, retrieves top-k chunks by semantic similarity at query time. Scales to very large corpora but adds infrastructure complexity.
- **Index-based retrieval**: The LLM maintains a `summaries.md` file with one-line descriptions of every article. At query time, the LLM reads this index to identify relevant full articles, then reads those articles directly.
- **Scale threshold**: Karpathy found index-based retrieval sufficient at ~100 articles and ~400K words. Above this scale, RAG or finetuning may become necessary.
- **LLM finetuning as alternative**: At large scale, synthetic data generation + finetuning could encode the corpus into model weights, eliminating context window retrieval entirely.

## Trade-offs

| | Index-Based | RAG | Finetuning |
|---|---|---|---|
| Infrastructure | Minimal | Vector DB required | Training pipeline |
| Scale | Small-medium | Large | Very large |
| Freshness | Immediate (recompile) | Re-embed on update | Retrain to update |
| Accuracy | High (LLM reads full articles) | Depends on chunk quality | Baked into weights |

## Sources

- [Karpathy Llm Knowledge Bases](#sources-karpathy-llm-knowledge-bases) — Karpathy's observation that RAG was not needed at small scale

## Related Concepts

- [Llm Qa Over Documents](#concepts-llm-qa-over-documents) — the Q&A system that uses this retrieval approach
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the broader system


---

## Second Brain {#concepts-second-brain}

***type:** concept | **sources:** Gallagher Second Brain Knowledge Graphs, Decodingai Second Brain Rag | **related:** Llm Knowledge Base, Personal Knowledge Management, Knowledge Graph | **last_compiled:** 2026-04-05 | **summary:** A personal AI system that stores, organizes, and retrieves the user's own knowledge — implemented either as a markdown wiki (Karpathy), a graph database (Gallagher), or a RAG pipeline (Decoding AI), all using LLMs as the intelligence layer.*

## Overview

The "second brain" concept refers to an external system that augments human cognition by storing and organizing personal knowledge in a way that can be retrieved and synthesized on demand. LLMs have dramatically expanded what's possible here — moving from passive note storage to active knowledge compilation and Q&A.

## Key Implementations

### Markdown Wiki (Karpathy)
- Storage: flat markdown files in a directory tree
- Retrieval: LLM reads index files + full articles within context window
- Intelligence: LLM compiles, links, and answers from the wiki
- Scale: ~100 articles, ~400K words
- Best for: research knowledge synthesis, personal learning

### Graph Database (Gallagher / Knowledge Graph Kit)
- Storage: SQLite graph with typed nodes (Task, Note, Person, Project) and labeled edges
- Retrieval: semantic search (ChromaDB) + structured graph queries
- Intelligence: LLM adds notes, creates connections, answers queries
- Best for: personal task/project management, relationship tracking

### Production RAG (Decoding AI)
- Storage: MongoDB vector database with embedded chunks
- Retrieval: semantic + hybrid search (Contextual Retrieval)
- Intelligence: fine-tuned Llama 3.1 8B + agentic RAG with smolagents
- Scale: 1000s of documents
- Best for: team-scale knowledge bases, production reliability

## Shared Principles Across All Approaches

1. **LLM as intelligence layer**: The LLM isn't just retrieval — it synthesizes, connects, and maintains
2. **Source provenance**: Raw input is preserved; derived knowledge traces back to sources
3. **Incremental enrichment**: New inputs add to, not replace, existing knowledge
4. **Natural language interface**: Users interact via conversation, not structured queries

## The Filing Loop (Karpathy's Key Innovation)

What distinguishes the LLM-KB from static note-taking: query outputs get filed back into the knowledge base. Every question asked enriches the system. This compounding effect doesn't exist in RAG (which doesn't remember query results) or fine-tuning (which requires retraining).

## Sources
- [Gallagher Second Brain Knowledge Graphs](#sources-gallagher-second-brain-knowledge-graphs) — graph-based personal KB
- [Decodingai Second Brain Rag](#sources-decodingai-second-brain-rag) — production RAG approach

## Related Concepts
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the Karpathy markdown approach
- [Personal Knowledge Management](#concepts-personal-knowledge-management) — the broader domain
- [Knowledge Graph](#concepts-knowledge-graph) — graph-based representations
- [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval) — retrieval comparison


---

## Temporal Knowledge {#concepts-temporal-knowledge}

***type:** concept | **sources:** Graphiti Temporal Knowledge Graphs | **related:** Knowledge Graph, Llm Knowledge Base | **last_compiled:** 2026-04-05 | **summary:** Graphiti's core contribution: representing knowledge with temporal validity windows (when a fact became true and when it was superseded) rather than treating facts as eternally true or false — critical for AI agents in dynamic environments.*

## Overview

Most knowledge systems treat facts as atemporal: a fact is true or false, with no concept of "true as of [date]" or "superseded by [new fact]." For static domains (mathematics, history) this works. For dynamic domains (product roadmaps, personnel, competitive landscape, medical guidelines), it fails badly.

## Graphiti's Solution

Graphiti models each fact (relationship edge) with a **validity window**:
- `valid_from`: when this fact became true
- `valid_until`: when this fact was superseded (null if still current)

Old facts are **invalidated**, not deleted — preserving historical context. This enables questions like "what did we know about X last quarter?" alongside "what do we know now?"

## Why This Matters for AI Agents

An AI agent operating over long time horizons accumulates memories that become outdated. Without temporal tracking:
- The agent doesn't know whether its knowledge about an entity is current or stale
- Conflicting facts (old and new) both appear equally valid
- The agent can't answer "when did X change?"

With Graphiti's temporal graphs, the agent can:
- Always retrieve the *current* state of an entity
- Query historical states ("what was true before date X?")
- Detect when new information contradicts existing (outdated) facts

## Contrast with Markdown Wiki

Karpathy's markdown wiki handles temporality via:
- File modification dates (implicit)
- Manual notes in articles ("updated March 2026")
- Linting health checks that flag stale content

This is sufficient for research knowledge (papers don't change) but insufficient for operational knowledge (org charts, product state, competitive analysis). Graphiti's explicit temporal model is superior for the latter.

## Sources
- [Graphiti Temporal Knowledge Graphs](#sources-graphiti-temporal-knowledge-graphs) — full Graphiti description

## Related Concepts
- [Knowledge Graph](#concepts-knowledge-graph) — the broader representation
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — handles temporality implicitly via linting


---

## Vault Separation {#concepts-vault-separation}

***type:** concept | **sources:** Antigravity Post Code Ai Workflow | **related:** Hallucination Contamination, Obsidian As Ide, Llm Knowledge Base | **last_compiled:** 2026-04-05 | **summary:** Steph Ango's (Obsidian CEO) recommendation to maintain a clean human-curated Obsidian vault separately from agent-generated content, preventing hallucination contamination of personal knowledge.*

## Overview

Vault separation is the practice of keeping LLM-generated wiki content in a separate Obsidian vault from human-curated personal notes. Recommended by Steph Ango (Obsidian CEO) as a direct response to Karpathy's LLM knowledge base approach.

## The Problem It Solves

LLMs occasionally hallucinate — generating plausible-sounding but incorrect connections or facts. In an LLM-maintained wiki, these errors get written into wiki articles and persist as part of the knowledge substrate. If this wiki is mixed with human-curated personal notes, the hallucinations can contaminate trusted knowledge.

## Implementation

**Two-vault pattern:**
- **Clean vault**: Human-curated notes, personal writing, trusted references. The LLM can read this but never writes here.
- **Agent vault**: LLM-maintained wiki, compiled from ingested sources. The LLM reads and writes here freely.

**In practice:**
- The `wiki/`, `raw/`, and `output/` directories live in the agent vault
- Personal notes and trusted references stay in the clean vault
- Cross-reference across vaults via file system links, not Obsidian wikilinks

## When to Override

For users who fully understand the hallucination risk and want unified search across personal notes and wiki content, a single vault with clear directory separation (and disciplined linting) may be acceptable. The key is intentionality.

## Sources
- [Antigravity Post Code Ai Workflow](#sources-antigravity-post-code-ai-workflow) — documents Steph Ango's recommendation

## Related Concepts
- [Hallucination Contamination](#concepts-hallucination-contamination) — the risk being mitigated
- [Obsidian As Ide](#concepts-obsidian-as-ide) — Obsidian as the vault viewer
- [Linting And Health Checks](#concepts-linting-and-health-checks) — complementary mitigation


---

## Vector Databases {#concepts-vector-databases}

***type:** concept | **sources:** Hn Vector Database Debate, Decodingai Second Brain Rag, Pebblous Cheap Ontology | **related:** Rag Vs Index Based Retrieval, Llm Knowledge Base, Knowledge Graph | **last_compiled:** 2026-04-05 | **summary:** Specialized databases for approximate nearest-neighbor (ANN) search over embedding vectors, necessary at billion-vector scale but often overkill for personal or team-scale LLM knowledge bases where pgvector, FAISS, or index-based LLM navigation suffice.*

## Overview

Vector databases store high-dimensional embedding vectors and support approximate nearest-neighbor (ANN) search — finding the most semantically similar documents to a query vector. They became popular as the retrieval backbone for RAG (Retrieval-Augmented Generation) systems.

## When You Actually Need One

**Specialized vector DB justified at:**
- Billion-vector scale (Wikipedia, social media, enterprise at scale)
- Sub-millisecond latency requirements for semantic search
- Multi-modal retrieval across text, images, audio

**Alternatives that suffice for smaller scale:**
- **pgvector** (PostgreSQL extension): handles most team/personal use cases; caveat: IVF algorithm with nprobes=3 default gives ~50% recall; HNSW support addresses this
- **Elasticsearch**: already deployed in most orgs, handles vector operations without new infrastructure
- **FAISS**: open-source, handles billions of vectors with disk-based indexing
- **Vespa.ai**: underrated hybrid engine (vector + metadata + multi-vector indexing)

## The Real Question

Rather than "do you need a vector database?", the better question is: "do you need approximate nearest-neighbor search?" This surfaces the accuracy-speed tradeoff: ANN is *approximate* — it may miss the true nearest neighbors. For knowledge base Q&A where recall matters, this can be a real problem.

## Relevance to LLM Knowledge Bases

Karpathy's key insight: at ~100 articles / ~400K words, an LLM with a 1M-token context window can load the entire index and navigate to relevant articles by reading one-line summaries — **no vector search needed at all**. This is not approximate; it's exact LLM reasoning over a compact index.

This "index-based navigation" approach:
- Eliminates ANN accuracy loss
- Eliminates vector DB infrastructure cost
- Requires only that the wiki fit within the LLM's context window
- Scales until the index + summaries exceed context limits (~400K words total, ~1M tokens)

## Sources
- [Hn Vector Database Debate](#sources-hn-vector-database-debate) — practitioner consensus on when vector DBs are actually needed
- [Decodingai Second Brain Rag](#sources-decodingai-second-brain-rag) — production RAG that does use MongoDB vector search (justified at scale)
- [Pebblous Cheap Ontology](#sources-pebblous-cheap-ontology) — context window expansion making vector DBs unnecessary at personal scale

## Related Concepts
- [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval) — the comparison with index-based navigation
- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the system that avoids vector DBs
- [Knowledge Graph](#concepts-knowledge-graph) — alternative structured retrieval approach


---

## Wiki Compilation {#concepts-wiki-compilation}

***type:** concept | **sources:** Karpathy Llm Knowledge Bases | **related:** Llm Knowledge Base, Linting And Health Checks | **last_compiled:** 2026-04-05 | **summary:** The LLM-driven pipeline that converts raw ingested documents into a structured, cross-linked markdown wiki with source summaries and concept articles.*

## Overview

Wiki compilation is the process by which an LLM transforms a `raw/` directory of ingested source documents into a structured `wiki/` of markdown files. The process is incremental — only new or changed sources trigger updates to the wiki.

## Key Ideas

- **Source summaries**: Each raw file gets a summary article in `wiki/sources/` covering key points, quotes, and related concepts.
- **Concept articles**: The LLM identifies concepts that appear across multiple sources and synthesizes cross-source articles in `wiki/concepts/`.
- **Cross-linking**: Obsidian-style `Wikilinks` connect concept articles, source summaries, and raw files into a navigable graph.
- **Index and metadata**: The LLM maintains `_index.md` (master article list), `_meta/summaries.md` (one-line summaries), `_meta/links.md` (backlink graph), and `_meta/manifest.md` (compiled file tracking).
- **Incrementalism**: The manifest tracks which raw files have been processed so compilation only touches what's new.

## Compilation Steps

1. Read `_meta/manifest.md` to identify unprocessed raw files
2. For each new raw file: create/update `wiki/sources/<name>.md`
3. Identify key concepts; create/update `wiki/concepts/<concept>.md`
4. Rebuild `wiki/_index.md`
5. Update `_meta/summaries.md`, `_meta/links.md`, `_meta/manifest.md`

## Sources

- [Karpathy Llm Knowledge Bases](#sources-karpathy-llm-knowledge-bases) — Karpathy's description of the raw→wiki pipeline

## Related Concepts

- [Llm Knowledge Base](#concepts-llm-knowledge-base) — the broader system this pipeline belongs to
- [Linting And Health Checks](#concepts-linting-and-health-checks) — downstream quality checks on the compiled wiki


---

## Andrej Karpathy {#entities-andrej-karpathy}

***type:** entity | **entity_type:** person | **sources:** Karpathy Llm Knowledge Bases, Dairai Llm Knowledge Bases Architecture, Glenrhodes Karpathy Workflow, Antigravity Post Code Ai Workflow, Pebblous Cheap Ontology | **related:** Llm Knowledge Base, Post Code Ai Workflow, Wiki Compilation, Obsidian As Ide, Obsidian, Marp | **last_compiled:** 2026-04-06 | **summary:** AI researcher and former Tesla/OpenAI lead who pioneered the LLM-maintained personal knowledge base workflow using markdown wikis and Obsidian.*

## Overview

Andrej Karpathy is a prominent AI researcher and educator known for his work at OpenAI and as the former head of AI at Tesla. In the context of this knowledge base, he is the originator of the LLM-maintained personal knowledge base methodology that serves as the central framework for the entire wiki. On April 2, 2026, Karpathy published a Twitter thread describing his workflow for using LLMs to build and maintain structured markdown wikis from raw ingested sources, sparking widespread discussion and analysis across the AI community.

Karpathy's background in deep learning research and engineering gives him a unique vantage point on how LLMs can be applied beyond code generation. His observation that "a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge" captures a broader shift in how AI practitioners relate to their tools.

## Key Contributions

- **LLM Knowledge Base Methodology**: Defined the raw-to-wiki compilation pipeline where an LLM ingests source documents and incrementally compiles them into a structured, cross-linked markdown wiki. The human acts as curator and questioner while the LLM handles all authoring and maintenance.

- **The Filing Loop**: Articulated the compounding knowledge pattern where query outputs are filed back into the wiki, making every exploration additive. As Glen Rhodes summarized: "His explorations accumulate. The knowledge base grows from use."

- **Post-Code AI Workflow**: Framed the intellectual trajectory from vibe coding (Feb 2025) through agentic engineering (Jan 2026) to knowledge orchestration (Apr 2026), arguing that once LLMs solve code generation, the bottleneck shifts to domain understanding.

- **Product Vision**: Acknowledged the current implementation is "a hacky collection of scripts" and identified the opportunity for a polished product, helping to define the [Knowledge Base Product Gap](#concepts-knowledge-base-product-gap).

- **Index-Based Retrieval**: Demonstrated that at personal scale (~100 articles, ~400K words), LLM-maintained index files and one-line summaries replace the need for vector database RAG entirely, a finding that challenged prevailing assumptions about retrieval infrastructure requirements.

## Role in LLM Knowledge Bases

Karpathy is the central figure in this knowledge base. His April 2026 thread is the primary source document, and virtually every other source in the wiki either directly analyzes his approach (DAIR.AI, Glen Rhodes, Antigravity Codes, Pebblous) or provides contrasting systems that are compared against his methodology ([Storm](#entities-storm), [Karma](#entities-karma), [Graphiti](#entities-graphiti)). His design choices -- markdown as substrate, Obsidian as viewer, LLM as sole author, filing loop for compounding -- define the reference architecture against which all alternatives are measured.

His intellectual trajectory also illustrates the broader theme of [Post Code Ai Workflow](#concepts-post-code-ai-workflow): the shift from using AI to write code toward using AI to compile and manage knowledge.

## Mentioned In

- [Karpathy Llm Knowledge Bases](#sources-karpathy-llm-knowledge-bases) -- original Twitter thread describing the full workflow
- [Dairai Llm Knowledge Bases Architecture](#sources-dairai-llm-knowledge-bases-architecture) -- Elvis Saravia's system architecture analysis of Karpathy's approach
- [Glenrhodes Karpathy Workflow](#sources-glenrhodes-karpathy-workflow) -- Glen Rhodes' technical walkthrough emphasizing the filing loop and product gap
- [Antigravity Post Code Ai Workflow](#sources-antigravity-post-code-ai-workflow) -- Antigravity Codes' broadest analysis placing Karpathy's work in the vibe-coding-to-knowledge trajectory
- [Pebblous Cheap Ontology](#sources-pebblous-cheap-ontology) -- Pebblous positions Karpathy's approach within 50 years of ontology history as "Cheap Ontology"


---

## ChromaDB {#entities-chromadb}

***type:** entity | **entity_type:** tool | **sources:** Gallagher Second Brain Knowledge Graphs | **related:** Vector Databases, Knowledge Graph, Second Brain, Sqlite, Faiss, Pgvector | **last_compiled:** 2026-04-06 | **summary:** An open-source embedding database used in Gallagher's Knowledge Graph Kit to provide semantic vector search over graph nodes alongside SQLite structural storage.*

## Overview

ChromaDB is an open-source vector database (embedding database) designed for AI applications. It stores high-dimensional embedding vectors and supports semantic similarity search, making it possible to find conceptually related content even when exact keywords do not overlap. ChromaDB is notable for its developer-friendly API, lightweight footprint, and easy integration with Python-based LLM workflows.

In the context of this knowledge base, ChromaDB appears as a key component of Sam Gallagher's Knowledge Graph Kit, where it provides the semantic search layer on top of a [Sqlite](#entities-sqlite) graph database. While the SQLite database stores the structural graph (nodes, edges, types, relationships), ChromaDB enables finding related nodes by meaning rather than by explicit link traversal or keyword matching.

## Key Features

- **Lightweight and embeddable**: ChromaDB can run in-process alongside application code, making it suitable for personal-scale projects without requiring separate database infrastructure.

- **Python-native API**: Designed for easy integration with Python-based AI workflows, including LangChain, LlamaIndex, and custom agent pipelines.

- **Automatic embedding**: ChromaDB can compute embeddings automatically using built-in embedding functions, reducing the setup required for vector search.

- **Metadata filtering**: Supports filtering search results by metadata alongside vector similarity, enabling hybrid queries that combine semantic meaning with structured attributes.

## Role in LLM Knowledge Bases

ChromaDB illustrates the spectrum of vector database options discussed in [Vector Databases](#concepts-vector-databases). It sits between full-scale production vector databases (Pinecone, Weaviate, Milvus) and simple in-memory solutions. For personal knowledge management applications like Gallagher's Knowledge Graph Kit, ChromaDB provides just enough semantic search capability without the operational complexity of a dedicated vector database service.

In the broader context of [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval), ChromaDB represents the vector search approach: embed content into vectors, then retrieve by semantic similarity at query time. Karpathy's alternative -- LLM-maintained index files and one-line summaries navigated directly by the LLM -- avoids the need for any vector database at personal scale, though ChromaDB could serve as a useful upgrade path when the wiki grows beyond context window limits.

## Mentioned In

- [Gallagher Second Brain Knowledge Graphs](#sources-gallagher-second-brain-knowledge-graphs) -- used as the vectorization layer in the Knowledge Graph Kit alongside SQLite


---

## DAIR.AI {#entities-dairai}

***type:** entity | **entity_type:** org | **sources:** Dairai Llm Knowledge Bases Architecture | **related:** Elvis Saravia, Llm Knowledge Base | **last_compiled:** 2026-04-06 | **summary:** An AI education and research organization whose Academy published the definitive system architecture analysis of Karpathy's LLM knowledge base methodology.*

## Overview

DAIR.AI (Democratizing Artificial Intelligence Research, Education, and Technologies) is an organization focused on making AI research and education accessible. Its Academy arm publishes technical deep-dives, tutorials, and analyses of cutting-edge AI methodologies. DAIR.AI is founded and led by [Elvis Saravia](#entities-elvis-saravia).

In the context of LLM knowledge bases, DAIR.AI Academy published what is arguably the most thorough technical analysis of Karpathy's workflow, formalizing it as a four-phase operational cycle and framing the LLM as a "compiler" for knowledge. This analysis transformed an informal Twitter thread into a reproducible system architecture that practitioners could implement and extend.

## Key Contributions

- **System architecture documentation**: The DAIR.AI Academy article provided the most structured and complete description of the LLM-KB system, including the four-phase cycle, distinguishing advantages, implementation requirements, and future directions.

- **Research extension**: The article author (Saravia) described building his own agent-based research indexing system using Obsidian and the qmd CLI tool for semantic indexing, demonstrating that the pattern extends beyond Karpathy's specific implementation.

- **Educational framing**: By publishing through an educational platform, DAIR.AI made the LLM-KB concept accessible to a broader audience of AI practitioners and students.

## Role in LLM Knowledge Bases

DAIR.AI represents the educational and documentation layer of the LLM-KB ecosystem. Its analysis is the primary source for understanding the system architecture in formal terms, and it serves as the bridge between Karpathy's original description and practitioner implementation.

## Mentioned In

- [Dairai Llm Knowledge Bases Architecture](#sources-dairai-llm-knowledge-bases-architecture) -- the DAIR.AI Academy article providing the four-phase operational cycle analysis


---

## Dataview {#entities-dataview}

***type:** entity | **entity_type:** tool | **sources:** Karpathy Llm Knowledge Bases, Dairai Llm Knowledge Bases Architecture | **related:** Obsidian, Obsidian As Ide, Llm Knowledge Base | **last_compiled:** 2026-04-06 | **summary:** An Obsidian community plugin that enables database-like queries over markdown file frontmatter, useful for dynamic views of LLM-maintained wiki metadata.*

## Overview

Dataview is one of the most popular community plugins for [Obsidian](#entities-obsidian), providing a query language for treating a vault of markdown files as a lightweight database. It reads YAML frontmatter metadata from `.md` files and allows users to write inline queries that generate dynamic tables, lists, and task views based on file properties like `type`, `last_compiled`, `sources`, and `related`.

In an LLM-maintained knowledge base where every article has structured frontmatter (as seen throughout this wiki), Dataview becomes a powerful navigation and auditing tool. Users can query for all concept articles modified before a certain date, list all sources related to a specific concept, or generate dashboards showing compilation status across the entire wiki.

## Key Features

- **Query language (DQL)**: Dataview provides a SQL-like query language for filtering, sorting, and grouping markdown files by their frontmatter properties. For example, `TABLE summary FROM "wiki/concepts" WHERE type = "concept" SORT last_compiled DESC` would produce a table of all concept articles sorted by compilation date.

- **Inline queries**: Short expressions like `= this.sources` can be embedded directly in article text to dynamically display metadata values.

- **JavaScript API**: For complex queries, Dataview exposes a JavaScript API (`dataviewjs`) enabling arbitrary computations over vault metadata.

- **Dynamic rendering**: Query results update in real time as files change, making Dataview views always current without manual maintenance.

## Role in LLM Knowledge Bases

Dataview complements the LLM-maintained wiki by providing human-navigable views over the wiki's metadata structure. While the LLM maintains `_index.md` and `_meta/summaries.md` as flat files, Dataview can generate equivalent views dynamically from frontmatter, serving as a cross-check on the LLM's metadata maintenance. It is particularly useful for [Linting And Health Checks](#concepts-linting-and-health-checks): a Dataview query listing articles where `last_compiled` is older than the most recent raw file ingestion date can quickly identify stale content.

Dataview also supports the wiki's function as a readable, navigable knowledge artifact. While the LLM interacts with files via direct reading and writing, humans interact via Obsidian's rendering layer, where Dataview queries provide dashboard-like views that make the wiki's structure transparent.

## Mentioned In

- [Karpathy Llm Knowledge Bases](#sources-karpathy-llm-knowledge-bases) -- referenced implicitly as part of the Obsidian plugin ecosystem used for viewing data in different ways
- [Dairai Llm Knowledge Bases Architecture](#sources-dairai-llm-knowledge-bases-architecture) -- the DAIR.AI author's research indexing extension uses similar plugin-based views


---

## Elvis Saravia {#entities-elvis-saravia}

***type:** entity | **entity_type:** person | **sources:** Dairai Llm Knowledge Bases Architecture, Antigravity Post Code Ai Workflow | **related:** Dairai, Llm Knowledge Base, Wiki Compilation | **last_compiled:** 2026-04-06 | **summary:** Founder of DAIR.AI Academy who provided the most thorough system architecture analysis of Karpathy's LLM knowledge base, coining the 'four-phase operational cycle' framework.*

## Overview

Elvis Saravia is the founder and primary author at DAIR.AI Academy, an educational platform focused on AI research and applied machine learning. In the context of this knowledge base, Saravia authored the most detailed system architecture analysis of Karpathy's LLM knowledge base methodology, formalizing it as a four-phase operational cycle: Ingestion, Compilation, Query & Enhancement, and Maintenance & Validation.

Saravia's analysis elevated Karpathy's Twitter thread from an informal workflow description to a structured system architecture, making it easier for other practitioners to understand and implement. He also confirmed the pattern's effectiveness from his own experience building agent-based research indexing systems using Obsidian and the qmd CLI tool.

## Key Contributions

- **Four-phase framework**: Formalized Karpathy's workflow into a clear system architecture: Ingestion -> Compilation -> Query & Enhancement -> Maintenance & Validation. This framework is used throughout the wiki to describe the LLM-KB lifecycle.

- **"LLM as compiler" framing**: Introduced the metaphor of the LLM as a "compiler" that transforms raw documents into structured wiki output, distinguishing this approach from the LLM-as-chatbot paradigm.

- **Practitioner validation**: Described his own research indexing system using Obsidian and qmd CLI for semantic indexing of hundreds of research papers, providing independent validation of the approach.

- **Community endorsement**: His public confirmation of the pattern's effectiveness, cited in the Antigravity Codes analysis, helped establish the LLM-KB as a legitimate methodology rather than a niche experiment.

## Role in LLM Knowledge Bases

Saravia bridges the gap between Karpathy's informal description and formal system design. His DAIR.AI Academy article is the primary reference for understanding the LLM-KB as a system architecture rather than a personal hack. The four-phase cycle he documented maps directly to the wiki's own operation: this knowledge base itself follows the Ingestion -> Compilation -> Query -> Maintenance cycle that Saravia formalized.

## Mentioned In

- [Dairai Llm Knowledge Bases Architecture](#sources-dairai-llm-knowledge-bases-architecture) -- authored the four-phase operational cycle analysis
- [Antigravity Post Code Ai Workflow](#sources-antigravity-post-code-ai-workflow) -- cited confirming the pattern's effectiveness and emphasizing data structure as foundational


---

## FAISS {#entities-faiss}

***type:** entity | **entity_type:** tool | **sources:** Hn Vector Database Debate | **related:** Vector Databases, Rag Vs Index Based Retrieval, Pgvector, Chromadb | **last_compiled:** 2026-04-06 | **summary:** Facebook AI Similarity Search -- an open-source library for efficient similarity search and clustering of dense vectors, supporting billions of vectors with disk-based indexing.*

## Overview

FAISS (Facebook AI Similarity Search) is an open-source library developed by Meta AI Research for efficient similarity search and clustering of dense vectors. It is widely used in the machine learning community as a foundational tool for approximate nearest-neighbor (ANN) search at scale, supporting billions of vectors through disk-based indexing strategies. FAISS provides a middle ground between simple brute-force search over small collections and fully managed vector database services.

Unlike dedicated vector database products (Pinecone, Weaviate, Milvus), FAISS is a library rather than a service -- it runs in-process within application code and does not provide built-in API servers, replication, or managed hosting. This makes it extremely flexible and free of operational overhead, but it requires developers to handle persistence, scaling, and serving infrastructure themselves.

## Key Features

- **Multiple index types**: FAISS supports flat (exact) search, IVF (inverted file) for partitioned approximate search, HNSW (hierarchical navigable small world) for graph-based ANN, and PQ (product quantization) for compressed representations. Developers choose the index type based on their accuracy-speed-memory tradeoff requirements.

- **Billion-vector scale**: With disk-based indexing and quantization, FAISS handles datasets far larger than can fit in memory, making it suitable for enterprise-scale similarity search.

- **GPU acceleration**: FAISS includes GPU implementations of key algorithms, enabling significantly faster search and index construction on CUDA-capable hardware.

- **Open source**: Freely available under MIT license, with extensive documentation and active community support.

## Role in LLM Knowledge Bases

FAISS appears in the [Hn Vector Database Debate](#sources-hn-vector-database-debate) as a key alternative to paid vector database services. The HN community consensus was that FAISS, combined with a standard database for metadata, handles most retrieval use cases without requiring a dedicated vector DB. For the LLM knowledge base domain specifically, FAISS would be relevant if a wiki grew beyond the ~400K word threshold where Karpathy's index-based navigation suffices -- providing a stepping stone before committing to a managed vector database.

The broader debate documented in [Vector Databases](#concepts-vector-databases) positions FAISS alongside [Pgvector](#entities-pgvector) as practical alternatives that eliminate the need for specialized infrastructure at personal and team scales.

## Mentioned In

- [Hn Vector Database Debate](#sources-hn-vector-database-debate) -- cited as an open-source middle ground between simple loops and paid vector database services, handling billions of vectors with disk-based indexing


---

## FreshWiki {#entities-freshwiki}

***type:** entity | **entity_type:** dataset | **sources:** Storm Automated Wiki Creation | **related:** Storm, Automated Wiki Creation | **last_compiled:** 2026-04-06 | **summary:** An evaluation dataset of recent Wikipedia articles created after LLM training cutoffs, introduced by the STORM project to prevent data leakage in automated wiki generation benchmarks.*

## Overview

FreshWiki is an evaluation dataset introduced alongside the [Storm](#entities-storm) system for benchmarking automated Wikipedia article generation. It consists of Wikipedia articles that were created after the training data cutoff dates of the LLMs being evaluated, ensuring that the models cannot have memorized the target articles during pre-training. This addresses a critical evaluation challenge: if an LLM has seen the Wikipedia article it is supposed to "generate" during training, the benchmark measures recall rather than genuine generation capability.

## Key Features

- **Temporal filtering**: Articles are selected based on creation dates that post-date LLM training cutoffs, providing a clean evaluation signal free of data leakage.

- **Wikipedia-quality reference**: Because the articles are actual Wikipedia entries, they meet Wikipedia's editorial standards for coverage, neutrality, verifiability, and structure -- providing high-quality reference outputs for comparison.

- **Multi-dimensional evaluation**: FreshWiki supports assessment through heading soft recall and entity recall (outline quality), ROUGE scores and entity recall (article quality), and expert rubrics from experienced Wikipedia editors evaluating interest, coherence, relevance, coverage, and verifiability.

## Role in LLM Knowledge Bases

FreshWiki is significant beyond the STORM project because it highlights a general problem in evaluating LLM-generated knowledge: distinguishing genuine synthesis from memorization. For LLM knowledge base systems like Karpathy's, this distinction matters during linting and quality assessment. An LLM that appears to generate accurate wiki content may simply be recalling training data rather than synthesizing from the provided raw sources. FreshWiki's temporal filtering methodology provides a blueprint for designing evaluations that test genuine compilation capability.

## Mentioned In

- [Storm Automated Wiki Creation](#sources-storm-automated-wiki-creation) -- introduced as STORM's evaluation dataset to prevent data leakage in benchmarking


---

## Graphiti {#entities-graphiti}

***type:** entity | **entity_type:** tool | **sources:** Graphiti Temporal Knowledge Graphs | **related:** Knowledge Graph, Temporal Knowledge, Zep, Rag Vs Index Based Retrieval, Knowledge Graph Vs Wiki | **last_compiled:** 2026-04-06 | **summary:** An open-source framework by Zep for building temporal context graphs where facts have validity windows, designed for AI agents operating in dynamic environments.*

## Overview

Graphiti is an open-source framework developed by [Zep](#entities-zep) for building and querying temporal context graphs designed specifically for AI agents. Unlike traditional knowledge graphs that treat facts as eternally true or false, Graphiti represents facts with temporal validity windows -- tracking when information became true and when it was superseded. This temporal awareness makes it uniquely suited for AI agents that need to reason over changing information in dynamic environments such as product management, competitive intelligence, and organizational knowledge.

Graphiti occupies the architectural middle ground between Karpathy's simple markdown wiki approach and heavyweight enterprise knowledge graph systems like KARMA. It provides more formal structure than markdown files (entities, relationships, and facts as first-class objects) while remaining more accessible than a full multi-agent ontology enrichment pipeline.

## Key Features

- **Temporal validity windows**: Every fact (relationship edge) has a `valid_from` and `valid_until` timestamp. Old facts are invalidated rather than deleted, preserving complete historical context. This enables queries like "what was true about X before date Y?" alongside "what is currently true about X?"

- **Four core components**: Entities (nodes with evolving summaries), Facts/Relationships (edges with time windows), Episodes (raw ingested data serving as ground truth), and Custom Types (developer-defined entity and edge types via Pydantic models).

- **Hybrid retrieval**: Combines three search methods -- semantic similarity, BM25 keyword matching, and graph traversal -- to provide more robust retrieval than any single approach. This hybrid strategy outperforms pure vector search or pure keyword search for knowledge graph queries.

- **Incremental updates**: New data integrates without batch recomputation of the entire graph. This incremental approach mirrors Karpathy's incremental wiki compilation but at the graph level.

- **Full provenance**: Every derived fact traces back to its source Episode, paralleling how Karpathy's wiki traces all claims back to `raw/` files. This enables auditability and error correction.

- **Neo4j backend**: Uses Neo4j as the graph database, providing mature graph query capabilities and visualization tools.

## Role in LLM Knowledge Bases

Graphiti addresses a key limitation of Karpathy's markdown wiki: temporal reasoning. Markdown files handle temporality only through file modification dates and manual notes, which is adequate for static research knowledge (papers do not change) but insufficient for operational knowledge that evolves over time (org charts, product roadmaps, competitive landscapes). Graphiti's explicit temporal model fills this gap.

The Episodes concept in Graphiti directly mirrors the `raw/` directory in Karpathy's system -- both serve as the immutable source of truth from which all derived knowledge is compiled. The key difference is that Graphiti stores derived knowledge as formal graph structures rather than markdown files, enabling structured queries and temporal reasoning at the cost of reduced human readability.

## Mentioned In

- [Graphiti Temporal Knowledge Graphs](#sources-graphiti-temporal-knowledge-graphs) -- full description of the framework, architecture, and comparison with markdown wiki and KARMA approaches


---

## KARMA {#entities-karma}

***type:** entity | **entity_type:** paper | **sources:** Karma Multi Agent Knowledge Graph | **related:** Knowledge Graph, Multi Agent Systems, Llm Knowledge Base, Andrej Karpathy | **last_compiled:** 2026-04-06 | **summary:** A NeurIPS 2025 Spotlight paper presenting a nine-agent LLM framework for automated knowledge graph enrichment from unstructured scientific text.*

## Overview

KARMA (Knowledge graph enrichment through Automated Retrieval and Multi-Agent systems) is a research framework published as a Spotlight paper at NeurIPS 2025. It automates the enrichment of knowledge graphs from unstructured text using nine collaborative LLM agents, each specialized for a distinct phase of the extraction pipeline. The system was evaluated on 1,200 PubMed articles across three scientific domains, discovering up to 38,230 new entities with 83.1% LLM-verified correctness and achieving an 18.6% reduction in conflict edges through multi-layer assessments.

KARMA represents the research-grade counterpart to Karpathy's markdown-based wiki approach. While both systems share the core architecture of converting raw documents into structured knowledge through LLM pipelines, KARMA produces formal graph triplets (entity, relation, entity) with schema constraints, whereas Karpathy produces human-readable markdown files with wikilinks.

## Key Features

- **Nine specialized agents**: Document parser, entity discoverer, relation extractor, schema aligner, conflict detector, conflict resolver, knowledge integrator, verifier, and schema validator. Each agent focuses on a single task, passing results to downstream agents and challenging each other's outputs.

- **Formal graph representation**: Knowledge is stored as triplets with domain-specific schema constraints, enabling structured querying and formal reasoning that markdown-based approaches cannot support.

- **Conflict resolution**: A multi-layer assessment mechanism where distinct agents independently evaluate the same facts, achieving 18.6% reduction in conflicting edges. This is a significant advantage over single-LLM approaches where contradictions may go undetected.

- **Schema adherence**: Domain-specific schemas constrain what types of entities and relationships are valid, preventing the LLM from generating structurally invalid knowledge.

- **Scalability**: Tested on thousands of scientific papers, well beyond the ~100-article sweet spot of Karpathy's personal wiki approach.

## Role in LLM Knowledge Bases

KARMA establishes the upper bound of automated knowledge extraction quality for formal knowledge graphs. It demonstrates that multi-agent LLM pipelines can achieve research-grade accuracy in entity and relation extraction, validating the core thesis of [Multi Agent Systems](#concepts-multi-agent-systems) for knowledge management. However, its formal graph output trades the human readability and auditability of Karpathy's markdown approach for structural precision and scalability. The comparison between these approaches illustrates a fundamental design axis: formal graphs for machine-queryable precision vs. markdown for human-auditable transparency.

## Mentioned In

- [Karma Multi Agent Knowledge Graph](#sources-karma-multi-agent-knowledge-graph) -- full paper description, methodology, results, and contrast with Karpathy's markdown approach


---

## Marp {#entities-marp}

***type:** entity | **entity_type:** tool | **sources:** Karpathy Llm Knowledge Bases, Antigravity Post Code Ai Workflow | **related:** Obsidian As Ide, Llm Knowledge Base, Obsidian, Matplotlib | **last_compiled:** 2026-04-06 | **summary:** A markdown-based presentation framework used within Obsidian to render LLM-generated slide decks as one of the multi-format output options in the knowledge base workflow.*

## Overview

Marp (Markdown Presentation Ecosystem) is an open-source framework that converts markdown files into presentation slides. It supports a simple syntax where slide separators, themes, and layouts are defined within standard markdown, making it trivially easy for an LLM to generate presentation content without requiring proprietary formats like PowerPoint or Google Slides.

In Karpathy's LLM knowledge base workflow, Marp serves as one of the multi-format output channels. When a user asks the LLM a question, the response can be rendered not just as a markdown report but as a Marp-formatted slide deck viewable directly within [Obsidian](#entities-obsidian) via a plugin.

## Key Features

- **Markdown-native**: Slides are written as plain markdown with `---` separators between slides, headers for titles, and bullet points for content. This means any LLM that can write markdown can write Marp presentations.

- **Obsidian integration**: The Marp plugin for Obsidian renders slide previews inline, keeping all artifacts -- wiki articles, reports, and presentations -- within the same viewing environment.

- **Export formats**: Marp can export to HTML, PDF, and PPTX, making LLM-generated presentations usable outside the Obsidian ecosystem.

- **Theming and directives**: CSS themes and per-slide directives (backgrounds, layouts, sizing) can be embedded in the markdown frontmatter.

## Role in LLM Knowledge Bases

Marp exemplifies the multi-format output principle of the LLM-KB workflow. Rather than restricting LLM output to text responses in a terminal, the system leverages markdown-based tools to produce diverse artifacts: reports (plain markdown), visualizations ([Matplotlib](#entities-matplotlib)), and presentations (Marp). These outputs can then be filed back into the wiki through the filing loop, enriching the knowledge base for future queries.

The choice of Marp over proprietary presentation tools also reinforces the [Markdown As Universal Interface](#concepts-markdown-as-universal-interface) principle: all content remains in human-readable, version-controllable plain text that any LLM can generate and any editor can display.

## Mentioned In

- [Karpathy Llm Knowledge Bases](#sources-karpathy-llm-knowledge-bases) -- listed as an Obsidian plugin used for rendering LLM-generated slide decks
- [Antigravity Post Code Ai Workflow](#sources-antigravity-post-code-ai-workflow) -- included in the multi-format output step (step 5) of the 6-step workflow


---

## Matplotlib {#entities-matplotlib}

***type:** entity | **entity_type:** tool | **sources:** Karpathy Llm Knowledge Bases, Antigravity Post Code Ai Workflow | **related:** Llm Knowledge Base, Obsidian As Ide, Marp, Obsidian | **last_compiled:** 2026-04-06 | **summary:** A Python plotting library used in the LLM-KB workflow to generate data visualizations that are saved as images and viewed within Obsidian alongside wiki articles.*

## Overview

Matplotlib is the foundational plotting library for the Python scientific computing ecosystem. It provides comprehensive tools for creating static, animated, and interactive visualizations including line plots, bar charts, scatter plots, histograms, heatmaps, and more. Matplotlib is one of the most widely used libraries in data science and machine learning.

In Karpathy's LLM knowledge base workflow, Matplotlib serves as one of the multi-format output channels alongside markdown reports and [Marp](#entities-marp) slide decks. When the LLM answers a query that benefits from visual representation -- comparative charts, timelines, distribution plots, relationship diagrams -- it generates Matplotlib code, executes it to produce image files, and saves those images within the wiki structure where they can be viewed in [Obsidian](#entities-obsidian).

## Key Features

- **Comprehensive plotting**: Supports virtually any 2D visualization type, from simple line plots to complex multi-panel figures with custom layouts.

- **Programmatic generation**: Because Matplotlib is a Python library, LLMs can generate the code to produce visualizations directly. The LLM writes Python code, the code is executed, and the resulting image is saved to the wiki.

- **Image output**: Renders to PNG, SVG, PDF, and other formats. PNG images embed naturally in markdown files and display inline in Obsidian.

- **Customization**: Styles, colors, annotations, and layouts are all controllable through code, allowing the LLM to produce publication-quality figures tailored to the query.

## Role in LLM Knowledge Bases

Matplotlib exemplifies a broader principle of the LLM-KB workflow: the knowledge base is not limited to text. By generating visualizations and filing them back into the wiki, the LLM produces a richer, more navigable knowledge artifact than text alone could provide. A chart comparing RAG accuracy vs. fine-tuning accuracy (as referenced in [Pebblous Cheap Ontology](#sources-pebblous-cheap-ontology)) communicates quantitative relationships faster than a paragraph of prose.

This multi-modal output capability is one of the advantages that distinguishes LLM-maintained wikis from traditional note-taking: the LLM can generate both the analysis and the visualization in a single pass, creating self-contained artifacts that combine prose, data, and imagery.

## Mentioned In

- [Karpathy Llm Knowledge Bases](#sources-karpathy-llm-knowledge-bases) -- listed as one of the output formats (markdown, Marp slides, matplotlib images) viewable in Obsidian
- [Antigravity Post Code Ai Workflow](#sources-antigravity-post-code-ai-workflow) -- included in the multi-format output step of the 6-step workflow


---

## Memex {#entities-memex}

***type:** entity | **entity_type:** concept | **sources:** Pebblous Cheap Ontology | **related:** Vannevar Bush, Personal Knowledge Management, Llm Knowledge Base, Cheap Ontology | **last_compiled:** 2026-04-06 | **summary:** Vannevar Bush's 1945 vision of a personal knowledge device with associative cross-referencing -- the conceptual ancestor of hypertext, wikis, and LLM-maintained knowledge bases.*

## Overview

The Memex (a portmanteau of "memory" and "index") is a hypothetical device described by [Vannevar Bush](#entities-vannevar-bush) in his 1945 essay "As We May Think." Bush envisioned a desk-sized machine that would store an individual's entire library of books, records, and communications on microfilm, with a mechanical system for creating "associative trails" -- user-defined cross-references linking related items across the collection. The user could then follow these trails to navigate their personal knowledge, much as one follows hyperlinks on the modern web.

The Memex was never built, but its influence on computing and knowledge management has been profound. It directly inspired Douglas Engelbart's work on augmenting human intellect, Ted Nelson's concept of hypertext, and ultimately the World Wide Web. In the context of this knowledge base, the Memex represents the 80-year-old dream that LLM-maintained wikis are now realizing.

## Key Ideas

- **Associative trails**: Bush observed that the human mind operates by association rather than indexing. The Memex would allow users to create named trails linking items in any order, mimicking how thought connects disparate ideas. This is functionally equivalent to `Wikilinks` in a modern markdown wiki.

- **Personal knowledge store**: The Memex was conceived as an individual tool, not a shared database. Each person would maintain their own Memex, populated with their own materials and annotated with their own trails. This maps directly to the personal nature of Karpathy's LLM knowledge base.

- **Augmented retrieval**: Bush recognized that the bottleneck in knowledge work was retrieval, not storage. The Memex addressed this through its trail system, just as the LLM-KB addresses it through index-based navigation and the filing loop.

## Role in LLM Knowledge Bases

The Memex provides historical context for understanding why Karpathy's approach feels significant. The Pebblous analysis traces a direct lineage: Memex (1945) -> hypertext (1960s) -> World Wide Web (1989) -> Semantic Web (2001) -> enterprise knowledge graphs (2007) -> LLM wikis (2024+). At each stage, the vision of personal, cross-referenced, navigable knowledge becomes more accessible and more automated.

The critical difference between the Memex and an LLM knowledge base is who creates the structure. Bush assumed the human would manually create every associative trail. In Karpathy's system, the LLM automatically generates cross-references, index files, and concept articles -- reducing the human role from author to curator. This shift represents the fulfillment of Bush's aspiration through a mechanism he could not have anticipated.

## Mentioned In

- [Pebblous Cheap Ontology](#sources-pebblous-cheap-ontology) -- the Memex is situated within the 50-year ontology history leading to LLM-maintained knowledge bases


---

## Obsidian {#entities-obsidian}

***type:** entity | **entity_type:** tool | **sources:** Karpathy Llm Knowledge Bases, Dairai Llm Knowledge Bases Architecture, Antigravity Post Code Ai Workflow, Gallagher Second Brain Knowledge Graphs | **related:** Obsidian As Ide, Vault Separation, Markdown As Universal Interface, Andrej Karpathy, Steph Ango, Dataview, Marp | **last_compiled:** 2026-04-06 | **summary:** A markdown-based knowledge management application used as the read-only frontend IDE for LLM-maintained wikis in Karpathy's workflow.*

## Overview

Obsidian is a desktop and mobile application for managing knowledge bases built on local markdown files. It supports `Wikilinks` for cross-referencing, a graph view that visualizes link structures, and a rich plugin ecosystem. In the LLM knowledge base workflow, Obsidian serves as the human-facing IDE -- a viewer and navigator for the raw data, compiled wiki, and generated artifacts that the LLM produces. Crucially, the human uses Obsidian primarily to read, while the LLM performs all writing and maintenance.

Obsidian was founded by Steph Ango and Shida Li. Its core philosophy of local-first, plain-text storage aligns perfectly with the LLM-KB approach: files remain human-readable, version-controllable, and independent of any proprietary format. This portability is a major reason Karpathy chose it as the frontend for his workflow.

## Key Features (Relevant to LLM-KB)

- **Wikilinks and backlinks**: Native `Wikilink` support creates an implicit graph structure that mirrors how the LLM cross-links concept articles during compilation. The backlinks panel shows all articles referencing the current file.

- **Graph view**: Visualizes the entire link graph of the wiki, making it possible to see clusters of related concepts and identify orphan articles at a glance.

- **Web Clipper**: A browser extension that converts web articles into markdown files, serving as the primary ingestion tool for adding new raw sources to the `raw/` directory.

- **Local image storage**: A hotkey workflow downloads referenced images locally, enabling the LLM to reference visual content during compilation.

- **Plugin ecosystem**: Plugins like [Marp](#entities-marp) (slide deck rendering) and [Dataview](#entities-dataview) (structured queries over frontmatter metadata) extend Obsidian's capabilities for viewing LLM-generated artifacts.

- **Vault system**: Obsidian organizes files into "vaults" (directories). [Steph Ango](#entities-steph-ango) recommended maintaining separate vaults for human-curated and agent-generated content to prevent [Hallucination Contamination](#concepts-hallucination-contamination).

## Role in LLM Knowledge Bases

Obsidian is the default viewing layer in Karpathy's architecture and in most derivative implementations. It provides the bridge between the LLM's markdown output and human comprehension. The wiki directory structure (`wiki/sources/`, `wiki/concepts/`, `wiki/_meta/`) maps directly to Obsidian's file-and-folder navigation. The graph view and backlinks surface the link structure the LLM builds during [Wiki Compilation](#concepts-wiki-compilation).

Gallagher initially used Obsidian for his personal knowledge management but found it insufficient for structural reasoning, leading him to develop the Knowledge Graph Kit with [Sqlite](#entities-sqlite) and [Chromadb](#entities-chromadb) instead. This contrast illustrates Obsidian's sweet spot: excellent for reading and navigating text-based knowledge, less suited for formal graph operations or task management.

## Mentioned In

- [Karpathy Llm Knowledge Bases](#sources-karpathy-llm-knowledge-bases) -- described as the IDE frontend for viewing raw data, wiki, and visualizations
- [Dairai Llm Knowledge Bases Architecture](#sources-dairai-llm-knowledge-bases-architecture) -- listed as a core implementation requirement
- [Antigravity Post Code Ai Workflow](#sources-antigravity-post-code-ai-workflow) -- included in the minimum viable setup; Steph Ango's vault separation recommendation
- [Gallagher Second Brain Knowledge Graphs](#sources-gallagher-second-brain-knowledge-graphs) -- Gallagher's initial tool before switching to graph-based approach


---

## pgvector {#entities-pgvector}

***type:** entity | **entity_type:** tool | **sources:** Hn Vector Database Debate | **related:** Vector Databases, Rag Vs Index Based Retrieval, Faiss, Chromadb | **last_compiled:** 2026-04-06 | **summary:** A PostgreSQL extension for vector similarity search, widely regarded as sufficient for most team-scale retrieval use cases without requiring dedicated vector database infrastructure.*

## Overview

pgvector is an open-source extension for PostgreSQL that adds support for storing and searching vector embeddings directly within an existing Postgres database. It enables approximate nearest-neighbor (ANN) search alongside traditional relational queries, meaning teams can add semantic search capabilities to their applications without introducing a separate vector database into their infrastructure stack.

In the Hacker News debate documented in [Hn Vector Database Debate](#sources-hn-vector-database-debate), pgvector emerged as the most frequently recommended alternative to specialized vector databases. Multiple practitioners reported that it handled their retrieval workloads adequately, eliminating the need for additional infrastructure.

## Key Features

- **PostgreSQL native**: Runs as an extension within existing PostgreSQL deployments, leveraging Postgres's mature ecosystem for backups, replication, monitoring, and access control.

- **IVF indexing**: The initial implementation uses Inverted File (IVF) indexes for approximate search. With default settings (nprobes=3), recall is approximately 50%, which drew criticism in the HN discussion. Tuning nprobes improves recall at the cost of query latency.

- **HNSW support**: Newer versions add Hierarchical Navigable Small World (HNSW) indexes, providing significantly better accuracy-speed tradeoffs than IVF and addressing the primary criticism of early pgvector.

- **Hybrid queries**: Because vectors live alongside relational data, queries can combine vector similarity with standard SQL filters (dates, categories, permissions) without cross-system joins.

- **No new infrastructure**: The key practical advantage: teams already running PostgreSQL can add vector search without provisioning, managing, or paying for a separate database service.

## Role in LLM Knowledge Bases

pgvector represents the pragmatic middle ground in the [Vector Databases](#concepts-vector-databases) debate. For organizations that have outgrown Karpathy's index-based navigation (wiki larger than ~400K words) but do not need billion-vector-scale search, pgvector provides semantic retrieval within existing infrastructure. It avoids the operational complexity of dedicated vector databases while offering better recall than simple keyword search.

In the context of [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval), pgvector is the most likely next step for an LLM-KB that has grown beyond context window limits: add embeddings to the existing data store rather than introducing a new system.

## Mentioned In

- [Hn Vector Database Debate](#sources-hn-vector-database-debate) -- recommended by multiple practitioners as sufficient for most use cases; criticized for low default recall with IVF indexing


---

## SQLite {#entities-sqlite}

***type:** entity | **entity_type:** tool | **sources:** Gallagher Second Brain Knowledge Graphs | **related:** Chromadb, Knowledge Graph, Second Brain | **last_compiled:** 2026-04-06 | **summary:** A lightweight, serverless relational database used as the structural storage layer in Gallagher's Knowledge Graph Kit for personal knowledge management.*

## Overview

SQLite is a self-contained, serverless, zero-configuration relational database engine that stores an entire database as a single file on disk. It is the most widely deployed database engine in the world, embedded in virtually every smartphone, web browser, and operating system. SQLite requires no separate server process -- applications read and write the database file directly, making it ideal for local, single-user applications.

In the LLM knowledge base domain, SQLite appears as the structural storage layer in Sam Gallagher's Knowledge Graph Kit. While Karpathy's approach uses the file system itself as the database (one `.md` file per article, with wikilinks as implicit edges), Gallagher chose SQLite to store an explicit graph of nodes and edges with typed relationships.

## Key Features

- **Zero configuration**: No server to install, configure, or manage. The entire database is a single file that can be copied, backed up, or version-controlled trivially.

- **Relational model**: Full SQL query support enables structured queries over knowledge graph nodes and edges -- something impossible with flat markdown files.

- **Embeddable**: SQLite runs in-process, making it suitable for MCP servers, CLI tools, and agent pipelines that need local structured storage without network dependencies.

- **Lightweight**: The entire library is under 1MB, with no external dependencies, making it the natural choice for personal-scale tools.

## Role in LLM Knowledge Bases

SQLite represents the relational-database approach to knowledge storage, contrasting with Karpathy's file-system-based approach. In Gallagher's Knowledge Graph Kit, SQLite stores four node types (Task, Note, Person, Project) with typed edges (part_of, mentions, related_to), enabling structural queries that markdown wikilinks cannot support. For example, "find all tasks related to Project X that mention Person Y" is a straightforward SQL join in SQLite but would require LLM-mediated natural language navigation in a markdown wiki.

The tradeoff is clear: SQLite provides structural querying power at the cost of human readability. You cannot open a SQLite file in a text editor and read it the way you can with markdown files in [Obsidian](#entities-obsidian). For personal task and project management (Gallagher's use case), the structural power justifies the readability cost. For research knowledge synthesis (Karpathy's use case), the readability and LLM-friendliness of markdown wins.

## Mentioned In

- [Gallagher Second Brain Knowledge Graphs](#sources-gallagher-second-brain-knowledge-graphs) -- used as the local storage backend for the Knowledge Graph Kit's node/edge graph structure


---

## Steph Ango {#entities-steph-ango}

***type:** entity | **entity_type:** person | **sources:** Antigravity Post Code Ai Workflow | **related:** Obsidian, Vault Separation, Hallucination Contamination | **last_compiled:** 2026-04-06 | **summary:** CEO of Obsidian who recommended vault separation as a strategy to prevent LLM hallucination contamination in personal knowledge bases.*

## Overview

Steph Ango is the CEO of Obsidian, the markdown-based knowledge management application that serves as the viewing frontend in Karpathy's LLM knowledge base workflow. Ango's contribution to the LLM-KB discourse is his recommendation of vault separation: maintaining a clean human-curated Obsidian vault separate from an agent-generated vault for LLM-compiled content.

This recommendation directly addresses the [Hallucination Contamination](#concepts-hallucination-contamination) risk. When LLMs compile wikis, they occasionally generate plausible but incorrect connections or facts. If agent-generated content is stored in the same vault as a user's personal, trusted notes, these hallucinations can contaminate the user's primary knowledge base. Ango's two-vault pattern provides a clean architectural boundary between trusted human knowledge and potentially imperfect LLM output.

## Key Contributions

- **Vault separation pattern**: The recommendation to maintain a "clean vault" (human-curated, trusted) separate from an "agent vault" (LLM-maintained, potentially hallucinated) has become a foundational best practice in the LLM-KB community. It is cited across multiple sources as the primary mitigation strategy for hallucination contamination.

- **Product perspective on LLM-KB**: As the CEO of the tool most commonly used as the LLM-KB frontend, Ango's endorsement of the workflow pattern while cautioning about contamination risk carries significant weight. It validates the approach while identifying the most important guardrail.

## Role in LLM Knowledge Bases

Ango represents the tool-maker perspective in the LLM-KB ecosystem. While Karpathy provides the methodology and researchers like the STORM and KARMA teams provide the academic foundations, Ango speaks from the position of someone building the tools that practitioners use daily. His vault separation recommendation has become the standard advice for anyone implementing Karpathy's workflow, directly shaping the [Vault Separation](#concepts-vault-separation) concept article.

## Mentioned In

- [Antigravity Post Code Ai Workflow](#sources-antigravity-post-code-ai-workflow) -- quoted recommending vault separation to prevent contamination of human-curated personal wikis


---

## STORM {#entities-storm}

***type:** entity | **entity_type:** paper | **sources:** Storm Automated Wiki Creation | **related:** Automated Wiki Creation, Multi Agent Systems, Wiki Compilation, Freshwiki, Storm Vs Karpathy Workflow | **last_compiled:** 2026-04-06 | **summary:** A research system for automated Wikipedia-style article creation using multi-perspective question-asking and retrieval-based outline synthesis.*

## Overview

STORM (Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking) is a research system that automates the creation of Wikipedia-style articles by focusing on the pre-writing stage -- research and outline generation -- rather than assuming these already exist. Developed as an academic research project, STORM represents the most rigorous automated approach to wiki article creation, standing in contrast to Karpathy's interactive, accumulating knowledge base methodology.

The core insight behind STORM is that high-quality articles require diverse research perspectives, not just information retrieval. By simulating conversations between LLM agents playing distinct expert roles, STORM produces more comprehensive and balanced content than single-perspective generation approaches.

## Key Features

- **Perspective discovery**: STORM analyzes related Wikipedia articles' tables of contents to identify N distinct viewpoints relevant to the target topic. This ensures coverage of multiple angles rather than defaulting to a single narrative.

- **Multi-turn simulated conversations**: LLMs are personified with specific perspectives and conduct simulated expert discussions. Each perspective-agent asks different questions, breaks complex queries into searchable sub-queries, filters results against Wikipedia reliability guidelines, and synthesizes evidence-based responses.

- **Outline-first synthesis**: Rather than generating text directly, STORM first produces a structured outline from the simulated conversations, then uses the outline to guide full article generation. This mirrors the human writing process of research-before-drafting.

- **FreshWiki evaluation dataset**: STORM introduced [Freshwiki](#entities-freshwiki), a dataset of Wikipedia articles created after LLM training cutoffs, ensuring evaluation is not contaminated by memorization. Assessment uses heading/entity recall for outlines, ROUGE scores for articles, and expert rubrics from experienced Wikipedia editors.

## Role in LLM Knowledge Bases

STORM provides the key contrasting model to Karpathy's approach (see Storm Vs Karpathy Workflow). Where Karpathy builds a persistent, accumulating knowledge base that grows through the filing loop, STORM performs single-shot article generation from web search without maintaining a persistent knowledge store. STORM is better for producing standalone reference articles on well-defined topics; Karpathy's approach is better for building compounding research knowledge over time.

Both systems share the fundamental insight that LLMs can serve as research synthesizers rather than just text generators. STORM achieves this through multi-agent perspective simulation; Karpathy achieves it through incremental compilation and iterative Q&A.

## Mentioned In

- [Storm Automated Wiki Creation](#sources-storm-automated-wiki-creation) -- full description of the system, methodology, evaluation, and comparison with Karpathy's approach


---

## Vannevar Bush {#entities-vannevar-bush}

***type:** entity | **entity_type:** person | **sources:** Pebblous Cheap Ontology | **related:** Memex, Personal Knowledge Management, Cheap Ontology | **last_compiled:** 2026-04-06 | **summary:** American engineer and science administrator who envisioned the Memex in 1945 -- a proto-hypertext personal knowledge device that prefigured modern LLM knowledge bases by 80 years.*

## Overview

Vannevar Bush (1890-1974) was an American engineer, inventor, and science administrator who served as the head of the U.S. Office of Scientific Research and Development during World War II. In the context of knowledge management history, he is best known for his landmark 1945 essay "As We May Think" published in The Atlantic, in which he described the [Memex](#entities-memex) -- a hypothetical device that would allow individuals to store, organize, and retrieve all of their books, records, and communications through associative trails rather than hierarchical filing systems.

Bush's vision is the intellectual ancestor of hypertext, the World Wide Web, and modern personal knowledge management tools. The Pebblous analysis of Karpathy's LLM knowledge base methodology traces a direct lineage from Bush's Memex through the Semantic Web era to today's LLM-maintained wikis, positioning the current moment as the realization of an 80-year-old dream of accessible, augmented human knowledge.

## Key Contributions

- **"As We May Think" (1945)**: Published in The Atlantic, this essay described a future where individuals would have personal devices to store and cross-reference all their knowledge. The essay introduced the concept of "associative trails" -- user-defined paths through knowledge that would be stored alongside the knowledge itself.

- **The Memex concept**: Bush's proposed machine would use microfilm to store an individual's entire library, with a mechanical system for creating and following cross-references between documents. This is conceptually identical to a wiki with wikilinks -- or to Karpathy's markdown knowledge base with its `Wikilinks` connecting concepts.

- **Science policy leadership**: Bush's role in establishing the National Science Foundation and shaping postwar American science policy demonstrated the same impulse driving LLM knowledge bases: the conviction that better organization of knowledge leads to better outcomes.

## Role in LLM Knowledge Bases

Bush represents the historical starting point of the intellectual trajectory that Karpathy's work continues. The Pebblous "Cheap Ontology" analysis explicitly places LLM wikis as the latest phase in a lineage that includes Bush's Memex, the Semantic Web, and enterprise knowledge graphs. What Bush imagined as a mechanical microfilm device, Karpathy implements as markdown files compiled by an LLM -- the same conceptual architecture (store everything, cross-reference associatively, navigate through trails) realized with modern technology.

The key difference: Bush envisioned the human creating all the trails and cross-references manually, while in Karpathy's system the LLM handles this automatically. This represents the shift from [Personal Knowledge Management](#concepts-personal-knowledge-management) as a manual practice to an LLM-maintained automated system.

## Mentioned In

- [Pebblous Cheap Ontology](#sources-pebblous-cheap-ontology) -- positioned within the historical context of ontology evolution from Bush's 1945 vision through modern LLM wikis


---

## Zep {#entities-zep}

***type:** entity | **entity_type:** org | **sources:** Graphiti Temporal Knowledge Graphs | **related:** Graphiti, Knowledge Graph, Temporal Knowledge | **last_compiled:** 2026-04-06 | **summary:** The organization behind Graphiti, offering both an open-source temporal context graph engine and enterprise-grade managed infrastructure for AI agent memory.*

## Overview

Zep (also known as Zep AI) is the company that developed and maintains [Graphiti](#entities-graphiti), the open-source temporal context graph framework for AI agents. Zep operates on an open-core business model: Graphiti is released as the open-source engine for building temporal knowledge graphs, while Zep provides enterprise-grade managed infrastructure on top of it. This split allows developers to experiment freely with Graphiti while offering a production-ready, hosted option for teams that need turnkey deployment.

The company focuses on the AI agent memory problem -- giving AI agents the ability to accumulate, organize, and recall information over long time horizons. This positions Zep at the intersection of knowledge graphs and agentic AI, two rapidly growing areas in the LLM ecosystem.

## Key Contributions

- **Graphiti open-source release**: Making temporal context graphs freely available for experimentation and self-hosting lowers the barrier to entry for developers building AI agents with structured memory.

- **Open-core model**: The Graphiti/Zep split mirrors patterns seen across developer tools (Redis/Redis Enterprise, Elasticsearch/Elastic Cloud) and establishes a clear path from experimentation to production.

- **Agent memory focus**: While most knowledge graph tools target general-purpose knowledge representation, Zep specifically focuses on the needs of AI agents -- temporal awareness, incremental updates, hybrid retrieval, and provenance tracking.

## Role in LLM Knowledge Bases

Zep represents the commercial side of the temporal knowledge graph approach. For organizations looking to implement structured knowledge management beyond what a personal markdown wiki can support, Zep's managed Graphiti service offers production-grade infrastructure without the operational burden of running Neo4j and maintaining the graph pipeline. This positions it as a potential solution for the [Knowledge Base Product Gap](#concepts-knowledge-base-product-gap) at the enterprise end of the spectrum.

## Mentioned In

- [Graphiti Temporal Knowledge Graphs](#sources-graphiti-temporal-knowledge-graphs) -- described as the enterprise managed service counterpart to the open-source Graphiti engine


---

## Dashboard {#dashboard}

***type:** dashboard | **last_updated:** 2026-04-05*

# LLM Knowledge Base Dashboard

---

## Quick Stats

| Metric | Count |
|--------|-------|
| Sources | 11 |
| Concepts | 20 |
| Entities | 0 |
| Comparisons | 0 |
| Total Articles | 31 |
| Raw Files Compiled | 11 / 11 |

> Tip: Install the Dataview plugin for live stats. Then replace the table above with:

```dataview
TABLE length(rows) AS "Count"
FROM "wiki"
WHERE type
GROUP BY type
```

---

## Recently Compiled

```dataview
TABLE summary, last_compiled
FROM "wiki/sources" OR "wiki/concepts"
SORT last_compiled DESC
LIMIT 10
```

---

## Recently Modified

```dataview
TABLE file.mtime AS "Modified", type, summary
FROM "wiki"
SORT file.mtime DESC
LIMIT 10
```

---

## Top Connected Concepts (Hub Nodes)

The most connected articles in the wiki, based on incoming + outgoing wikilinks:

| Article | Incoming | Outgoing | Total |
|---------|----------|----------|-------|
| [Llm Knowledge Base](#concepts-llm-knowledge-base) | 24 | 5 | 29 |
| [Wiki Compilation](#concepts-wiki-compilation) | 8 | 2 | 10 |
| [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval) | 10 | 2 | 12 |
| [Knowledge Graph](#concepts-knowledge-graph) | 6 | 4 | 10 |
| [Hallucination Contamination](#concepts-hallucination-contamination) | 5 | 4 | 9 |
| [Linting And Health Checks](#concepts-linting-and-health-checks) | 5 | 2 | 7 |
| [Personal Knowledge Management](#concepts-personal-knowledge-management) | 5 | 4 | 9 |
| [Multi Agent Systems](#concepts-multi-agent-systems) | 4 | 3 | 7 |
| [Data Quality Bottleneck](#concepts-data-quality-bottleneck) | 3 | 4 | 7 |
| [Obsidian As Ide](#concepts-obsidian-as-ide) | 5 | 2 | 7 |

---

## Orphan Watch

Articles with no incoming links from other wiki pages:

```dataview
LIST
FROM "wiki/sources" OR "wiki/concepts" OR "wiki/entities" OR "wiki/comparisons"
WHERE length(file.inlinks) = 0
```

Currently known orphans (static):
- [Karpathy Llm Knowledge Bases](#sources-karpathy-llm-knowledge-bases) (root source, referenced only from `_index.md`)

---

## Quick Actions

- **New article**: Create from template with `Cmd+Shift+T`
- **Search wiki**: `Cmd+Shift+F` for full-text search
- **Graph view**: `Cmd+Shift+G` to visualize connections
- **Quick switcher**: `Cmd+O` to jump to any article

| Action | Link |
|--------|------|
| Browse all articles | _Index |
| View summaries | Summaries |
| View link graph | Links |
| View compilation manifest | Manifest |
| Pre-built queries | [Queries](#queries) |
| Graph analysis | [Graph](#graph) |
| Tag index | [Tags](#tags) |
| Compilation log | [Log](#log) |

---

## Tag Cloud

```dataview
LIST WITHOUT ID
FROM "wiki"
FLATTEN file.tags AS tag
GROUP BY tag
```

> Note: Tags will appear here once articles include `tags:` in their frontmatter. Use tags like `#architecture`, `#risk`, `#retrieval`, `#workflow`, `#multi-agent`, `#ontology`, `#pkm`.

---

## Article Type Breakdown

```dataview
TABLE WITHOUT ID
  type AS "Type",
  length(rows) AS "Count",
  map(rows, (r) => link(r.file.path, r.file.name)) AS "Articles"
FROM "wiki"
WHERE type AND type != "meta" AND type != "index" AND type != "log" AND type != "dashboard"
GROUP BY type
SORT length(rows) DESC
```

---

## Stale Articles

Articles not updated in the last 30 days:

```dataview
TABLE last_compiled, summary
FROM "wiki/sources" OR "wiki/concepts"
WHERE last_compiled AND date(last_compiled) < date(now) - dur(30 days)
SORT last_compiled ASC
LIMIT 15
```

---

*Last manual update: 2026-04-05. Most sections use Dataview for live data.*


---

## Graph Analysis {#graph}

***type:** reference | **last_updated:** 2026-04-05*

# Graph Analysis

Static analysis of the wiki's internal link graph, computed from Links.

---

## Overview

| Metric | Value |
|--------|-------|
| Total nodes (articles) | 31 |
| Source nodes | 11 |
| Concept nodes | 20 |
| Entity nodes | 0 |
| Comparison nodes | 0 |
| Total directed edges | ~130 |
| Average connections per node | ~8.4 |

---

## Hub Nodes (Most Connected)

Articles with the highest combined incoming + outgoing link count. These are the "load-bearing" pages of the wiki.

| Rank | Article | Incoming | Outgoing | Total | Role |
|------|---------|----------|----------|-------|------|
| 1 | [Llm Knowledge Base](#concepts-llm-knowledge-base) | 24 | 5 | 29 | Central hub -- every source and concept links here |
| 2 | [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval) | 10 | 2 | 12 | Key infrastructure concept |
| 3 | [Wiki Compilation](#concepts-wiki-compilation) | 8 | 2 | 10 | Core pipeline concept |
| 4 | [Knowledge Graph](#concepts-knowledge-graph) | 6 | 4 | 10 | Bridge between formal KG and markdown approaches |
| 5 | [Personal Knowledge Management](#concepts-personal-knowledge-management) | 5 | 4 | 9 | Human workflow hub |
| 6 | [Hallucination Contamination](#concepts-hallucination-contamination) | 5 | 4 | 9 | Central risk concept |
| 7 | [Linting And Health Checks](#concepts-linting-and-health-checks) | 5 | 2 | 7 | Quality assurance hub |
| 8 | [Obsidian As Ide](#concepts-obsidian-as-ide) | 5 | 2 | 7 | Tooling hub |
| 9 | [Multi Agent Systems](#concepts-multi-agent-systems) | 4 | 3 | 7 | Multi-agent architecture hub |
| 10 | [Data Quality Bottleneck](#concepts-data-quality-bottleneck) | 3 | 4 | 7 | Risk/quality hub |

---

## Bridge Nodes

Articles that connect otherwise separate topic clusters. Removing these would fragment the graph.

| Bridge Node | Clusters Connected |
|-------------|-------------------|
| [Knowledge Graph](#concepts-knowledge-graph) | Connects the formal KG cluster (KARMA, Graphiti, Gallagher) to the markdown wiki cluster |
| [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval) | Bridges retrieval infrastructure debates (vector DBs, HN debate) to the core LLM-KB system |
| [Hallucination Contamination](#concepts-hallucination-contamination) | Connects risk/quality cluster to the vault-separation and linting topics |
| [Personal Knowledge Management](#concepts-personal-knowledge-management) | Bridges the human workflow side (second brain, product gap) to the technical system |
| [Cheap Ontology](#concepts-cheap-ontology) | Links ontology/knowledge-representation theory to practical markdown implementation |
| [Multi Agent Systems](#concepts-multi-agent-systems) | Connects KARMA and STORM (academic systems) to the broader KB concepts |

---

## Cluster Identification

### Cluster 1: Core LLM-KB System
The densest cluster, centered on [Llm Knowledge Base](#concepts-llm-knowledge-base).
- [Wiki Compilation](#concepts-wiki-compilation)
- [Obsidian As Ide](#concepts-obsidian-as-ide)
- [Llm Qa Over Documents](#concepts-llm-qa-over-documents)
- [Linting And Health Checks](#concepts-linting-and-health-checks)
- [Post Code Ai Workflow](#concepts-post-code-ai-workflow)
- [Markdown As Universal Interface](#concepts-markdown-as-universal-interface)

### Cluster 2: Retrieval & Infrastructure
Focused on how knowledge is retrieved and stored.
- [Rag Vs Index Based Retrieval](#concepts-rag-vs-index-based-retrieval)
- [Vector Databases](#concepts-vector-databases)
- [Hn Vector Database Debate](#sources-hn-vector-database-debate)
- [Decodingai Second Brain Rag](#sources-decodingai-second-brain-rag)

### Cluster 3: Knowledge Graphs & Multi-Agent
Formal knowledge representation and automated systems.
- [Knowledge Graph](#concepts-knowledge-graph)
- [Multi Agent Systems](#concepts-multi-agent-systems)
- [Automated Wiki Creation](#concepts-automated-wiki-creation)
- [Temporal Knowledge](#concepts-temporal-knowledge)
- [Karma Multi Agent Knowledge Graph](#sources-karma-multi-agent-knowledge-graph)
- [Storm Automated Wiki Creation](#sources-storm-automated-wiki-creation)
- [Graphiti Temporal Knowledge Graphs](#sources-graphiti-temporal-knowledge-graphs)

### Cluster 4: Risk & Quality
Focused on failure modes and mitigations.
- [Hallucination Contamination](#concepts-hallucination-contamination)
- [Data Quality Bottleneck](#concepts-data-quality-bottleneck)
- [Vault Separation](#concepts-vault-separation)
- [Linting And Health Checks](#concepts-linting-and-health-checks)

### Cluster 5: Human Workflow & PKM
Human-facing knowledge management evolution.
- [Personal Knowledge Management](#concepts-personal-knowledge-management)
- [Second Brain](#concepts-second-brain)
- [Knowledge Base Product Gap](#concepts-knowledge-base-product-gap)
- [Gallagher Second Brain Knowledge Graphs](#sources-gallagher-second-brain-knowledge-graphs)
- [Glenrhodes Karpathy Workflow](#sources-glenrhodes-karpathy-workflow)

### Cluster 6: Ontology & Representation
Knowledge representation theory.
- [Cheap Ontology](#concepts-cheap-ontology)
- [Markdown As Universal Interface](#concepts-markdown-as-universal-interface)
- [Pebblous Cheap Ontology](#sources-pebblous-cheap-ontology)

---

## Density Metrics

| Cluster | Nodes | Internal Edges | Density |
|---------|-------|----------------|---------|
| Core LLM-KB System | 6 | ~15 | High |
| Retrieval & Infrastructure | 4 | ~8 | Medium |
| Knowledge Graphs & Multi-Agent | 7 | ~14 | Medium-High |
| Risk & Quality | 4 | ~10 | High |
| Human Workflow & PKM | 5 | ~10 | Medium-High |
| Ontology & Representation | 3 | ~6 | High |

---

## Star Pattern

[Llm Knowledge Base](#concepts-llm-knowledge-base) exhibits a strong star pattern: nearly every other article links to it, making it the gravitational center. This is expected for the core concept, but suggests that:

1. **Adding more mid-tier hub nodes** would improve navigability (e.g., split "llm-knowledge-base" into sub-concepts if it grows too large)
2. **Cross-cluster links** are primarily mediated through this single node -- creating direct links between peripheral clusters would improve resilience

---

## Leaf Nodes (Fewest Connections)

| Article | Incoming | Outgoing | Total |
|---------|----------|----------|-------|
| [Post Code Ai Workflow](#concepts-post-code-ai-workflow) | 1 | 2 | 3 |
| [Temporal Knowledge](#concepts-temporal-knowledge) | 2 | 2 | 4 |
| [Vault Separation](#concepts-vault-separation) | 2 | 3 | 5 |
| [Automated Wiki Creation](#concepts-automated-wiki-creation) | 2 | 3 | 5 |

These are candidates for further development and cross-linking.

---

## Source Coverage

Every source links to [Llm Knowledge Base](#concepts-llm-knowledge-base). Source-to-source links are absent (by design -- sources link to concepts, not to each other).

| Source | Concepts Linked |
|--------|----------------|
| [Karpathy Llm Knowledge Bases](#sources-karpathy-llm-knowledge-bases) | 6 |
| [Antigravity Post Code Ai Workflow](#sources-antigravity-post-code-ai-workflow) | 6 |
| [Pebblous Cheap Ontology](#sources-pebblous-cheap-ontology) | 5 |
| [Dairai Llm Knowledge Bases Architecture](#sources-dairai-llm-knowledge-bases-architecture) | 5 |
| [Glenrhodes Karpathy Workflow](#sources-glenrhodes-karpathy-workflow) | 5 |
| [Gallagher Second Brain Knowledge Graphs](#sources-gallagher-second-brain-knowledge-graphs) | 4 |
| [Storm Automated Wiki Creation](#sources-storm-automated-wiki-creation) | 4 |
| [Decodingai Second Brain Rag](#sources-decodingai-second-brain-rag) | 4 |
| [Graphiti Temporal Knowledge Graphs](#sources-graphiti-temporal-knowledge-graphs) | 4 |
| [Karma Multi Agent Knowledge Graph](#sources-karma-multi-agent-knowledge-graph) | 3 |
| [Hn Vector Database Debate](#sources-hn-vector-database-debate) | 2 |

---

*This analysis was computed statically from the link graph on 2026-04-05. Re-run the analysis after adding new articles to keep it current.*


---

## Dataview Queries {#queries}

***type:** reference | **last_updated:** 2026-04-05*

# Dataview Queries Reference

Pre-built Dataview queries for exploring and maintaining the knowledge base. Copy any query into a note or use directly from this page (requires the Dataview plugin).

---

## All Concepts Sorted by Source Count

```dataview
TABLE length(sources) AS "Source Count", summary
FROM "wiki/concepts"
WHERE type = "concept"
SORT length(sources) DESC
```

---

## All Sources with Related Concepts

```dataview
TABLE related AS "Related Concepts", last_compiled, summary
FROM "wiki/sources"
WHERE type = "source-summary"
SORT last_compiled DESC
```

---

## All Entities by Type

```dataview
TABLE entity_type AS "Entity Type", summary, url
FROM "wiki/entities"
WHERE type = "entity"
GROUP BY entity_type
```

---

## Articles Missing Summaries

```dataview
LIST
FROM "wiki"
WHERE !summary OR summary = ""
```

---

## Articles by Tag

```dataview
TABLE file.tags AS "Tags", type, summary
FROM "wiki"
WHERE file.tags
FLATTEN file.tags AS tag
GROUP BY tag
```

---

## Recent Ingests Timeline

```dataview
TABLE date_ingested AS "Ingested", type, summary
FROM "wiki"
WHERE date_ingested
SORT date_ingested DESC
```

---

## Cross-Reference Matrix: Sources and Concepts They Discuss

```dataview
TABLE WITHOUT ID
  file.link AS "Source",
  length(related) AS "Concepts Linked",
  related AS "Concepts"
FROM "wiki/sources"
SORT length(related) DESC
```

---

## Orphan Detection

Articles with no incoming backlinks (may need attention):

```dataview
LIST
FROM "wiki/sources" OR "wiki/concepts" OR "wiki/entities" OR "wiki/comparisons"
WHERE length(file.inlinks) = 0
```

---

## Stale Articles (Not Updated in 30+ Days)

```dataview
TABLE last_compiled AS "Last Compiled", summary
FROM "wiki/sources" OR "wiki/concepts"
WHERE last_compiled AND date(last_compiled) < date(now) - dur(30 days)
SORT last_compiled ASC
```

---

## Most Linked-To Articles

```dataview
TABLE length(file.inlinks) AS "Incoming Links", length(file.outlinks) AS "Outgoing Links", type
FROM "wiki"
SORT length(file.inlinks) DESC
LIMIT 20
```

---

## All Articles with Frontmatter Field Listing

```dataview
TABLE type, last_compiled, length(sources) AS "Sources", length(related) AS "Related"
FROM "wiki"
WHERE type AND type != "meta" AND type != "index" AND type != "log"
SORT type, file.name
```

---

## Articles by Compilation Date

```dataview
TABLE type, summary
FROM "wiki"
WHERE last_compiled
GROUP BY last_compiled
SORT last_compiled DESC
```

---

## Concepts Not Referenced by Any Source

```dataview
LIST
FROM "wiki/concepts"
WHERE !sources OR length(sources) = 0
```

---

## Full Text Search Helpers

To find articles mentioning specific terms, use Obsidian's built-in search (`Cmd+Shift+F`) with these patterns:

- `path:wiki/concepts "RAG"` -- concepts mentioning RAG
- `path:wiki/sources "Karpathy"` -- sources mentioning Karpathy
- `tag:#risk` -- articles tagged with risk
- `[summary:` -- articles with summary field (regex search)

---

*Install the Dataview community plugin to render these queries. In Obsidian: Settings > Community Plugins > Browse > "Dataview" > Install > Enable.*


---

## Tag Index {#tags}

***type:** reference | **last_updated:** 2026-04-05*

# Tag Index

Browse all tags used across the knowledge base. Tags are defined in article frontmatter (`tags:` field) and inline (`#tag`).

---

## All Tags (Dataview)

```dataview
LIST WITHOUT ID tag + " (" + length(rows) + " articles)"
FROM "wiki"
FLATTEN file.tags AS tag
GROUP BY tag
SORT tag ASC
```

---

## Suggested Tag Taxonomy

The following tags are recommended for consistent categorization. Add them to article frontmatter as needed.

### A

- `#architecture` -- System design and structural patterns
- `#agent` -- LLM agent systems and multi-agent frameworks

### C

- `#comparison` -- Comparative analysis articles

### D

- `#data-quality` -- Data quality, cleaning, validation

### E

- `#evaluation` -- Benchmarks, metrics, testing

### F

- `#framework` -- Software frameworks and libraries

### G

- `#graph` -- Knowledge graphs, graph databases

### H

- `#hallucination` -- LLM hallucination and contamination risks

### I

- `#infrastructure` -- Databases, vector stores, deployment

### K

- `#knowledge-management` -- PKM, enterprise KM, knowledge workflows

### L

- `#llm` -- Large language models (general)

### M

- `#markdown` -- Markdown as knowledge substrate
- `#multi-agent` -- Multi-agent LLM systems

### O

- `#obsidian` -- Obsidian-specific features and workflows
- `#ontology` -- Ontology, taxonomy, schema design

### P

- `#pipeline` -- Data and compilation pipelines
- `#pkm` -- Personal knowledge management
- `#product` -- Product opportunities and gaps

### R

- `#rag` -- Retrieval-augmented generation
- `#retrieval` -- Information retrieval (general)
- `#risk` -- Risks, failure modes, mitigations

### S

- `#scale` -- Scalability considerations
- `#second-brain` -- Second brain / personal AI assistant

### T

- `#temporal` -- Time-aware knowledge, versioning
- `#tool` -- Specific tools (Obsidian, ChromaDB, etc.)

### W

- `#wiki` -- Wiki compilation and maintenance
- `#workflow` -- Human and LLM workflows

---

## Articles Per Tag (Dataview)

### Architecture
```dataview
LIST summary
FROM "wiki"
WHERE contains(file.tags, "#architecture")
```

### Risk
```dataview
LIST summary
FROM "wiki"
WHERE contains(file.tags, "#risk")
```

### Retrieval
```dataview
LIST summary
FROM "wiki"
WHERE contains(file.tags, "#retrieval") OR contains(file.tags, "#rag")
```

### Multi-Agent
```dataview
LIST summary
FROM "wiki"
WHERE contains(file.tags, "#multi-agent") OR contains(file.tags, "#agent")
```

### Knowledge Management
```dataview
LIST summary
FROM "wiki"
WHERE contains(file.tags, "#pkm") OR contains(file.tags, "#knowledge-management")
```

### Wiki & Pipeline
```dataview
LIST summary
FROM "wiki"
WHERE contains(file.tags, "#wiki") OR contains(file.tags, "#pipeline")
```

---

## Type-Based Browsing

Not using tags yet? Browse by article type instead:

- **Sources**: `path:wiki/sources` in search, or _Index#Sources
- **Concepts**: `path:wiki/concepts` in search, or _Index#Concepts
- **Entities**: `path:wiki/entities` in search
- **Comparisons**: `path:wiki/comparisons` in search

---

*Add tags to articles using the `tags:` frontmatter field (e.g., `tags: ["#architecture", "#llm"]`) or inline with `#tagname`. This page will automatically update via Dataview.*


---

## Activity Log {#log}

***type:** log*

# Activity Log

Append-only chronological record of all wiki operations.

## [2026-04-05] ingest | Thread by @karpathy — LLM Knowledge Bases
- Source: Clippings/Thread by @karpathy.md → raw/karpathy-llm-knowledge-bases.md
- Created: sources/karpathy-llm-knowledge-bases, 6 concept articles
- Compiled index, summaries, links, manifest

## [2026-04-05] research | LLM knowledge bases and personal wikis
- Searched: "LLM knowledge bases", "personal wiki AI", "automated wiki creation", "knowledge graph LLM"
- Ingested 10 new sources (DAIR.AI, Glen Rhodes, Antigravity, Pebblous, KARMA, Gallagher, STORM, Decoding AI, HN debate, Graphiti)
- Created: 11 source summaries, 20 concept articles
- Updated: index, summaries, links, manifest


---
