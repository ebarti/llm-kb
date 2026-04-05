---
title: "The State of LLM Knowledge Bases: A Comprehensive Research Report"
type: report
generated: 2026-04-05
sources_consulted: 42
word_target: 3000+
---

# The State of LLM Knowledge Bases

## Executive Summary

LLM knowledge bases represent a paradigm shift in how humans organize, maintain, and query structured knowledge. Rather than manually curating notes, wikis, or databases, an LLM acts as both author and maintainer of a structured knowledge repository, with humans interacting solely through natural language. Pioneered publicly by Andrej Karpathy in early 2026, this approach has catalyzed a rethinking of personal knowledge management, enterprise knowledge graphs, and the role of retrieval-augmented generation.

This report synthesizes findings from 42 sources compiled into this wiki, covering the foundational vision, competing architectures, the tool landscape, persistent challenges, and the trajectory of the field. The central finding is that **data quality, not model scale, is the decisive bottleneck** for LLM knowledge bases ([[concepts/data-quality-bottleneck]]), and that the approach represents what Pebblous calls a "Cheap Ontology" ([[concepts/cheap-ontology]]) — a 1,000x cost reduction over traditional enterprise knowledge graphs.

The field is at an inflection point. The conceptual framework is proven, the tools are maturing, but the gap between "hacky scripts" and polished products accessible to non-technical users ([[concepts/knowledge-base-product-gap]]) represents a significant market opportunity in a $62B enterprise knowledge management sector.

---

## 1. The Karpathy Vision and Its Implications

### The Original Workflow

In early 2026, [[entities/andrej-karpathy]] described a workflow where an LLM acts as the sole author and maintainer of a personal knowledge base ([[sources/karpathy-llm-knowledge-bases]]). The architecture is deceptively simple:

```
raw/          <- ingested source documents (source of truth)
wiki/         <- LLM-compiled and maintained
  _index.md   <- master article index
  _meta/      <- summaries, link graph, manifest
  sources/    <- per-source summary articles
  concepts/   <- cross-source concept articles
output/       <- reports, slides, images
```

Source documents are ingested into a `raw/` directory. An LLM incrementally compiles these into a structured wiki of markdown files, producing per-source summaries, concept articles with cross-links, and backlink graphs ([[concepts/wiki-compilation]]). The human owner interacts with the system only through natural language prompts — the LLM writes, updates, and maintains all wiki content directly.

### Key Insights

Three insights from Karpathy's work have proven particularly influential:

1. **"Manipulating knowledge, not code"** ([[concepts/post-code-ai-workflow]]): The next developer competitive advantage lies not in generating code, but in compiling and curating knowledge. The Antigravity analysis ([[sources/antigravity-post-code-ai-workflow]]) identified a 6-step workflow and 7 use cases, arguing that developer roles are transforming from coders to curators.

2. **RAG is unnecessary at personal scale**: Karpathy found that simple LLM-maintained index files and one-line summaries were sufficient for navigating a ~400K word corpus without a vector database ([[concepts/rag-vs-index-based-retrieval]]). This challenges the assumption that vector infrastructure is a prerequisite for knowledge retrieval.

3. **Self-reinforcing knowledge**: Queries and explorations produce outputs (reports, slides, images) that get filed back into the wiki, making the knowledge base compound over time. This "filing loop" ([[sources/glenrhodes-karpathy-workflow]]) is what distinguishes a persistent KB from a one-shot Q&A system.

### The DAIR.AI Architecture

[[entities/elvis-saravia]] at [[entities/dairai]] provided the most thorough system architecture analysis ([[sources/dairai-llm-knowledge-bases-architecture]]), formalizing Karpathy's approach into a four-phase operational cycle:

1. **Ingest**: Acquire raw source documents
2. **Compile**: LLM transforms raw documents into structured wiki
3. **Query**: LLM answers questions by navigating the compiled wiki
4. **Maintain**: LLM lints, health-checks, and enriches the wiki over time

This cycle emphasizes that no vector infrastructure is needed at the ~100-article personal scale, making the approach accessible to individuals and small teams.

---

## 2. Current Approaches to LLM Knowledge Management

### 2.1 LLM-Maintained Markdown Wikis (Karpathy Approach)

The foundational approach ([[concepts/llm-knowledge-base]]): markdown files as substrate, LLM as author, [[entities/obsidian]] as read-only IDE ([[concepts/obsidian-as-ide]]). Key advantages include human readability, version controllability, and future-proofness ([[concepts/markdown-as-universal-interface]]).

**Scale**: ~100-400 articles, ~50K-400K words. Beyond this, retrieval infrastructure becomes necessary.

### 2.2 Retrieval-Augmented Generation (RAG)

The dominant production paradigm ([[concepts/retrieval-augmented-generation]]). As of early 2026, approximately 85% of production LLM applications incorporate RAG. The architecture has evolved through three phases:

- **Naive RAG** (2020-2023): Simple retrieve-then-generate
- **Advanced RAG** (2023-2025): Query rewriting, hybrid search, reranking
- **Agentic RAG** (2025-present): Self-reflective, modular, orchestrated ([[concepts/agentic-rag]])

RAG and the Karpathy approach are not mutually exclusive. RAG provides the retrieval infrastructure needed when a knowledge base exceeds the scale where index-based navigation suffices.

### 2.3 Knowledge Graphs

Formal node-and-edge knowledge representation ([[concepts/knowledge-graph]]) with three distinct modern approaches:

- **KARMA** ([[sources/karma-multi-agent-knowledge-graph]]): 9 collaborative LLM agents for automated KG enrichment. NeurIPS 2025 Spotlight. 83.1% accuracy, 38,230 new entities from 1,200 PubMed papers.
- **Graphiti** ([[sources/graphiti-temporal-knowledge-graphs]]): Open-source temporal context graphs where facts have validity windows. Hybrid retrieval (semantic + BM25 + graph traversal).
- **Knowledge Graph Kit** ([[sources/gallagher-second-brain-knowledge-graphs]]): Personal-scale SQLite + ChromaDB MCP server for task/relationship management.

Knowledge graphs offer formal queryability and temporal reasoning but require significantly more setup complexity than markdown wikis ([[comparisons/knowledge-graph-vs-wiki]]).

### 2.4 Fine-Tuning and Domain Adaptation

Rather than retrieving knowledge at query time, fine-tuning bakes domain knowledge into model weights ([[concepts/fine-tuning]]). Key approaches include:

- **LoRA/QLoRA** ([[sources/lora-qlora-efficient-fine-tuning]]): Parameter-efficient fine-tuning reducing VRAM from 60GB to 6GB for a 7B model
- **RAFT** ([[sources/raft-retrieval-augmented-fine-tuning]]): Hybrid approach achieving up to 76% improvement by training models to ignore distractor documents and cite sources
- **Domain Adaptive Pretraining** ([[sources/domain-adaptive-pretraining-dapt]]): Intermediate pretraining on unlabeled domain text

The three-layer recommendation emerging from the research: domain-adaptive pretraining for broad knowledge, LoRA fine-tuning for task-specific skills, and RAG for dynamic facts and citations ([[comparisons/rag-vs-fine-tuning]]).

### 2.5 Long-Context and Compression Approaches

Context windows are growing ~30x/year since mid-2023 ([[sources/epoch-context-window-growth]]). Frontier models now support 1M+ tokens (Claude, Gemini), with experimental systems reaching 100M tokens ([[sources/magic-ltm-100m-context]]). However, the "lost in the middle" problem ([[concepts/lost-in-the-middle]]) causes >30% degradation for middle-positioned content.

Compression techniques ([[sources/context-compression-techniques]]) offer dramatic token reductions: LLMLingua (20x), soft prompts (480x), Provence (95%). These make large-context approaches economically viable but do not eliminate the need for structured knowledge organization.

---

## 3. Tool Landscape

### Knowledge Management Platforms

| Tool | Type | Strengths | Limitations |
|------|------|-----------|-------------|
| [[entities/obsidian]] | Markdown IDE | Local-first, 2000+ plugins, graph view | No built-in LLM compilation |
| [[entities/notion]] | Collaborative workspace | AI assistant, rich media | Proprietary format, no wiki compilation |
| [[entities/google-notebooklm]] | Document Q&A | Closest to Karpathy vision | Single-session, no persistent wiki |

### Retrieval Infrastructure

| Tool | Type | Key Metric |
|------|------|------------|
| [[entities/pinecone]] | Managed vector DB | Sub-10ms latency, billions of vectors |
| [[entities/weaviate]] | Open-source vector DB | Highest QPS (791), native hybrid search |
| [[entities/qdrant]] | Open-source vector DB | Richest feature set, Rust performance |
| [[entities/pgvector]] | PostgreSQL extension | Sufficient for most team-scale use cases |
| [[entities/chromadb]] | Embedding database | Simple, used in personal KG systems |

### Knowledge Graph Tools

| Tool | Type | Scale |
|------|------|-------|
| [[entities/microsoft-graphrag]] | Graph-based RAG | Enterprise, open-source |
| [[entities/graphiti]] | Temporal context graphs | Production, open-source |
| [[entities/neo4j]] | Graph database | Enterprise |
| [[entities/kggen]] | KG extraction library | Research/production |

### Document Processing Pipeline

| Tool | Strength | See Also |
|------|----------|----------|
| [[entities/unstructured-io]] | 30+ formats, typed elements | [[sources/unstructured-io-document-etl]] |
| [[entities/firecrawl]] | Web-to-markdown API | [[sources/firecrawl-web-data-api]] |
| [[entities/docling]] | Enterprise PDF parsing | [[sources/pdf-parser-comparison-2026]] |
| [[entities/llamaparse]] | Complex tables/figures | [[entities/llamaindex]] |
| [[entities/markitdown]] | Office/PDF to markdown | [[sources/microsoft-markitdown]] |

### Automated Wiki Creation

| System | Approach | See Also |
|--------|----------|----------|
| [[entities/storm]] | Multi-perspective article generation | [[sources/storm-automated-wiki-creation]] |
| Karpathy workflow | Incremental compilation from raw sources | [[sources/karpathy-llm-knowledge-bases]] |

---

## 4. Challenges

### 4.1 Hallucination Contamination

The primary systemic risk ([[concepts/hallucination-contamination]]). When an LLM hallucinates a fact and writes it into the wiki, that error propagates through future queries and, critically, into fine-tuning datasets. Tanwar et al. (2024) demonstrated that fine-tuning on hallucinated data causes permanent weight corruption — qualitatively worse than a runtime retrieval error.

Mitigation strategies include:
- **Vault separation** ([[concepts/vault-separation]]): [[entities/steph-ango]] recommends keeping AI-generated content separate from human-curated notes
- **Provenance tracing**: All claims should trace back to `raw/` source files
- **LLM linting** ([[concepts/linting-and-health-checks]]): Periodic automated scans for contradictions
- **Claim extraction** ([[concepts/claim-extraction]]): Decomposing content into atomic verifiable claims (the [[entities/claimify]] pattern)

### 4.2 Data Quality as the Decisive Bottleneck

[[concepts/data-quality-bottleneck]] is the recurring theme across the research. Microsoft's Phi research ([[sources/textbooks-are-all-you-need-phi]]) demonstrated that a 1.3B-parameter model trained on "textbook quality" synthetic data can match models 10x larger. The implication: curating high-quality raw inputs matters more than model selection or infrastructure sophistication.

As [[sources/pebblous-agentic-framework-explosion]] notes, all three 2025 agent framework paradigms (RL, self-improvement, TDD) are bottlenecked by data quality, not model capability.

### 4.3 Scaling Limitations

The Karpathy approach works elegantly at personal scale (~100-400 articles) but faces challenges beyond that:

- **Context window saturation**: Even with 1M+ token windows, loading an entire wiki becomes impractical beyond ~400K words
- **Index-based navigation degrades**: One-line summaries lose discriminating power as article count grows
- **Compilation time increases**: Incremental compilation helps, but cross-article consistency checks scale quadratically
- **Quality assurance becomes harder**: More articles mean more potential contradictions and hallucination propagation paths

The scaling path leads to hybrid architectures: markdown wiki for core knowledge, RAG or GraphRAG for retrieval at scale, and fine-tuning for stable domain knowledge in weights.

### 4.4 The Product Gap

Despite the proven concept, the current implementation is what Karpathy himself called "a hacky collection of scripts" ([[concepts/knowledge-base-product-gap]]). Barriers include CLI/API requirements, manual directory setup, no automated multi-source ingestion, no scheduled compilation, and no UI for non-technical users.

The market opportunity is significant: McKinsey data shows employees spend 1.8 hours/day (25% of workday) searching for information. The knowledge graph market is growing from $1.07B (2024) to $6.94B (2030) at 36.6% CAGR.

---

## 5. Future Directions

### 5.1 Context Engineering as Discipline

[[concepts/context-engineering]] is emerging as the successor to prompt engineering (2025-2026). The insight: managing everything an LLM encounters during inference — domain knowledge, tool data, conversation state — is a systems discipline, not a prompting trick ([[sources/context-engineering-2026]]). LLM knowledge bases are a natural application of context engineering principles.

### 5.2 Hierarchical Memory for Agents

[[sources/hierarchical-memory-llm-agents]] describes multi-tier memory architectures: working (in-context), episodic (summaries), semantic (abstractions), archival (external DB). LLM wikis naturally map onto the semantic and archival tiers. The AgeMem framework ([[sources/agentic-memory-unified-framework]]) unifies memory as tool-based actions trained via reinforcement learning.

### 5.3 Multi-Agent Knowledge Construction

Single-LLM compilation will likely give way to multi-agent architectures ([[concepts/multi-agent-systems]]):
- **KARMA's 9-agent pipeline** for knowledge graph enrichment
- **STORM's perspective-simulating agents** for article creation
- Specialized agents for ingestion, compilation, quality assurance, and querying

### 5.4 Convergence of Graphs and Wikis

The strict boundary between knowledge graphs and markdown wikis is dissolving. [[entities/microsoft-graphrag]] demonstrates that graphs can be extracted from text and used to enhance retrieval. [[concepts/graphrag]] dramatically outperforms baseline RAG on holistic and cross-document queries. The future likely involves markdown as the human-readable layer atop a graph-structured knowledge substrate.

### 5.5 Temporal Knowledge and Fact Decay

[[concepts/temporal-knowledge]] — tracking what was true when — is an unsolved challenge for flat wikis. [[entities/graphiti]]'s approach of associating facts with validity windows points toward a future where knowledge bases automatically track fact currency and flag outdated assertions.

### 5.6 Local and Private Knowledge Bases

The open-source LLM ecosystem ([[concepts/open-source-llms]], [[concepts/local-llm-inference]]) is making it feasible to run entire knowledge base pipelines locally. [[entities/ollama]] (150K+ GitHub stars) combined with models like Qwen 3.5 or DeepSeek V3.2 enables zero-cloud-dependency operation ([[concepts/local-knowledge-base]]). The tradeoff: reduced reasoning capability vs. complete privacy and zero per-token cost.

Small language models ([[concepts/small-language-models]]) are particularly relevant: [[entities/phi]]-4 (14B parameters) beats GPT-4o on MATH benchmarks, [[entities/gemma]] 4B runs multimodal in 3GB of RAM, and Qwen 3 4B is viable for many knowledge compilation tasks at 10-30x lower cost than frontier APIs ([[sources/small-language-models-guide-2026]]). On Apple Silicon, [[entities/mlx]] outperforms [[entities/llama-cpp]] by 21-87% for models under 14B parameters ([[sources/mlx-vs-llamacpp-apple-silicon]]), making M-series Macs effective personal knowledge base servers.

### 5.7 The Markdown Ecosystem as Knowledge Substrate

The choice of markdown as the universal format for LLM knowledge bases is not incidental — it reflects deep structural advantages ([[concepts/markdown-as-universal-interface]]). Quantified benefits include 25-75% token reduction vs HTML and 89% vs 62% RAG retrieval accuracy when using markdown ([[sources/llms-love-markdown]]). The format satisfies five requirements simultaneously: human readability, LLM compatibility, version controllability, tool agnosticism, and archival durability ([[concepts/plain-text-longevity]]).

The ecosystem supporting markdown continues to grow: [[entities/pandoc]] converts between 40+ formats via a markdown-centric AST ([[sources/pandoc-universal-converter]]), [[entities/markitdown]] from Microsoft converts Office documents and PDFs to markdown ([[sources/microsoft-markitdown]]), [[entities/marp]] converts markdown to presentations ([[sources/marp-markdown-presentations]]), and [[entities/markdowndb]] indexes markdown files into SQLite for SQL querying ([[sources/markdowndb-queryable-markdown]]). The [[concepts/file-over-app]] philosophy articulated by [[entities/steph-ango]] underpins this: files must outlast applications, and plain text is the only format guaranteed to be readable centuries from now ([[sources/sivers-plain-text-files]], [[sources/ango-file-over-app]], [[sources/mit-digital-preservation-formats]]).

### 5.8 Information Extraction Advances

The quality of wiki compilation depends directly on information extraction capabilities ([[concepts/information-extraction]]). Key advances relevant to LLM knowledge bases include:

- **Structured extraction** ([[concepts/structured-output-extraction]]): Simon Willison's LLM 0.23 introduced FSM-guaranteed JSON output across all major providers ([[sources/willison-llm-schemas-structured-extraction]]). [[entities/instructor]] achieves 3M+ monthly downloads as the de facto Python library for Pydantic-based LLM extraction ([[sources/instructor-library-structured-extraction]]).
- **Claim extraction** ([[concepts/claim-extraction]]): Microsoft's [[entities/claimify]] decomposes LLM outputs into atomic verifiable claims with 99% source entailment ([[sources/claimify-claim-extraction]]), enabling systematic quality assurance of wiki content.
- **Named entity recognition**: GPT-NER achieves supervised-comparable NER performance through task reformulation ([[sources/gpt-ner-named-entity-recognition]]), with self-verification combating hallucinated entities.
- **Knowledge graph extraction**: [[entities/kggen]] outperforms GraphRAG by 18% using a three-stage pipeline ([[sources/kggen-knowledge-graph-extraction]]), while KARMA's multi-agent approach achieves 83.1% accuracy ([[sources/karma-multi-agent-knowledge-graph]]).

These capabilities directly improve the compilation phase of the LLM knowledge base cycle ([[concepts/wiki-compilation]]).

### 5.9 The Agentic Future

The convergence of agentic AI ([[concepts/agentic-workflows]]) and knowledge management suggests a future where knowledge bases are maintained by specialized agent teams rather than single LLM calls. [[entities/andrew-ng]]'s observation that "GPT-3.5 with agentic workflow beats GPT-4 zero-shot" ([[sources/ng-agentic-design-patterns]]) applies directly to knowledge compilation: an orchestrated pipeline of ingestion agents, compilation agents, quality assurance agents, and query agents could outperform a single frontier model. The Model Context Protocol ([[sources/mcp-model-context-protocol]]) — adopted by OpenAI and Google, donated to the Linux Foundation, with 97M monthly downloads — provides the standardized interface for this kind of agent-tool interoperability.

---

## 6. Recommendations

### For Individual Practitioners

1. **Start with the Karpathy workflow**: `raw/` + LLM compilation + Obsidian viewing. The simplicity is the feature, not a limitation.
2. **Prioritize source quality over quantity**: One high-quality source compiled well is worth ten low-quality sources ([[concepts/data-quality-bottleneck]]).
3. **Implement vault separation early** ([[concepts/vault-separation]]): Keep AI-generated content separate from personal notes.
4. **Use markdown as your substrate** ([[concepts/markdown-as-universal-interface]]): It is the only format that is simultaneously human-readable, LLM-friendly, version-controllable, and future-proof.

### For Teams and Organizations

1. **Evaluate the RAG vs. index-based decision honestly** ([[concepts/rag-vs-index-based-retrieval]]): If your corpus is under 400K words, you may not need vector infrastructure.
2. **Consider hybrid architectures**: Markdown wiki for core knowledge, GraphRAG for cross-document queries, fine-tuning for stable domain expertise ([[comparisons/rag-vs-fine-tuning]]).
3. **Invest in data quality gates**: The quality assurance layer — validating raw material before pipeline entry — is the highest-leverage investment.
4. **Watch the product gap**: The first polished product that implements the full Karpathy pipeline will capture significant market share.

### For Tool Builders

1. **The product opportunity is real** ([[concepts/knowledge-base-product-gap]]): One-click setup, multi-source ingestion, automated compilation, proactive health checks, and accessible UI. The first polished product that implements the full Karpathy pipeline — raw ingestion, LLM compilation, structured wiki, Q&A, output filing, and automated linting — will capture significant market share in a $62B enterprise knowledge management sector.
2. **Design for trust** ([[concepts/trust-in-ai]]): Inline citations, confidence signals, progressive disclosure from answer to sources to raw material. If the system propagates errors into users' knowledge bases, it destroys its own value proposition.
3. **Use hybrid UI patterns**: Not chat-only. Research shows chat achieves 70% but fails at refinement. The [[concepts/copilot-pattern]] with full-screen knowledge canvas is the right interaction model, enhanced with embedded inline AI on individual articles.
4. **Enable customer-as-trainer**: Every user correction should improve compilation quality. The [[concepts/blank-page-problem]] is the first barrier for non-technical users — launch with templates, example queries, and gallery wikis to reduce adoption friction.
5. **Build on open standards**: Use markdown as the knowledge substrate ([[concepts/markdown-as-universal-interface]]), MCP for tool interoperability ([[sources/mcp-model-context-protocol]]), and open file formats throughout. Users must be able to export and migrate — this is the [[concepts/file-over-app]] principle applied to knowledge products.

### For Researchers

1. **Knowledge base evaluation**: There is no standardized benchmark for LLM knowledge base quality — coverage, accuracy, freshness, coherence, and navigability all matter but lack agreed-upon metrics.
2. **Hallucination propagation dynamics**: How do errors compound through the self-reinforcing cycle of compilation, querying, and fine-tuning? Quantitative studies of contamination rates over multiple compilation cycles would be valuable.
3. **Scale transitions**: At what exact thresholds do different retrieval strategies become necessary? The ~400K word threshold is anecdotal — controlled experiments comparing index-based, RAG, and hybrid retrieval across corpus sizes would inform architecture decisions.
4. **Multi-agent compilation quality**: Does a specialized multi-agent pipeline (KARMA-style) produce higher quality wiki content than a single frontier model? Comparative studies would guide architectural choices.
5. **Temporal knowledge integration**: How should wikis handle fact decay, supersession, and temporal context? The Graphiti approach ([[sources/graphiti-temporal-knowledge-graphs]]) is promising but needs evaluation at wiki scale.

---

## 7. Bibliography

### Primary Sources

- [[sources/karpathy-llm-knowledge-bases]] — foundational workflow description
- [[sources/dairai-llm-knowledge-bases-architecture]] — four-phase architecture analysis
- [[sources/glenrhodes-karpathy-workflow]] — filing loop and product gap acknowledgment
- [[sources/antigravity-post-code-ai-workflow]] — 6-step workflow, 7 use cases, developer role transformation
- [[sources/pebblous-cheap-ontology]] — historical ontology context, cost analysis, data quality bottleneck

### Knowledge Graph and Retrieval Sources

- [[sources/karma-multi-agent-knowledge-graph]] — NeurIPS 2025 multi-agent KG enrichment
- [[sources/gallagher-second-brain-knowledge-graphs]] — personal KG with SQLite + ChromaDB
- [[sources/storm-automated-wiki-creation]] — multi-perspective automated article generation
- [[sources/graphiti-temporal-knowledge-graphs]] — temporal context graphs
- [[sources/graphrag-microsoft-research]] — graph-based RAG with community detection
- [[sources/hn-vector-database-debate]] — practitioner debate on vector DB necessity
- [[sources/kg-vs-vector-db-glean]] — enterprise KG vs vector DB analysis

### Context and Memory Sources

- [[sources/epoch-context-window-growth]] — 30x/year context window growth
- [[sources/redis-rag-vs-long-context]] — RAG vs long-context tradeoffs
- [[sources/lost-in-the-middle-paper]] — U-shaped performance curve
- [[sources/context-engineering-2026]] — context engineering as successor to prompt engineering
- [[sources/hierarchical-memory-llm-agents]] — multi-tier memory architectures
- [[sources/magic-ltm-100m-context]] — 100M token context

### Fine-Tuning and Data Quality Sources

- [[sources/raft-retrieval-augmented-fine-tuning]] — hybrid RAG + fine-tuning
- [[sources/textbooks-are-all-you-need-phi]] — data quality > model scale
- [[sources/synthetic-data-generation-llms]] — synthetic training data generation
- [[sources/ai-training-2026-synthetic-human-data]] — exhausted web data, synthetic flywheels

### Markdown and Tool Sources

- [[sources/sivers-plain-text-files]] — plain text as future-proof format
- [[sources/ango-file-over-app]] — file over app philosophy
- [[sources/microsoft-markitdown]] — Office/PDF to markdown conversion
- [[sources/llms-love-markdown]] — quantified markdown advantages for LLMs

### Core Concept Articles

- [[concepts/llm-knowledge-base]] — the core system concept
- [[concepts/wiki-compilation]] — the compilation pipeline
- [[concepts/rag-vs-index-based-retrieval]] — when to use what
- [[concepts/hallucination-contamination]] — the primary systemic risk
- [[concepts/cheap-ontology]] — the cost disruption framing
- [[concepts/knowledge-base-product-gap]] — the market opportunity
- [[concepts/data-quality-bottleneck]] — the decisive factor
- [[concepts/context-engineering]] — the emerging discipline
- [[concepts/retrieval-augmented-generation]] — the dominant retrieval paradigm
- [[concepts/knowledge-graph]] — the formal alternative
