---
title: "Activity Log"
type: log
reading_time: "1 min"
---

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

## [2026-04-05] research | Markdown as universal knowledge format, structured documents, and plain text in AI-era knowledge management
- Searched 14 queries: markdown knowledge management, plain text vs databases, MDX components, Obsidian features, YAML frontmatter standards, markdown interoperability, structured data in markdown, Pandoc converter, Marp presentations, static site generators, Derek Sivers plain text, file over app philosophy, future-proof file formats, markdown AI token efficiency
- Fetched 10 sources: Derek Sivers (sive.rs/plaintext), Steph Ango (file-over-app), MDX (mdxjs.com), Microsoft MarkItDown (GitHub), markdown agent task format (dev.to), Why LLMs Love Markdown (craftmarkdown.com), Pandoc (pandoc.org), Marp (marp.app), MarkdownDB (markdowndb.com), MIT Libraries digital preservation
- Ingested 10 raw files to raw/
- Created 10 source summaries in wiki/sources/
- Created 7 new concept articles: plain-text-longevity, file-over-app, markdown-ecosystem, yaml-frontmatter, markdown-for-ai-agents, mdx, static-site-generators
- Created 7 new entity pages: derek-sivers, pandoc, markitdown, mdx, markdowndb (new); updated steph-ango, marp, obsidian (existing)
- Created 1 comparison: markdown-vs-proprietary-formats
- Substantially expanded: concepts/markdown-as-universal-interface (from 2 sources to 9 sources, added quantitative data, ecosystem map, longevity case, AI agent interface)
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md, _meta/links.md, log.md

## [2026-04-05] research | Synthetic data generation, fine-tuning, and knowledge in weights vs context
- Topic: Deep research on synthetic data generation, fine-tuning LLMs on domain knowledge, and putting knowledge into model weights vs context windows (Karpathy future direction)
- Searched 11 queries: synthetic data generation LLM training, fine-tuning LLM domain knowledge, RAG vs fine-tuning, LoRA QLoRA PEFT, textbook quality synthetic data phi models, RAFT retrieval augmented fine-tuning, domain adaptive pretraining DAPT, knowledge distillation small models, catastrophic forgetting mitigation, synthetic data quality filtering, knowledge editing ROME MEMIT
- Fetched 10 sources via WebFetch (2 failed: IBM 403, Neptune redirected to OpenAI acquisition)
- Ingested 8 raw files: synthetic-data-generation-llms, raft-retrieval-augmented-fine-tuning, lora-qlora-efficient-fine-tuning, textbooks-are-all-you-need-phi, domain-adaptive-pretraining-dapt, rome-memit-knowledge-editing, ai-training-2026-synthetic-human-data, llm-knowledge-distillation-survey
- Created 8 source summaries in wiki/sources/
- Created 11 new concept articles: synthetic-data-generation, fine-tuning, parameter-efficient-fine-tuning, knowledge-distillation, catastrophic-forgetting, model-collapse, domain-adaptive-pretraining, continued-pretraining, knowledge-editing, raft, weights-vs-context
- Created 2 new entity pages: microsoft-phi, rome-memit
- Created 3 new comparison pages: rag-vs-fine-tuning, lora-vs-qlora, knowledge-editing-vs-fine-tuning
- Updated existing articles: data-quality-bottleneck (added sources, cross-links), hallucination-contamination (added cross-links)
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md, _meta/links.md, log.md

## [2026-04-05] research | Information extraction with LLMs — NER, relation extraction, structured knowledge extraction
- Topic: Deep research on information extraction with LLMs — named entity recognition, relation extraction, structured knowledge extraction from unstructured text. Directly relevant to wiki compiler's entity/concept/relationship extraction from raw sources.
- Searched 11 queries: LLM information extraction structured output, named entity recognition LLMs, relation extraction knowledge graph LLM, structured output JSON extraction Pydantic, document understanding LLM, LLM summarization extractive abstractive, claim extraction fact verification, schema-guided extraction ontology-driven, zero-shot information extraction survey, instructor library structured extraction, entity linking knowledge base construction
- Fetched 8 sources via WebFetch (1 failed: Springer 303, 2 TDS content-blocked)
- Ingested 6 new raw files: willison-llm-schemas-structured-extraction, gpt-ner-named-entity-recognition, instructor-library-structured-extraction, claimify-claim-extraction, ontogpt-ontology-extraction, wolfe-llm-summarization-evolution (2 already existed: kggen-knowledge-graph-extraction, llm-kg-construction-survey)
- Created 6 new source summaries: willison-llm-schemas-structured-extraction, gpt-ner-named-entity-recognition, instructor-library-structured-extraction, claimify-claim-extraction, ontogpt-ontology-extraction, wolfe-llm-summarization-evolution
- Created 9 new concept articles: information-extraction, named-entity-recognition, relation-extraction, structured-output-extraction, claim-extraction, llm-summarization, entity-linking, zero-shot-information-extraction, schema-guided-extraction
- Created 6 new entity pages: instructor, pydantic, claimify, ontogpt, kggen, simon-willison
- Created 1 new comparison: schema-guided-vs-schema-free-extraction
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md, log.md
## [2026-04-06] compile | Full entity and comparison pass
- Created 24 entity pages in wiki/entities/ (people: Karpathy, Steph Ango, Elvis Saravia, Vannevar Bush, Sam Gallagher; tools: Obsidian, Obsidian Web Clipper, Marp, Matplotlib, Dataview, Graphiti, ChromaDB, FAISS, pgvector, SQLite, Neo4j, MongoDB, Llama, ZenML, Vespa, Notion, Google NotebookLM; orgs: Zep, DAIR.AI; papers: STORM, KARMA, FreshWiki; historical: Memex)
- Created 8 comparison pages in wiki/comparisons/ (RAG vs Index, Vector DB vs BM25, STORM vs Karpathy, Knowledge Graph vs Wiki, Manual PKM vs LLM PKM, Fine-tuning vs Context Window, Single-Agent vs Multi-Agent, Obsidian vs Graph Database)
- Updated index, summaries, links with all new articles

## [2026-04-05] research | Prompt engineering, structured prompting techniques, and best practices
- Searched 13 queries: prompt engineering best practices, chain-of-thought, tree of thoughts, self-consistency, few-shot, prompt chaining, meta-prompting, role prompting, structured output, system prompt design, RAG prompting, prompt injection defense, Claude/Anthropic guide
- Fetched 10 high-quality sources: Prompt Engineering Guide (DAIR.AI) x6 technique pages, Anthropic official Claude guide, Lakera prompt engineering guide, Lakera prompt injection guide, PromptHub role-prompting research, IntuitionLabs meta-prompting
- Created 11 raw files: promptingguide-chain-of-thought, promptingguide-tree-of-thoughts, promptingguide-self-consistency, promptingguide-few-shot, promptingguide-prompt-chaining, promptingguide-rag-prompting, anthropic-claude-prompting-best-practices, lakera-prompt-engineering-guide, lakera-prompt-injection-guide, prompthub-role-prompting-research, intuitionlabs-meta-prompting
- Created 11 source summaries in wiki/sources/
- Created 13 concept articles: prompt-engineering, chain-of-thought-prompting, few-shot-prompting, zero-shot-prompting, tree-of-thoughts-prompting, self-consistency-prompting, role-prompting, prompt-chaining, meta-prompting, structured-output-prompting, system-prompt-design, prompt-injection, rag-prompting
- Created 6 entity pages: anthropic, claude, dspy, textgrad, owasp, prompt-engineering-guide
- Created 3 comparison pages: cot-vs-tot-vs-self-consistency, few-shot-vs-zero-shot, manual-vs-automated-prompt-optimization
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md, log.md

## [2026-04-05] research | Multimodal AI, vision-language models, and images in knowledge bases
- Searched 11 queries: multimodal AI VLMs 2025-2026, GPT-4V/Claude vision, image understanding LLM extraction, diagram/chart AI, VQA state of art, multimodal RAG, OCR document AI, image captioning, visual knowledge representation, CLIP multimodal embeddings, scientific figure understanding
- Fetched 8 sources: BentoML VLM survey, NVIDIA multimodal RAG intro, Viso.ai VQA guide, Pixno OCR evolution, Anthropic Claude vision docs, Pinecone CLIP deep dive, KX Systems multimodal RAG guide, ScienceDirect image captioning survey
- Ingested 8 raw files to raw/
- Created 8 source summaries in wiki/sources/
- Created 8 new concept articles: multimodal-ai, vision-language-models, multimodal-rag, multimodal-embeddings, image-understanding, visual-question-answering, document-ai-ocr, image-captioning
- Created 3 new entity pages: clip, qwen3-vl, deplot
- Created 1 comparison: text-rag-vs-multimodal-rag
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md, log.md

## [2026-04-05] research | Text embeddings, vector search, semantic similarity, and search infrastructure
- Searched: 12 web searches covering embedding models, MTEB benchmarks, vector databases, HNSW, hybrid search, ColBERT, reranking, chunking strategies, semantic vs keyword search
- Fetched and ingested 11 sources:
  - pinecone-embedding-models-rundown (Pinecone embedding model comparison)
  - huggingface-matryoshka-embeddings (Matryoshka Representation Learning tutorial)
  - weaviate-hybrid-search-explained (Hybrid search with BM25 + vector + RRF)
  - pinecone-hnsw-explained (HNSW algorithm deep dive)
  - jina-colbert-late-interaction (ColBERT late interaction architecture)
  - pinecone-rerankers-two-stage (Cross-encoder reranking and two-stage retrieval)
  - xenoss-vector-db-comparison (Pinecone vs Qdrant vs Weaviate)
  - redis-semantic-vs-keyword-search (Semantic vs keyword search tradeoffs)
  - superlinked-hybrid-search-reranking (Full RAG pipeline with hybrid + reranking)
  - modal-mteb-leaderboard (MTEB benchmark analysis and top models)
  - weaviate-chunking-strategies (Text chunking strategies for RAG)
- Created 11 source summaries in wiki/sources/
- Created 14 concept articles: text-embeddings, vector-search, semantic-search, keyword-search, bm25, hybrid-search, hnsw, approximate-nearest-neighbor-search, bi-encoder-vs-cross-encoder, reranking, two-stage-retrieval, colbert-late-interaction, matryoshka-representation-learning, chunking-strategies
- Created 6 entity pages: mteb, sentence-transformers, pinecone, qdrant, weaviate, openai-embeddings
- Created 3 comparison pages: semantic-vs-keyword-search, pinecone-vs-qdrant-vs-weaviate, bi-encoder-vs-cross-encoder-vs-colbert
- Updated existing concept: vector-databases (added new sources and related links)
- Updated existing concept: rag-vs-index-based-retrieval (added related links)
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md, _meta/links.md

## [2026-04-05] research | Knowledge graphs, graph databases, and their use with LLMs for knowledge management
- Searched 11 queries: knowledge graph construction with LLMs, GraphRAG Microsoft research, Neo4j KG LLM integration, KG vs document store for AI, ontology construction automated LLM, RDF OWL knowledge representation, KG embedding models, property graph vs RDF, temporal knowledge graphs, KG completion with LLMs, LLM structured extraction KG
- Fetched 10 sources:
  - Microsoft Research GraphRAG documentation and blog
  - arXiv survey: LLM-empowered KG construction (2510.20345)
  - KGGen: extracting KGs from text (2502.09956)
  - KG-LLM: link prediction with LLMs (2403.07311)
  - Temporal KG survey (2403.04782)
  - Wikipedia: Knowledge graph embeddings overview
  - Glean: KG vs vector database comparison
  - Phyvant: RAG vs KG enterprise analysis
  - Neo4j/Ontotext/TigerGraph: RDF vs property graph comparison
  - Dean Allemang: LLMs, KGs, and property graphs
- Created 10 raw files in raw/
- Created 10 source summaries in wiki/sources/
- Created 11 new concept articles: graphrag (updated existing), knowledge-graph-construction, knowledge-extraction, knowledge-fusion, ontology-engineering, knowledge-graph-embeddings, knowledge-graph-completion, temporal-knowledge-graphs, rdf-knowledge-representation, property-graphs, hybrid-retrieval
- Updated existing concepts: knowledge-graph (added graph data models, embeddings, GraphRAG sections)
- Created 3 entity pages: microsoft-graphrag, dean-allemang, karma-framework; updated kggen
- Created 3 comparison pages: rdf-vs-property-graph, knowledge-graph-vs-vector-database, kge-vs-llm-for-knowledge-graphs
- Updated: _index.md, _meta/summaries.md, _meta/links.md, _meta/manifest.md

## [2026-04-05] research | Open-source LLMs, local inference, and local KB systems
- Topic: Open source LLMs, local inference, and running AI knowledge systems without cloud APIs
- Searches: 12 web searches covering open-source LLM comparisons, Llama 4, Mistral, Qwen/DeepSeek, Ollama, llama.cpp, vLLM, open vs closed tradeoffs, local RAG, MLX/Apple Silicon, SLMs, coding models
- Sources fetched: 10 URLs via WebFetch (BentoML, Red Hat, Meta AI, AI Merge, Groundy, ArXiv, Local AI Master, freeCodeCamp, HatchWorks, Medium)
- Raw files created: 11 (bentoml-open-source-llms-2026, deepseek-revolution-2026, meta-llama-4-multimodal, ollama-complete-guide, ollama-vs-vllm-benchmarks, mlx-vs-llamacpp-apple-silicon, apple-silicon-llm-inference-study, small-language-models-guide-2026, freecodecamp-local-rag-ollama, open-source-vs-closed-llms-enterprise, local-llm-hosting-tools-comparison, coding-models-comparison-2026)
- Source summaries created: 12 (one per raw file)
- Concept articles created: 8 (open-source-llms, local-llm-inference, mixture-of-experts, quantization, apple-silicon-inference, small-language-models, local-knowledge-base, open-source-coding-models)
- Entity pages created: 10 (deepseek, qwen, meta-llama, ollama, vllm, llama-cpp, mlx, lm-studio, phi, gemma)
- Comparison pages created: 4 (open-source-vs-closed-llms, ollama-vs-vllm, local-vs-cloud-knowledge-base, mlx-vs-llamacpp)
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md, log.md
- Key finding: This KB could feasibly run on local models (Ollama + Qwen 3 32B or DeepSeek V3 distilled) with a hybrid approach recommended — local for routine ops, cloud for complex compilation

## [2026-04-05] research | LLM Agents, Tool Use, Autonomous AI Systems, and Agentic Workflows

Deep research pass on agentic AI for knowledge work.

### Web Searches (14 queries)
- LLM agent frameworks 2025 2026
- ReAct reasoning acting LLM agents
- Claude computer use tool use agents
- AutoGPT BabyAGI agent architectures
- Multi-agent LLM systems collaboration patterns
- Agentic workflows Andrew Ng
- LLM tool use function calling best practices
- Agent memory long-term short-term LLM
- LLM agent planning reflection self-improvement
- Claude Code agentic coding
- Devin AI software engineering agent
- MCP model context protocol anthropic
- Agent orchestration patterns
- LLM agent evaluation benchmarks SWE-bench

### Sources Fetched and Ingested (11 raw files)
1. `raw/superannotate-llm-agents-guide.md` — LLM Agents Ultimate Guide 2026
2. `raw/martinfowler-function-calling-llm.md` — Function Calling Using LLMs
3. `raw/ng-agentic-design-patterns.md` — Andrew Ng on Agentic Design Patterns
4. `raw/react-prompting-framework.md` — ReAct: Reasoning + Acting Framework
5. `raw/mcp-model-context-protocol.md` — MCP Specification and Ecosystem
6. `raw/claude-code-agentic-coding.md` — Claude Code and 2026 Software Development Trends
7. `raw/pebblous-agentic-framework-explosion.md` — 3 Paths in Autonomous AI
8. `raw/multi-agent-collaboration-survey.md` — Multi-Agent Collaboration Survey (arXiv)
9. `raw/agentic-memory-unified-framework.md` — AgeMem: Unified Memory (arXiv)
10. `raw/databricks-agent-design-patterns.md` — Agent System Design Patterns
11. `raw/devin-ai-software-engineer.md` — Devin AI: First Autonomous SE Agent

### Wiki Pages Created/Updated
**Source summaries (11):**
- sources/superannotate-llm-agents-guide, martinfowler-function-calling-llm, ng-agentic-design-patterns
- sources/react-prompting-framework, mcp-model-context-protocol, claude-code-agentic-coding
- sources/pebblous-agentic-framework-explosion, multi-agent-collaboration-survey
- sources/agentic-memory-unified-framework, databricks-agent-design-patterns, devin-ai-software-engineer

**Concept articles (12):**
- concepts/llm-agent-architecture (NEW) — four-component architecture + design pattern spectrum
- concepts/agentic-workflows (NEW) — four design patterns, three evolution stages, enterprise strategy
- concepts/react-pattern (NEW) — Thought-Action-Observation loop, performance data
- concepts/reflection-pattern (NEW) — self-critique pattern, Reflexion, multi-agent reflection
- concepts/tool-use (NEW) — function calling, best practices, security, MCP integration
- concepts/agent-memory (NEW) — STM/LTM, AgeMem unified framework
- concepts/agent-planning (NEW) — CoT, ToT, task decomposition, feedback mechanisms
- concepts/model-context-protocol (NEW, later extended by MCP research) — spec, adoption, ecosystem
- concepts/agentic-coding (NEW) — Devin to Claude Code, developer role shift
- concepts/agent-orchestration (NEW) — orchestrator-worker, supervisor, router patterns
- concepts/agent-frameworks (NEW) — framework landscape and selection criteria
- concepts/swe-bench (NEW) — benchmark variants and performance timeline

**Entity pages (4):**
- entities/andrew-ng (NEW) — four design patterns, enterprise strategy
- entities/claude-code (NEW) — $2.5B revenue, SWE-bench leader
- entities/devin-ai (NEW) — first autonomous SE agent
- entities/anthropic (UPDATED) — added agentic AI leadership section

**Comparison pages (3):**
- comparisons/single-agent-vs-multi-agent (UPDATED) — expanded with orchestration patterns
- comparisons/claude-code-vs-devin (NEW) — terminal-first vs sandboxed
- comparisons/react-vs-reflection-vs-planning (NEW) — three complementary patterns

**Existing pages updated:**
- concepts/multi-agent-systems — added collaboration taxonomy, Ng's design pattern, orchestration section
- wiki/_index.md — added all new sources, concepts, entities, comparisons
- wiki/_meta/summaries.md — added all new article summaries
- wiki/_meta/manifest.md — added 11 new raw files

## [2026-04-05] research | LLM context windows, long-context models, memory systems, context management
- Searched: 14 web queries covering context windows, long-context models, lost-in-the-middle, MemGPT, RAG vs context, needle-in-a-haystack, prompt caching, hierarchical memory, context compression, infinite context, context engineering, Magic LTM, Letta
- Fetched 10 detailed sources via WebFetch (Epoch AI, Redis, LogRocket, arXiv Lost-in-Middle, MemGPT/arXiv, PromptHub caching, Magic LTM blog, Agenta techniques, arXiv Infini-attention/Ring Attention, Letta agent memory)
- Ingested 10 raw files: epoch-context-window-growth, redis-rag-vs-long-context, logrocket-llm-context-problem, lost-in-the-middle-paper, memgpt-llm-operating-system, prompt-caching-providers, magic-ltm-100m-context, infinite-context-approaches, context-compression-techniques, hierarchical-memory-llm-agents, context-engineering-2026
- Created 11 source summaries in wiki/sources/
- Created 10 concept articles: context-windows, long-context-models, lost-in-the-middle, context-engineering, context-compression, needle-in-a-haystack, prompt-caching, virtual-context-management, hierarchical-memory, infinite-context
- Created 3 entity pages: memgpt-letta, magic-ltm, lost-in-the-middle-paper
- Created 2 comparison pages: rag-vs-long-context, context-management-approaches
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md, _meta/links.md
- Key insight: the LLM wiki approach (summaries.md → selective article loading) is itself a context engineering system that mirrors hierarchical memory and virtual context management patterns

## [2026-04-05] research | Data pipelines for AI, ETL for knowledge systems, document processing
- Topic: Data pipelines for AI, ETL for knowledge systems, document processing pipelines, unstructured data ingestion at scale
- Motivation: The KB's ingest/compile pipeline is fundamentally a document processing pipeline
- Searched 14 queries covering: document processing pipelines, unstructured data ingestion, LlamaIndex, LangChain, Apache Airflow, web scraping, PDF parsing, chunking strategies, VLMs, OCR, data cleaning, incremental ETL, Unstructured.io, Firecrawl
- Fetched and ingested 9 sources:
  - alan-llm-document-pipeline-production (Alan healthcare pipeline, Medium)
  - rag-chunking-strategies-dasroot (chunking benchmarks, dasroot.net)
  - stackoverflow-chunking-rag (Stack Overflow Blog chunking guide)
  - huggingface-vlms-2025 (HuggingFace VLM landscape survey)
  - unstructured-io-document-etl (Unstructured.io GitHub/docs)
  - firecrawl-web-data-api (Firecrawl docs)
  - llamaindex-ingestion-pipeline (LlamaIndex loading docs)
  - airflow-mlops-orchestration (Astronomer Airflow MLOps guide)
  - pdf-parser-comparison-2026 (multi-source PDF parser benchmarks)
- Created 9 source summaries in wiki/sources/
- Created 7 concept articles: document-processing-pipeline, document-chunking-strategies, ocr-document-extraction, pdf-parsing-tools, web-scraping-at-scale, pipeline-orchestration, incremental-etl
- Updated 1 existing concept: vision-language-models (added document processing section)
- Created 11 entity pages: unstructured-io, firecrawl, apache-airflow, pymupdf, docling, surya-ocr, llamaparse, llamaindex, langchain, colpali
- Created 3 comparison pages: pdf-parsers-comparison, unstructured-vs-langchain, ocr-vs-vlm-document-processing
- Updated cross-references in: wiki-compilation, data-quality-bottleneck
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md, log.md
- Key insight: The KB's own pipeline (fetch → clean → save markdown → compile wiki) mirrors the canonical document processing pipeline architecture but operates at the simple end of the spectrum — no vector DB, no embedding, just markdown and index files, validating the rag-vs-index-based-retrieval concept at ~100-article scale

## [2026-04-05] research | AI safety, alignment, and trustworthy AI-generated knowledge
- Topic: AI safety, alignment, hallucination risks, verification, and trustworthy AI systems
- Searches: 12 web searches covering AI safety overview, LLM hallucination causes/prevention, trustworthy AI verification, RLHF/Constitutional AI, grounding techniques, safety benchmarks, responsible AI, content watermarking, human-in-the-loop, AI governance, scalable oversight, red teaming
- Sources fetched: 11 web pages via WebFetch (FLI Safety Index, Lakera hallucination guide, arXiv hallucination survey, International AI Safety Report 2026, Confident AI red teaming guide, Anthropic safety directions, Galileo HITL oversight, Holistic AI AI-governing-AI, EC-Council governance comparison, AI2Work safety progress, DataCamp watermarking)
- Raw files created: 9 (fli-ai-safety-index-2025, llm-hallucination-comprehensive-survey, lakera-llm-hallucinations-2026, international-ai-safety-report-2026, red-teaming-llm-safety-guide, anthropic-safety-research-directions-2025, hitl-ai-agent-oversight, ai-governance-frameworks-comparison, ai-safety-alignment-progress-2025)
- Source summaries created: 9 (wiki/sources/ for each raw file)
- Concept articles created: 12 (ai-safety, ai-alignment, llm-hallucination, constitutional-ai, red-teaming, scalable-oversight, human-in-the-loop, ai-governance, ai-safety-benchmarks, ai-content-verification, grounding-and-faithfulness, calibrated-uncertainty)
- Entity pages created: 4 (eu-ai-act, nist-ai-rmf, yoshua-bengio, future-of-life-institute)
- Entity pages updated: 1 (anthropic — added AI safety leadership section)
- Concept articles updated: 1 (hallucination-contamination — linked to new hallucination and verification concepts)
- Comparison articles created: 1 (rlhf-vs-constitutional-ai)
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md, log.md

## [2026-04-05] research | Developer Tools for AI-Assisted Workflows
- Topic: AI coding assistants, AI pair programming, how developers integrate LLMs into daily work
- Performed 11 web searches covering: AI coding assistants comparison, Claude Code vs Cursor vs Copilot, AI pair programming workflows, developer productivity studies (METR RCT), LLM IDE integration, agentic coding tools, AI code review, AI test generation, AI documentation generation, productivity statistics
- Fetched and ingested 10 raw sources:
  - metr-ai-developer-productivity-study (METR RCT: 19% slowdown finding)
  - osmani-llm-coding-workflow-2026 (Addy Osmani's 10-step workflow)
  - faros-ai-coding-agents-2026 (comprehensive agent review)
  - faros-ai-productivity-paradox (10K+ developer telemetry study)
  - dextralabs-claude-cursor-copilot-30day (30-day practitioner comparison)
  - redmonk-agentic-ides-2025 (10 agentic IDE requirements)
  - graphite-ai-code-review-tools (7 AI code review tools)
  - index-dev-ai-pair-programming-statistics (100+ statistics compendium)
  - qodo-ai-coding-assistants-2026 (15-tool five-tier taxonomy)
  - panto-ai-coding-productivity-stats (DORA metrics for AI ROI)
- Created 10 source summaries in wiki/sources/
- Created 6 concept articles: ai-coding-assistants, ai-pair-programming, ai-productivity-paradox, ai-code-review, spec-driven-development, developer-experience-ai
- Updated 1 existing concept: agentic-coding (added RedMonk 10 requirements, multi-agent future, market landscape)
- Created 8 entity pages: cursor, github-copilot, aider, devin, coderabbit, graphite, addy-osmani, metr
- Updated 1 existing entity: claude-code (added practitioner assessment, 4 new source references)
- Created 1 comparison page: cursor-vs-claude-code-vs-copilot
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md, log.md
- Total new wiki pages: 26 (10 sources + 6 concepts + 8 entities + 1 comparison + 1 existing concept updated + 1 existing entity updated)
- Key findings:
  - AI Productivity Paradox: 84% adoption but METR RCT shows 19% slowdown for experienced devs; Faros telemetry shows no org-level gains
  - Market leaders: Cursor ($2B ARR), Claude Code ($2.5B ARR, 80.8% SWE-bench), Copilot (90% Fortune 100)
  - The bottleneck has shifted from code writing to code review — AI review tools (Graphite 55% action rate) now exceed human reviewer action rates
  - Spec-driven development emerges as the single most effective practice for AI-assisted coding
  - Developer role transforming from coder to architect/reviewer/agent-orchestrator

## [2026-04-05] research | Tokenization, BPE, text processing for LLMs
- Searched: 10 queries covering BPE algorithm, tokenizer comparison, multilingual tokenization, vocabulary size tradeoffs, byte-level models, token counting, Karpathy minbpe, subword algorithms, text preprocessing
- Fetched and ingested 10 sources:
  - raschka-bpe-from-scratch (Sebastian Raschka BPE tutorial)
  - huggingface-tokenization-algorithms (BPE/WordPiece/Unigram/SentencePiece comparison)
  - kamali-tokenization-killing-multilingual (multilingual tokenization critique)
  - trott-tokenization-llms (tokenization impact on LLM behavior)
  - karpathy-minbpe-lecture (2h13m GPT tokenizer lecture)
  - rohan-paul-vocabulary-size-tradeoffs (vocab size analysis across GPT-4/LLaMA/Mistral)
  - evabyte-tokenization-free-model (6.5B byte-level language model)
  - ali-tokenizer-choice-negligible-crucial (24-model empirical study)
  - winder-token-count-practical-guide (token counting for APIs)
  - github-faster-bpe-tokenizer (linear-time BPE implementation)
- Created 10 source summaries, 10 concept articles, 5 entity pages, 1 comparison page
- New concepts: tokenization, byte-pair-encoding, subword-tokenization, wordpiece, unigram-tokenization, sentencepiece, vocabulary-size-tradeoffs, multilingual-tokenization, byte-level-models, token-counting
- New entities: tiktoken, minbpe, evabyte, sebastian-raschka, philip-gage
- New comparison: bpe-vs-wordpiece-vs-unigram
- Updated: andrej-karpathy entity, _index.md, summaries.md, links.md, manifest.md

## [2026-04-05] research | RAG Systems, Retrieval-Augmented Generation, and Alternatives to RAG

Deep research pass covering RAG architecture evolution, advanced techniques, evaluation, limitations, and alternatives.

- **12 web searches** across different angles (architecture, fine-tuning comparison, alternatives, BM25/vector, evaluation, advanced techniques, GraphRAG, RAPTOR, ColBERT, hybrid search, failures, agentic RAG)
- **12 sources fetched and ingested** to raw/: ragflow-rag-review-2025, rag-vs-finetuning-agriculture, cache-augmented-generation, microsoft-graphrag, raptor-tree-retrieval, colbert-late-interaction, hybrid-search-rag-optimization, hybrid-search-bm25-splade-vector, rag-hallucinations-explained, self-reflective-rag-langgraph, rag-evaluation-metrics-benchmarks, agentic-rag-survey
- **12 source summaries** created in wiki/sources/
- **13 concept articles** created: retrieval-augmented-generation, cache-augmented-generation, raptor, agentic-rag, self-rag, corrective-rag, rag-hallucinations, rag-evaluation, colbert, splade, late-interaction-retrieval, hierarchical-retrieval, multimodal-rag (concepts/graphrag already existed with rich content)
- **5 existing concepts updated**: hybrid-search, context-engineering, fine-tuning, bm25, reranking, multimodal-rag
- **4 entity pages** created: ragas, langgraph, microsoft-research, raptor-paper
- **3 comparison pages** created: rag-vs-cag, bm25-vs-vector-search, naive-vs-advanced-vs-agentic-rag
- **1 existing comparison updated**: rag-vs-fine-tuning
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md, _meta/links.md
- Key findings: 85% production adoption; RAG→Context Engine evolution; CAG 10x faster for small KBs; hybrid search +26-31% NDCG; 17-33% hallucination in legal RAG; agentic RAG as current frontier

## [2026-04-05] research | LLM inference optimization, deployment strategies, cost management
- Searched 12 queries: inference optimization, API cost reduction, prompt caching, KV cache, speculative decoding, batching strategies, quantization, model routing, serving frameworks, token optimization, edge AI, latency optimization
- Fetched 10 high-quality sources: PremAI cost guide, Anthropic prompt caching, BentoML speculative decoding, BentoML batching, PremAI inference servers, Redis token optimization, KV cache techniques, quantization comparison, IBM routing research, Meta on-device LLMs
- Created 10 raw files, 10 source summaries, 10 new concept articles, 4 new entity pages, 2 new comparison pages
- Updated 3 existing articles: concepts/quantization (added GPTQ/AWQ/GGUF production methods), concepts/prompt-caching (added Anthropic benchmarks, KV cache foundation), entities/vllm (added 2026 H100 benchmarks)
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md, _meta/links.md
- Total new wiki pages: 26 | Total updated: 3

## [2026-04-05] research | LLM Evaluation, Benchmarks & Quality Assessment

Deep research pass on how to measure if an LLM-generated knowledge base is actually good.

### Web Searches (12 searches)
- LLM evaluation benchmarks 2025 2026
- LLM output quality assessment metrics
- Hallucination detection LLM evaluation methods
- RAGAS RAG evaluation framework 2025
- LLM as judge evaluator bias limitations
- Summarization quality metrics ROUGE BERTScore
- Knowledge base quality assessment evaluation framework
- Chatbot Arena LLM leaderboard ELO ranking
- LLM grounding faithfulness evaluation factual consistency NLI
- Automated fact checking verification LLM 2025
- DeepEval LLM evaluation framework open source
- LLM evaluation taxonomy reference-free human preference alignment

### Sources Ingested (10 raw files)
- `raw/confident-ai-llm-evaluation-metrics.md` — Confident AI metric taxonomy
- `raw/eugeneyan-llm-evaluators.md` — Eugene Yan LLM-as-Judge effectiveness
- `raw/cameron-wolfe-llm-as-judge.md` — Cameron Wolfe LLM-as-Judge methodology
- `raw/datadog-hallucination-detection.md` — Datadog hallucination detection
- `raw/evidentlyai-llm-evaluation-guide.md` — Evidently AI evaluation framework
- `raw/raschka-state-of-llms-2025.md` — Sebastian Raschka benchmaxxing analysis
- `raw/openfactcheck-factuality-framework.md` — OpenFactCheck framework
- `raw/deepset-rag-groundedness.md` — deepset groundedness monitoring
- `raw/responsible-ai-labs-benchmarks-2025.md` — Benchmark & safety dataset overview
- `raw/chatbot-arena-methodology.md` — Chatbot Arena / Arena AI methodology

### Wiki Pages Created/Updated
- **10 source summaries**: confident-ai-llm-evaluation-metrics, eugeneyan-llm-evaluators, cameron-wolfe-llm-as-judge, datadog-hallucination-detection, evidentlyai-llm-evaluation-guide, raschka-state-of-llms-2025, openfactcheck-factuality-framework, deepset-rag-groundedness, responsible-ai-labs-benchmarks-2025, chatbot-arena-methodology
- **9 concept articles**: llm-evaluation-metrics, llm-as-judge, evaluation-bias, hallucination-detection, faithfulness-and-groundedness, llm-benchmarks, benchmark-saturation, automated-fact-checking, evaluation-workflow
- **9 entity pages**: deepeval, g-eval, mt-bench, chatbot-arena, openfactcheck, mmlu, helm, truthfulqa, prometheus
- **3 comparison pages**: static-vs-dynamic-benchmarks, llm-judge-vs-human-evaluation, ragas-vs-deepeval
- **Updated existing**: rag-evaluation (enriched with new sources), ragas (added metrics), hallucination-contamination (linked to new concepts)
- **Updated metadata**: _index.md, _meta/summaries.md, _meta/manifest.md

## [2026-04-05] research | Model Context Protocol, tool ecosystems, and agent protocols
- Searched: "Model Context Protocol MCP Anthropic", "MCP servers tools ecosystem", "LLM tool use standards protocols", "OpenAI function calling vs MCP", "AI agent tool integration patterns", "MCP server development guide", "LLM plugin architecture design", "composable AI tool chains", "MCP adoption OpenAI Google", "MCP specification architecture JSON-RPC" (10 searches)
- Fetched and ingested 10 new sources: Wikipedia MCP, Anthropic MCP announcement, Pento year-of-MCP review, Anthropic Linux Foundation donation, Descope MCP vs function calling, Zilliz function calling vs MCP vs A2A, Google AI agent protocols, Composio integration patterns, Anthropic building effective agents, Anthropic code execution with MCP
- Created 10 source summaries: sources/wikipedia-model-context-protocol, sources/anthropic-mcp-announcement, sources/pento-year-of-mcp-review, sources/anthropic-mcp-linux-foundation, sources/descope-mcp-vs-function-calling, sources/zilliz-function-calling-vs-mcp-vs-a2a, sources/google-ai-agent-protocols, sources/composio-api-integration-patterns, sources/anthropic-building-effective-agents, sources/anthropic-code-execution-mcp
- Created/updated 10 concept articles: concepts/model-context-protocol (updated), concepts/function-calling, concepts/tool-use-standards, concepts/mcp-ecosystem, concepts/mcp-security, concepts/mcp-code-execution-pattern, concepts/agent-to-agent-protocol, concepts/augmented-llm, concepts/agentic-workflow-patterns, concepts/ai-agent-integration-patterns
- Created 2 entity pages: entities/agentic-ai-foundation, entities/google-adk
- Created 1 comparison: comparisons/mcp-vs-function-calling
- Updated: entities/anthropic (added new sources), concepts/multi-agent-systems (added A2A and workflow patterns)
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md, log.md

## [2026-04-05] research | AI product design, LLM-powered product UX, and human-AI collaboration interfaces for knowledge work
- Motivation: Karpathy said "there is room here for an incredible new product" — this research explores what that product looks like from a design perspective
- Searched 11 queries: AI product design patterns, human-AI collaboration interface, LLM UX best practices, AI copilot design patterns, conversational vs structured UI, AI transparency/explainability UX, knowledge management AI product design, Notion AI vs Obsidian AI, AI-native applications design, progressive disclosure AI complexity, trust calibration human-AI
- Fetched 10 sources:
  - shapeof-ai-ux-patterns (shapeof.ai — 57 AI UX patterns taxonomy)
  - zhuo-conversational-interfaces (Julie Zhuo Substack — five problems with chat UI)
  - smashing-practical-xai-ux (Smashing Magazine — practical XAI for UX)
  - microsoft-copilot-ux-guidance (Microsoft Learn — copilot UX guidance)
  - sapphire-ai-native-applications (Sapphire Ventures — 5-D AI-native framework)
  - uxforai-12-llm-product-practices (UX for AI — 12 LLM product practices)
  - schmidt-designing-human-ai-collaboration (Schema Design Studio — 5 principles)
  - arxiv-interface-design-human-ai-decisions (arXiv 2501.16627 — engagement-overload paradox)
  - progressive-disclosure-ai-pattern (AI UX Design Guide — progressive disclosure)
  - projects-by-if-copilot-pattern (Projects by IF — copilot design pattern)
- Ingested 9 raw files to raw/
- Created 9 source summaries in wiki/sources/
- Created 13 new concept articles: ai-ux-design-patterns, copilot-pattern, conversational-ui-vs-structured-ui, blank-page-problem, trust-in-ai, trust-calibration, human-ai-collaboration-design, progressive-disclosure-ai, explainable-ai-ux, personalization-in-ai, ai-native-design, collaborative-ux, llm-product-development
- Created 5 new entity pages: julie-zhuo, figma, hax-toolkit, sapphire-ventures, shape-of-ai
- Created 1 comparison: conversational-vs-structured-vs-hybrid-ai-ui
- Updated 2 existing articles: knowledge-base-product-gap (added product design specifications section), human-in-the-loop (added UX patterns for HITL section)
- Updated: _meta/summaries.md, _meta/manifest.md, log.md
- Key findings:
  1. Chat interfaces get to 70% but fail at refinement — hybrid UI (conversation + structured controls) is the winning pattern
  2. Trust, not attention, is the true currency of AI products (Schmidt)
  3. More explanation can paradoxically HARM performance — the engagement-overload paradox requires progressive disclosure (2-3 layers max)
  4. 57 named AI UX patterns now cataloged across 6 categories (Shape of AI)
  5. AI-native products are evaluated across 5 dimensions: Design, Data, Domain Expertise, Dynamism, Distribution
  6. The "incredible new product" Karpathy envisions should be: Immersive focus (full-screen KB), hybrid UI, Wayfinder onboarding, trust-by-design with citations and progressive disclosure, personalization of how (not just what), and customer-as-trainer feedback loop

## [2026-04-05] research | PKM, Zettelkasten, Second Brain Methodologies, and AI/LLM Transformation

Deep research pass on Personal Knowledge Management (PKM), Zettelkasten, second brain methodologies, and how AI/LLMs are transforming them.

### Web Searches Performed (12)
- Zettelkasten method digital tools 2025 2026
- Second brain Tiago Forte building methodology CODE PARA
- Personal knowledge management AI LLM transformation 2025
- Obsidian vs Notion vs Logseq knowledge management comparison
- Evergreen notes Andy Matuschak networked thought
- PKM automation AI agents note-taking 2025 2026
- Roam Research bidirectional linking knowledge graph
- Digital garden philosophy public notes knowledge sharing
- Spaced repetition knowledge management Anki learning
- Memex Vannevar Bush "As We May Think" 1945
- Niklas Luhmann Zettelkasten sociology slip box original method
- Progressive summarization Tiago Forte layers highlighting technique

### Sources Ingested (10 raw files)
1. `raw/forte-building-second-brain.md` — Tiago Forte's BASB: CODE, PARA, Progressive Summarization
2. `raw/matuschak-evergreen-notes.md` — Andy Matuschak's five principles for evergreen notes
3. `raw/appleton-digital-garden-history.md` — Maggie Appleton's digital garden history and six patterns
4. `raw/sebastien-agentic-knowledge-management.md` — Sebastien Dubois on Agentic KM
5. `raw/zettelkasten-de-introduction.md` — Canonical Zettelkasten method guide
6. `raw/luhmann-original-zettelkasten.md` — Luhmann's actual system vs modern interpretations
7. `raw/memex-vannevar-bush.md` — Bush's 1945 memex and its influence chain
8. `raw/pkm-tools-comparison-2026.md` — Obsidian vs Logseq vs Notion 2026 benchmarks
9. `raw/llms-for-knowledge-work-arxiv.md` — arXiv longitudinal study on LLM adoption
10. `raw/spaced-repetition-knowledge-management.md` — Spaced repetition and Anki integration with PKM

### Wiki Pages Created/Updated

**Source Summaries (10 new):**
- wiki/sources/forte-building-second-brain.md
- wiki/sources/matuschak-evergreen-notes.md
- wiki/sources/appleton-digital-garden-history.md
- wiki/sources/sebastien-agentic-knowledge-management.md
- wiki/sources/zettelkasten-de-introduction.md
- wiki/sources/luhmann-original-zettelkasten.md
- wiki/sources/memex-vannevar-bush.md
- wiki/sources/pkm-tools-comparison-2026.md
- wiki/sources/llms-for-knowledge-work-arxiv.md
- wiki/sources/spaced-repetition-knowledge-management.md

**Concept Articles (10 new):**
- wiki/concepts/zettelkasten.md — comprehensive article with Luhmann's original vs modern, digital implementation, comparison table
- wiki/concepts/evergreen-notes.md — Matuschak's five principles, relationship to Zettelkasten and SRS
- wiki/concepts/networked-thought.md — 80-year arc from Bush through Luhmann to modern tools
- wiki/concepts/digital-garden.md — six patterns, Garden vs Stream, key figures
- wiki/concepts/progressive-summarization.md — four-layer distillation technique
- wiki/concepts/para-method.md — actionability-based organization vs topic-based
- wiki/concepts/memex-and-tools-for-thought.md — Bush-Engelbart-Nelson-Web lineage
- wiki/concepts/spaced-repetition.md — forgetting curve, Anki, PKM integration
- wiki/concepts/learning-in-public.md — epistemic status markers, garden philosophy
- wiki/concepts/agentic-knowledge-management.md — proactive AI agents in PKM, Digital Twin concept

**Entity Pages (8 new):**
- wiki/entities/niklas-luhmann.md
- wiki/entities/tiago-forte.md
- wiki/entities/andy-matuschak.md
- wiki/entities/maggie-appleton.md
- wiki/entities/anki.md
- wiki/entities/roam-research.md
- wiki/entities/logseq.md
- wiki/entities/vannevar-bush.md (updated with influence chain)

**Comparison Pages (3 new):**
- wiki/comparisons/zettelkasten-vs-basb.md — philosophy, structure, when to use each
- wiki/comparisons/obsidian-vs-logseq-vs-notion.md — 2026 feature/performance comparison
- wiki/comparisons/manual-vs-ai-pkm.md — four-stage PKM evolution with tradeoffs

**Updated Existing Pages:**
- wiki/concepts/personal-knowledge-management.md — added full methodology landscape section
- wiki/concepts/second-brain.md — added Forte source and new cross-references
- wiki/entities/obsidian.md — added new sources and PKM-related cross-references
- wiki/entities/notion.md — added new sources and cross-references
- wiki/entities/vannevar-bush.md — added influence chain section
- wiki/_index.md — added all new entries
- wiki/_meta/summaries.md — added all new summaries
- wiki/_meta/manifest.md — added all 10 new raw files

### Key Findings
- PKM has an 80-year intellectual lineage from Bush's memex (1945) through Luhmann's Zettelkasten to modern AI-maintained systems
- Modern popular understanding of Zettelkasten (fleeting/literature/permanent notes) differs significantly from Luhmann's actual practice
- The four stages of PKM evolution: manual → AI-assisted → AI-maintained → agentic
- Agentic Knowledge Management (2025-2026) represents the frontier: AI agents proactively monitoring and acting on knowledge bases
- Trust remains the key barrier to AI adoption in knowledge work (70% want automation, but significant quality and hallucination concerns)
- The Zettelkasten and BASB methodologies are complementary: Zettelkasten for insight generation, BASB for creative output

## [2026-04-05] research | Collective intelligence, collaborative knowledge building, Wikipedia-style systems, AI transformation of group knowledge creation
- Searched: "collective intelligence AI knowledge building", "Wikipedia knowledge creation process", "collaborative knowledge graphs", "wisdom of crowds AI aggregation", "knowledge commons digital", "semantic web linked data Wikidata", "federated knowledge bases decentralized wiki", "AI Wikipedia automated editing", "knowledge synthesis LLM sensemaking", "epistemic commons AI", "crowdsourced vs AI knowledge", "Collective Intelligence Project CIP"
- Fetched and ingested 10 sources:
  - Brookings: AI changing physics of collective intelligence (Taylor, Page)
  - CIP Whitepaper: collective intelligence for AI governance (Siddarth, Huang)
  - Wiki Education: AI Wikipedia editing audit 2025 (Davis)
  - Wikipedia: AI in Wikimedia projects (comprehensive history)
  - CIP: Generative AI and digital commons (Huang, Siddarth)
  - COHUMAIN: Collective intelligence in human-AI collaboration (Gupta, Gonzalez, Woolley)
  - Reeves & Simperl: Systematic review of automated Wikipedia content generation
  - Federated Wiki: Ward Cunningham's forking-based collaborative knowledge
  - Wisdom of the Crowd: comprehensive overview (Galton, Surowiecki, Page)
  - Knowledge Commons: Hess/Ostrom governance framework
- Created 10 source summaries, 11 concept articles, 5 entity pages, 1 comparison page
- New concepts: collective-intelligence, wisdom-of-crowds, wikipedia-knowledge-model, collaborative-knowledge-building, knowledge-commons, human-ai-collaboration, federated-knowledge, ai-generated-content-risks, ai-alignment-democratic, transactive-memory-systems, digital-commons-governance
- New entities: collective-intelligence-project, ward-cunningham, wikipedia, wikidata, elinor-ostrom
- New comparison: consensus-vs-federated-vs-ai-knowledge
- Updated existing: entities/anthropic (added CIP partnership), concepts/automated-wiki-creation (added cross-links)
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md

## [2026-04-05] research | Obsidian as a Knowledge Platform — Deep Research Pass
- Searched: 13 queries covering plugins, Dataview, graph view, AI plugins, Canvas, Templater, community workflows, PKM comparison, digital gardens, API/plugin dev, YAML properties, vault organization, Steph Ango philosophy
- Fetched: 10 web sources (dsebastien plugins guide, stephango file-over-app, stephango vault, nxcode AI second brain, systemsculpt AI plugins, obsidian copilot, stephango dialectic interview, pkm comparison 2026, digital garden docs, capacities comparison)
- Ingested 8 new raw files: dsebastien-obsidian-plugins-2026, stephango-file-over-app, stephango-vault-organization, stephango-dialectic-interview, nxcode-obsidian-ai-second-brain-2026, systemsculpt-obsidian-ai-plugins-2026, obsidian-copilot-overview, pkm-comparison-obsidian-notion-logseq
- Created 8 new source summaries
- Created 7 new concept articles: obsidian-plugin-ecosystem, obsidian-ai-integration, vault-organization, obsidian-frontmatter-properties, obsidian-graph-view, obsidian-canvas, (digital-garden updated)
- Created 4 new entity pages: obsidian-copilot, smart-connections, templater, excalidraw
- Updated 6 existing pages: entities/obsidian (major expansion with stats, philosophy, plugins, AI), entities/steph-ango (company principles, vault workflow, design philosophy), entities/dataview (query types, ecosystem position), entities/logseq (2026 developments), concepts/obsidian-as-ide (two AI modes, plugin details), concepts/file-over-app (civilizational stance, broader influence), concepts/digital-garden (Obsidian publishing methods), comparisons/obsidian-vs-logseq-vs-notion (2025-2026 developments, pricing, philosophy)
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md, _meta/links.md (pending)

## [2026-04-05] research | History of AI knowledge representation
- Topic: From expert systems and symbolic AI through neural networks to modern LLMs — the evolution of machine knowledge
- Searched: 11 web queries covering KR history, expert systems, symbolic vs connectionist, Cyc, Semantic Web, Bush/Memex, Nelson/Xanadu, Engelbart, neural KR, LLM-enhanced KRL, LLMs as KBs
- Fetched and ingested 10 sources:
  - Wikipedia: Knowledge Representation & Reasoning, Expert Systems, Symbolic AI, Cyc, As We May Think, Project Xanadu, Semantic Web
  - Outsider Art: "Cyc: History's Forgotten AI Project"
  - arXiv: LLM-Enhanced Knowledge Representation Learning Survey (2024)
  - arXiv: Large Language Models as Reliable Knowledge Bases? (2024)
- Created 10 source summaries in wiki/sources/
- Created 11 new concept articles: knowledge-representation, expert-systems, symbolic-ai, symbolic-vs-connectionist, neural-symbolic-integration, ontology, semantic-web, memex, hypertext, transclusion, llms-as-knowledge-bases
- Created 7 new entity pages: douglas-engelbart, ted-nelson, john-mccarthy, marvin-minsky, edward-feigenbaum, doug-lenat, cyc-project
- Updated 1 existing entity: vannevar-bush (added new source)
- Created 1 comparison: symbolic-vs-neural-knowledge-representation
- Updated: _index.md, _meta/summaries.md, _meta/manifest.md
- Total new wiki pages: 29 (10 sources + 11 concepts + 7 entities + 1 comparison)

## [2026-04-05] research | LLM reasoning capabilities — chain-of-thought, tree-of-thought, mathematical reasoning, and the nature of LLM intelligence
- Searched 12 queries: chain of thought reasoning LLM, tree of thoughts LLM, LLM mathematical reasoning, reasoning models o1 o3, Claude extended thinking, self-consistency majority voting, LLM logical reasoning limitations, process reward models, test time compute scaling, can LLMs truly reason stochastic parrots, emergent abilities LLMs, System 1 System 2 thinking LLM
- Fetched 12 sources from: arXiv (6 papers), Anthropic blog, Adaline Labs, Kili Technology, Sebastian Raschka, Le Wagon, Georgetown CSET
- Ingested 11 raw files:
  - wei-chain-of-thought-prompting (Wei et al. 2022, foundational CoT paper)
  - yao-tree-of-thoughts (Yao et al. NeurIPS 2023, ToT framework)
  - mirzadeh-gsm-symbolic (Mirzadeh et al. ICLR 2025, math reasoning fragility)
  - snell-test-time-compute-scaling (Snell et al. 2024, test-time compute)
  - lightman-lets-verify-step-by-step (OpenAI 2023, process reward models)
  - song-llm-reasoning-failures-survey (Song et al. TMLR 2026, failure taxonomy)
  - wei-emergent-abilities (Wei et al. TMLR 2022, emergent abilities)
  - li-system1-system2-reasoning-survey (Li et al. 2025, dual-process reasoning)
  - anthropic-extended-thinking (Anthropic 2025, Claude extended thinking)
  - adaline-inside-reasoning-models (Adaline Labs 2025, o3 vs R1 deep-dive)
  - raschka-state-of-reasoning-inference (Raschka 2025, inference scaling survey)
- Created 11 source summaries in wiki/sources/
- Created 13 concept articles: llm-reasoning, chain-of-thought, tree-of-thought, reasoning-models, test-time-compute, process-reward-models, self-consistency, llm-reasoning-limitations, mathematical-reasoning-llm, emergent-abilities, stochastic-parrot-debate, system-1-system-2-thinking, reinforcement-learning-for-reasoning
- Created 2 entity pages: jason-wei, openai
- Updated 3 entity pages: deepseek (R1 training details), anthropic (extended thinking source), claude (extended thinking section)
- Created 2 comparison pages: o3-vs-r1-vs-claude-reasoning, process-vs-outcome-supervision
- Updated 1 comparison page: cot-vs-tot-vs-self-consistency (added reasoning model context and new sources)
- Updated: _index.md, summaries.md, manifest.md, log.md

## [2026-04-05] research | LLM training data, dataset curation, data quality, and role of data in AI performance
- Ran 13 web searches covering: training data curation, Common Crawl preprocessing, data quality vs model size scaling, DCLM, FineWeb, data deduplication, benchmark contamination, synthetic data in pretraining, instruction tuning datasets, RLHF preference data, multilingual data, copyright and training data, Nemotron-CC
- Fetched and ingested 10 sources:
  - DCLM paper (arxiv.org) — dataset benchmark and model-based filtering
  - FineWeb dataset (HuggingFace + Kili Technology) — per-dump dedup discovery
  - Nemotron-CC paper (arxiv.org) — classifier ensembling and synthetic augmentation
  - Scaling Laws Revisited paper (arxiv.org) — quality-aware scaling law L(N,D,Q)
  - Synthetic Data in Pretraining paper (arxiv.org) — 30/70 optimal mixture
  - Data Deduplication at Trillion Scale (Zilliz) — MinHash LSH practical guide
  - RLHF Book preference data chapter (rlhfbook.com) — on-policy data, collection complexity
  - Benchmark contamination analysis (Medium) — fidelity-resistance tradeoff
  - Multilingual LLMs survey (PremAI) — low-resource language challenges
  - Copyright litigation overview (Morrison Foerster) — 2025 fair use rulings
  - Nebius data preparation guide — end-to-end pipeline
- Created 11 raw files, 11 source summaries, 10 concept articles, 8 entity pages, 2 comparison pages
- Updated 3 existing concept articles (data-quality-bottleneck, synthetic-data-generation, rlhf) with new source references
- Updated index, summaries, manifest, log
- Key findings:
  - Model-based filtering (fastText classifiers) is the single most impactful data curation technique
  - Quality-aware scaling law: L(N,D,Q) = A/N^alpha + B/(D^beta * Q^gamma) + E
  - 30% rephrased synthetic + 70% natural web text is the optimal pretraining mixture
  - Per-dump deduplication outperforms cross-dump deduplication
  - Benchmark contamination has an unsolvable fidelity-resistance tradeoff
  - On-policy preference data dramatically outperforms off-policy for RLHF
  - Copyright litigation expected to peak in 2026 with OpenAI/Google cases

## [2026-04-05] research | Scaling knowledge systems -- personal to enterprise

- **Topic**: Scaling knowledge systems from personal wikis to team/enterprise knowledge bases, and the infrastructure needed
- **Searches**: 11 web searches covering enterprise KM trends, AI knowledge bases, platform comparisons, scaling challenges, distributed systems, enterprise search, KM ROI, team wiki patterns, knowledge silos, information architecture, enterprise knowledge graphs
- **Sources fetched and ingested**: 11 new raw files
  - `raw/ek-km-trends-2026.md` -- Enterprise Knowledge 2026 KM trends
  - `raw/glean-enterprise-search-guide.md` -- Glean AI enterprise search guide
  - `raw/helpjuice-km-challenges.md` -- KM challenges inventory
  - `raw/eesel-confluence-notion-sharepoint.md` -- Platform comparison (Confluence/Notion/SharePoint)
  - `raw/ksa-knowledge-system-scalability.md` -- Knowledge system scalability framework
  - `raw/ek-taxonomy-ia-semantic-layer.md` -- Taxonomy and IA for semantic layers
  - `raw/branzan-production-knowledge-graphs-2025.md` -- Production KG systems guide
  - `raw/keerok-enterprise-rag-2026.md` -- Enterprise RAG deployment guide
  - `raw/cio-knowledge-graphs-enterprise-ai.md` -- KGs as enterprise AI missing link
  - `raw/glean-knowledge-silos-unified-search.md` -- Knowledge silos and unified search
  - `raw/earley-ontology-ia-role-in-ai.md` -- Ontology and IA role in AI
- **Wiki pages created**: 32 new pages
  - 11 source summaries (sources/)
  - 10 concept articles (concepts/): enterprise-knowledge-management, knowledge-system-scaling, knowledge-silos, enterprise-search, semantic-layer, ontology-and-taxonomy, information-architecture, knowledge-governance, tacit-knowledge-capture, knowledge-management-challenges
  - 7 entity pages (entities/): glean, confluence, sharepoint, enterprise-knowledge, falkordb, cognee, novartis
  - 1 comparison: personal-vs-enterprise-knowledge-systems
- **Wiki pages updated**: 3
  - concepts/knowledge-graph -- added enterprise deployment section with production tools and benchmarks
  - entities/notion -- added enterprise evolution section (AI Agent, Enterprise Search, 100M+ users)
  - _index.md, _meta/summaries.md, _meta/manifest.md

## [2026-04-05] research | LLM Pretraining — How Large Language Models Are Trained from Scratch
- **Topic**: LLM pretraining process, training infrastructure, distributed training, compute requirements, scaling laws
- **Searches**: 12 web searches covering pretraining pipeline, distributed parallelism, GPU clusters, training costs, DeepSpeed/Megatron, learning rate schedules, training stability, loss spikes, data pipelines, Chinchilla scaling, and famous training runs
- **Sources fetched**: 10 URLs via WebFetch (MLOps Community, Jeremy Jordan, Life Architect/Chinchilla, arXiv/Spike No More, Local AI Master/costs, Rohan Paul/stability, APXML/frameworks, Sebastian Raschka/paradigms, Analytics Vidhya/guide, InfoQ/HF playbook)
- **Raw files created**: 10
  - raw/mlops-pretraining-pipeline.md
  - raw/jeremy-jordan-distributed-training.md
  - raw/chinchilla-scaling-laws-explained.md
  - raw/spike-no-more-training-stability.md
  - raw/training-costs-2026-analysis.md
  - raw/rohan-paul-stabilizing-llm-training.md
  - raw/deepspeed-megatron-frameworks.md
  - raw/raschka-pretraining-post-training-paradigms.md
  - raw/analyticsvidhya-llm-pretraining-guide.md
  - raw/hf-ultrascale-playbook.md
- **Source summaries created**: 10
  - sources/mlops-pretraining-pipeline, sources/jeremy-jordan-distributed-training, sources/chinchilla-scaling-laws-explained, sources/spike-no-more-training-stability, sources/training-costs-2026-analysis, sources/rohan-paul-stabilizing-llm-training, sources/deepspeed-megatron-frameworks, sources/raschka-pretraining-post-training-paradigms, sources/analyticsvidhya-llm-pretraining-guide, sources/hf-ultrascale-playbook
- **Concept articles created**: 18
  - concepts/llm-pretraining, concepts/distributed-training, concepts/data-parallelism, concepts/tensor-parallelism, concepts/pipeline-parallelism, concepts/3d-parallelism, concepts/5d-parallelism, concepts/chinchilla-scaling-laws, concepts/compute-optimal-training, concepts/training-stability, concepts/loss-spikes, concepts/learning-rate-schedules, concepts/mixed-precision-training, concepts/zero-optimizer, concepts/next-token-prediction, concepts/pretraining-data-pipeline, concepts/multi-stage-pretraining, concepts/llm-training-costs
- **Entity pages created**: 3
  - entities/deepspeed, entities/megatron-lm, entities/deepseek-v3
- **Entity pages updated**: 3
  - entities/chinchilla (added new source + pretraining links)
  - entities/fineweb (added pretraining pipeline links)
  - entities/llama (added pretraining/distributed training sources and links)
- **Comparison pages created**: 2
  - comparisons/deepspeed-vs-megatron-lm, comparisons/compute-optimal-vs-inference-optimal
- **Existing pages updated**: 1
  - concepts/tokenization (added pretraining-related links)
- **Metadata updated**: _index.md, _meta/summaries.md, _meta/manifest.md, log.md
- **Total new wiki pages**: 33 (10 sources + 18 concepts + 3 entities + 2 comparisons)

## [2026-04-05] research | RLHF, Constitutional AI, DPO, and LLM Alignment Techniques
- Deep research pass on aligning LLMs with human preferences
- Ran 11 web searches covering: RLHF explained, DPO, Constitutional AI, RLHF alternatives (DPO/KTO/IPO), reward models, preference data collection, instruction tuning vs RLHF, AI alignment techniques, RLAIF, PPO vs DPO, reward hacking/overoptimization
- Fetched 10 high-quality web sources from HuggingFace, Cameron Wolfe (Deep Learning Focus), Anthropic, Argilla/MantisNLP, Lilian Weng (Lil'Log), arXiv
- **Raw files ingested** (9):
  - huggingface-rlhf-illustrated (foundational RLHF tutorial)
  - wolfe-direct-preference-optimization (DPO mathematical derivation)
  - anthropic-constitutional-ai (Constitutional AI paper)
  - argilla-rlhf-alternatives-overview (9+ method comparison)
  - wolfe-reward-models-llm (reward model architecture and best practices)
  - wolfe-rlaif-reinforcement-learning-ai-feedback (RLAIF technical overview)
  - lilianweng-reward-hacking (reward hacking taxonomy)
  - dpo-vs-ppo-comprehensive-study (PPO vs DPO empirical comparison)
  - argilla-kto-kahneman-tversky (KTO prospect theory alignment)
- **Source summaries created** (9): one per raw file
- **Concept articles created** (12): rlhf, dpo, rlaif, reward-model, reward-hacking, ppo-for-llms, kto, bradley-terry-model, sycophancy, orpo, ipo, process-reward-model
- **Concept articles updated** (5): constitutional-ai (major expansion), preference-data (method comparison table), instruction-tuning (pipeline context), scalable-oversight (RLHF links), ai-alignment (RLHF links)
- **Entity pages created** (4): instructgpt, cameron-wolfe, lilian-weng, trl
- **Comparison pages created** (2): ppo-vs-dpo, rlhf-alternatives
- **Comparison pages updated** (1): rlhf-vs-constitutional-ai (added new sources)
- **Metadata updated**: _index.md, _meta/summaries.md, _meta/manifest.md, log.md
- **Total new wiki pages**: 27 (9 sources + 12 concepts + 4 entities + 2 comparisons)

## [2026-04-05] research | Transformer architecture, attention mechanisms, and LLM architecture evolution

- **Topic**: Deep research on transformer architecture fundamentals — the models powering the KB system itself
- **Searches**: 14 web searches covering:
  - Transformer architecture and "Attention Is All You Need"
  - Self-attention, multi-head attention mechanisms
  - Transformer variants (GPT, BERT, T5 comparison)
  - Mixture of Experts (MoE) architecture and 2025 models
  - State space models (Mamba, S4) vs transformers
  - FlashAttention-3 efficient attention
  - Chinchilla scaling laws
  - KV cache optimization techniques
  - Rotary Position Embeddings (RoPE)
  - Speculative decoding inference optimization
  - Multimodal transformers and VLMs 2025
  - Sparse attention and linear attention alternatives
  - Grouped-Query Attention (GQA)
  - Transformer architecture improvements 2025-2026
- **Sources fetched and ingested**: 11 raw files
  - `raw/illustrated-transformer-jalammar.md` — Jay Alammar's visual Transformer walkthrough
  - `raw/raschka-self-attention-coding.md` — Sebastian Raschka's attention variants with code
  - `raw/huggingface-mixture-of-experts.md` — Comprehensive MoE guide from Hugging Face
  - `raw/mamba-state-space-models-visual-guide.md` — Maarten Grootendorst's Mamba visual guide
  - `raw/flashattention-3-paper.md` — Tri Dao's FlashAttention-3 paper
  - `raw/eleutherai-rotary-embeddings.md` — EleutherAI's RoPE technical deep dive
  - `raw/kv-cache-optimization-techniques.md` — Omri Mallis KV cache optimization (already existed, updated)
  - `raw/speculative-decoding-bentoml.md` — BentoML speculative decoding guide
  - `raw/ssm-vs-transformers-tradeoffs.md` — Goomba Lab SSM vs Transformer analysis
  - `raw/vlms-2025-huggingface.md` — Hugging Face VLM survey 2025
  - `raw/chinchilla-scaling-laws.md` — DeepMind Chinchilla scaling law paper
  - `raw/unite-ai-bert-gpt-t5-comparison.md` — BERT/GPT/T5 comparison
  - `raw/moe-models-comparison-2025.md` — 2025 MoE model comparison
- **Wiki pages created**: 38 new pages
  - 12 source summaries (sources/)
  - 15 concept articles (concepts/): transformer-architecture, self-attention, multi-head-attention, causal-attention, cross-attention, positional-encoding, rotary-position-embeddings, flash-attention, state-space-models, mamba, selective-state-space, grouped-query-attention, sliding-window-attention, paged-attention, sparse-attention, multimodal-transformers
  - 8 entity pages (entities/): attention-is-all-you-need, bert, gpt, t5, switch-transformer, mixtral, tri-dao
  - 3 comparison pages: transformers-vs-state-space-models, encoder-only-vs-decoder-only-vs-encoder-decoder, dense-vs-moe-transformers
- **Wiki pages updated**: 5
  - concepts/mixture-of-experts — added architecture deep dive, routing strategies, load balancing
  - concepts/scaling-laws — added Chinchilla source and transformer-architecture link
  - concepts/kv-cache — added links to GQA, sliding window, paged attention, speculative decoding
  - concepts/speculative-decoding — added new source and transformer architecture links
  - entities/chinchilla — added Chinchilla scaling laws source
- **Metadata updated**: _index.md, _meta/summaries.md, _meta/manifest.md, _meta/links.md, log.md

## [2026-04-05] research | Claude by Anthropic — architecture, capabilities, constitutional AI, safety, model family evolution
- **Scope**: Deep research pass on Claude/Anthropic for the KB system's self-understanding
- **Web searches**: 14 searches across model family, capabilities, safety, comparisons, founding, API
- **Sources fetched and ingested** (9 raw files):
  - raw/wikipedia-claude-language-model.md — Wikipedia article on Claude model family
  - raw/wikipedia-anthropic.md — Wikipedia article on Anthropic company
  - raw/anthropic-claude-models-overview.md — Official API model documentation
  - raw/anthropic-rsp-v3.md — Responsible Scaling Policy v3.0
  - raw/anthropic-extended-thinking-docs.md — Extended thinking API reference
  - raw/anthropic-claude-3-family-announcement.md — Claude 3 launch announcement
  - raw/anthropic-claude-4-announcement.md — Claude 4 launch announcement
  - raw/dario-amodei-machines-of-loving-grace.md — Dario Amodei's vision essay
  - raw/improvado-claude-vs-chatgpt-vs-gemini-2026.md — 2026 frontier model comparison
- **Source summaries created** (9):
  - sources/wikipedia-claude-language-model, sources/wikipedia-anthropic
  - sources/anthropic-claude-models-overview, sources/anthropic-rsp-v3
  - sources/anthropic-extended-thinking-docs, sources/anthropic-claude-3-family-announcement
  - sources/anthropic-claude-4-announcement, sources/dario-amodei-machines-of-loving-grace
  - sources/improvado-claude-vs-chatgpt-vs-gemini-2026
- **Concept articles created** (3):
  - concepts/claude-model-family-evolution — 17-release timeline, context/output/pricing trends
  - concepts/extended-thinking — manual to adaptive thinking evolution, interleaved reasoning
  - concepts/responsible-scaling-policy — ASL framework, defense-in-depth, industry impact
- **Entity pages created** (2):
  - entities/dario-amodei — CEO, "Machines of Loving Grace" essay
  - entities/daniela-amodei — President, operational growth
- **Entity pages updated** (2):
  - entities/claude — expanded from prompting tips to full model family coverage with benchmarks, release history, pricing
  - entities/anthropic — added founding details, RSP section, valuation history, Machines of Loving Grace
- **Comparison articles created** (1):
  - comparisons/claude-vs-gpt-vs-gemini — 2026 multi-model landscape
- **Metadata updated**: _index.md, _meta/summaries.md, _meta/manifest.md, log.md

## [2026-04-05] research | Andrej Karpathy deep profile — career, philosophy, and influence
- **Scope**: Deep research on Karpathy's full contributions, from Tesla Autopilot to AI education to the LLM wiki methodology
- **Web searches**: 16 queries covering biography, Software 2.0, Tesla, OpenAI, YouTube education, minbpe, nanoGPT, micrograd, Eureka Labs, vibe coding, LLM OS, State of GPT, Recipe for Training NNs, llm.c, CS231n, context engineering
- **Web fetches**: 10 pages fetched (Wikipedia biography, Software 2.0 essay, Recipe blog post, vibe coding Wikipedia, Zero to Hero page, llm.c README, 2025 Year in Review, Klover profile, LLM OS blog, Software 3.0 article)
- **Raw files ingested** (8 new):
  - raw/karpathy-wikipedia-biography.md
  - raw/karpathy-recipe-training-neural-networks.md
  - raw/karpathy-vibe-coding.md
  - raw/karpathy-2025-llm-year-review.md
  - raw/karpathy-llm-os-concept.md
  - raw/karpathy-eureka-labs.md
  - raw/karpathy-state-of-gpt.md
  - raw/karpathy-educational-projects.md
- **Source summaries created** (8 new):
  - sources/karpathy-wikipedia-biography
  - sources/karpathy-recipe-training-neural-networks
  - sources/karpathy-vibe-coding
  - sources/karpathy-2025-llm-year-review
  - sources/karpathy-llm-os-concept
  - sources/karpathy-eureka-labs
  - sources/karpathy-state-of-gpt
  - sources/karpathy-educational-projects
- **Concept articles created** (2 new):
  - concepts/llm-os — LLM as operating system kernel
  - concepts/ai-native-education — Teacher + AI Teaching Assistant symbiosis
- **Concept articles updated** (3):
  - concepts/software-2-0 — added LLM OS and 2025 review sources
  - concepts/vibe-coding — added Karpathy-specific sources
  - concepts/context-engineering — added 2025 review source
- **Entity pages created** (6 new):
  - entities/eureka-labs — AI-native education company
  - entities/micrograd — 100-line autograd engine
  - entities/nanogpt — GPT training repository
  - entities/llm-c — C/CUDA LLM training
  - entities/fei-fei-li — Karpathy's PhD advisor
  - entities/tesla — Karpathy's employer 2017-2022
- **Entity pages updated** (2):
  - entities/andrej-karpathy — MAJOR expansion: from 3-min to 12-min read, full biography, career timeline, intellectual contributions (Software 2.0, LLM OS, vibe coding, context engineering, Recipe for Training NNs, State of GPT, LLM KB), open-source projects table, educational arc, notable quotes, 15 source references
  - entities/minbpe — added educational projects source and related links
- **Metadata updated**: _index.md, _meta/summaries.md, _meta/manifest.md, log.md

## [2026-04-05] research | AI Code Generation & the Code-to-Knowledge Shift
- **Topic**: Deep research pass on AI code generation, automated software engineering, and how LLMs are transforming programming — the Software 2.0 → vibe coding → agentic engineering arc Karpathy described
- **Web searches**: 11 queries covering AI code generation state of art, LLM software engineering, SWE-bench benchmarks, vibe coding, code LLM model comparisons, AI pair programming productivity, automated testing, natural language to code, LLM debugging, future of programming, and Software 2.0
- **Sources fetched and ingested** (8 raw files):
  - raw/karpathy-software-2-0.md — foundational 2017 Software 2.0 essay
  - raw/wikipedia-vibe-coding.md — comprehensive vibe coding history and evolution
  - raw/greptile-state-of-ai-coding-2025.md — telemetry data on AI coding adoption
  - raw/morphllm-coding-models-comparison-2026.md — March 2026 model benchmarks
  - raw/morphllm-codex-vs-claude-code.md — Codex vs Claude Code comparison
  - raw/osmani-ai-productivity-reality.md — meta-analysis of AI coding productivity research
  - raw/swe-bench-leaderboard-2026.md — SWE-bench evolution and leaderboard
  - raw/osmani-llm-coding-workflow-addendum.md — practical AI coding workflow guide
- **Source summaries created** (8):
  - sources/karpathy-software-2-0, sources/wikipedia-vibe-coding, sources/greptile-state-of-ai-coding-2025
  - sources/morphllm-coding-models-comparison-2026, sources/morphllm-codex-vs-claude-code
  - sources/osmani-ai-productivity-reality, sources/swe-bench-leaderboard-2026, sources/osmani-llm-coding-workflow-addendum
- **Concept articles created** (5):
  - concepts/software-2-0 — Karpathy's 2017 paradigm, three-stage arc, code-to-knowledge shift
  - concepts/vibe-coding — February 2025 origin, quality evidence, evolution to agentic engineering
  - concepts/ai-code-generation — comprehensive landscape, benchmark table, scaffold insight, productivity evidence
  - concepts/natural-language-programming — spec-driven development, the specification spectrum
  - concepts/automated-testing-for-ai-code — agentic testing, self-healing, AI-on-AI review
- **Entity pages created** (3):
  - entities/openai-codex — OpenAI's agentic coding tool with benchmarks
  - entities/codestral — Mistral's open-weight coding model
  - entities/swe-bench — benchmark entity page with timeline and variants
- **Entity pages updated** (2):
  - entities/andrej-karpathy — added links to new concepts and sources
  - entities/addy-osmani — added productivity reality and workflow sources
- **Comparison pages created** (2):
  - comparisons/codex-vs-claude-code — speed vs depth, sandbox vs multi-agent
  - comparisons/vibe-coding-vs-agentic-engineering — maturation arc from hype to production
- **Existing concept articles updated** (3):
  - concepts/post-code-ai-workflow — added Software 2.0 lineage, productivity evidence, cross-links
  - concepts/swe-bench — added scaffold finding, open-source convergence, new sources
  - concepts/agentic-coding — added new sources and cross-links to vibe coding, Software 2.0, comparisons
- **Metadata updated**: _index.md, _meta/summaries.md, _meta/manifest.md, log.md

## [2026-04-05] research | Web scraping, content extraction, and HTML-to-markdown conversion
- **Topic**: Web scraping, content extraction, and converting messy web into clean structured data for knowledge bases
- **Searches performed** (12): web scraping best practices 2025/2026, readability algorithm content extraction, trafilatura web content extraction, beautiful soup vs playwright, headless browser scraping, HTML to markdown conversion tools, web scraping ethics robots.txt, structured data extraction schema.org, Jina AI reader API, web archiving preservation tools, crawl4ai open source web crawler, firecrawl web scraping API
- **Sources fetched and ingested** (9):
  - raw/web-scraping-best-practices-2026.md (ScraperAPI comprehensive guide)
  - raw/mozilla-readability-algorithm.md (WebcrawlerAPI Readability.js deep dive)
  - raw/trafilatura-web-extraction.md (GitHub + docs for Trafilatura library)
  - raw/jina-reader-lm-html-to-markdown.md (Jina AI Reader-LM v1 + v2 articles)
  - raw/crawl4ai-llm-web-crawler.md (GitHub README for Crawl4AI)
  - raw/web-scraping-legality-ethics-2025.md (Browserless legal analysis)
  - raw/python-scraping-tools-comparison.md (DasRoot BS4 vs Scrapy vs Playwright)
  - raw/schema-org-structured-data.md (Schema.org getting started guide)
  - raw/web-archiving-warc-tools.md (IIPC awesome-web-archiving)
- **Source summaries created** (9): sources/web-scraping-best-practices-2026, sources/mozilla-readability-algorithm, sources/trafilatura-web-extraction, sources/jina-reader-lm-html-to-markdown, sources/crawl4ai-llm-web-crawler, sources/web-scraping-legality-ethics-2025, sources/python-scraping-tools-comparison, sources/schema-org-structured-data, sources/web-archiving-warc-tools
- **Concept articles created** (7): concepts/content-extraction, concepts/boilerplate-removal, concepts/html-to-markdown-conversion, concepts/web-scraping-ethics-and-law, concepts/anti-bot-evasion, concepts/structured-data-extraction, concepts/web-archiving
- **Concept articles updated** (1): concepts/web-scraping-at-scale (added 4 new sources, tool selection guide, related concepts)
- **Entity pages created** (8): entities/mozilla-readability, entities/trafilatura, entities/jina-reader, entities/reader-lm, entities/crawl4ai, entities/playwright, entities/scrapy, entities/beautiful-soup
- **Comparison pages created** (2): comparisons/heuristic-vs-neural-content-extraction, comparisons/crawl4ai-vs-firecrawl
- **Total wiki pages touched**: 27 (9 sources + 8 concepts + 8 entities + 2 comparisons)
- **Metadata updated**: _index.md, _meta/summaries.md, _meta/manifest.md, _meta/links.md, log.md

## [2026-04-05] research | LLM Applications Beyond Code — Writing, Research, Education, Science, Creative Work

Deep research pass on the expanding frontier of LLM applications beyond code generation, following Karpathy's shift from code to knowledge manipulation.

- **Web searches performed**: 11 (LLM applications beyond coding, AI scientific discovery, LLM education tutoring, AI writing tools, LLM data analysis, AI medical diagnosis, LLM legal analysis, AI research assistant tools, LLM workflow automation, AI creativity debate, frontier AI applications)
- **Sources fetched and ingested**: 10
  - `raw/hbr-llms-unlock-creative-ideas.md` — HBR: LLMs unlock creativity via persistence and flexibility
  - `raw/assemblyai-llm-use-cases-2026.md` — Seven primary enterprise LLM use cases
  - `raw/frontiers-ai-lab-automation-scientific-discovery.md` — AI as lab-pilot for science (Hartung, Frontiers in AI)
  - `raw/pmc-llms-healthcare-medical-review.md` — Seven healthcare LLM application domains (PMC review)
  - `raw/ai-deep-research-tools-2026.md` — Seven best AI research tools in 2026
  - `raw/mergen-llm-data-analysis-automation.md` — LLM data analysis automation (PMC study)
  - `raw/emergentmind-llm-tutoring-solutions.md` — LLM tutoring systems survey
  - `raw/microsoft-research-ai-2026-frontiers.md` — Microsoft Research 20 AI frontiers for 2026
  - `raw/gavel-law-firm-llm-guide-2026.md` — Small law firm LLM guide
  - `raw/science-advances-ai-creativity-diversity-paradox.md` — AI creativity paradox (Science Advances)
- **Source summaries created** (10): sources/hbr-llms-unlock-creative-ideas, sources/assemblyai-llm-use-cases-2026, sources/frontiers-ai-lab-automation-scientific-discovery, sources/pmc-llms-healthcare-medical-review, sources/ai-deep-research-tools-2026, sources/mergen-llm-data-analysis-automation, sources/emergentmind-llm-tutoring-solutions, sources/microsoft-research-ai-2026-frontiers, sources/gavel-law-firm-llm-guide-2026, sources/science-advances-ai-creativity-diversity-paradox
- **Concept articles created** (9): concepts/llm-applications-beyond-code (master map), concepts/ai-scientific-discovery, concepts/llm-healthcare-applications, concepts/llm-education-tutoring, concepts/llm-creative-applications, concepts/llm-legal-applications, concepts/ai-creativity-paradox, concepts/llm-data-analysis, concepts/ai-research-assistants
- **Entity pages created** (6): entities/perplexity-ai, entities/elicit, entities/scite, entities/alphafold, entities/med-palm, entities/everlaw
- **Comparison pages created** (1): comparisons/coding-vs-knowledge-work-llm-applications
- **Existing articles updated** (1): concepts/post-code-ai-workflow (added link to llm-applications-beyond-code)
- **Total wiki pages touched**: 27 (10 sources + 9 concepts + 6 entities + 1 comparison + 1 updated)
- **Metadata updated**: _index.md, _meta/summaries.md, _meta/manifest.md, _meta/links.md, log.md

## [2026-04-05] research | Attention mechanisms, memory in neural networks, and how models store and retrieve information
- **Topic**: Deep research on attention mechanisms (history, variants, efficiency), memory-augmented neural networks (NTMs, DNCs, RETRO), and how transformers store and retrieve factual knowledge (knowledge circuits, MLP-as-memory)
- **Searches performed** (13): attention mechanism neural networks explained, multi-head attention transformer detail, flash attention 2 3 efficient attention, linear attention alternatives, memory augmented neural networks, neural turing machine differentiable memory, retrieval augmented transformers RETRO, attention sink window attention, grouped query attention GQA MQA, cross attention self attention comparison, how transformers store knowledge MLP layers, KV cache optimization paged attention, mamba state space model alternative
- **Sources fetched and ingested** (9):
  - raw/attention-mechanisms-comprehensive-survey.md (arXiv 2601.03329 survey)
  - raw/flashattention-3-tri-dao-blog.md (Tri Dao's FA-3 blog)
  - raw/streamingllm-attention-sinks.md (MIT HAN Lab ICLR 2024)
  - raw/retro-illustrated-retrieval-transformer.md (Jay Alammar illustrated guide)
  - raw/differentiable-neural-computers-deepmind.md (DeepMind DNC blog)
  - raw/mamba-visual-guide-grootendorst.md (Grootendorst visual SSM guide)
  - raw/knowledge-circuits-transformers-research.md (NeurIPS 2024 knowledge circuits)
  - raw/kv-caching-huggingface-explained.md (Hugging Face KV cache tutorial)
  - raw/gqa-grouped-query-attention-overview.md (IBM GQA overview)
- **Source summaries created** (9): sources/attention-mechanisms-comprehensive-survey, sources/flashattention-3-tri-dao-blog, sources/streamingllm-attention-sinks, sources/retro-illustrated-retrieval-transformer, sources/differentiable-neural-computers-deepmind, sources/mamba-visual-guide-grootendorst, sources/knowledge-circuits-transformers-research, sources/kv-caching-huggingface-explained, sources/gqa-grouped-query-attention-overview
- **Concept articles created** (5): concepts/attention-mechanisms (umbrella), concepts/attention-sinks, concepts/linear-attention, concepts/memory-augmented-neural-networks, concepts/knowledge-storage-in-transformers
- **Concept articles updated** (8): concepts/self-attention, concepts/cross-attention, concepts/multi-head-attention, concepts/flash-attention, concepts/grouped-query-attention, concepts/kv-cache, concepts/mamba, concepts/sparse-attention (+new source refs and related links)
- **Entity pages created** (4): entities/flashattention, entities/retro, entities/neural-turing-machine, entities/streamingllm
- **Entity pages updated** (2): entities/tri-dao, concepts/paged-attention (+new source refs)
- **Comparison pages created** (3): comparisons/softmax-vs-linear-attention, comparisons/mha-vs-gqa-vs-mqa, comparisons/self-attention-vs-cross-attention
- **Total wiki pages touched**: 31 (9 sources + 13 concepts + 6 entities + 3 comparisons)
- **Metadata updated**: _index.md, _meta/summaries.md, _meta/manifest.md, log.md
