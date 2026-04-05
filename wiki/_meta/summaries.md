---
title: "Article Summaries"
type: meta
last_updated: 2026-04-05
reading_time: "4 min"
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

## Sources (PKM Methodologies, Tools & AI Transformation)

- [[sources/forte-building-second-brain]] — Tiago Forte BASB: CODE workflow (Capture, Organize, Distill, Express), PARA folder system, Progressive Summarization in 4 layers, and Intermediate Packets as reusable work units.
- [[sources/matuschak-evergreen-notes]] — Andy Matuschak: evergreen notes with five principles (atomic, concept-oriented, densely linked, associative ontologies, written for self); "better thinking" not "better note-taking."
- [[sources/zettelkasten-de-introduction]] — Canonical Zettelkasten guide: three traits (hypertextual, atomic, personal), link context requirement, Structure Notes, and 2-3 month learning curve.
- [[sources/luhmann-original-zettelkasten]] — Ernest Chiang corrects modern misinterpretations: Luhmann used two slip boxes (bibliographic + main), Folgezettel branching numbers, and the "communication partner" concept; modern fleeting/literature/permanent notes are Ahrens' 2017 interpretation.
- [[sources/appleton-digital-garden-history]] — Maggie Appleton: digital garden history from Bernstein (1998) through Caufield's "Garden and Stream" (2015) to the 2020 movement; six core patterns including topography over timelines and learning in public.
- [[sources/memex-vannevar-bush]] — Bush's 1945 memex: associative trails through stored knowledge; directly inspired Engelbart (mouse, hypertext), Nelson ("hypertext" coined 1965), and Berners-Lee (Web); "selection is still a stone adze" (1967).
- [[sources/sebastien-agentic-knowledge-management]] — Defines Agentic KM: AI agents proactively monitor knowledge bases, propose actions with human approval; Digital Twin concept where KB becomes "AI's brain too"; security via self-hosting and least privilege.
- [[sources/pkm-tools-comparison-2026]] — 2026 benchmarks: Obsidian v1.5.12 (95% responsive, <200ms at 20K notes), Logseq v0.12.6 (90%, 250ms), Notion v2.12 (98% online, 70% offline); Notion v3.0 AI Agents work autonomously for 20 minutes.
- [[sources/llms-for-knowledge-work-arxiv]] — Longitudinal study: LLM work adoption 24.5% (2023) to 34.6% (2024); four use categories; 70% want automation; trust barrier: "I don't trust the work of people who use LLMs."
- [[sources/spaced-repetition-knowledge-management]] — Forgetting curve: 50% lost in 1 hour, 90% in 1 week; Anki FSRS algorithm; structural cards preserve knowledge context; bridges the gap between PKM understanding and retention.

## Sources (Context Windows, Memory & Long-Context)

- [[sources/epoch-context-window-growth]] — Epoch AI analysis: frontier context windows growing ~30x/year since mid-2023, effective usage growing ~250x in 9 months, based on 123 models.
- [[sources/redis-rag-vs-long-context]] — RAG vs long-context: RAG wins on cost/latency (1s vs 30-60s), long context wins on full-document reasoning; hybrid approaches are the pragmatic standard.
- [[sources/logrocket-llm-context-problem]] — Identifies four context failure modes (poisoning, distraction, confusion, clash) and six practical techniques; context quality beats quantity.
- [[sources/lost-in-the-middle-paper]] — Liu et al. (TACL 2023): U-shaped performance curve, >30% degradation for middle-positioned content in LLM context windows.
- [[sources/memgpt-llm-operating-system]] — MemGPT: OS-inspired virtual context management with self-directed memory hierarchy (core/recall/archival); evolved into Letta platform.
- [[sources/prompt-caching-providers]] — Cross-provider prompt caching comparison: Anthropic (90% savings), OpenAI (50%), Google (75%) — making large contexts economically viable.
- [[sources/magic-ltm-100m-context]] — Magic LTM-2-Mini achieves 100M token context using sequence-dimension algorithm 1,000x cheaper than standard attention.
- [[sources/infinite-context-approaches]] — Four architectural approaches to infinite context: StreamingLLM (attention sinks), Infini-attention (compressive memory), Ring Attention (multi-device), InfLLM (external lookup).
- [[sources/context-compression-techniques]] — Compression techniques survey: LLMLingua (20x), soft prompts (480x), Provence (95%), hierarchical summarization, adaptive compression.
- [[sources/hierarchical-memory-llm-agents]] — H-MEM (EACL 2026) 4-layer architecture, multi-layer frameworks (working/episodic/semantic), five storage paradigms, sleep-time compute.
- [[sources/context-engineering-2026]] — Context engineering as successor to prompt engineering (2025-2026): structured context objects, ACE framework, three dimensions.

## Sources (Data Pipelines & Document Processing)

- [[sources/alan-llm-document-pipeline-production]] — Production lessons from Alan's healthcare document pipeline: OCR+image multimodal input, Pydantic validation, HNSW few-shot retrieval, and 70% automation with human-in-the-loop fallback.
- [[sources/rag-chunking-strategies-dasroot]] — Comprehensive comparison of five chunking strategies for RAG with benchmarks: fixed-size (92% recall), semantic boundary (95% coherence), hybrid (94% accuracy + 30% latency reduction).
- [[sources/stackoverflow-chunking-rag]] — Stack Overflow Blog practical guide to five chunking strategies: fixed-size, random, sliding window, context-aware, and adaptive (ML-based).
- [[sources/huggingface-vlms-2025]] — Hugging Face VLM landscape: any-to-any architectures, MoE decoders, ColPali multimodal retrieval, document understanding models, 2025 trends toward smaller capable models.
- [[sources/unstructured-io-document-etl]] — Unstructured.io open-source library: partition() auto-detects 30+ formats, outputs typed semantic elements, four processing strategies, enterprise 15M pages/hour.
- [[sources/firecrawl-web-data-api]] — Firecrawl converts websites to LLM-ready markdown/JSON via single API call, handles JS rendering and anti-bot, six modes, MCP Server for LLM integration.
- [[sources/llamaindex-ingestion-pipeline]] — LlamaIndex composable ingestion pipeline: SimpleDirectoryReader + LlamaParse + LlamaHub loaders, node parsers, cache-optimized deduplication.
- [[sources/airflow-mlops-orchestration]] — Astronomer's MLOps best practices: three orchestration patterns, Airflow 3.0 event-driven scheduling, 35% enterprise adoption.
- [[sources/pdf-parser-comparison-2026]] — Multi-source PDF parser comparison: PyMuPDF4LLM fastest (0.12s), Docling best enterprise (9/10), Nougat best scientific, OCR+VLM hybrid as 2026 best practice.


## Sources (AI Safety, Alignment & Trust)

- [[sources/fli-ai-safety-index-2025]] — FLI independent evaluation of 7 AI companies across 33 indicators in 6 domains; Anthropic leads at C+, no company above D in existential safety.
- [[sources/llm-hallucination-comprehensive-survey]] — Exhaustive 2025 survey by Alansari & Luqman covering hallucination taxonomy, causes across the full LLM lifecycle, 5 detection approaches, and 4 mitigation categories.
- [[sources/lakera-llm-hallucinations-2026]] — Lakera practitioner guide reframing hallucinations as incentive-driven guessing, covering CLAP/MetaQA detection and strategic shift toward calibrated uncertainty.
- [[sources/international-ai-safety-report-2026]] — 100+ expert global report led by Yoshua Bengio: AI capabilities advancing faster than safety measures; models can detect when being tested.
- [[sources/red-teaming-llm-safety-guide]] — Confident AI comprehensive guide to LLM red teaming: 5 vulnerability categories, PAIR algorithm (50% jailbreak on GPT-4), DeepTeam framework.
- [[sources/anthropic-safety-research-directions-2025]] — Anthropic alignment team identifies 10 priority research areas including evaluating alignment, scalable oversight, adversarial robustness.
- [[sources/hitl-ai-agent-oversight]] — Galileo AI + Holistic AI on HITL design patterns, confidence thresholds, and evolution toward AI-governing-AI.
- [[sources/ai-governance-frameworks-comparison]] — Plain-English comparison of EU AI Act (binding), NIST AI RMF (voluntary), ISO/IEC 42001 (certifiable).
- [[sources/ai-safety-alignment-progress-2025]] — 2025 AI safety advances: extended reasoning, visible thought processes, Constitutional AI evolution, safety as competitive differentiator.

## Concepts (AI Safety, Alignment & Trust)

- [[concepts/ai-safety]] — The field ensuring AI systems do not cause unintended harm — spanning technical robustness, alignment, evaluation, governance, and societal risk mitigation.
- [[concepts/ai-alignment]] — The technical challenge of ensuring AI systems pursue the goals their operators intend — RLHF, Constitutional AI, scalable oversight, deceptive alignment detection.
- [[concepts/llm-hallucination]] — When LLMs generate fluent but factually incorrect text — classified by type, caused across the full development lifecycle, addressed through detection and mitigation taxonomies.
- [[concepts/constitutional-ai]] — Anthropic's alignment approach using a written constitution of principles for AI self-critique, replacing reliance on human labelers with RLAIF.
- [[concepts/red-teaming]] — Deliberate adversarial testing of LLM systems to uncover safety vulnerabilities — prompt injection, jailbreaking, multi-turn attacks, automated frameworks.
- [[concepts/scalable-oversight]] — The challenge of maintaining meaningful human oversight over AI systems more capable than their overseers — recursive oversight, debate, AI-governing-AI.
- [[concepts/human-in-the-loop]] — Design patterns embedding human judgment into AI workflows — synchronous approval, asynchronous audit, confidence-based escalation.
- [[concepts/ai-governance]] — Regulatory and organizational frameworks: EU AI Act (binding, Aug 2026 enforcement), NIST AI RMF (voluntary), ISO/IEC 42001 (certifiable).
- [[concepts/ai-safety-benchmarks]] — Standardized evaluations for measuring AI safety: HarmBench, TruthfulQA, HELM Safety, FLI Safety Index; models learning to game evaluations.
- [[concepts/ai-content-verification]] — Methods for verifying AI-generated content accuracy: source attribution, span-level checking, multi-model peer review, CLAP detection.
- [[concepts/grounding-and-faithfulness]] — Techniques anchoring LLM outputs to source material: RAG, knowledge graph integration, span-level attribution, faithfulness checking.
- [[concepts/calibrated-uncertainty]] — Strategic shift from zero hallucinations to systems that transparently signal doubt, refuse when uncertain, produce confidence-calibrated outputs.

## Concepts (PKM Methodologies & History)

- [[concepts/zettelkasten]] — Niklas Luhmann's slip-box method: atomic, hypertextually linked notes forming a "communication partner" for thinking; foundational methodology behind modern networked note-taking tools.
- [[concepts/evergreen-notes]] — Andy Matuschak's framework: five principles (atomic, concept-oriented, densely linked, associative ontologies, written for self) for notes that evolve and accumulate insight over time.
- [[concepts/networked-thought]] — The paradigm of organizing knowledge as interconnected networks rather than hierarchical trees; from Bush (1945) through Luhmann to modern bidirectional linking tools.
- [[concepts/digital-garden]] — Public knowledge-sharing philosophy rejecting chronological blogging; six patterns: topography over timelines, continuous growth, learning in public, experimentation, diversity, independent ownership.
- [[concepts/progressive-summarization]] — Tiago Forte's 4-layer distillation: raw text, bolded keywords, highlighted best-of-best, executive summary in own words; designing notes for Future Self.
- [[concepts/para-method]] — Forte's organizational framework: Projects (short-term), Areas (ongoing), Resources (interest), Archive (inactive); organizing by actionability rather than topic.
- [[concepts/memex-and-tools-for-thought]] — 80-year lineage from Bush's 1945 memex through Engelbart, Nelson, Berners-Lee to modern PKM; the persistent challenge of intelligent selection.
- [[concepts/spaced-repetition]] — Adaptive review scheduling combating the forgetting curve (50% lost in 1 hour); Anki FSRS algorithm; complements PKM systems that build connections.
- [[concepts/learning-in-public]] — Publishing half-finished thoughts with epistemic status markers; core digital garden practice reducing friction between learning and sharing.
- [[concepts/agentic-knowledge-management]] — AI agents proactively monitoring knowledge bases, proposing and executing tasks with human approval; the "Digital Twin" where KB becomes shared cognitive infrastructure.

## Entities (PKM)

- [[entities/niklas-luhmann]] — German sociologist (1927-1998) who created the Zettelkasten with 90,000 cards across two systems; described it as a "communication partner."
- [[entities/tiago-forte]] — Productivity consultant who created Building a Second Brain (BASB), PARA, and Progressive Summarization; most popular PKM framework globally.
- [[entities/andy-matuschak]] — Researcher who developed the evergreen notes framework; pioneered public sliding-pane note systems; works on tools for thought.
- [[entities/maggie-appleton]] — Designer and anthropologist who compiled the definitive history and pattern language of digital gardens.
- [[entities/vannevar-bush]] — Engineer (1890-1974) who envisioned the memex in "As We May Think" (1945); conceptual ancestor of hypertext and the Web.
- [[entities/roam-research]] — Note-taking tool that popularized bidirectional linking (2020); "graph database" for ideas; triggered modern PKM tool ecosystem.
- [[entities/logseq]] — Open-source, local-first outliner with block-based architecture; positioned between Obsidian and Roam.
- [[entities/anki]] — Open-source spaced repetition software using FSRS algorithm; standard SRS tool for knowledge retention.

## Comparisons (PKM)

- [[comparisons/zettelkasten-vs-basb]] — Zettelkasten (insight generation, network position, atomic) vs BASB (creative output, actionability, PARA folders); complementary use possible.
- [[comparisons/obsidian-vs-logseq-vs-notion]] — 2026 tool comparison: Obsidian (local-first, 95% responsive), Logseq (open-source outliner), Notion (cloud-first, AI Agents in v3.0).
- [[comparisons/manual-vs-ai-pkm]] — Four PKM evolution stages: manual (human writes), AI-assisted (AI helps), AI-maintained (LLM compiles), agentic (AI monitors proactively).

## Entities (AI Safety, Alignment & Trust)

- [[entities/eu-ai-act]] — World's first comprehensive AI regulation; risk-tiered, penalties up to EUR 35M, full enforcement August 2, 2026.
- [[entities/nist-ai-rmf]] — Voluntary U.S. AI risk management framework; Govern/Map/Measure/Manage functions; globally referenced baseline.
- [[entities/future-of-life-institute]] — Research organization publishing the AI Safety Index evaluating AI companies across 33 indicators.
- [[entities/yoshua-bengio]] — Turing Award winner; chaired the 2026 International AI Safety Report with 100+ experts.

## Comparisons (AI Safety, Alignment & Trust)

- [[comparisons/rlhf-vs-constitutional-ai]] — RLHF (human preference labels) vs Constitutional AI (principle-guided self-critique): scalability, consistency, transparency tradeoffs.
## Concepts (Data Pipelines & Document Processing)

- [[concepts/document-processing-pipeline]] — Multi-stage system: acquire → parse → chunk → enrich → embed → store, with quality validation at each stage.
- [[concepts/document-chunking-strategies]] — Eight strategies from fixed-size to adaptive ML-based; semantic chunking improves retrieval accuracy by 18-40%.
- [[concepts/ocr-document-extraction]] — Modern OCR: traditional engines (99%+ printed text) and LLM-powered models for complex layouts; hybrid OCR+VLM is 2026 best practice.
- [[concepts/pdf-parsing-tools]] — Tool landscape: PyMuPDF4LLM (fastest), Docling (enterprise), Nougat (scientific), LlamaParse (tables); pipeline vs. end-to-end paradigms.
- [[concepts/web-scraping-at-scale]] — Async concurrency, proxy rotation, headless browsers, and API services (Firecrawl) for acquiring web content for LLM pipelines.
- [[concepts/pipeline-orchestration]] — Scheduling and managing multi-stage pipelines: Airflow dominates (35% enterprise), Airflow 3.0 event-driven scheduling.
- [[concepts/incremental-etl]] — Processing only new/changed data: watermarking, CDC, docstore deduplication, reducing compute by 10-100x.

## Entities (Data Pipelines & Document Processing)

- [[entities/unstructured-io]] — Open-source Python library for document ETL: 30+ formats, typed semantic elements, Apache 2.0, 14.4k GitHub stars.
- [[entities/firecrawl]] — AI web scraping API by Mendable.ai: markdown/JSON output, JS rendering, anti-bot, MCP Server integration.
- [[entities/apache-airflow]] — Dominant pipeline orchestrator: 35% enterprise adoption, event-driven DAGs, Python-native.
- [[entities/pymupdf]] — Fastest PDF parser: 0.12s markdown output via PyMuPDF4LLM variant.
- [[entities/docling]] — IBM document parsing toolkit (MIT): DocLayNet + TableFormer, 9/10 performance, air-gapped capable.
- [[entities/surya-ocr]] — Multilingual OCR by Vik Paruchuri: 90+ languages, 15-20% table improvement over commercial alternatives.
- [[entities/llamaparse]] — LlamaIndex managed PDF API: best-in-class for complex tables and figures.
- [[entities/llamaindex]] — Leading RAG framework: composable ingestion pipeline, node parsers, LlamaHub connectors.
- [[entities/langchain]] — LLM application framework: document loaders, RecursiveCharacterTextSplitter, chains, provider integrations.
- [[entities/colpali]] — ColBERT-like multimodal retrieval: direct visual document search without OCR via MaxSim similarity.

## Comparisons (Data Pipelines & Document Processing)

- [[comparisons/pdf-parsers-comparison]] — PyMuPDF vs Docling vs Unstructured vs Nougat vs LlamaParse: speed, accuracy, deployment, license, best use cases.
- [[comparisons/unstructured-vs-langchain]] — Unstructured (document ETL preprocessing) vs LangChain (LLM orchestration): complementary, use both together.
- [[comparisons/ocr-vs-vlm-document-processing]] — Traditional OCR vs VLMs vs hybrid: speed/accuracy/cost tradeoffs, hybrid OCR+VLM as 2026 best practice.

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

## Sources (Developer Tools & AI-Assisted Workflows)

- [[sources/metr-ai-developer-productivity-study]] — Landmark RCT finding experienced open-source developers are 19% slower with AI tools, despite believing they were 20% faster.
- [[sources/osmani-llm-coding-workflow-2026]] — Google Chrome lead's 10-step workflow for AI-augmented engineering: spec-first planning, small iterations, model rotation, testing as force multiplier.
- [[sources/faros-ai-coding-agents-2026]] — Comprehensive 2026 review of AI coding agents: Cursor leads on flow, Claude Code on reasoning, Copilot on frictionless integration, with 10+ runner-ups.
- [[sources/faros-ai-productivity-paradox]] — Faros AI telemetry from 10,000+ developers: 21% more tasks but 9% more bugs, 154% larger PRs, 91% longer reviews, no org-level gain.
- [[sources/dextralabs-claude-cursor-copilot-30day]] — Practitioner 30-day head-to-head: Cursor (balanced IDE 9/10), Claude Code (deep reasoning 8.5/10), Copilot (zero friction 8/10).
- [[sources/redmonk-agentic-ides-2025]] — RedMonk: 10 must-haves for agentic IDEs — background agents, persistent memory, predictable pricing, MCP, specs, skills.
- [[sources/graphite-ai-code-review-tools]] — Overview of 7 AI code review tools: Graphite Agent (55% action rate), CodeRabbit (2M+ repos), Qodo (review + test generation).
- [[sources/index-dev-ai-pair-programming-statistics]] — Comprehensive statistics: 84% developer adoption, 41% code AI-generated, 55% faster tasks, but 46% don't trust output.
- [[sources/qodo-ai-coding-assistants-2026]] — Five-tier taxonomy of 15 AI coding tools: code review, IDE assistants, cloud-specific, autonomous agents, and low-code builders.
- [[sources/panto-ai-coding-productivity-stats]] — AI coding productivity overview: perception-reality gap, DORA-style metrics recommended over output volume.

## Concepts (Developer Tools & AI-Assisted Workflows)

- [[concepts/ai-coding-assistants]] — The landscape of LLM-powered developer tools from inline autocomplete to autonomous agents, organized in five tiers with 84% adoption.
- [[concepts/ai-pair-programming]] — Collaborating with AI as a programming partner — treating it as a capable but fallible junior developer requiring clear direction and review.
- [[concepts/ai-productivity-paradox]] — The disconnect between perceived and measured AI productivity: 19% slowdown in RCTs, no organizational improvement despite 84% adoption.
- [[concepts/ai-code-review]] — AI-powered PR review tools achieving 55% action rates that exceed human reviewers at 49%, identified as key bottleneck in the productivity paradox.
- [[concepts/spec-driven-development]] — Writing detailed specification documents before AI code generation: "waterfall in 15 minutes," eliminates 80% of AI confusion.
- [[concepts/developer-experience-ai]] — How AI tools reshape the daily developer workflow: perception-reality gap, role transformation, and the 10 DX requirements for agentic IDEs.

## Entities (Developer Tools & AI-Assisted Workflows)

- [[entities/cursor]] — AI-native IDE (VS Code fork): $2B+ ARR, $29.3B valuation, praised for "magical" inline editing and codebase indexing.
- [[entities/github-copilot]] — Industry-standard AI coding assistant: $10-21/mo, 90% Fortune 100, universal IDE support, pragmatic enterprise default.
- [[entities/aider]] — Open-source CLI coding agent: Git-native, model-flexible, transparent diffs, 88% SWE-bench via GPT-5.
- [[entities/devin]] — First autonomous AI software engineer by Cognition Labs (March 2024); Devin 2.0 dropped from $500/mo to $20/mo.
- [[entities/coderabbit]] — Most installed AI code review app: 2M+ repos, 13M+ PRs processed, free for open source, highest false-positive rate.
- [[entities/graphite]] — AI code review tool: 96% positive rate, 55% developer action rate exceeds human reviewers at 49%.
- [[entities/addy-osmani]] — Google Chrome engineering lead; published influential 10-step LLM coding workflow for 2026.
- [[entities/metr]] — AI safety research org behind landmark RCT finding 19% developer slowdown with AI tools.

## Comparisons (Developer Tools & AI-Assisted Workflows)

- [[comparisons/cursor-vs-claude-code-vs-copilot]] — The three dominant AI coding tools: Cursor (best balanced IDE), Claude Code (deepest reasoning, 80.8% SWE-bench), Copilot (lowest friction, 90% Fortune 100).

## Concepts (Context Windows, Memory & Long-Context)

- [[concepts/context-windows]] — The fixed-size token buffer an LLM processes in a single inference call; growing ~30x/year but effective utilization lags behind raw capacity.
- [[concepts/long-context-models]] — Models designed for extended context: Gemini (1-2M), Claude (1M), Llama 4 Scout (10M), Magic LTM-2-Mini (100M) — each with distinct tradeoffs.
- [[concepts/lost-in-the-middle]] — LLMs exhibit a U-shaped performance curve — best at beginning/end of context, >30% degradation in the middle — caused by attention accumulation.
- [[concepts/context-engineering]] — The systems discipline of managing everything an LLM encounters during inference — successor to prompt engineering, credited to Karpathy.
- [[concepts/context-compression]] — Techniques for reducing token count while preserving information: hard prompts (20x), soft prompts (480x), structured pruning (95%).
- [[concepts/needle-in-a-haystack]] — Standard evaluation for long-context LLMs: embed a specific fact at varying depths within a large context and test retrieval.
- [[concepts/prompt-caching]] — Provider-level optimization caching computed state of static prompt prefixes: Anthropic (90%), OpenAI (50%), Google (75%) savings.
- [[concepts/virtual-context-management]] — OS-inspired technique where LLMs page information between in-context memory (RAM) and external storage (disk).
- [[concepts/hierarchical-memory]] — Multi-tier memory for LLM agents: working (in-context), episodic (summaries), semantic (abstractions), archival (external DB).
- [[concepts/infinite-context]] — Architectural approaches to unbounded sequences: StreamingLLM, Infini-attention, Ring Attention, InfLLM.

## Sources (Multimodal AI & Vision)

- [[sources/bentoml-vision-language-models-2026]] — Survey of open-source VLMs in 2026: GLM-4.6V, Qwen3-VL (235B), Gemma 3, DeepSeek-OCR, Molmo, Pixtral with benchmarks and deployment guidance.
- [[sources/nvidia-multimodal-rag-intro]] — Three multimodal RAG architectures (unified embeddings, text grounding, separate stores with re-ranking) with full preprocessing and inference pipelines.
- [[sources/viso-visual-question-answering-2025]] — VQA overview: CNN+LSTM+attention architecture, key datasets (COCO-QA through Visual Genome), applications, and state-of-the-art models (LLaMA3, NVILA, Qwen3).
- [[sources/ocr-technology-evolution-2026]] — OCR evolution from 85%-accurate Tesseract to 99%+ VLM-powered document intelligence; Claude 3 highest median accuracy on industrial images.
- [[sources/claude-vision-capabilities]] — Anthropic official vision docs: JPEG/PNG/GIF/WebP, token formula (w*h/750), three input methods, MMMLU ~88-89%, limitations.
- [[sources/pinecone-clip-multimodal-embeddings]] — CLIP deep dive: dual 512-dim encoders, contrastive learning, zero-shot classification, and successors (Jina CLIP v2, Voyage multimodal-3).
- [[sources/multimodal-rag-images-text-guide]] — Practical multimodal RAG: unified multimodal embeddings (Voyage AI) vs LLM-based image summarization with vector DB implementation.
- [[sources/image-captioning-survey-transformers-mllms]] — Image captioning evolution: template-based to CNN+LSTM to attention to transformers to MLLMs; evaluation metrics (BLEU, CIDEr, SPICE).

## Concepts (Multimodal AI & Vision)

- [[concepts/multimodal-ai]] — AI systems processing multiple data modalities (text, images, audio, video); by 2026, multimodal capability is baseline rather than differentiator.
- [[concepts/vision-language-models]] — Models jointly processing images and text; from CLIP's dual encoders to GPT-4V/Claude/Qwen3-VL; open-source rivals proprietary by 2026.
- [[concepts/multimodal-rag]] — Extending RAG to retrieve images alongside text; three architectures (unified embeddings, text grounding, separate stores) with tradeoffs.
- [[concepts/multimodal-embeddings]] — Shared vector spaces (CLIP, Jina CLIP, Voyage) for cross-modal similarity search via contrastive learning.
- [[concepts/image-understanding]] — AI capability hierarchy for visual content: perception, comprehension, reasoning, knowledge integration.
- [[concepts/visual-question-answering]] — Answering natural language questions about images; considered "AI-complete"; evolved from CNN+LSTM to VLM-based approaches.
- [[concepts/document-ai-ocr]] — From 85%-accurate character recognition to 99%+ document intelligence via VLMs; three paradigms (traditional, layout-aware, VLM).
- [[concepts/image-captioning]] — Generating text descriptions of images; evolved from CNN+LSTM through transformers to MLLMs; critical for making visual content searchable in KBs.

## Entities (Multimodal AI & Vision)

- [[entities/clip]] — OpenAI's CLIP (2021): dual text/image encoders producing 512-dim shared embeddings via contrastive learning; foundational for multimodal search and RAG.
- [[entities/qwen3-vl]] — Alibaba's flagship open-source VLM: 235B params (22B active MoE), 256K-1M context, rivals GPT-5 and Gemini-2.5-Pro.
- [[entities/deplot]] — Google's chart-to-text conversion tool for multimodal RAG preprocessing pipelines.

## Comparisons (Multimodal AI & Vision)

- [[comparisons/text-rag-vs-multimodal-rag]] — Text-only RAG vs multimodal RAG: when visual content justifies added complexity; hybrid "text grounding" approach recommended for markdown KBs.

## Sources (Prompt Engineering)

- [[sources/promptingguide-chain-of-thought]] — DAIR.AI overview of CoT prompting: Wei et al. (2022) technique enabling complex reasoning via intermediate steps, plus Zero-Shot CoT and Auto-CoT variants.
- [[sources/promptingguide-tree-of-thoughts]] — DAIR.AI overview of ToT: Yao et al. (2023) framework generalizing CoT into tree-structured exploration with BFS/DFS search, achieving 25% gains over CoT on Game of 24.
- [[sources/promptingguide-self-consistency]] — DAIR.AI overview of self-consistency: Wang et al. (2022) technique sampling multiple CoT reasoning paths and selecting the most frequent answer via majority voting.
- [[sources/promptingguide-few-shot]] — DAIR.AI overview of few-shot prompting: in-context learning via demonstration examples, with research showing format and label distribution matter more than label accuracy.
- [[sources/promptingguide-prompt-chaining]] — DAIR.AI overview of prompt chaining: decomposing complex tasks into sequential LLM calls where each output feeds the next.
- [[sources/promptingguide-rag-prompting]] — DAIR.AI overview of RAG prompting: combining retrieval with generation, query rewriting (Query2Doc, HyDE), and context integration techniques.
- [[sources/anthropic-claude-prompting-best-practices]] — Anthropic's official prompting guide for Claude 4.6: XML tags, role assignment, few-shot, adaptive thinking, long-context strategies, agentic system design.
- [[sources/lakera-prompt-engineering-guide]] — Lakera's 2026 guide covering 9 essential techniques plus model-specific tips and adversarial prompting security.
- [[sources/lakera-prompt-injection-guide]] — Lakera's deep dive on prompt injection: direct vs indirect types, 5 attack techniques, 5 real-world incidents, multi-layered defense strategies.
- [[sources/prompthub-role-prompting-research]] — PromptHub research review: role/persona prompting helps for creative/style tasks but is unreliable for factual accuracy.
- [[sources/intuitionlabs-meta-prompting]] — IntuitionLabs deep dive on meta-prompting: DSPy (46%->64%), TextGrad (Nature 2025), Self-Refine (~20% improvement), recursive meta-prompting.

## Concepts (Prompt Engineering)

- [[concepts/prompt-engineering]] — The discipline of designing LLM inputs for high-quality, accurate outputs — from clarity principles to advanced reasoning scaffolds and automated optimization.
- [[concepts/chain-of-thought-prompting]] — Wei et al. (2022) technique enabling complex reasoning by having LLMs decompose problems into intermediate steps — the most impactful prompting technique for reasoning.
- [[concepts/few-shot-prompting]] — In-context learning via 3-5 demonstration examples — the highest-ROI technique where format matters more than label accuracy.
- [[concepts/zero-shot-prompting]] — Direct instruction without examples; the simplest approach and recommended starting point before adding complexity.
- [[concepts/tree-of-thoughts-prompting]] — Yao et al. (2023) framework generalizing CoT into tree-structured exploration with BFS/DFS search, enabling deliberate problem-solving with backtracking.
- [[concepts/self-consistency-prompting]] — Wang et al. (2022) technique sampling multiple CoT paths and selecting the most frequent answer via majority voting — strictly improves over single-path CoT.
- [[concepts/role-prompting]] — Assigning a persona to an LLM — effective for tone/style control but unreliable for factual accuracy where "none of the strategies outperformed random selection."
- [[concepts/prompt-chaining]] — Decomposing complex tasks into sequential LLM calls where each output feeds the next — foundational pattern for production LLM workflows.
- [[concepts/meta-prompting]] — Using LLMs to generate, evaluate, and optimize prompts — DSPy (46%->64%), TextGrad (Nature 2025), Self-Refine (~20% improvement).
- [[concepts/structured-output-prompting]] — Getting LLMs to produce predictable, parseable formats (JSON, XML, tables) — essential for production systems consuming model outputs.
- [[concepts/system-prompt-design]] — Architecture-level prompt patterns defining consistent LLM behavior, roles, and constraints across all interactions.
- [[concepts/prompt-injection]] — Manipulation exploiting inability to separate LLM instructions from user input — #1 AI security risk (OWASP 2025), no foolproof defense exists.
- [[concepts/rag-prompting]] — Prompt engineering within RAG pipelines: query rewriting (HyDE, Query2Doc), context integration, and grounded generation.

## Entities (Prompt Engineering)

- [[entities/anthropic]] — AI safety PBC founded 2021 by 7 ex-OpenAI researchers (Dario & Daniela Amodei + 5); $380B valuation; builds Claude, Claude Code ($2.5B ARR), MCP; #1 FLI Safety Index.
- [[entities/claude]] — Anthropic's frontier LLM family named after Claude Shannon; 4 generations (Claude 1-4.6), Opus/Sonnet/Haiku tiers, 1M context, adaptive thinking, 80.9% SWE-bench.
- [[entities/dario-amodei]] — CEO/co-founder of Anthropic; ex-VP Research at OpenAI; authored "Machines of Loving Grace" essay on AI's transformative upside.
- [[entities/daniela-amodei]] — President/co-founder of Anthropic; ex-VP Operations at OpenAI; drives business growth and partnerships.
- [[entities/dspy]] — Declarative Self-improving Python: compiler for prompt optimization that raised accuracy from 46.2% to 64.0%.
- [[entities/textgrad]] — Gradient-based prompt optimization using natural language feedback instead of numeric scores — published in Nature (2025).
- [[entities/owasp]] — Ranked prompt injection as #1 AI security risk in 2025 Top 10 for LLMs.
- [[entities/prompt-engineering-guide]] — DAIR.AI's comprehensive open-source prompting reference at promptingguide.ai — the de facto reference for the field.

## Comparisons (Prompt Engineering)

- [[comparisons/cot-vs-tot-vs-self-consistency]] — CoT (single path, cheap) vs Self-Consistency (multi-path voting, moderate) vs ToT (tree search, expensive) — progressive upgrade path for reasoning.
- [[comparisons/few-shot-vs-zero-shot]] — Zero-shot (simpler, try first) vs few-shot (3-5 examples, better format control) — format/distribution matters more than label accuracy.
- [[comparisons/manual-vs-automated-prompt-optimization]] — Manual crafting vs DSPy/TextGrad/Self-Refine: automated achieves 20-64% improvements but adds complexity — hybrid recommended.

## Sources (Markdown & Plain Text Research)

- [[sources/sivers-plain-text-files]] — Derek Sivers argues that plain text files are the only truly future-proof format: portable across all devices, independent of vendors, and readable centuries from now.
- [[sources/ango-file-over-app]] — Obsidian CEO Steph Ango argues that files must outlast apps — digital artifacts should exist in controllable, accessible formats independent of any software vendor.
- [[sources/mdx-markdown-components]] — MDX extends markdown with JSX components, enabling interactive content within markdown documents — compiled at build time with no runtime overhead.
- [[sources/microsoft-markitdown]] — Microsoft's open-source MarkItDown converts PDFs, Office docs, images, and audio to markdown for LLM ingestion — treating markdown as the universal preprocessing format for AI pipelines.
- [[sources/markdown-agent-task-format]] — Advocates markdown+YAML frontmatter over JSON for AI agent task management: human-readable, git-native, agent-compatible, with Unix tooling for querying.
- [[sources/llms-love-markdown]] — Quantifies markdown's advantages for LLMs: 25-75% token reduction vs HTML, 89% vs 62% RAG retrieval accuracy, and superior semantic parsing via AST tokenization.
- [[sources/pandoc-universal-converter]] — Pandoc converts between dozens of markup and document formats via a markdown-centric AST — effectively making markdown the hub of the document format universe.
- [[sources/marp-markdown-presentations]] — Marp converts markdown into presentation slides (HTML, PDF, PowerPoint) — demonstrating that markdown can replace proprietary formats even for visual content.
- [[sources/markdowndb-queryable-markdown]] — MarkdownDB indexes markdown files into SQLite for SQL/JSON querying while preserving files on disk — bridging the plain-text vs. database gap.
- [[sources/mit-digital-preservation-formats]] — MIT Libraries recommends plain text (UTF-8) as the preferred preservation format for text content — validating markdown's archival durability from an institutional perspective.

## Concepts (Markdown & Plain Text)

- [[concepts/plain-text-longevity]] — Plain text is the only digital format guaranteed to be readable decades or centuries from now — validated by individual practitioners, Obsidian's CEO, and institutional archivists.
- [[concepts/file-over-app]] — Steph Ango's philosophy that digital artifacts must exist as user-controlled files in accessible formats — because apps are ephemeral, but files can endure for centuries.
- [[concepts/markdown-ecosystem]] — The constellation of tools, converters, frameworks, and standards that make markdown a practical universal format: Pandoc, MDX, Marp, MarkdownDB, MarkItDown, SSGs, and more.
- [[concepts/yaml-frontmatter]] — YAML frontmatter is the de facto standard for embedding structured metadata in markdown files — enabling queryability, categorization, and machine processing while preserving plain-text readability.
- [[concepts/markdown-for-ai-agents]] — LLMs natively comprehend markdown due to training data representation and AST-based tokenization — making it 25-75% more token-efficient than HTML and yielding 89% vs 62% RAG retrieval accuracy.
- [[concepts/mdx]] — MDX extends markdown with JSX components — enabling interactive, component-based content within markdown documents while compiling to JavaScript at build time with zero runtime.
- [[concepts/static-site-generators]] — Hugo, Jekyll, Astro, Eleventy, Gatsby, and Next.js all consume markdown as their primary content format — making markdown the default authoring language for the modern web.

## Sources (Synthetic Data, Fine-Tuning & Model Adaptation)

- [[sources/synthetic-data-generation-llms]] — Five-step architecture for LLM-driven synthetic data generation (chunk → context → query → evolve → answer) with quality filtering at every stage.
- [[sources/raft-retrieval-augmented-fine-tuning]] — UC Berkeley paper combining RAG with fine-tuning: train models to ignore distractor documents and cite verbatim from oracle docs, achieving up to 76% improvement.
- [[sources/lora-qlora-efficient-fine-tuning]] — Comparison of LoRA (low-rank adapter matrices, 90-95% of full quality) and QLoRA (4-bit quantized base + LoRA, 80-90% quality) with memory requirement tables.
- [[sources/textbooks-are-all-you-need-phi]] — Microsoft Research demonstrates that 1.3B-parameter phi-1 trained on "textbook quality" synthetic data matches models 10x larger — data quality decisively outperforms scale.
- [[sources/domain-adaptive-pretraining-dapt]] — DAPT adds an intermediate domain-specific pretraining step between general pretraining and task fine-tuning; operates on unlabeled data; combined with TAPT yields best results.
- [[sources/rome-memit-knowledge-editing]] — ROME uses causal tracing to locate facts in MLP layers, then makes rank-one edits to change individual factual associations; MEMIT scales to thousands of simultaneous edits.
- [[sources/ai-training-2026-synthetic-human-data]] — 2026 perspective: web training data is exhausted; competitive advantage lies in human-synthetic data flywheels with governance guardrails to prevent model collapse.
- [[sources/llm-knowledge-distillation-survey]] — Overview of LLM knowledge distillation: teacher-student paradigm, white-box vs. black-box methods, rationale-based distillation, and practical deployment benefits.

## Concepts (Synthetic Data, Fine-Tuning & Model Adaptation)

- [[concepts/synthetic-data-generation]] — Using LLMs to generate training data at scale — from textbook-quality corpora to instruction-following datasets — with quality filtering as the critical success factor.
- [[concepts/fine-tuning]] — Adapting pretrained LLMs to domain-specific tasks by training on curated datasets — from full fine-tuning to parameter-efficient methods (LoRA/QLoRA) to hybrid approaches (RAFT).
- [[concepts/parameter-efficient-fine-tuning]] — LoRA and QLoRA enable fine-tuning LLMs by updating only 0.5-5% of parameters via low-rank adapter matrices, reducing VRAM from 60GB to 6GB for a 7B model.
- [[concepts/knowledge-distillation]] — Transferring capabilities from large teacher models to small student models via logit matching, feature mimicry, or rationale extraction.
- [[concepts/catastrophic-forgetting]] — Models losing previously learned knowledge when fine-tuned on new data — mitigated by PEFT, regularization (EWC), experience replay, and parameter isolation.
- [[concepts/model-collapse]] — Degenerative feedback loop where models trained on synthetic data from models trained on synthetic data progressively lose capability.
- [[concepts/domain-adaptive-pretraining]] — Intermediate pretraining step on unlabeled domain text between general pretraining and task fine-tuning — requires no labeled data.
- [[concepts/continued-pretraining]] — Extending a model's pretraining phase on new corpora (domain text, synthetic data, or instruction data) to specialize before task-specific fine-tuning.
- [[concepts/knowledge-editing]] — Targeted modification of specific factual associations in model weights without full retraining — via ROME (single facts) and MEMIT (thousands of facts).
- [[concepts/raft]] — RAFT (Retrieval Augmented Fine-Tuning): hybrid approach training models on questions with oracle + distractor documents, achieving up to 76% improvement.
- [[concepts/weights-vs-context]] — The fundamental design question: which knowledge belongs in model weights (persistent, fast, opaque) vs. context windows (dynamic, traceable, limited) vs. external tools.

## Sources (Information Extraction)

- [[sources/willison-llm-schemas-structured-extraction]] — Simon Willison's LLM 0.23 introduces schema-based structured extraction — FSM-guaranteed JSON output across all major providers as of 2026.
- [[sources/gpt-ner-named-entity-recognition]] — GPT-NER transforms NER from sequence labeling to text generation using marker tokens; achieves supervised-comparable performance; self-verification combats hallucinated entities.
- [[sources/instructor-library-structured-extraction]] — Instructor: most popular Python library for structured LLM extraction (3M+ downloads), using Pydantic models with automatic validation and retry across 15+ providers.
- [[sources/claimify-claim-extraction]] — Microsoft's Claimify (ACL 2025) decomposes LLM outputs into atomic verifiable claims via a 4-stage pipeline, achieving 99% entailment with source sentences.
- [[sources/ontogpt-ontology-extraction]] — OntoGPT's SPIRES method uses zero-shot LLM extraction grounded in biomedical ontologies, producing structured output without training data.
- [[sources/wolfe-llm-summarization-evolution]] — Cameron Wolfe traces how summarization research led to RLHF; reveals LLMs are more extractive in practice than theory suggests.

## Concepts (Information Extraction)

- [[concepts/information-extraction]] — The discipline of extracting structured knowledge (entities, relations, claims) from unstructured text using LLMs — foundational capability for wiki compilation.
- [[concepts/named-entity-recognition]] — Identifying named entities in text; LLMs bridge the sequence-labeling-to-generation gap via task reformulation and self-verification.
- [[concepts/relation-extraction]] — Extracting subject-predicate-object relationships between entities; LLMs enable zero-shot RE matching supervised models.
- [[concepts/structured-output-extraction]] — Forcing LLM outputs into schema-conformant JSON via FSM constrained decoding or Pydantic validation-retry loops.
- [[concepts/claim-extraction]] — Breaking complex text into atomic, independently verifiable claims for fact-checking and wiki quality assurance.
- [[concepts/llm-summarization]] — Extractive vs. abstractive summarization; hybrid extract-then-abstract produces most reliable wiki summaries; RLHF originated from summarization research.
- [[concepts/entity-linking]] — Mapping textual entity mentions to canonical KB entries; resolving ambiguity and merging synonyms via LLM clustering or ontology grounding.
- [[concepts/zero-shot-information-extraction]] — IE without labeled training data; few-shot GPT-4/Claude matches supervised models; prompt design is the critical variable.
- [[concepts/schema-guided-extraction]] — Constraining LLM extraction with ontologies or schemas; from static templates to dynamic co-evolving schemas.

## Entities (Information Extraction)

- [[entities/instructor]] — Most popular Python library for structured LLM extraction (3M+ monthly downloads); Pydantic validation + automatic retry across 15+ providers.
- [[entities/pydantic]] — Python data validation library; de facto standard for defining LLM extraction schemas across Instructor, Pydantic AI, LangChain.
- [[entities/claimify]] — Microsoft Research's 4-stage claim extraction system (ACL 2025); 99% source entailment; first to handle ambiguity by flagging rather than guessing.
- [[entities/ontogpt]] — Python package for ontology-grounded IE using SPIRES zero-shot method; maps extracted entities to established biomedical ontologies.
- [[entities/kggen]] — Open-source KG extraction library with 3-stage pipeline (generate, aggregate, cluster); 66% MINE score, 18% above GraphRAG.
- [[entities/simon-willison]] — Creator of Datasette and LLM CLI; champions structured extraction as "the single most commercially valuable LLM application."

## Comparisons

- [[comparisons/markdown-vs-proprietary-formats]] — Systematic comparison of markdown against proprietary formats (Word, Notion, Evernote) across longevity, AI-readability, version control, portability, and queryability.
- [[comparisons/rag-vs-fine-tuning]] — RAG injects knowledge at inference time (dynamic, traceable); fine-tuning bakes it into weights (persistent, fast) — hybrid RAFT combines both.
- [[comparisons/lora-vs-qlora]] — LoRA (16-bit adapters, 90-95% quality, 16GB for 7B) vs. QLoRA (4-bit quantized base, 80-90% quality, 6GB for 7B).
- [[comparisons/knowledge-editing-vs-fine-tuning]] — Knowledge editing is surgical and cheap for individual facts but degrades with sequential edits; fine-tuning is broader but expensive.
- [[comparisons/schema-guided-vs-schema-free-extraction]] — Schema-guided (OntoGPT, KARMA) trades flexibility for precision; schema-free (KGGen, OpenIE) discovers novel patterns but needs post-processing.
- [[comparisons/rag-vs-long-context]] — RAG (fast, cheap, precise) vs long context (full reasoning, simple); hybrid approaches combining both are the 2026 standard.
- [[comparisons/context-management-approaches]] — Four approaches compared: compression, virtual context (MemGPT), infinite context (architectural), and context engineering.


## Entities (Synthetic Data, Fine-Tuning & Model Adaptation)

- [[entities/microsoft-phi]] — Microsoft Research model family (phi-1 through phi-4) demonstrating that "textbook quality" synthetic data enables small models to rival or surpass models 10-25x larger.
- [[entities/rome-memit]] — Pioneering knowledge editing methods: ROME makes rank-one MLP modifications for single fact edits; MEMIT scales to thousands of simultaneous edits.

## Entities (Markdown & Plain Text)

- [[entities/derek-sivers]] — Programmer, author, and entrepreneur who has written exclusively in plain text since 1990 — the most prominent individual advocate for plain-text-as-productivity-system.
- [[entities/steph-ango]] — CEO of Obsidian who coined 'file over app' — the philosophy that digital artifacts must exist as user-controlled files in accessible formats because apps are ephemeral.
- [[entities/pandoc]] — Universal document converter (Haskell, GPL) that converts between 40+ formats via a markdown-centric AST — maintained since 2006 by John MacFarlane.
- [[entities/markitdown]] — Microsoft's open-source Python tool for converting PDFs, Office docs, images, audio, and web content to markdown — designed for LLM ingestion pipelines.
- [[entities/mdx]] — Authoring format that blends markdown with JSX components — 'Markdown for the component era' — with zero runtime, compiling to JavaScript at build time.
- [[entities/marp]] — Open-source markdown presentation ecosystem: write slides in CommonMark, export to HTML/PDF/PPTX via the Marpit framework, VS Code extension, and CLI.
- [[entities/markdowndb]] — Open-source JS library that indexes markdown files into SQLite for SQL/JSON querying — files remain on disk as plain text, with the database as a derived index.
- [[entities/obsidian]] — Markdown-based knowledge management app embodying 'file over app': local-first, plain-text storage, graph view, wikilinks, 2000+ community plugins.

## Entities (LLM Knowledge Base Ecosystem)

- [[entities/andrej-karpathy]] — Slovak-Canadian AI researcher, educator, and entrepreneur: OpenAI co-founder, Tesla AI Director, creator of Software 2.0 and vibe coding, builder of micrograd/nanoGPT/llm.c, founder of Eureka Labs, and originator of the LLM knowledge base methodology that inspired this wiki.
- [[entities/elvis-saravia]] — Founder of DAIR.AI Academy who provided the most thorough system architecture analysis of Karpathy's LLM knowledge base, coining the 'four-phase operational cycle' framework.
- [[entities/sam-gallagher]] — Developer who built the Knowledge Graph Kit, an open-source MCP server using SQLite and ChromaDB, as a structure-first alternative to markdown-based personal knowledge management.
- [[entities/vannevar-bush]] — American engineer and science administrator who envisioned the Memex in 1945 -- a proto-hypertext personal knowledge device that prefigured modern LLM knowledge bases by 80 years.
- [[entities/memex]] — Vannevar Bush's 1945 vision of a personal knowledge device with associative cross-referencing -- the conceptual ancestor of hypertext, wikis, and LLM-maintained knowledge bases.
- [[entities/obsidian-web-clipper]] — A browser extension for converting web articles into markdown files for ingestion into the raw/ directory of an LLM knowledge base.
- [[entities/dataview]] — An Obsidian community plugin that enables database-like queries over markdown file frontmatter, useful for dynamic views of LLM-maintained wiki metadata.

## Entities (Context Windows & Memory)

- [[entities/memgpt-letta]] — MemGPT/Letta: open-source platform for stateful LLM agents with OS-inspired virtual context management; LLM self-manages core/recall/archival memory.
- [[entities/magic-ltm]] — Magic LTM-2-Mini: 100M token context model using novel sequence-dimension algorithm 1,000x cheaper than standard attention.
- [[entities/lost-in-the-middle-paper]] — Liu et al. (Stanford/UC Berkeley, TACL 2023): landmark paper documenting the U-shaped performance curve in LLM context utilization.

- [[entities/matplotlib]] — A Python plotting library used in the LLM-KB workflow to generate data visualizations that are saved as images and viewed within Obsidian alongside wiki articles.
- [[entities/graphiti]] — An open-source framework by Zep for building temporal context graphs where facts have validity windows, designed for AI agents operating in dynamic environments.
- [[entities/zep]] — The organization behind Graphiti, offering both an open-source temporal context graph engine and enterprise-grade managed infrastructure for AI agent memory.
- [[entities/chromadb]] — An open-source embedding database used in Gallagher's Knowledge Graph Kit to provide semantic vector search over graph nodes alongside SQLite structural storage.
- [[entities/faiss]] — Facebook AI Similarity Search -- an open-source library for efficient similarity search and clustering of dense vectors, supporting billions of vectors with disk-based indexing.
- [[entities/pgvector]] — A PostgreSQL extension for vector similarity search, widely regarded as sufficient for most team-scale retrieval use cases without requiring dedicated vector database infrastructure.
- [[entities/sqlite]] — A lightweight, serverless relational database used as the structural storage layer in Gallagher's Knowledge Graph Kit for personal knowledge management.
- [[entities/neo4j]] — A native graph database used as the backend for Graphiti's temporal context graphs, providing mature graph query and visualization capabilities.
- [[entities/mongodb]] — A document database with vector search capabilities used as the storage and retrieval backend in the Decoding AI production RAG pipeline.
- [[entities/llama]] — Meta's open-source LLM family, with Llama 3.1 8B used in the Decoding AI second-brain RAG pipeline as the fine-tuned summarization model.
- [[entities/zenml]] — An open-source MLOps pipeline orchestration framework used in the Decoding AI second-brain RAG system to manage offline data processing and training workflows.
- [[entities/vespa]] — Yahoo's hybrid search engine combining vector, keyword, and metadata search with multi-vector indexing -- described as underappreciated in the HN vector database debate.
- [[entities/notion]] — A popular knowledge management and productivity tool representing the traditional, manually-maintained approach to personal knowledge management.
- [[entities/google-notebooklm]] — Google's AI notebook product that allows users to upload documents and ask questions -- the closest existing product to Karpathy's vision, but lacking persistent wiki compilation.
- [[entities/storm]] — A research system for automated Wikipedia-style article creation using multi-perspective question-asking and retrieval-based outline synthesis.
- [[entities/karma]] — A NeurIPS 2025 Spotlight paper presenting a nine-agent LLM framework for automated knowledge graph enrichment from unstructured scientific text.
- [[entities/freshwiki]] — An evaluation dataset of recent Wikipedia articles created after LLM training cutoffs, introduced by the STORM project to prevent data leakage.
- [[entities/dairai]] — An AI education and research organization whose Academy published the definitive system architecture analysis of Karpathy's LLM knowledge base methodology.

## Comparisons (LLM Knowledge Base Ecosystem)

- [[comparisons/rag-vs-index-based-retrieval]] — Comparing vector-database RAG pipelines with Karpathy's index-based LLM navigation for knowledge base Q&A -- when each approach is appropriate and why.
- [[comparisons/vector-db-vs-bm25-search]] — Comparing dense vector semantic search with sparse keyword-based BM25 retrieval -- and why hybrid approaches combining both outperform either alone.
- [[comparisons/storm-vs-karpathy-workflow]] — Comparing STORM's single-shot automated article generation from web search with Karpathy's persistent, accumulating knowledge base.
- [[comparisons/knowledge-graph-vs-wiki]] — Comparing formal knowledge graphs (nodes/edges with typed relationships) against flat markdown wikis (files with wikilinks) as substrates for LLM-maintained knowledge bases.
- [[comparisons/manual-pkm-vs-llm-pkm]] — Comparing traditional human-authored personal knowledge management (Zettelkasten, Notion, Obsidian notes) with LLM-maintained knowledge bases.
- [[comparisons/fine-tuning-vs-context-window]] — Comparing two strategies for giving LLMs domain knowledge: fine-tuning (encoding knowledge in model weights) vs. context window retrieval (loading knowledge at query time).
- [[comparisons/single-agent-vs-multi-agent]] — Comparing Karpathy's single-LLM approach with multi-agent architectures (KARMA's 9 agents, STORM's perspective agents) for knowledge extraction.
- [[comparisons/obsidian-vs-graph-database]] — Comparing file-system-based knowledge storage (markdown + Obsidian) with graph database storage (SQLite, Neo4j) as substrates for LLM-maintained knowledge bases.

## Sources (Knowledge Graphs & Graph Databases)

- [[sources/graphrag-microsoft-research]] — Microsoft Research's GraphRAG system uses LLM-extracted knowledge graphs with Leiden community detection and hierarchical summarization to dramatically outperform baseline RAG on holistic and cross-document queries.
- [[sources/llm-kg-construction-survey]] — Comprehensive survey cataloguing the paradigm shift from rule-based to LLM-driven knowledge graph construction across ontology engineering, knowledge extraction, and knowledge fusion.
- [[sources/kggen-knowledge-graph-extraction]] — KGGen introduces a three-stage LLM pipeline (extract, aggregate, cluster) for knowledge graph construction from text, outperforming GraphRAG by 18% on the novel MINE benchmark.
- [[sources/kg-llm-link-prediction]] — KG-LLM converts knowledge graph paths to natural language chain-of-thought prompts and fine-tunes LLMs for multi-hop link prediction, dramatically outperforming traditional embedding methods (F1 0.84-0.98 vs 0.25-0.61).
- [[sources/temporal-knowledge-graphs-survey]] — Comprehensive survey of temporal KG representation learning: 10 method categories from TTransE to LLM-based approaches, covering interpolation, extrapolation, entity alignment, and temporal QA.
- [[sources/knowledge-graph-embeddings-overview]] — Comprehensive overview of KGE models: tensor decomposition (DistMult, ComplEx), geometric (TransE family, RotatE), deep learning (ConvE, CapsE), with training methodology, benchmarks, and relationship to modern LLMs.
- [[sources/kg-vs-vector-db-glean]] — Glean's analysis of knowledge graphs vs vector databases for enterprise AI: graphs for explainability and multi-hop reasoning, vectors for semantic search, hybrid architectures combining both as optimal.
- [[sources/rag-vs-kg-enterprise-phyvant]] — Practitioner analysis of RAG vs knowledge graph failure modes in enterprise: RAG lacks entity understanding and temporal awareness; KGs require upfront ontology work; hybrid architecture combining both is optimal.
- [[sources/rdf-vs-property-graph-comparison]] — Synthesized comparison of RDF (edge-centric, W3C standardized, reasoning-capable) vs property graphs (node-centric, performance-optimized, developer-friendly) with LLM integration implications.
- [[sources/allemang-llms-kg-property-graphs]] — Dean Allemang argues LLMs have created a renaissance for ontologies, demonstrating that OWL ontologies and property graphs are complementary (not competing), and LLMs natively understand formal ontological languages.

## Concepts (Knowledge Graphs & Graph Databases)

- [[concepts/graphrag]] — Graph-based Retrieval Augmented Generation: using LLM-extracted knowledge graphs with community detection and hierarchical summarization to dramatically improve RAG for holistic and multi-hop queries.
- [[concepts/knowledge-graph-construction]] — The end-to-end process of building knowledge graphs from unstructured data, now transformed by LLMs from rule-based pipelines to generative frameworks achieving near-human-expert quality.
- [[concepts/knowledge-extraction]] — LLM-driven extraction of entities, relations, and facts from unstructured text — the core pipeline stage of knowledge graph construction, now achieving near-expert accuracy via few-shot prompting.
- [[concepts/knowledge-fusion]] — The process of merging, deduplicating, and reconciling extracted knowledge from multiple sources into a unified knowledge graph.
- [[concepts/ontology-engineering]] — The design of formal schemas (ontologies) that define entity types, relation types, and constraints for knowledge graphs — now increasingly automated by LLMs.
- [[concepts/knowledge-graph-embeddings]] — Machine learning methods that map knowledge graph entities and relations to continuous vector spaces for link prediction, with three model families increasingly complemented by LLM approaches.
- [[concepts/knowledge-graph-completion]] — Predicting missing facts in incomplete knowledge graphs via link prediction — now dramatically improved by LLM-based approaches outperforming traditional embedding methods.
- [[concepts/temporal-knowledge-graphs]] — Knowledge graphs that associate facts with explicit temporal information, enabling reasoning about what was true when — 10+ method categories from translation-based to LLM-integrated.
- [[concepts/rdf-knowledge-representation]] — The W3C-standardized Resource Description Framework for representing knowledge as subject-predicate-object triples with URIs, SPARQL queries, and OWL reasoning.
- [[concepts/property-graphs]] — Node-centric graph data model where nodes and edges carry rich attribute data, optimized for traversal performance and developer experience.
- [[concepts/hybrid-retrieval]] — Combining knowledge graphs and vector databases for AI retrieval: graphs provide entity relationships and multi-hop reasoning while vectors enable semantic search.

## Entities (Knowledge Graphs & Graph Databases)

- [[entities/microsoft-graphrag]] — Open-source modular graph-based RAG system from Microsoft Research with Leiden community detection and hierarchical summarization.
- [[entities/kggen]] — Open-source Python library for LLM-driven knowledge graph extraction using a three-stage pipeline (extract, aggregate, cluster) with GPT-4o and DSPy.
- [[entities/dean-allemang]] — Knowledge graph and semantic web expert who demonstrated that LLMs natively understand OWL ontologies.
- [[entities/karma-framework]] — NeurIPS 2025 Spotlight: 9-agent LLM framework for automated knowledge graph enrichment (83.1% accuracy).

## Comparisons (Knowledge Graphs & Graph Databases)

- [[comparisons/rdf-vs-property-graph]] — RDF (edge-centric, W3C-standardized, reasoning-capable) vs property graphs (node-centric, performance-optimized, developer-friendly).
- [[comparisons/knowledge-graph-vs-vector-database]] — Knowledge graphs (explainability, governance, multi-hop) vs vector databases (semantic search, fast prototyping); hybrid recommended.
- [[comparisons/kge-vs-llm-for-knowledge-graphs]] — Traditional KGE methods (TransE, ComplEx) vs LLM-based approaches: LLMs dominate multi-hop reasoning (F1 0.98 vs 0.61).

## Sources (Embeddings, Vector Search & Retrieval Infrastructure)

- [[sources/pinecone-embedding-models-rundown]] — Pinecone's practical guide comparing OpenAI, Cohere, and E5 embedding models on speed, dimensions, asymmetric search, and MTEB benchmark interpretation.
- [[sources/huggingface-matryoshka-embeddings]] — Hugging Face tutorial on Matryoshka Representation Learning: training embeddings that can be truncated to any dimension with minimal quality loss, preserving 98.37% performance at just 8.3% of original size.
- [[sources/weaviate-hybrid-search-explained]] — Weaviate's technical explanation of hybrid search combining BM25 keyword scoring with dense vector search via Reciprocal Rank Fusion, including the alpha parameter for tuning the balance.
- [[sources/pinecone-hnsw-explained]] — Pinecone's deep technical walkthrough of the HNSW algorithm: multi-layer graph structure, parameters (M, efConstruction, efSearch), performance characteristics on Sift1M, and memory tradeoffs.
- [[sources/jina-colbert-late-interaction]] — Jina AI's technical overview of ColBERT's late interaction mechanism: per-token embeddings with MaxSim scoring, 180-23,000x faster than BERT reranking, and ColBERTv2's 6-10x storage compression.
- [[sources/pinecone-rerankers-two-stage]] — Pinecone's guide to cross-encoder reranking: why bi-encoders lose information, how two-stage retrieval (retrieve top-25, rerank to top-3) improves RAG, and practical impact of moving relevant chunks from position 23 to position 1.
- [[sources/xenoss-vector-db-comparison]] — Detailed comparison of the three leading vector databases: Pinecone (managed, compliance-first), Qdrant (Rust-based, feature-rich), and Weaviate (highest QPS at 791, native hybrid search).
- [[sources/redis-semantic-vs-keyword-search]] — Redis's comprehensive comparison of semantic vs keyword search: complementary failure modes, when to use each, and why production systems need hybrid approaches combining both.
- [[sources/superlinked-hybrid-search-reranking]] — VectorHub's guide to the full RAG retrieval pipeline: BM25 + vector search fusion via RRF or weighted alpha, followed by transformer-based reranking, with specific model recommendations and performance benchmarks.
- [[sources/modal-mteb-leaderboard]] — Modal's analysis of the MTEB leaderboard: 8 task categories, top open-weight models (Qwen3-Embedding-8B, NVIDIA Nemotron, bge-m3), domain-specific outperformance, and the open-source catch-up to proprietary APIs.
- [[sources/weaviate-chunking-strategies]] — Weaviate's comprehensive guide to text chunking for RAG: fixed-size, recursive, semantic, document-based, and advanced strategies (late chunking, hierarchical, agentic), with the baseline recommendation of 512 tokens and 50-100 token overlap.

## Concepts (Embeddings, Vector Search & Retrieval Infrastructure)

- [[concepts/text-embeddings]] — Dense vector representations of text that capture semantic meaning, enabling similarity-based retrieval; the foundation of modern semantic search, RAG, and vector database infrastructure.
- [[concepts/vector-search]] — Finding similar items by computing distance between dense vector embeddings in high-dimensional space, typically using ANN algorithms like HNSW for sub-millisecond retrieval at scale.
- [[concepts/semantic-search]] — Search based on meaning rather than exact terms: transformer models encode text into dense vectors, enabling retrieval of conceptually related content even when queries and documents share no common words.
- [[concepts/keyword-search]] — Lexical search using inverted indexes and BM25 ranking: fast, deterministic, and precise for exact terms, but blind to synonyms and conceptual relationships.
- [[concepts/bm25]] — Best Matching 25: the standard probabilistic ranking algorithm for keyword search, building on TF-IDF with term frequency saturation and document length normalization.
- [[concepts/hybrid-search]] — Combining BM25 keyword search with dense vector search in parallel, merging results via Reciprocal Rank Fusion (RRF), to get the precision of exact matching with the recall of semantic understanding.
- [[concepts/hnsw]] — The dominant graph-based ANN algorithm for vector search: a multi-layer proximity graph enabling O(log n) nearest-neighbor queries with 80-99% recall at 1-50ms latency, used by nearly all major vector databases.
- [[concepts/approximate-nearest-neighbor-search]] — Trading small amounts of accuracy for dramatic speed gains when searching high-dimensional vector spaces: the foundational tradeoff underlying all vector database indexing.
- [[concepts/bi-encoder-vs-cross-encoder]] — The two fundamental architectures for neural text matching: bi-encoders encode texts independently for fast retrieval but lose information; cross-encoders process pairs jointly for high accuracy but cannot scale to full collections.
- [[concepts/reranking]] — Using cross-encoder models to re-score and reorder retrieval candidates, improving RAG precision by 30-50% by applying query-specific analysis to the top-k results from fast initial retrieval.
- [[concepts/two-stage-retrieval]] — The standard RAG retrieval architecture: fast bi-encoder/hybrid retrieval narrows millions of documents to top-k candidates, then a cross-encoder reranker selects the top-n most relevant for the LLM.
- [[concepts/colbert-late-interaction]] — A retrieval paradigm between bi-encoders and cross-encoders: encode queries and documents independently at the token level, then score via MaxSim — achieving near-cross-encoder accuracy at orders of magnitude less compute.
- [[concepts/matryoshka-representation-learning]] — Training technique that produces embeddings usable at any dimension by frontloading important information in earlier dimensions — preserving 98.37% of performance at just 8.3% of original size, now standard in state-of-the-art models.
- [[concepts/chunking-strategies]] — How text is split into segments for embedding and retrieval in RAG: from simple fixed-size splitting (512 tokens, 10-20% overlap) to semantic, hierarchical, and agentic approaches that align chunk boundaries with meaning.

## Entities (Embeddings & Vector Search)

- [[entities/mteb]] — The standard benchmark for evaluating text embedding models: 8 task categories across 56+ English datasets (MMTEB: 131 tasks, 250+ languages), hosted on Hugging Face with a continuously updated leaderboard.
- [[entities/sentence-transformers]] — The leading open-source Python library for text embeddings (Hugging Face): provides pretrained models (all-MiniLM-L6-v2, mpnet), training utilities (MatryoshkaLoss, contrastive losses), and a simple encode() API.
- [[entities/pinecone]] — Fully managed vector database service: proprietary indexing, sub-10ms latency at tens of billions of vectors, SOC 2 + HIPAA + ISO 27001, with Pinecone Assistant for integrated RAG (GA January 2025).
- [[entities/qdrant]] — Open-source vector database written in Rust: HNSW indexing, richest feature set (hybrid search, geo-spatial, multi-vector, sparse vectors), 326 QPS, available as self-hosted, managed cloud, or hybrid deployment.
- [[entities/weaviate]] — Cloud-native open-source vector database: highest QPS (791), native hybrid search with alpha parameter and BM25F, generative module for server-side RAG, HIPAA on AWS (2025).
- [[entities/openai-embeddings]] — OpenAI's embedding API models: text-embedding-ada-002 (1536 dims, legacy), text-embedding-3-small/large (native Matryoshka, up to 3072 dims) — widely used but increasingly matched by open-source alternatives.

## Comparisons (Embeddings & Vector Search)

- [[comparisons/semantic-vs-keyword-search]] — Complementary retrieval approaches: semantic search captures meaning via dense vectors but misses exact identifiers; keyword search matches precise terms via inverted indexes but misses synonyms — production systems combine both.
- [[comparisons/pinecone-vs-qdrant-vs-weaviate]] — The three leading vector databases compared: Pinecone (managed simplicity + compliance), Qdrant (Rust performance + richest features), Weaviate (highest QPS + best hybrid search) — with detailed feature, performance, and pricing tables.
- [[comparisons/bi-encoder-vs-cross-encoder-vs-colbert]] — The three neural retrieval architectures compared: bi-encoders (fast, lossy single-vector), cross-encoders (accurate but slow pairwise scoring), and ColBERT (token-level late interaction bridging both) — with speed, accuracy, and storage tradeoffs.

## Sources (Agentic AI & Tool Use)

- [[sources/superannotate-llm-agents-guide]] — Comprehensive 2026 guide to LLM agent architecture: four components (brain, memory, planning, tools), frameworks, challenges.
- [[sources/martinfowler-function-calling-llm]] — Function calling architecture, security layers, MCP protocol, rules-engine comparison.
- [[sources/ng-agentic-design-patterns]] — Andrew Ng's four agentic design patterns; GPT-3.5 with agentic workflow beats GPT-4 zero-shot.
- [[sources/react-prompting-framework]] — ReAct paper (Yao et al. 2022): Thought-Action-Observation loop; ReAct+Reflexion achieves 130/134 tasks.
- [[sources/mcp-model-context-protocol]] — MCP specification: JSON-RPC 2.0, adopted by OpenAI/Google, donated to Linux Foundation, 97M monthly downloads.
- [[sources/claude-code-agentic-coding]] — Eight 2026 trends: coding-to-coordination, Claude Code $2.5B revenue, Computer Use, real-world impact.
- [[sources/pebblous-agentic-framework-explosion]] — Three 2025 agent frameworks (RL, self-improvement, TDD paths), all bottlenecked by data quality.
- [[sources/multi-agent-collaboration-survey]] — 2025 survey: five-dimension taxonomy of multi-agent collaboration mechanisms.
- [[sources/agentic-memory-unified-framework]] — AgeMem (2026): memory as tool-based actions, trained via three-stage RL.
- [[sources/databricks-agent-design-patterns]] — Design pattern spectrum from LLM+Prompt to multi-agent with orchestration patterns.
- [[sources/devin-ai-software-engineer]] — First autonomous AI software engineer: 13.86% SWE-bench at launch, $20/month with 2.0.

## Concepts (Agentic AI & Tool Use)

- [[concepts/llm-agent-architecture]] — Four-component architecture (brain, memory, planning, tools) and design pattern spectrum.
- [[concepts/agentic-workflows]] — Iterative multi-step LLM workflows: reflection, tool use, planning, multi-agent. Architecture > model size.
- [[concepts/react-pattern]] — Thought-Action-Observation loop: foundational agent execution pattern.
- [[concepts/reflection-pattern]] — Automated self-critique: generate, critique, revise, iterate. Quick to implement, surprising gains.
- [[concepts/tool-use]] — Function calling enabling LLMs to interact with external systems via structured JSON, standardized via MCP.
- [[concepts/agent-memory]] — STM (working) and LTM (persistent) memory. AgeMem unifies both as RL-learned tool actions.
- [[concepts/agent-planning]] — Task decomposition via CoT, ToT, hierarchical planning with ReAct/Reflexion feedback.
- [[concepts/agentic-coding]] — AI agents that autonomously write, test, debug, ship code. Devin (2024) to Claude Code ($2.5B, 2026).
- [[concepts/agent-orchestration]] — Multi-agent coordination: orchestrator-worker, supervisor, router patterns.
- [[concepts/agent-frameworks]] — LangChain/LangGraph, AutoGen, CrewAI, OpenAI Agents SDK, 2025 autonomous wave.
- [[concepts/swe-bench]] — Primary benchmark for LLM SE agents: 1.96% (2024) to 80.9% Claude Opus 4.5 (2026).

## Entities (Agentic AI & Tool Use)

- [[entities/andrew-ng]] — Four agentic design patterns; architecture > model size for enterprises.
- [[entities/claude-code]] — Anthropic's agentic coding tool: $2.5B revenue, 80.9% SWE-bench, Computer Use.
- [[entities/devin-ai]] — First autonomous AI software engineer by Cognition Labs (2024), $20/month with 2.0.

## Comparisons (Agentic AI & Tool Use)

- [[comparisons/claude-code-vs-devin]] — Terminal-first ($2.5B, 80.9%) vs sandboxed ($20/month, first autonomous SE agent).
- [[comparisons/react-vs-reflection-vs-planning]] — Three complementary patterns: best combined (plan, then ReAct, then reflect).

## Sources (Open-Source LLMs & Local Inference)

- [[sources/bentoml-open-source-llms-2026]] — Comprehensive ranking of S-tier open-source LLMs in 2026: Qwen3.5, DeepSeek V3.2, GLM-5, Kimi-K2.5, MiniMax-M2.5, and gpt-oss-120b — all using MoE architectures.
- [[sources/deepseek-revolution-2026]] — DeepSeek V3.2 (685B, MIT) surpassed GPT-5-High on math; Sparse Attention cuts inference costs 70%; catalyzed 1,500+ Chinese open LLMs.
- [[sources/meta-llama-4-multimodal]] — Meta Llama 4 introduced MoE: Scout (109B, 10M context), Maverick (400B, multimodal), Behemoth (2T, STEM benchmark leader).
- [[sources/ollama-complete-guide]] — Ollama (150K+ GitHub stars) abstracts llama.cpp into Docker-like experience with Modelfiles, OpenAI-compatible API, cross-platform GPU support.
- [[sources/ollama-vs-vllm-benchmarks]] — Red Hat benchmarks: vLLM 793 TPS vs Ollama 41 TPS on A100; Ollama for dev, vLLM for production.
- [[sources/mlx-vs-llamacpp-apple-silicon]] — MLX outperforms llama.cpp by 21-87% on <14B models on Apple Silicon; llama.cpp wins for 70B+ via CPU+GPU split.
- [[sources/apple-silicon-llm-inference-study]] — ArXiv study on M2 Ultra: MLX leads throughput (~230 tok/s), all five frameworks viable for production on-device inference.
- [[sources/small-language-models-guide-2026]] — SLMs under 10B params run on 4GB RAM: Phi-4 (beats GPT-4o on MATH), Gemma 3, Qwen 3 4B — 10-30x cheaper than LLMs.
- [[sources/freecodecamp-local-rag-ollama]] — Complete local RAG tutorial: Ollama + Qwen 3 + ChromaDB + LangChain, zero cloud dependency.
- [[sources/open-source-vs-closed-llms-enterprise]] — Enterprise tradeoffs: open-source ~10x cheaper per token; 41% plan to increase usage; projected 50-50 split.
- [[sources/local-llm-hosting-tools-comparison]] — 15+ local LLM tools compared: Ollama (dev CLI), vLLM (production), LM Studio (GUI), Jan (privacy), LocalAI (multimodal).
- [[sources/coding-models-comparison-2026]] — Qwen 2.5 Coder (88.4% HumanEval, Apache 2.0) leads; Codestral (95.3% FIM) for autocomplete; DeepSeek (338 languages, 10GB).

## Concepts (Open-Source LLMs & Local Inference)

- [[concepts/open-source-llms]] — Open-weight LLMs from DeepSeek, Qwen, Meta, Mistral have closed the gap with proprietary models to ~3 months, using MoE and MIT/Apache licensing.
- [[concepts/local-llm-inference]] — Running LLM inference on local hardware (Ollama, vLLM, llama.cpp, MLX) for privacy, offline operation, and zero per-token cost.
- [[concepts/mixture-of-experts]] — Architecture activating subset of parameters per token (e.g., 17B of 400B); dominant in 2025-2026 frontier open models.
- [[concepts/quantization]] — Reducing weight precision (FP16 to 4-bit) to shrink memory 4x and enable local inference on consumer hardware with minimal quality loss.
- [[concepts/apple-silicon-inference]] — Unified memory Macs for local inference; MLX leads <14B throughput, llama.cpp handles larger models via CPU+GPU split.
- [[concepts/small-language-models]] — Sub-10B models (Phi-4, Gemma 3, Qwen 3 4B) running on 4GB RAM; 10-30x cheaper than LLMs, adequate for many tasks.
- [[concepts/local-knowledge-base]] — Running an LLM-powered KB entirely local with Ollama + open models + ChromaDB; privacy, offline, zero cost vs reduced reasoning.
- [[concepts/open-source-coding-models]] — Code LLMs matching GPT-4: Qwen Coder 88.4% HumanEval, Codestral 95.3% FIM, DeepSeek 338 languages.

## Entities (Open-Source LLMs & Local Inference)

- [[entities/deepseek]] — Chinese AI lab; R1 (Jan 2025) triggered the "DeepSeek moment"; V3.2 (685B, MIT) surpassed GPT-5-High on math.
- [[entities/qwen]] — Alibaba's LLM family; Qwen 3.5 (397B MoE) leads reasoning; Qwen 2.5 Coder (88.4% HumanEval) beats GPT-4.
- [[entities/meta-llama]] — Meta's Llama family; Llama 4 introduced MoE with Scout (10M context), Maverick (multimodal), Behemoth (2T).
- [[entities/ollama]] — Most popular local LLM tool (150K+ stars); abstracts llama.cpp with Modelfiles and OpenAI-compatible API.
- [[entities/vllm]] — Production-grade inference engine; PagedAttention achieves 793 TPS on A100 vs Ollama's 41.
- [[entities/llama-cpp]] — C/C++ inference engine; GGUF format, 1.5-8 bit quantization, CPU+GPU splitting, cross-platform.
- [[entities/mlx]] — Apple's ML framework; zero-copy unified memory, leads Apple Silicon throughput on <14B models.
- [[entities/lm-studio]] — Desktop GUI for local LLMs; polished model browser, best for non-technical users.
- [[entities/phi]] — Microsoft's SLM family; Phi-4 (14B) beats GPT-4o on MATH; Phi-4-mini (3.8B) runs on 3GB VRAM.
- [[entities/gemma]] — Google's SLM family; 4B multimodal in 3GB; 270M runs 25 chats on 0.75% phone battery.

## Comparisons (Open-Source LLMs & Local Inference)

- [[comparisons/open-source-vs-closed-llms]] — Performance gap near zero by 2026; open ~10x cheaper per token but requires -190K/year infrastructure; 87% enterprise on closed but shifting.
- [[comparisons/ollama-vs-vllm]] — Ollama (dev, single-user, 41 TPS) vs vLLM (production, multi-user, 793 TPS).
- [[comparisons/local-vs-cloud-knowledge-base]] — Cloud KB superior reasoning for complex compilation; local KB offers privacy/offline/zero cost; hybrid recommended.
- [[comparisons/mlx-vs-llamacpp]] — MLX +21-87% for <14B on Apple Silicon; llama.cpp for large models, cross-platform, fine-grained quantization.

## Sources (RAG & Retrieval Deep-Dive, Research: 2026-04-05)

- [[sources/ragflow-rag-review-2025]] — RAGFlow's 2025 year-end review: RAG evolving from retrieval pattern into a Context Engine combining domain knowledge, tool retrieval, and memory.
- [[sources/rag-vs-finetuning-agriculture]] — ArXiv paper: RAG and fine-tuning are complementary (+6pp fine-tuning, +5pp RAG, 47%→72% geographic transfer).
- [[sources/cache-augmented-generation]] — ArXiv paper: CAG preloads all docs into KV cache, 10x faster (0.85s vs 9.24s), higher BERTScores on small KBs.
- [[sources/microsoft-graphrag]] — Microsoft Research: GraphRAG constructs knowledge graphs with community summaries for holistic queries baseline RAG cannot answer.
- [[sources/raptor-tree-retrieval]] — ICLR 2024: RAPTOR builds recursive summary trees via GMM clustering, +20% absolute on QuALITY benchmark.
- [[sources/colbert-late-interaction]] — Weaviate: ColBERT keeps per-token embeddings with MaxSim scoring, 100x faster than cross-encoders; ColPali/ColQwen for visual docs.
- [[sources/hybrid-search-rag-optimization]] — VectorHub: combining BM25 + vector search via RRF fusion with transformer reranking for production RAG.
- [[sources/hybrid-search-bm25-splade-vector]] — PremAI: BM25 vs SPLADE vs dense vector with three fusion strategies; +26-31% NDCG on BEIR with hybrid.
- [[sources/rag-hallucinations-explained]] — Mindee: RAG hallucination from retrieval failure and fusion errors; Stanford found 17-33% rates in legal tools.
- [[sources/self-reflective-rag-langgraph]] — LangChain: Self-RAG (reflection tokens) and CRAG (web fallback) implemented as LangGraph state machines.
- [[sources/rag-evaluation-metrics-benchmarks]] — Label Your Data: three-tier RAG evaluation (retrieval, generation, operational) with RAGAS, benchmarks, frameworks.
- [[sources/agentic-rag-survey]] — ArXiv survey: agentic RAG taxonomy by agent cardinality, control structure, autonomy level, knowledge representation.

## Concepts (RAG & Retrieval Deep-Dive, Research: 2026-04-05)

- [[concepts/retrieval-augmented-generation]] — The dominant paradigm for grounding LLM outputs in external knowledge: retrieve docs, inject as context, generate. 85% of production LLM apps by 2026.
- [[concepts/cache-augmented-generation]] — RAG alternative: preload all documents into KV cache, eliminating retrieval. 10x faster, higher accuracy on small, stable knowledge bases.
- [[concepts/graphrag]] — Microsoft's graph-based RAG: constructs knowledge graphs from text, clusters into communities with summaries, answers holistic queries baseline RAG cannot.
- [[concepts/raptor]] — ICLR 2024: recursive clustering + abstractive summarization into a tree structure. +20% on QuALITY; 18-57% of useful nodes from summary layers.
- [[concepts/agentic-rag]] — Current frontier: agents orchestrate retrieval via reflection, planning, tool use. Router + Retriever + Grader + Generator + Hallucination Checker.
- [[concepts/self-rag]] — Self-Reflective RAG: four reflection tokens (Retrieve, ISREL, ISSUP, ISUSE) enable model to self-assess retrieval need and output quality.
- [[concepts/corrective-rag]] — CRAG: lightweight retrieval evaluator + web search fallback + document strip grading for knowledge refinement.
- [[concepts/hybrid-search]] — Combining BM25/SPLADE (sparse) with vector (dense) retrieval via RRF or convex combination. +26-31% NDCG on BEIR benchmarks.
- [[concepts/rag-hallucinations]] — Fabricated outputs despite grounding sources: retrieval failure, fusion errors, confidence misalignment. 17-33% in legal RAG tools.
- [[concepts/rag-evaluation]] — Three-tier measurement: retrieval (Precision@k, MRR, nDCG), generation (faithfulness, hallucination rate), operational (latency, safety).
- [[concepts/colbert]] — ColBERT: per-token late interaction retrieval, 100x faster than cross-encoders, 10,000x fewer FLOPs, strong zero-shot. ColPali/ColQwen for visual docs.
- [[concepts/late-interaction-retrieval]] — Paradigm between bi-encoders and cross-encoders: independently encode, keep per-token embeddings, compute MaxSim at query time.
- [[concepts/splade]] — Learned sparse retrieval with transformer-based vocabulary expansion. Outperforms BM25 on BEIR while maintaining inverted index compatibility.
- [[concepts/hierarchical-retrieval]] — Multi-level abstraction retrieval: RAPTOR (trees), GraphRAG (graphs), TreeRAG (document structure).
- [[concepts/context-engineering]] — (Updated) RAG evolving into unified Context Engine serving domain knowledge, tool retrieval, and conversation state.
- [[concepts/fine-tuning]] — (Updated) RAG + fine-tuning complementary: volatile knowledge in retrieval, stable behavior in fine-tuning.

## Entities (RAG & Retrieval Deep-Dive, Research: 2026-04-05)

- [[entities/ragas]] — Leading open-source framework for reference-free RAG evaluation: faithfulness, context precision/recall, answer relevancy metrics.
- [[entities/langgraph]] — LangChain's state machine framework for agentic RAG: cycles, conditional routing, persistent state, execution traces.
- [[entities/microsoft-research]] — Developed GraphRAG and LazyGraphRAG; available as open-source on GitHub and in Azure Discovery.
- [[entities/raptor-paper]] — ICLR 2024 paper by Sarthi, Abdullah et al.: recursive tree retrieval achieving +20% on QuALITY benchmark.

## Comparisons (RAG & Retrieval Deep-Dive, Research: 2026-04-05)

- [[comparisons/rag-vs-cag]] — RAG (unlimited KB, selective retrieval) vs CAG (10x faster, preload all, limited to context window size).
- [[comparisons/bm25-vs-vector-search]] — BM25 (exact match, no training) vs vector (semantic, GPU required): use both via hybrid for +26-31% NDCG.
- [[comparisons/naive-vs-advanced-vs-agentic-rag]] — Three evolutionary phases: naive (fixed pipeline) → advanced (optimized retrieval) → agentic (self-correcting agent loops).

## Tokenization & Text Processing

### Sources
- [[sources/raschka-bpe-from-scratch]] — Sebastian Raschka's hands-on tutorial building a BPE tokenizer from scratch, covering the three-step algorithm, encoding/decoding, and GPT-2 compatibility.
- [[sources/huggingface-tokenization-algorithms]] — Hugging Face's authoritative reference comparing BPE, WordPiece, Unigram, and SentencePiece with worked examples and model mappings.
- [[sources/kamali-tokenization-killing-multilingual]] — Omar Kamali argues tokenization is the structural barrier preventing multilingual LLMs, identifying four compounding taxes on low-resource languages.
- [[sources/trott-tokenization-llms]] — Sean Trott explains how LLMs process tokens (not words), the subword-morpheme disconnect, and mixed research findings on morphological tokenization.
- [[sources/karpathy-minbpe-lecture]] — Karpathy's 2h13m lecture building a GPT tokenizer from scratch, cataloging LLM problems (spelling, arithmetic, non-English) traceable to tokenization.
- [[sources/rohan-paul-vocabulary-size-tradeoffs]] — Vocabulary size trade-offs across GPT-4 (~100k), LLaMA 3 (~128k), Mistral (~131k), showing diminishing returns beyond 100k.
- [[sources/evabyte-tokenization-free-model]] — EvaByte: 6.5B tokenization-free byte-level LM matching token-based models, using multibyte prediction and EVA attention.
- [[sources/ali-tokenizer-choice-negligible-crucial]] — Ali et al. train 24 LLMs varying tokenizer algorithm/library/vocab-size; finding tokenizer choice is crucial, not negligible.
- [[sources/winder-token-count-practical-guide]] — Practical guide to counting tokens for LLM APIs using tiktoken, AutoTokenizer, with cost optimization strategies.
- [[sources/github-faster-bpe-tokenizer]] — GitHub's open-source BPE tokenizer achieves 4x tiktoken speed using Aho-Corasick automaton with linear time complexity.

### Concepts
- [[concepts/tokenization]] — The process of converting raw text into discrete integer tokens that LLMs process — the fundamental first step in all language model pipelines.
- [[concepts/byte-pair-encoding]] — The most popular tokenization algorithm for LLMs — iteratively merges frequent adjacent byte pairs, used by GPT, Llama, Gemma, Qwen.
- [[concepts/subword-tokenization]] — The dominant paradigm: splitting text between words and characters, keeping frequent words intact while decomposing rare words into subword pieces.
- [[concepts/wordpiece]] — BERT-family tokenization algorithm; like BPE but merges pairs maximizing training data likelihood rather than simple frequency.
- [[concepts/unigram-tokenization]] — Top-down probabilistic algorithm starting with a large vocabulary and iteratively pruning least impactful tokens; used by T5, BigBird.
- [[concepts/sentencepiece]] — Language-agnostic tokenization library applying BPE or Unigram on raw text streams; critical for languages without whitespace.
- [[concepts/vocabulary-size-tradeoffs]] — The tension between vocabulary size, sequence length, embedding overhead, and language coverage; modern LLMs trend toward 100k-131k tokens.
- [[concepts/multilingual-tokenization]] — The structural barrier preventing equitable LLM performance; English-trained tokenizers create 2-15x overhead for low-resource languages.
- [[concepts/byte-level-models]] — Models processing raw UTF-8 bytes instead of tokens, eliminating tokenization; EvaByte and BLT now match tokenized models at scale.
- [[concepts/token-counting]] — Practical techniques for measuring token usage in LLM applications; critical for cost management and context window budgeting.

### Entities
- [[entities/tiktoken]] — OpenAI's fast BPE tokenizer library (Rust + Python) for counting tokens in GPT models.
- [[entities/minbpe]] — Karpathy's minimal reference implementation of BPE — the most cited educational tokenization codebase.
- [[entities/evabyte]] — 6.5B open-source tokenization-free byte-level language model from HKU/SambaNova using multibyte prediction and EVA attention.
- [[entities/sebastian-raschka]] — ML researcher/educator; author of "Build a Large Language Model From Scratch" and BPE implementation tutorials.
- [[entities/philip-gage]] — Inventor of Byte Pair Encoding (1994), originally for text compression, later adapted for LLM tokenization.

### Comparisons
- [[comparisons/bpe-vs-wordpiece-vs-unigram]] — BPE (frequency merging, GPT/Llama) vs WordPiece (likelihood merging, BERT) vs Unigram (probabilistic pruning, T5); no single winner across all tasks.

## Sources (LLM Inference Optimization)

- [[sources/premai-llm-cost-optimization-guide]] — PremAI 2026 guide: 8 layered strategies (prompt optimization, caching, routing, batching, self-hosting, monitoring) achieving 80% API cost reduction with fintech case study.
- [[sources/anthropic-prompt-caching]] — Anthropic's prompt caching: 90% cost reduction and 79% latency improvement for repeated context, tiered write/read pricing across Claude model family.
- [[sources/bentoml-speculative-decoding]] — BentoML handbook: speculative decoding achieves 2-3x speedup by pairing fast draft model with target verifier, practical guidance on acceptance rates and deployment.
- [[sources/bentoml-batching-strategies]] — BentoML handbook: evolution from static to continuous batching, achieving 23x throughput and 90%+ GPU utilization via iteration-level scheduling.
- [[sources/premai-inference-servers-compared]] — 2026 comparison: SGLang leads throughput by 29%, vLLM is safe production default, TGI entered maintenance mode, Triton suits NVIDIA enterprise.
- [[sources/redis-token-optimization]] — Redis guide: semantic caching achieves 73% cost reduction, output tokens matter more than input for latency, multi-tier caching eliminates inference calls.
- [[sources/kv-cache-optimization-techniques]] — Deep technical review: GQA (8x reduction), SWA (2x), PagedAttention (waste 60-80% to 4%), distributed caching for million-token contexts.
- [[sources/quantization-gptq-gguf-awq]] — Grootendorst comparison: GPTQ (GPU-optimized, most adopted), GGUF (CPU-friendly, Apple), AWQ (best speed-quality via activation-aware compression).
- [[sources/ibm-llm-routing]] — IBM Research: predictive routers trained on HELM benchmarks matched GPT-4 quality while saving 5 cents/query; 13B models beat 70B on specialized tasks.
- [[sources/on-device-llms-2026]] — Meta AI Research: sub-1B to 3B models now practical on mobile with 4-bit quantization, ExecuTorch 1.0, and 20ms/token latency.

## Concepts (LLM Inference Optimization)

- [[concepts/llm-inference-optimization]] — Umbrella discipline: reducing latency, cost, and resource consumption through KV cache, batching, quantization, speculative decoding, and serving infrastructure.
- [[concepts/llm-cost-optimization]] — 8-strategy framework for 50-85% API cost reduction: prompt optimization, caching, routing, batching, output constraints, self-hosting.
- [[concepts/kv-cache]] — Attention KV cache stores pre-computed vectors; management (PagedAttention, GQA, SWA) is the central bottleneck of LLM inference.
- [[concepts/speculative-decoding]] — Draft-then-verify technique: small model proposes tokens, large model verifies in parallel, achieving 2-3x lossless speedup.
- [[concepts/continuous-batching]] — Iteration-level scheduling where completed sequences are immediately replaced, achieving 23x throughput and 90%+ GPU utilization.
- [[concepts/model-routing]] — Intelligent dispatching of queries to appropriately-sized models based on complexity, achieving 40-85% cost reduction.
- [[concepts/semantic-caching]] — Caching LLM responses keyed by semantic similarity using vector embeddings, achieving 61-73% cost reduction.
- [[concepts/token-optimization]] — Systematic reduction of token consumption through prompt compression, output constraints, and context assembly optimization.
- [[concepts/edge-inference]] — Running LLMs on mobile devices: sub-3B models with 4-bit quantization achieve <20ms/token, zero API cost, full privacy.
- [[concepts/llm-serving-frameworks]] — Production LLM serving: vLLM (default), SGLang (throughput leader), Triton (enterprise), TGI (maintenance mode).
- [[concepts/llm-api-pricing]] — 2026 pricing landscape: 80% drop since 2025, output 3-5x more than input, premium-to-lightweight gap 60-300x.
- [[concepts/batch-inference]] — Bulk processing at discounted rates (50% via batch APIs) or server-level continuous batching for throughput.

## Entities (LLM Inference Optimization)

- [[entities/vllm]] — (updated) Production LLM serving engine: PagedAttention, 14-24x throughput, broadest hardware support; 2026 H100 benchmarks added.
- [[entities/sglang]] — Open-source LLM serving: RadixAttention, 16,215 tok/s on H100, 29% faster than vLLM for multi-turn workloads.
- [[entities/executorch]] — Meta's on-device inference framework: 50KB footprint, 12+ backends, 1.0 GA October 2025, serves billions of users.
- [[entities/redis]] — In-memory platform for LLM semantic caching: LangCache stores query embeddings, 73% cost reduction, sub-millisecond vector search.
- [[entities/ibm-research]] — AI research: predictive LLM routing using HELM benchmarks, RouterBench evaluation.

## Comparisons (LLM Inference Optimization)

- [[comparisons/gptq-vs-awq-vs-gguf]] — GPTQ (GPU default, largest ecosystem) vs AWQ (best speed-quality, Marlin 741 tok/s) vs GGUF (CPU/Apple via llama.cpp).
- [[comparisons/vllm-vs-sglang]] — vLLM (safe production default, broadest hardware) vs SGLang (throughput leader +29%, automatic KV cache reuse via RadixAttention).


## LLM Evaluation, Benchmarks & Quality Assessment (Research: 2026-04-05)

### Sources
- [[sources/confident-ai-llm-evaluation-metrics]] — Comprehensive taxonomy of LLM evaluation metrics: statistical scorers (BLEU, ROUGE), model-based (BERTScore, NLI), LLM-as-a-Judge (G-Eval, DAG, QAG), and domain-specific RAG/agent metrics.
- [[sources/eugeneyan-llm-evaluators]] — Data-rich analysis of LLM-as-Judge effectiveness: GPT-4 achieves 85% agreement with humans on MT-Bench, but exhibits position bias (50-70%), verbosity bias (>90%), and self-enhancement bias (10-25%).
- [[sources/cameron-wolfe-llm-as-judge]] — Deep dive into LLM-as-a-Judge methodology: three scoring approaches, critical biases with quantified severity, and practical mitigation strategies.
- [[sources/datadog-hallucination-detection]] — Datadog production hallucination detection: rubric-based LLM-as-a-Judge with structured output, two-stage prompting achieving 0.81-0.84 F1.
- [[sources/evidentlyai-llm-evaluation-guide]] — Practical evaluation framework: model vs product evaluation, six evaluation scenarios, five-phase implementation workflow.
- [[sources/raschka-state-of-llms-2025]] — Sebastian Raschka's annual review: 'benchmaxxing' crisis, benchmark saturation, contamination, only 4 of 15 benchmarks predict production outcomes.
- [[sources/openfactcheck-factuality-framework]] — OpenFactCheck unifies LLM factuality evaluation with ResponseEvaluator, FactQA (6,480 examples), and FactBench (4,507 annotated examples).
- [[sources/deepset-rag-groundedness]] — deepset production groundedness monitoring: numerical scoring, document reference analysis, cost optimization (40% savings), statement-level citations.
- [[sources/responsible-ai-labs-benchmarks-2025]] — Comprehensive benchmark taxonomy across seven dimensions plus safety datasets (HEx-PHI, RAIL-HH-10K) and real-world failure cases.
- [[sources/chatbot-arena-methodology]] — Chatbot Arena crowdsourced evaluation: anonymous pairwise battles with 300+ models, 1.5M+ preferences, Elo/Bradley-Terry scoring.

### Concepts
- [[concepts/llm-evaluation-metrics]] — Taxonomy of metrics for evaluating LLM output quality: statistical scorers, LLM-as-Judge methods, and domain-specific metrics for RAG, agents, safety, and factuality.
- [[concepts/llm-as-judge]] — Using powerful LLMs to evaluate other LLMs; achieves 80-85% human agreement but exhibits position, verbosity, and self-enhancement biases requiring active mitigation.
- [[concepts/evaluation-bias]] — Systematic biases in LLM-based evaluation: position bias (2.5%-82.5% win-rate swing), verbosity bias (>90%), self-enhancement (87.76%), with mitigation strategies.
- [[concepts/hallucination-detection]] — Methods for detecting LLM hallucinations: white-box (semantic entropy), black-box (LLM-judge, SelfCheckGPT), rubric-based approaches achieving 0.81-0.86 F1.
- [[concepts/faithfulness-and-groundedness]] — Whether LLM outputs are factually consistent with provided context; the positive framing of not hallucinating. Core metric for RAG and KB quality.
- [[concepts/llm-benchmarks]] — Standardized evaluation datasets: MMLU (knowledge), HELM (holistic), TruthfulQA (factuality), HumanEval (code), MT-Bench (conversation), Chatbot Arena (crowdsourced).
- [[concepts/benchmark-saturation]] — The crisis of benchmark reliability: benchmaxxing, data contamination, MMLU saturated above 90%, only 4 of 15 predict production outcomes.
- [[concepts/automated-fact-checking]] — Automated verification of LLM claims: claim decomposition, evidence retrieval, verdict generation via OpenFactCheck, FIRE, and VERIFAID.
- [[concepts/evaluation-workflow]] — Phased approach: define criteria, build datasets, run experiments, stress-test, deploy production monitoring, iterate.

### Entities
- [[entities/deepeval]] — Open-source LLM evaluation framework by Confident AI with 14+ built-in metrics, Pytest-like API, and CI/CD integration.
- [[entities/g-eval]] — LLM-as-a-Judge scoring method using chain-of-thought reasoning before evaluation; produces scores with optional token probability normalization.
- [[entities/mt-bench]] — Fixed 80-question multi-turn benchmark across 8 categories, created by LMSYS for evaluating LLM conversation quality.
- [[entities/chatbot-arena]] — Crowdsourced LLM evaluation platform: anonymous pairwise battles with 300+ models and 1.5M+ preferences using Elo/Bradley-Terry scoring.
- [[entities/openfactcheck]] — Unified framework for LLM factuality evaluation with three modules: ResponseEvaluator, LLMEvaluator (FactQA), FactCheckerEvaluator (FactBench).
- [[entities/mmlu]] — Most widely-cited LLM knowledge benchmark: 15,908 questions across 57 subjects; saturated above 90% for frontier models.
- [[entities/helm]] — Most comprehensive academic LLM evaluation: 42 scenarios, 7 metrics, 16+ models with standardized methodology.
- [[entities/truthfulqa]] — 817-question benchmark testing misconception propagation; state-of-the-art models score surprisingly low on truthfulness.
- [[entities/prometheus]] — Open-source LLM evaluator fine-tuned on 100K GPT-4 samples; achieves 0.897 Pearson correlation with human judgments.

### Comparisons
- [[comparisons/static-vs-dynamic-benchmarks]] — Static benchmarks (MMLU, fixed) suffer contamination/saturation; dynamic (Arena, LiveCodeBench) resist gaming but reduce reproducibility.
- [[comparisons/llm-judge-vs-human-evaluation]] — LLM judges (sub-, sub-minute, 80-85% agreement) vs humans (gold standard for factuality, safety, edge cases); hybrid approach recommended.
- [[comparisons/ragas-vs-deepeval]] — RAGAS (RAG-specialized, reference-free) vs DeepEval (general LLM eval, 14+ metrics, Pytest API, agent/safety support).

## Sources (MCP, Tool Ecosystems & Agent Protocols)

- [[sources/wikipedia-model-context-protocol]] — Wikipedia overview of MCP: history, architecture (JSON-RPC 2.0), adoption timeline, SDKs in 11 languages, security concerns.
- [[sources/anthropic-mcp-announcement]] — Anthropic's Nov 2024 MCP launch: motivation (models isolated behind silos), client-server architecture, initial partners (Block, Zed, Replit).
- [[sources/pento-year-of-mcp-review]] — Year-in-review: 97M SDK downloads, 10K+ servers, security vulnerabilities, Skills vs MCP distinction, 2026 predictions.
- [[sources/anthropic-mcp-linux-foundation]] — Dec 2025 MCP donation to AAIF (Linux Foundation); co-founded by Anthropic, Block, OpenAI; supported by Google, Microsoft, AWS.
- [[sources/descope-mcp-vs-function-calling]] — Deep comparison: MCP (provider-agnostic, per-server isolation) vs function calling (tight coupling, all-or-nothing security).
- [[sources/zilliz-function-calling-vs-mcp-vs-a2a]] — Three-way comparison showing protocols at different layers: function calling/MCP (tools), A2A (agent collaboration).
- [[sources/google-ai-agent-protocols]] — Google's six-protocol agent stack: MCP, A2A, UCP, AP2, A2UI, AG-UI — all integrated via ADK.
- [[sources/composio-api-integration-patterns]] — Five integration patterns taxonomy: direct API → function calling → MCP gateway → unified API → A2A.
- [[sources/anthropic-building-effective-agents]] — Canonical guide: augmented LLM as building block, five workflow patterns, tool engineering as first-class design concern.
- [[sources/anthropic-code-execution-mcp]] — Code execution pattern: agents write code to interact with MCP servers, 98.7% token savings, PII filtering, persistent state.

## Concepts (MCP, Tool Ecosystems & Agent Protocols)

- [[concepts/model-context-protocol]] — (updated) Open standard (JSON-RPC 2.0) for connecting AI models to external tools — "USB-C for AI". 12K+ servers, 97M SDK downloads.
- [[concepts/function-calling]] — Provider-specific tool invocation (OpenAI, Anthropic, Google each different). Simple for prototyping but creates M×N problem and vendor lock-in.
- [[concepts/tool-use-standards]] — Evolution from vendor-specific function calling (2023) to universal MCP (2024) to six-protocol agent stack (2026).
- [[concepts/mcp-ecosystem]] — 12K+ MCP servers across public registries; shift from local stdio to remote HTTP/SSE transport; enterprise adoption accelerating.
- [[concepts/mcp-security]] — Prompt injection via tool descriptions, tool spoofing, OAuth vulnerabilities, toxic agent data exfiltration; per-server isolation as mitigation.
- [[concepts/mcp-code-execution-pattern]] — Anthropic's optimization: agents write code to interact with MCP tools, achieving 98.7% token savings and PII filtering.
- [[concepts/agent-to-agent-protocol]] — Google's A2A protocol: agents publish Agent Cards for capability discovery and dynamic task delegation. Complementary to MCP.
- [[concepts/augmented-llm]] — Foundational building block of agentic AI: LLM enhanced with retrieval, tool integration, and memory.
- [[concepts/agentic-workflow-patterns]] — Five canonical patterns (Anthropic): prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer.
- [[concepts/ai-agent-integration-patterns]] — Five patterns for connecting agents to external systems: direct API, function calling, MCP gateway, unified API, A2A.

## Entities (MCP, Tool Ecosystems & Agent Protocols)

- [[entities/agentic-ai-foundation]] — Linux Foundation directed fund governing MCP; co-founded by Anthropic, Block, OpenAI (Dec 2025).
- [[entities/google-adk]] — Google's Agent Development Kit: framework integrating six agent protocols (MCP, A2A, UCP, AP2, A2UI, AG-UI).

## Comparisons (MCP, Tool Ecosystems & Agent Protocols)

- [[comparisons/mcp-vs-function-calling]] — MCP (provider-agnostic, secure, scalable) vs function calling (simple, fast setup). MCP for production; function calling for prototypes.

## AI Product Design & Human-AI Collaboration (Research: 2026-04-05)

### Sources
- [[sources/shapeof-ai-ux-patterns]] — Comprehensive catalog of 57 AI UX design patterns in six categories: Wayfinders, Prompt Actions, Tuners, Governors, Trust Builders, and Identifiers.
- [[sources/zhuo-conversational-interfaces]] — Julie Zhuo argues chat interfaces were a breakthrough for accessibility but create five critical UX problems; the real opportunity is AI-powered personalization of how content is presented.
- [[sources/smashing-practical-xai-ux]] — Four practical XAI design patterns (Because Statement, What-If Interactive, Highlight Reel, Push-and-Pull Visual) plus the Goldilocks Principle for calibrating explanation depth.
- [[sources/microsoft-copilot-ux-guidance]] — Microsoft's official UX guidance for copilot-style AI: three focus frameworks (Immersive/Assistive/Embedded), three foundational principles, and detailed collaborative UX input/output design tips.
- [[sources/sapphire-ai-native-applications]] — Sapphire Ventures' 5-D framework for evaluating AI-native enterprise software: Design, Data, Domain Expertise, Dynamism, Distribution.
- [[sources/uxforai-12-llm-product-practices]] — Twelve actionable practices for shipping LLM products: thin-slice MVPs, master-LLM routing, customer-driven training, data collection first iteration.
- [[sources/schmidt-designing-human-ai-collaboration]] — Five-principle framework (Transparency, Personalization, Control, Resilience, Trust) with Figma Make as exemplar; "trust, not attention, is the true currency."
- [[sources/arxiv-interface-design-human-ai-decisions]] — arXiv study: human+AI teams perform worse than AI alone due to automation bias; confidence levels help but cognitive forcing functions backfire.
- [[sources/progressive-disclosure-ai-pattern]] — Progressive disclosure as AI design pattern: 2-3 layers max; RAG itself is progressive disclosure at the data layer.

### Concepts
- [[concepts/ai-ux-design-patterns]] — Emerging taxonomy of 57+ interaction patterns for AI products, covering the full lifecycle from onboarding to oversight.
- [[concepts/copilot-pattern]] — The dominant AI product architecture where AI assists alongside humans — three focus variants: Immersive, Assistive, Embedded.
- [[concepts/conversational-ui-vs-structured-ui]] — Chat achieves 70% but fails at refinement; hybrid approaches (conversation + structured UI) are the emerging winner.
- [[concepts/blank-page-problem]] — Empty chat box provides no affordance for capabilities — solved by Wayfinder patterns (Suggestions, Templates, Gallery).
- [[concepts/trust-in-ai]] — Trust is the true currency of AI products — built through transparency, appropriate friction, citations, and consistent competence.
- [[concepts/trust-calibration]] — Matching user reliance on AI with actual reliability — the engagement-overload paradox means more explanation can backfire.
- [[concepts/human-ai-collaboration-design]] — Product design discipline for AI collaboration: five principles with fluid control between human and AI.
- [[concepts/progressive-disclosure-ai]] — Foundational AI pattern: reveal complexity in 2-3 layers max; RAG is progressive disclosure at the data layer.
- [[concepts/explainable-ai-ux]] — Four design patterns for XAI in products: Because Statement, What-If Interactive, Highlight Reel, Push-and-Pull Visual.
- [[concepts/personalization-in-ai]] — The billion-dollar opportunity: adapting how AI presents information, not just what.
- [[concepts/ai-native-design]] — Products where AI is fundamental, not supplementary — evaluated across five dimensions (5-D framework).
- [[concepts/collaborative-ux]] — Microsoft's framework: tight input-output feedback loops, history, appropriate friction, citations, editable outputs.
- [[concepts/llm-product-development]] — Fundamentally different from traditional software: thin-slice MVPs, provisional approvals, customer-driven training, data collection first.
- [[concepts/knowledge-base-product-gap]] — (Updated) Now includes detailed product design specifications based on AI UX research.

### Entities
- [[entities/julie-zhuo]] — Former VP Design at Meta; five problems with conversational UI; personalization as the billion-dollar opportunity.
- [[entities/figma]] — Collaborative design tool; Figma Make exemplifies AI-native collaboration with NL prompts + creative control.
- [[entities/hax-toolkit]] — Microsoft Research's design library for human-AI interaction with lifecycle-stage guidelines.
- [[entities/sapphire-ventures]] — Enterprise VC; developed the 5-D framework for evaluating AI-native applications.
- [[entities/shape-of-ai]] — Community catalog of 57 AI UX design patterns — the most comprehensive open taxonomy.

### Comparisons
- [[comparisons/conversational-vs-structured-vs-hybrid-ai-ui]] — Three UI paradigms compared: chat excels at intent but fails at refinement; structured excels at precision; hybrid is the emerging winner.

## Sources (Collective Intelligence & Collaborative Knowledge)

- [[sources/brookings-ai-collective-intelligence]] — Brookings analysis: AI as translation engine bridging design-minded collaboration rooms and model-minded simulations for better collective problem-solving.
- [[sources/cip-whitepaper-collective-intelligence]] — CIP whitepaper proposes collective intelligence mechanisms (quadratic voting, liquid democracy, citizens' assemblies) to escape the trilemma of progress vs. safety vs. participation in AI governance.
- [[sources/wikiedu-ai-wikipedia-editing-2025]] — Wiki Education audit: 5.8% of articles AI-generated since 2022; two-thirds of AI-flagged articles failed verification; 87% of editors found AI helpful for research but not content generation.
- [[sources/ai-in-wikimedia-projects]] — Comprehensive history of AI in Wikipedia: from rambot (2002) through ClueBot NG to the 2025-2026 LLM content generation crisis, policy battles, and the symbiotic-parasitic relationship between AI and Wikipedia.
- [[sources/cip-generative-ai-digital-commons]] — CIP working paper: generative AI simultaneously depends on and threatens digital commons — identifies 7 risks and 3 governance proposals.
- [[sources/cohumain-collective-intelligence-human-ai]] — Carnegie Mellon/Illinois: COHUMAIN framework with Transactive Systems Model (memory, attention, reasoning) for understanding when human-AI teams achieve collective intelligence vs. when AI undermines it.
- [[sources/reeves-automated-wikipedia-content-review]] — Systematic review of 51 papers on automated Wikipedia content generation: five technical approaches, massive evaluation gap (only 4 of 51 engaged editors).
- [[sources/federated-wiki-cunningham]] — Ward Cunningham's Federated Wiki: forking-based collaborative knowledge where multiple perspectives coexist ('chorus of voices').
- [[sources/wisdom-of-the-crowd]] — Crowd wisdom: Galton's ox experiment, Surowiecki's conditions, Page's diversity prediction theorem, digital-era challenges.
- [[sources/knowledge-commons-overview]] — Knowledge commons: non-subtractible shared resources, Hess/Ostrom governance, copyleft licensing, AI-era enclosure tension.

## Concepts (Collective Intelligence & Collaborative Knowledge)

- [[concepts/collective-intelligence]] — The capacity of groups to outperform individuals through diverse, independent contributions aggregated via structured mechanisms — now being fundamentally reshaped by AI.
- [[concepts/wisdom-of-crowds]] — Aggregated independent judgments from diverse groups outperform individual experts — mathematically formalized by Page's Diversity Prediction Theorem.
- [[concepts/wikipedia-knowledge-model]] — Wikipedia's collaborative editorial model — anyone can edit, consensus-driven, verifiability over truth — the most successful collective knowledge creation system, now under AI stress.
- [[concepts/collaborative-knowledge-building]] — Structured group processes for creating shared knowledge — three paradigms: consensus (Wikipedia), plurality (Federated Wiki), accumulation (LLM-KB).
- [[concepts/knowledge-commons]] — Collectively owned non-subtractible knowledge resources — now facing existential challenge as AI extracts value while degrading the ecosystem.
- [[concepts/human-ai-collaboration]] — Human-AI teams for knowledge creation — COHUMAIN framework; sobering finding: human-only teams currently outperform human-AI teams in information sharing.
- [[concepts/federated-knowledge]] — Distributed knowledge architectures: Cunningham's Federated Wiki ('chorus of voices'), Wikibase federation (underlays, overlays, interlace).
- [[concepts/ai-generated-content-risks]] — Risks beyond hallucination: subtle misattribution, content homogenization, verification overwhelm, contribution displacement.
- [[concepts/ai-alignment-democratic]] — Citizens' assemblies, quadratic voting, liquid democracy for AI alignment (CIP + Anthropic Collective Constitutional AI).
- [[concepts/transactive-memory-systems]] — Distributed cognition architecture: who knows what, coordinated attention and reasoning — augmented and threatened by AI (COHUMAIN).
- [[concepts/digital-commons-governance]] — Ostrom's principles applied to digital knowledge; AI-era governance gap; CIP's three governance proposals.

## Entities (Collective Intelligence & Collaborative Knowledge)

- [[entities/collective-intelligence-project]] — Nonprofit R&D lab (Siddarth, Huang) for CI mechanisms in AI governance — Collective Constitutional AI with Anthropic, Global Dialogues (70+ countries).
- [[entities/ward-cunningham]] — Inventor of the wiki (1995) and Federated Wiki (2011) — 'a chorus of voices' via forking rather than consensus.
- [[entities/wikipedia]] — World's largest collaboratively edited encyclopedia (60M+ articles) — paradigmatic CI and knowledge commons, navigating AI crisis.
- [[entities/wikidata]] — Wikimedia's structured knowledge base — 100M+ items, SPARQL endpoint, linked to 7,500+ external databases.
- [[entities/elinor-ostrom]] — Nobel Prize-winning commons governance theorist; framework adapted to digital knowledge commons by Hess.

## Comparisons (Collective Intelligence & Collaborative Knowledge)

- [[comparisons/consensus-vs-federated-vs-ai-knowledge]] — Wikipedia consensus vs Federated Wiki plurality vs AI-compiled knowledge: authority, diversity, verification, scalability.

## Sources (Obsidian as Knowledge Platform, Research: 2026-04-05)
- [[sources/dsebastien-obsidian-plugins-2026]] — Comprehensive guide to 75+ Obsidian plugins organized by category — identifies Dataview, Templater, and QuickAdd as the foundational trio for power users.
- [[sources/stephango-file-over-app]] — Steph Ango's manifesto for digital longevity: files you control in open formats outlast any app — Obsidian is built on this principle.
- [[sources/stephango-vault-organization]] — Steph Ango's personal vault structure: flat folders, profuse internal links, fractal journaling, 7-point rating system, and bottom-up emergent organization.
- [[sources/stephango-dialectic-interview]] — Deep interview with Obsidian CEO: five company principles (independence, no investors, small team, privacy, data durability), design as care, constraints as creativity.
- [[sources/nxcode-obsidian-ai-second-brain-2026]] — Complete 2026 guide to AI-powered Obsidian: Smart Connections, Copilot, Claude Code + MCP integration, context engineering principles.
- [[sources/systemsculpt-obsidian-ai-plugins-2026]] — Workflow-first evaluation of four AI plugin categories: governed workflows, inbox organization, agent autonomy, and local retrieval.
- [[sources/obsidian-copilot-overview]] — Copilot for Obsidian: model-agnostic AI assistant with vault RAG, project workspaces, diff-preview composer, and 100K+ users — all data stored as plain markdown.
- [[sources/pkm-comparison-obsidian-notion-logseq]] — 2026 three-way PKM comparison: Obsidian dominates for solo knowledge workers (local, 200ms, free), Notion for teams (cloud, real-time), Logseq for open-source block-based outlining.

### Concepts (Obsidian as Knowledge Platform)
- [[concepts/obsidian-plugin-ecosystem]] — Obsidian's 2,700+ community plugin ecosystem transforms a markdown editor into a programmable knowledge platform.
- [[concepts/obsidian-ai-integration]] — Two paradigms for AI in Obsidian: plugin-based (Copilot, Smart Connections) and external-agent (Claude Code + MCP) — converging toward governed autonomous vault operations.
- [[concepts/file-over-app]] — (Updated) Steph Ango's philosophy that files in open formats outlast any application — now enriched with Dialectic interview insights on civilizational stance and company principles.
- [[concepts/vault-organization]] — Strategies for organizing Obsidian vaults: flat+links (Ango), PARA, MOCs, AI-optimized architectures.
- [[concepts/obsidian-frontmatter-properties]] — YAML frontmatter properties in Obsidian: enabling Dataview queries, AI retrieval, search filtering, and database-like views via Bases.
- [[concepts/obsidian-graph-view]] — Graph visualization of vault link structure for pattern discovery, orphan detection, and compilation quality verification.
- [[concepts/obsidian-canvas]] — Infinite spatial boards for mapping notes, media, and ideas — enhanced by Advanced Canvas plugin.

### Entities (Obsidian as Knowledge Platform)
- [[entities/obsidian-copilot]] — The #1 downloaded AI plugin for Obsidian (100K+ users): model-agnostic chat, vault RAG, project workspaces — all data as markdown.
- [[entities/smart-connections]] — Leading free Obsidian AI plugin using RAG to enable conversational queries across the entire vault.
- [[entities/templater]] — Obsidian's advanced templating plugin (230K+ installs): dynamic variables, JavaScript execution, file manipulation.
- [[entities/excalidraw]] — The most-downloaded Obsidian community plugin: full-featured freehand drawing and diagramming.

### Sources (History of AI Knowledge Representation)
- [[sources/wikipedia-knowledge-representation-reasoning]] — Comprehensive KR&R overview from 1959 GPS through frames, expert systems, Cyc, and Semantic Web.
- [[sources/wikipedia-expert-systems]] — Expert systems: 1965 origins, 1980s boom (2/3 Fortune 500), knowledge acquisition bottleneck, absorption into business rules.
- [[sources/wikipedia-symbolic-ai]] — Symbolic AI: two summers/winters, neats vs. scruffies, six neuro-symbolic integration architectures.
- [[sources/wikipedia-cyc]] — Cyc project: 40 years, $60M+, 1.5M terms, 24.5M assertions of common-sense knowledge in CycL.
- [[sources/outsiderart-cyc-forgotten-ai]] — Narrative of Doug Lenat's Cyc: from AM/EURISKO through 40 years of encoding to deep learning eclipse and final Cyc+LLM vision.
- [[sources/wikipedia-as-we-may-think]] — Vannevar Bush's 1945 Atlantic essay proposing the Memex with associative trails — conceptual ancestor of hypertext, the web, and PKM.
- [[sources/wikipedia-project-xanadu]] — Ted Nelson's Project Xanadu (1960-present): first hypertext, bidirectional links, transclusion — "longest-running vaporware."
- [[sources/wikipedia-semantic-web]] — Tim Berners-Lee's Semantic Web: RDF/OWL/SPARQL layer cake, enterprise adoption, but mass-web failure due to formalization overhead.
- [[sources/llm-enhanced-knowledge-representation-survey]] — 2024 survey: three-part taxonomy of LLM-enhanced KG embeddings (encoder/encoder-decoder/decoder), trend toward generative approaches.
- [[sources/llms-as-reliable-knowledge-bases]] — 2024 evaluation: best LLM achieves only 32% consistently correct as KB; motivates hybrid structured+neural approaches.

### Concepts (History of AI Knowledge Representation)
- [[concepts/knowledge-representation]] — 65+ years of encoding world knowledge for machines: logic, frames, rules, ontologies, KGs, LLM parametric knowledge.
- [[concepts/symbolic-ai]] — The paradigm (1950s-present): intelligence via symbol manipulation and logic — dominant through 1980s, eclipsed by deep learning, resurging via hybrid approaches.
- [[concepts/expert-systems]] — Rule-based AI (1965-1990s): if-then knowledge bases + inference engines — first commercial AI success, killed by knowledge acquisition bottleneck.
- [[concepts/symbolic-vs-connectionist]] — AI's central paradigm war: symbols vs. neural networks — resolving toward System 1/System 2 complementarity.
- [[concepts/neural-symbolic-integration]] — Six architectures for combining symbolic reasoning with neural pattern recognition, from LLM tokens to tool-using agents.
- [[concepts/ontology]] — Formal specification of domain concepts: from Cyc's 1.5M terms through OWL to LLM-era "cheap ontology."
- [[concepts/semantic-web]] — Berners-Lee's machine-readable web (1994-present): RDF/OWL/SPARQL — succeeded in enterprise, failed on public web.
- [[concepts/memex]] — Bush's 1945 hypothetical device for personal knowledge with associative trails — ancestor of hypertext and the web.
- [[concepts/hypertext]] — Nonsequential linked text: coined by Ted Nelson (1965), partially realized by the web (1989), foundational to wiki KBs.
- [[concepts/transclusion]] — Nelson's concept of live content inclusion by reference — never widely adopted but anticipating modern content embedding.
- [[concepts/llms-as-knowledge-bases]] — Whether LLMs can replace traditional KBs: ~32% consistent correctness says no; motivates hybrid approaches.

### Entities (History of AI Knowledge Representation)
- [[entities/douglas-engelbart]] — Inventor (1925-2013) of the mouse, hyperlink, and GUI; "Mother of All Demos" (1968); inspired by Bush's Memex.
- [[entities/ted-nelson]] — Pioneer (b. 1937) who coined "hypertext" (1965) and founded Project Xanadu (1960); envisioned bidirectional links and transclusion.
- [[entities/john-mccarthy]] — Computer scientist (1927-2011) who coined "AI" (1956), invented LISP (1958), and championed logic-based AI.
- [[entities/marvin-minsky]] — Cognitive scientist (1927-2016), frame theory (1970s), Perceptrons critique (1969), co-founded MIT AI Lab.
- [[entities/edward-feigenbaum]] — Computer scientist (b. 1936), "father of expert systems," led Stanford Heuristic Programming Project.
- [[entities/doug-lenat]] — AI researcher (1950-2023) who spent 39 years building the Cyc knowledge base; proposed Cyc+LLM integration before death.
- [[entities/cyc-project]] — AI's most ambitious KR project (1984-present): 1.5M terms, 24.5M assertions, 2000 person-years, $60M+.

### Comparisons (Knowledge Representation)
- [[comparisons/symbolic-vs-neural-knowledge-representation]] — Explicit symbolic KR (rules, ontologies, KGs) vs implicit neural KR (LLM parameters): complementary strengths, motivating hybrid architectures.

## LLM Reasoning (Research: 2026-04-05)

### Sources
- [[sources/wei-chain-of-thought-prompting]] — Foundational 2022 paper showing step-by-step reasoning exemplars in prompts unlock arithmetic, commonsense, and symbolic reasoning in 100B+ parameter LLMs.
- [[sources/yao-tree-of-thoughts]] — NeurIPS 2023 paper introducing Tree of Thoughts (ToT), generalizing CoT via tree search to achieve 74% on Game of 24 vs. CoT's 4%.
- [[sources/mirzadeh-gsm-symbolic]] — ICLR 2025 paper demonstrating LLM math reasoning is fragile: up to 65% drops with irrelevant info, variance with number changes.
- [[sources/snell-test-time-compute-scaling]] — Landmark 2024 paper showing test-time compute scaling can outperform a 14x larger model, establishing the basis for reasoning models.
- [[sources/lightman-lets-verify-step-by-step]] — OpenAI 2023: process supervision (step-level feedback) significantly outperforms outcome supervision for mathematical reasoning. Released PRM800K.
- [[sources/song-llm-reasoning-failures-survey]] — TMLR 2026 survey: first comprehensive taxonomy of LLM reasoning failures (fundamental, application-specific, robustness).
- [[sources/wei-emergent-abilities]] — Influential 2022 paper defining emergent abilities as capabilities appearing suddenly at scale, with the "mirage" debate about measurement artifacts.
- [[sources/li-system1-system2-reasoning-survey]] — 2025 survey applying Kahneman's dual-process theory to LLMs: standard LLMs as System 1, reasoning models (o1, R1) as System 2.
- [[sources/anthropic-extended-thinking]] — Anthropic 2025: Claude 3.7 Sonnet extended thinking with configurable thinking budgets, 96.5% on GPQA physics.
- [[sources/adaline-inside-reasoning-models]] — Deep technical analysis of o3 and R1: training pipelines, architectures (dense vs MoE), benchmarks, RL as foundation.
- [[sources/raschka-state-of-reasoning-inference]] — Sebastian Raschka 2025: four categories of inference-time scaling, emerging techniques (latent reasoning, self-backtracking).
- [[sources/zhang-test-time-scaling-survey]] — Definitive 2025 survey organizing TTS along four dimensions (what/how/where/how well), cataloguing 30+ techniques from parallel sampling to internal scaling.
- [[sources/agarwal-art-of-scaling-test-time-compute]] — First large-scale empirical TTS study (30B+ tokens, 8 models, 7B-235B): no universal best strategy, monotonic scaling within model types, practical selection recipe.
- [[sources/roberts-train-to-test-scaling-laws]] — T2 scaling laws jointly optimizing training+inference: overtraining smaller models becomes compute-optimal when accounting for test-time scaling costs.
- [[sources/wu-inference-scaling-laws]] — ICLR 2025 inference scaling laws: log10(C) = 1.19*log10(N) + 2.03; Llemma-7B + tree search > Llemma-34B; generation > verification in compute-optimal allocation.
- [[sources/ttrl-test-time-reinforcement-learning]] — NeurIPS 2025: majority voting as RL reward signal on unlabeled data, 211% AIME improvement, bridges test-time scaling and test-time training.
- [[sources/hao-coconut-latent-reasoning]] — COCONUT: reasoning in continuous latent space via hidden state feedback, enabling implicit BFS, fewer tokens; some performance degradation vs explicit CoT.
- [[sources/khalifa-thinkprm]] — ThinkPRM: generative verification CoT needing only 1% of PRM800K labels, outperforms discriminative PRMs by 8% -- thinking paradigm extends to verification.
- [[sources/chen-deep-thinking-tokens]] — Deep-thinking tokens (significant layer-by-layer revision) correlate with accuracy; raw token count unreliable; Think@n strategy for cost-efficient inference.
- [[sources/introl-inference-time-scaling-paradigm-shift]] — December 2025 paradigm shift analysis: 7B+100x inference = 70B; inference demand 118x training by 2026; DeepSeek-R1, P1, ThreadWeaver breakthroughs.
- [[sources/emergehaus-test-time-compute-overview]] — Enterprise TTC overview: AIME 9%->87.5%, System 2 analogy, model cascades (60/30/10), 12-24 month infrastructure outlook.
- [[sources/iacobacci-thinking-budget-not-enough]] — Increasing thinking budget shows diminishing returns; summary/self-consistency (parallel) outperform naive sequential extension, especially for weaker models.
- [[sources/hu-test-time-learning-llm]] — TLM (ICML 2025): test-time domain adaptation via perplexity minimization on unlabeled data with LoRA, 20%+ improvement without labels.
- [[sources/sakana-ab-mcts]] — AB-MCTS: multi-LLM cooperation via Thompson Sampling over depth/width/model dimensions, 30%+ on ARC-AGI-2 through collective intelligence.

### Concepts
- [[concepts/llm-reasoning]] — Multi-step inference, logical deduction, and problem-solving in LLMs via prompting, training, and inference-time scaling.
- [[concepts/chain-of-thought]] — Prompting technique that elicits step-by-step reasoning, dramatically improving performance at 100B+ parameter scale.
- [[concepts/tree-of-thought]] — Reasoning framework generalizing CoT via tree search (BFS/DFS) with backtracking and self-evaluation.
- [[concepts/reasoning-models]] — LLMs trained via RL for extended deliberation: o1/o3, DeepSeek R1, Claude 3.7 extended thinking.
- [[concepts/test-time-compute]] — Paradigm of allocating more compute at inference for better reasoning; small models can outperform 14x larger ones.
- [[concepts/process-reward-models]] — Trained verifiers evaluating each reasoning step; key building block of test-time compute scaling.
- [[concepts/self-consistency]] — Majority voting over multiple CoT samples for improved accuracy on reasoning tasks.
- [[concepts/llm-reasoning-limitations]] — Systematic failures: fragility to distractors, numerical sensitivity, compositional breakdown, architectural root causes.
- [[concepts/mathematical-reasoning-llm]] — Math reasoning from GSM8K to AIME; o3 achieves 96.7% but fundamental fragility persists.
- [[concepts/emergent-abilities]] — Capabilities absent in smaller models that appear suddenly at scale; debate about genuine emergence vs. measurement artifact.
- [[concepts/stochastic-parrot-debate]] — Whether LLMs genuinely reason or perform sophisticated pattern matching; evidence on both sides.
- [[concepts/system-1-system-2-thinking]] — Kahneman's dual-process theory applied to LLMs: fast/intuitive (System 1) vs slow/deliberate (System 2).
- [[concepts/reinforcement-learning-for-reasoning]] — RL (GRPO, scaled RL with verifiers) as the core training methodology for reasoning models.
- [[concepts/inference-scaling-laws]] — Formal mathematical relationships governing inference compute: log10(C) = 1.19*log10(N) + 2.03; counterpart to Chinchilla; T2 joint optimization.
- [[concepts/training-vs-inference-compute]] — The fundamental paradigm shift from training bigger to reasoning harder; inference demand projected 118x training by 2026; $255B market by 2030.
- [[concepts/adaptive-compute-allocation]] — Dynamic per-query compute allocation based on difficulty/confidence/quality signals; 4x efficiency over uniform; model cascades (60/30/10).
- [[concepts/best-of-n-sampling]] — Fundamental parallel TTS: generate N, select best via verifier; baseline for all comparisons; generation diversity > verification at scale.
- [[concepts/mcts-llm-reasoning]] — Monte Carlo Tree Search for LLM reasoning: selection/expansion/simulation/backprop; o3, rStar-Math; multi-model AB-MCTS (30%+ ARC-AGI-2).
- [[concepts/latent-reasoning]] — Reasoning in continuous hidden states (COCONUT): implicit BFS, fewer tokens, but performance degradation and alignment concerns from opaque reasoning.
- [[concepts/test-time-training]] — Modifying model weights at inference time: TTRL (RL with majority voting rewards, 211% AIME), TLM (perplexity minimization, 20%+); complementary to TTS.
- [[concepts/reasoning-tokens]] — The tokens constituting thinking: deep-thinking ratio > raw count for quality; overthinking real; logarithmic scaling; budget control via BudgetThinker.

### Entities
- [[entities/jason-wei]] — Google Brain/DeepMind researcher; first author of both the CoT Prompting and Emergent Abilities papers.
- [[entities/openai]] — Organization behind GPT-4, o1/o3 reasoning models, and PRM800K process reward model dataset.
- [[entities/thinkprm]] — Generative PRM that verifies by generating verification CoT; only 1% of PRM800K labels needed; outperforms discriminative PRMs by 8%.
- [[entities/coconut]] — COCONUT (Chain of Continuous Thought): Meta research on latent reasoning via continuous hidden state feedback; implicit breadth-first search.
- [[entities/ttrl]] — TTRL (Test-Time Reinforcement Learning): NeurIPS 2025 paper; RL on unlabeled test data via majority voting rewards; 211% AIME improvement.

### Comparisons
- [[comparisons/o3-vs-r1-vs-claude-reasoning]] — Three leading reasoning model approaches compared: architecture, training, transparency, benchmarks.
- [[comparisons/process-vs-outcome-supervision]] — Process supervision (step-level, 78% MATH) vs outcome supervision (answer-only, weaker).
- [[comparisons/parallel-vs-sequential-test-time-scaling]] — Parallel (BoN, majority voting) vs sequential (extended thinking) vs hybrid (MCTS) TTS: no universal winner; adaptive routing emerging.
- [[comparisons/training-time-vs-inference-time-scaling]] — The defining AI paradigm comparison: Chinchilla training scaling vs inference-time reasoning; T2 shows joint optimization with overtraining optimal.

## LLM Training Data, Dataset Curation & Data Quality (Research: 2026-04-05)

### Sources
- [[sources/dclm-datacomp-language-models]] — DCLM: 240T-token testbed; fastText filtering enables 7B to reach 64% MMLU; model-based filtering decisively outperforms alternatives.
- [[sources/fineweb-dataset-huggingface]] — FineWeb: 15T tokens from 96 CC dumps; per-dump dedup outperforms cross-dump; FineWeb-Edu + FineWeb-2.
- [[sources/nemotron-cc-nvidia]] — Nemotron-CC: 6.3T tokens (4.4T real + 1.9T synthetic); classifier ensembling; exceeds Llama 3.1 8B.
- [[sources/scaling-laws-data-quality]] — Quality-aware scaling law L(N,D,Q); gamma 0.17-0.40; quality modulates effective dataset size.
- [[sources/synthetic-data-llm-pretraining-study]] — 30% rephrased + 70% natural optimal; textbook shows collapse; 8B generators best.
- [[sources/data-deduplication-trillion-scale]] — MinHash LSH, exact matching, semantic dedup at trillion scale; tools and tradeoffs.
- [[sources/rlhf-preference-data-collection]] — Preference data: on-policy critical; millions wasted; vendor complexity; bias transfer.
- [[sources/benchmark-data-contamination]] — Fidelity-resistance tradeoff; no strategy achieves both; question-level analysis needed.
- [[sources/multilingual-llm-training-data]] — English dominance; NMT-based synthetic data; multilinguality not solved.
- [[sources/copyright-ai-training-data-2025]] — Fair use rulings 2025 (Anthropic, Meta); 2026 peak litigation expected.
- [[sources/nebius-llm-data-preparation]] — End-to-end pipeline; three challenges: data scarcity, synthetic pollution, copyright.

### Concepts
- [[concepts/training-data-curation]] — Transforming raw web crawls into high-quality training datasets; single highest-leverage activity in LLM development.
- [[concepts/model-based-filtering]] — Trained classifiers for data filtering; fastText outperforms by 4+ points; ensembling increases recall from 9% to 25%.
- [[concepts/data-deduplication]] — Removing duplicates at trillion-token scale; MinHash LSH dominant; per-dump dedup outperforms cross-dump.
- [[concepts/scaling-laws]] — Model/data/compute/quality relationships; Chinchilla extended to quality-aware; rankings transfer across scales.
- [[concepts/synthetic-data-in-pretraining]] — 30/70 synthetic/natural optimal; rephrased safe, textbook risky; 8B generators best.
- [[concepts/benchmark-contamination]] — Evaluation data in training corpora; fundamental fidelity-resistance tradeoff; DCLM decontamination as best practice.
- [[concepts/preference-data]] — Human/AI judgments for RLHF; on-policy critical; expensive; biases transfer to models.
- [[concepts/multilingual-training-data]] — Non-English training data challenges; FineWeb-2 covers 1,000+ languages.
- [[concepts/copyright-and-training-data]] — Legal landscape; highly transformative consensus developing; 2026 peak litigation.
- [[concepts/instruction-tuning]] — Instruction-response pair fine-tuning; bridge between pretraining and RLHF.

### Entities
- [[entities/common-crawl]] — Non-profit web crawl archive; foundational for all open LLM pretraining.
- [[entities/fineweb]] — HuggingFace 15T-token dataset; FineWeb-Edu; FineWeb-2 (1,000+ languages).
- [[entities/dclm]] — Apple/UW benchmark + 2T-token dataset; 64% MMLU on 7B model.
- [[entities/nemotron-cc]] — NVIDIA 6.3T-token dataset; classifier ensembling; MMLU 70.3 on 8B.
- [[entities/chinchilla]] — DeepMind compute-optimal scaling; ~20 tokens per parameter.
- [[entities/minhash-lsh]] — Standard near-duplicate detection for LLM data dedup.
- [[entities/anthropic-hh-rlhf]] — 170K preference comparisons; foundational open RLHF dataset.
- [[entities/nathan-lambert]] — RLHF Book author; preference data collection expert.

### Comparisons
- [[comparisons/fineweb-vs-dclm-vs-nemotron-cc]] — FineWeb (scale) vs DCLM (rigor) vs Nemotron-CC (long-horizon balance).
- [[comparisons/heuristic-vs-model-based-filtering]] — Heuristic (cheap, obvious noise) vs model-based (decisive, 4+ point advantage).

## LLM Pretraining, Distributed Training & Compute (Research: 2026-04-05)

### Sources
- [[sources/mlops-pretraining-pipeline]] — MLOps Community: pretraining pipeline, next-token prediction, RPT, instruction-augmented pretraining.
- [[sources/jeremy-jordan-distributed-training]] — Distributed training walkthrough: DP/TP/PP, 3D parallelism, Llama 3.1 405B (16,384 GPUs).
- [[sources/chinchilla-scaling-laws-explained]] — Chinchilla scaling: 20:1 token/param, evolution to 60,000:1 (Qwen3).
- [[sources/spike-no-more-training-stability]] — Loss spike causes (shortcut + LN explosion) and fixes (Embed LN, Scaled Embed).
- [[sources/training-costs-2026-analysis]] — Frontier costs: GPT-4 ~$150M, Gemini Ultra ~$191M, DeepSeek V3 ~$5.6M.
- [[sources/rohan-paul-stabilizing-llm-training]] — Stability: gradient clipping, BFloat16, SPAM/LAMB, DeepNorm, SLW.
- [[sources/deepspeed-megatron-frameworks]] — DeepSpeed ZeRO (1-3) + Megatron-LM TP/PP, combined as Megatron-DeepSpeed.
- [[sources/raschka-pretraining-post-training-paradigms]] — 2024 pipelines: Qwen 2, Apple AFM, Gemma 2, Llama 3.1 multi-stage.
- [[sources/analyticsvidhya-llm-pretraining-guide]] — FineWeb 7-stage pipeline, BPE (100K vocab), training mechanics.
- [[sources/hf-ultrascale-playbook]] — 5D parallelism, ZeRO, 4,000+ scaling experiments.

### Concepts
- [[concepts/llm-pretraining]] — Training LLMs from scratch: next-token prediction, trillions of tokens, $5M-$200M.
- [[concepts/distributed-training]] — Splitting training across GPUs: DP, TP, PP, CP, EP strategies.
- [[concepts/data-parallelism]] — Replicate model, split batches, all-reduce gradients.
- [[concepts/tensor-parallelism]] — Split weight matrices within layers; NVLink-bandwidth dependent.
- [[concepts/pipeline-parallelism]] — Split layers across GPUs; micro-batching reduces bubbles.
- [[concepts/3d-parallelism]] — DP+TP+PP mapped to cluster topology.
- [[concepts/5d-parallelism]] — 3D + Context Parallelism + Expert Parallelism.
- [[concepts/chinchilla-scaling-laws]] — ~20 tokens/param compute-optimal; shifted to inference-optimal.
- [[concepts/compute-optimal-training]] — Balancing parameters and data per FLOP budget.
- [[concepts/training-stability]] — Gradient clipping, warmup, BFloat16, initialization.
- [[concepts/loss-spikes]] — Gradient explosions (1000x) ruining training runs.
- [[concepts/learning-rate-schedules]] — Warmup + cosine decay or WSD.
- [[concepts/mixed-precision-training]] — BFloat16 now standard over FP16.
- [[concepts/zero-optimizer]] — DeepSpeed ZeRO: progressive sharding (Stages 1-3).
- [[concepts/next-token-prediction]] — Self-supervised CLM: predict next token via cross-entropy.
- [[concepts/pretraining-data-pipeline]] — 7-stage pipeline from web crawl to clean tokens.
- [[concepts/multi-stage-pretraining]] — Broad data -> quality upweighting -> context extension.
- [[concepts/llm-training-costs]] — GPU compute 70-80%; 405B needs 5,000+ GPUs.

### Entities
- [[entities/deepspeed]] — Microsoft ZeRO optimizer; easy PyTorch integration via JSON config.
- [[entities/megatron-lm]] — NVIDIA tensor/pipeline parallelism; requires code changes.
- [[entities/deepseek-v3]] — 671B MoE, $5.6M training cost; architectural innovation.

### Comparisons
- [[comparisons/deepspeed-vs-megatron-lm]] — ZeRO (memory) vs TP/PP (compute); complementary.
- [[comparisons/compute-optimal-vs-inference-optimal]] — Chinchilla 20:1 vs modern 1,875:1+ overtraining.

## Scaling Knowledge Systems (Research: 2026-04-05)

### Sources
- [[sources/ek-km-trends-2026]] — Enterprise Knowledge CEO identifies 8 KM trends for 2026: semantic layers powering AI, boxed vs. built AI, tacit knowledge capture, conversational search replacing traditional search.
- [[sources/glean-enterprise-search-guide]] — Glean's guide to AI enterprise search: Enterprise Graph architecture, 100+ SaaS integrations, permission-aware RAG, code intelligence, agentic workflows. Market $6.83B (2025).
- [[sources/helpjuice-km-challenges]] — 8+ enterprise KM challenges: lack of buy-in, outdated tools, silos, unstructured processes, scaling difficulties, ROI measurement.
- [[sources/eesel-confluence-notion-sharepoint]] — 2026 comparison: Confluence (structured wiki + Rovo AI), Notion (flexible blocks + autonomous Agent), SharePoint (compliance + Copilot at $30/user extra).
- [[sources/ksa-knowledge-system-scalability]] — 4-phase scaling architecture (partition/federation, indexing, validation, governance), 3V complexity model, governance maturity as prerequisite.
- [[sources/ek-taxonomy-ia-semantic-layer]] — Taxonomy and IA as semantic layer building blocks: controlled vocabularies, ontologies, and SKOS governance.
- [[sources/branzan-production-knowledge-graphs-2025]] — 5 production KG tools (FalkorDB, Cognee, GraphRAG, LightRAG, AutoSchemaKG), decision matrix, 300-320% ROI.
- [[sources/keerok-enterprise-rag-2026]] — Enterprise RAG deployment: $1.2B to $11B market (49.1% CAGR), 4 architecture approaches, 3-phase roadmap.
- [[sources/cio-knowledge-graphs-enterprise-ai]] — KGs as enterprise AI missing link: traditional RAG capped at ~80% accuracy; LinkedIn +78% accuracy with KG+RAG; Novartis drug discovery KG.
- [[sources/glean-knowledge-silos-unified-search]] — 79% of employees confirm silos; ~3.7h/day lost; revenue impact up to 30%; unified search as solution.
- [[sources/earley-ontology-ia-role-in-ai]] — Ontology as "master data management for AI": knowledge model hierarchy, multi-parent inheritance, Cleveland Museum case study.

### Concepts
- [[concepts/enterprise-knowledge-management]] — Organizational discipline of capturing, organizing, governing knowledge at scale. $13.7B market (2025), $37.6B by 2031. AI transforming every layer.
- [[concepts/knowledge-system-scaling]] — Expanding knowledge infrastructure for thousands of users: 3V complexity (Volume, Velocity, Variety), 4-phase architecture, governance maturity thresholds.
- [[concepts/knowledge-silos]] — Knowledge trapped in teams/systems. 79% of employees confirm; ~3.7h/day lost; up to 30% revenue impact. Solutions: unified search, governance, cultural change.
- [[concepts/enterprise-search]] — AI-powered unified search across enterprise apps. $6.83B market. Enterprise Graph architecture, semantic search, RAG, agentic workflows.
- [[concepts/semantic-layer]] — Standardized abstraction between data repos and front-end apps. Comprises glossaries, metadata, catalogs, taxonomies, ontologies. Key 2026 enterprise AI enabler.
- [[concepts/ontology-and-taxonomy]] — Knowledge model hierarchy: vocabulary to thesaurus to taxonomy to ontology to knowledge graph. Ontology = "master data management for AI."
- [[concepts/information-architecture]] — Structural design of shared information environments. Determines how knowledge is organized, labeled, searched, navigated. Operates across all levels, not just presentation.
- [[concepts/knowledge-governance]] — Policies, processes, roles governing knowledge lifecycle. Prerequisite to scaling. Includes validation pipelines, access control, content ownership.
- [[concepts/tacit-knowledge-capture]] — Capturing undocumented experiential knowledge. AI note-taking and transcription make enterprise-scale programs feasible for the first time.
- [[concepts/knowledge-management-challenges]] — 8+ interconnected KM obstacles. Well-implemented KM generates 200-400% ROI but fewer than 40% can articulate clear metrics.

### Entities
- [[entities/glean]] — AI enterprise search platform. Enterprise Graph architecture, 100+ integrations, Series F ($150M). Market leader.
- [[entities/confluence]] — Atlassian structured wiki. Rovo AI with 20+ agents. Deep Jira integration (76% ship faster). $5.42/user/month.
- [[entities/sharepoint]] — Microsoft enterprise CMS. 190M+ users, granular permissions, HIPAA. Copilot at $30/user/month extra.
- [[entities/enterprise-knowledge]] — KM consulting firm (CEO Zach Wahl). Influential annual trend reports since 2019.
- [[entities/falkordb]] — Graph database with GraphRAG SDK. Sub-50ms latency, 90% hallucination reduction.
- [[entities/cognee]] — Cognitive memory layer for agentic AI. Hybrid graph+vector, 30+ connectors, incremental learning.
- [[entities/novartis]] — Pharma company using KG for drug discovery (genes, diseases, compounds).

### Comparisons
- [[comparisons/personal-vs-enterprise-knowledge-systems]] — Personal (markdown+LLM) vs. team (wiki) vs. enterprise (semantic layers+search+KG). Each tier adds qualitative new challenges.

## RLHF, Alignment & Preference Optimization (Research: 2026-04-05)

### Sources
- [[sources/huggingface-rlhf-illustrated]] — HuggingFace's foundational RLHF tutorial: three-step pipeline (pretrain, reward model, PPO), KL penalties, open-source tooling (TRL, TRLX, RL4LMs).
- [[sources/wolfe-direct-preference-optimization]] — Cameron Wolfe's DPO deep-dive: mathematical derivation from RLHF objective to implicit reward, Bradley-Terry integration, comparison table vs PPO.
- [[sources/anthropic-constitutional-ai]] — Anthropic's Constitutional AI paper: two-phase training (self-critique + RLAIF), principle-based harmlessness, non-evasive responses.
- [[sources/argilla-rlhf-alternatives-overview]] — Argilla/MantisNLP systematic comparison of 9+ alignment methods (RLHF, DPO, KTO, IPO, ORPO, SPIN, CoH, RLAIF, SimPO) with data requirements and compute costs.
- [[sources/wolfe-reward-models-llm]] — Reward model architecture (LLM + linear head), five types (classifier, LLM-as-judge, DPO implicit, ORM, PRM), RewardBench best practices.
- [[sources/wolfe-rlaif-reinforcement-learning-ai-feedback]] — RLAIF: AI-generated preference labels achieve ~50% win rate vs RLHF; soft labels outperform hard; chain-of-thought improves quality.
- [[sources/lilianweng-reward-hacking]] — Definitive taxonomy: Goodhart's Law decomposition (4 types), overoptimization scaling laws (Gao et al.), sycophancy, evaluator hacking, mitigation strategies.
- [[sources/dpo-vs-ppo-comprehensive-study]] — Xu et al.: PPO consistently outperforms DPO across dialogue and code generation; DPO sensitive to distribution shift.
- [[sources/argilla-kto-kahneman-tversky]] — KTO: prospect-theory-based alignment using binary signals; outperforms DPO on noisy data; matches SFT+DPO on Llama.

### Concepts
- [[concepts/rlhf]] — Dominant LLM alignment technique: reward model on preference data + PPO fine-tuning with KL penalty. Powers ChatGPT, Claude, Gemini.
- [[concepts/dpo]] — Reward-free alignment solving RLHF objective in closed form via implicit reward. Standard post-training for Qwen, Llama, Zephyr.
- [[concepts/constitutional-ai]] — Anthropic's principle-based self-critique + RLAIF. Produces harmless, non-evasive AI. Foundation of Claude.
- [[concepts/rlaif]] — AI-generated preference labels replacing human annotators. Achieves ~50% win rate vs RLHF at lower cost.
- [[concepts/reward-model]] — Learned preference function (LLM + linear head). Five types: classifier, LLM-as-judge, DPO implicit, ORM, PRM.
- [[concepts/reward-hacking]] — RL agents exploiting proxy rewards (Goodhart's Law). Manifests as sycophancy, verbosity gaming, fabricated evidence.
- [[concepts/ppo-for-llms]] — Proximal Policy Optimization for RLHF: trust-region RL, 4 model copies, highest performance but highest cost.
- [[concepts/kto]] — Kahneman-Tversky Optimization: binary feedback, prospect theory, robust to noise, matches SFT+DPO combined.
- [[concepts/bradley-terry-model]] — Statistical foundation converting pairwise preferences to probability estimates via sigmoid of reward differences.
- [[concepts/sycophancy]] — RLHF failure mode: models match user beliefs over truth because belief-matching predicts human approval.
- [[concepts/orpo]] — Single-step SFT + preference alignment, no reference model. Works with as few as 7K examples.
- [[concepts/ipo]] — DPO variant adding regularization to prevent overfitting on deterministic preferences.
- [[concepts/process-reward-model]] — Step-level reward scoring for reasoning chains. Harder to hack but requires expensive step-level supervision.

### Entities
- [[entities/instructgpt]] — OpenAI's 2022 RLHF paper: 1.3B aligned model preferred over 175B GPT-3. Direct precursor to ChatGPT.
- [[entities/cameron-wolfe]] — Ph.D. researcher, Deep (Learning) Focus newsletter: detailed DPO, reward model, RLAIF technical articles.
- [[entities/lilian-weng]] — OpenAI researcher, Lil'Log author: definitive surveys on reward hacking, agents, LLM training.
- [[entities/trl]] — HuggingFace's alignment library: SFT, PPO, DPO, IPO, KTO, ORPO. De facto open-source standard.

### Comparisons
- [[comparisons/ppo-vs-dpo]] — PPO wins on hard tasks (code, reasoning) via online learning; DPO wins on simplicity, cost, accessibility.
- [[comparisons/rlhf-alternatives]] — 9+ method comparison (RLHF, DPO, KTO, IPO, ORPO, SPIN): no single winner; data quality dominates method choice.
- [[comparisons/rlhf-vs-constitutional-ai]] — RLHF (human labels, all dimensions) vs CAI (AI labels for harmlessness, human for helpfulness).

---

## Transformer Architecture & LLM Internals (Research: 2026-04-05)

### Sources
- [[sources/illustrated-transformer-jalammar]] — Jay Alammar's visual walkthrough of the original Transformer: encoder-decoder stacks, Q/K/V self-attention, multi-head attention, positional encoding.
- [[sources/raschka-self-attention-coding]] — Sebastian Raschka's code-first deep dive into self-attention, multi-head, causal masking, and cross-attention with PyTorch.
- [[sources/huggingface-mixture-of-experts]] — Comprehensive MoE guide: routing, load balancing, Switch Transformer, Mixtral 8x7B, fine-tuning, expert parallelism.
- [[sources/mamba-state-space-models-visual-guide]] — Visual walkthrough of SSM/S4/Mamba: selective scan, hardware-aware kernel fusion, dual train/infer modes.
- [[sources/flashattention-3-paper]] — FlashAttention-3: 75% H100 utilization via warp specialization, interleaved matmul/softmax, FP8 (1.2 PFLOPS).
- [[sources/eleutherai-rotary-embeddings]] — RoPE: position as rotation in complex-number space, outperforms learned/T5 RPE, 1-3% overhead.
- [[sources/kv-cache-optimization-techniques]] — GQA (8x reduction), sliding window, PagedAttention (waste 60-80% to 4%), distributed cache.
- [[sources/speculative-decoding-bentoml]] — Draft-then-verify: EAGLE (<5% overhead for 70B), P-EAGLE (parallel drafting), 2-3x speedup.
- [[sources/ssm-vs-transformers-tradeoffs]] — Gu's analysis: SSMs=brains, Transformers=databases; SSMs win on byte/DNA data; hybrids 3:1-10:1 optimal.
- [[sources/vlms-2025-huggingface]] — 2025 VLMs: MoE decoders (Kimi-VL 2.8B active), any-to-any, video understanding, VLAs, multimodal RAG.
- [[sources/chinchilla-scaling-laws]] — 20:1 token/parameter ratio; 70B Chinchilla beats 280B Gopher, 175B GPT-3 on same compute.
- [[sources/unite-ai-bert-gpt-t5-comparison]] — BERT (encoder-only, bidirectional), GPT (decoder-only, causal), T5 (enc-dec, text-to-text).
- [[sources/moe-models-comparison-2025]] — 2025 MoE specs: DeepSeek-R1 671B/37B, Llama 4 400B/17B, Qwen3 235B/22B.
- [[sources/attention-mechanisms-comprehensive-survey]] — 2026 arXiv survey: attention history (Bahdanau 2014 to Transformers), scoring function comparison, O(n^2*d) self-attention properties, multi-head specialization.
- [[sources/flashattention-3-tri-dao-blog]] — Tri Dao's FlashAttention-3 blog: async warp specialization + FP8 incoherent processing achieves 740 TFLOPS (75% H100 utilization).
- [[sources/streamingllm-attention-sinks]] — MIT HAN Lab ICLR 2024: attention sinks phenomenon; StreamingLLM preserves 4 sink tokens + rolling window for 4M+ token generation with 22.2x speedup.
- [[sources/retro-illustrated-retrieval-transformer]] — Jay Alammar's RETRO: 7.5B params matching GPT-3 (185B) via 2T-token retrieval database with chunked cross-attention.
- [[sources/differentiable-neural-computers-deepmind]] — DeepMind DNC: neural controller + external memory via differentiable attention, temporal linking, graph navigation and multi-step reasoning.
- [[sources/mamba-visual-guide-grootendorst]] — Grootendorst: SSM fundamentals, LTI limitation, Mamba selective mechanism (input-dependent B, C, delta), hardware-aware parallel scan.
- [[sources/knowledge-circuits-transformers-research]] — NeurIPS 2024: MLPs store facts as key-value memories, attention heads route information — fact-storing MLPs are modular and swappable.
- [[sources/kv-caching-huggingface-explained]] — Hugging Face: KV caching 5.21x speedup (11.7s vs 61s for 300 tokens on T4 GPU).
- [[sources/gqa-grouped-query-attention-overview]] — IBM: GQA generalizes MHA/MQA, 90% KV cache reduction, 30-40% faster inference, uptrain at 5% compute.

### Concepts
- [[concepts/transformer-architecture]] — The foundational NN architecture based on attention, powering all frontier LLMs since 2017.
- [[concepts/self-attention]] — Scaled dot-product Q/K/V attention: Attention(Q,K,V) = softmax(QK^T/sqrt(d_k))V.
- [[concepts/multi-head-attention]] — Parallel attention heads with independent Q/K/V for diverse representation subspaces.
- [[concepts/causal-attention]] — Masked self-attention restricting each position to attend only to previous positions (decoder-only LLMs).
- [[concepts/cross-attention]] — Queries from one sequence, keys/values from another — for encoder-decoder and multimodal fusion.
- [[concepts/positional-encoding]] — Injecting position information: sinusoidal → learned → relative → RoPE.
- [[concepts/rotary-position-embeddings]] — Parameter-free position encoding via complex-number rotation; standard for all modern LLMs.
- [[concepts/flash-attention]] — IO-aware tiling reducing attention memory O(N^2)→O(N); FlashAttention-3 at 75% H100 utilization.
- [[concepts/state-space-models]] — SSMs: linear-complexity sequence models; Mamba/S4; excel on raw data; hybrid architectures emerging.
- [[concepts/mamba]] — Selective SSM with input-dependent state transitions and hardware-aware kernel fusion.
- [[concepts/selective-state-space]] — S6: Mamba's mechanism making B, C, delta input-dependent for content-aware reasoning.
- [[concepts/grouped-query-attention]] — Share KV heads across query groups; Llama-2-70B achieves 8x cache reduction.
- [[concepts/sliding-window-attention]] — Attend only to W recent tokens; effective receptive field = W * n_layers.
- [[concepts/paged-attention]] — Virtual-memory-inspired KV cache: non-contiguous allocation, 60-80% waste to 4%.
- [[concepts/sparse-attention]] — Subset-of-pairs attention via fixed patterns, routing, clustering, or linear approximation.
- [[concepts/multimodal-transformers]] — Multi-modality architectures: vision encoders + LLM decoders, MoE, VLAs.
- [[concepts/attention-mechanisms]] — The family of mechanisms enabling dynamic focus on relevant input parts — from Bahdanau 2014 through Transformer self-attention to modern variants (flash, linear, sparse, GQA).
- [[concepts/attention-sinks]] — Initial tokens receive disproportionate attention regardless of content due to softmax sum-to-one constraint; enables StreamingLLM for infinite generation (ICLR 2024).
- [[concepts/linear-attention]] — Kernel-based approximation avoiding the N x N attention matrix, reducing to O(N*d^2) — but consistently underperforms softmax due to lost injectivity and sharpness.
- [[concepts/memory-augmented-neural-networks]] — Neural architectures with explicit external memory via differentiable read/write: NTMs (2014), DNCs (2016), RETRO (2021) — the lineage connecting attention to external knowledge storage.
- [[concepts/knowledge-storage-in-transformers]] — MLP layers store facts as key-value memories while attention heads route queries to storage — forming modular, swappable "knowledge circuits" enabling surgical editing.

### Entities
- [[entities/attention-is-all-you-need]] — 2017 paper: the Transformer architecture, most cited ML paper of 21st century.
- [[entities/bert]] — Google 2018 encoder-only bidirectional Transformer; 110M-340M params; now mainly for embeddings.
- [[entities/gpt]] — OpenAI decoder-only family: GPT-1 (117M) to GPT-4; established the dominant LLM architecture.
- [[entities/t5]] — Google 2019 encoder-decoder text-to-text; 220M-11B; basis for Switch Transformer.
- [[entities/switch-transformer]] — Google 2021: 1.6T params, 2048 experts, single-expert routing, 4x speedup over T5-XXL.
- [[entities/mixtral]] — Mistral 2023: 47B total / 12B active MoE; outperforms Llama 2 70B.
- [[entities/tri-dao]] — Creator of FlashAttention and co-creator of Mamba.
- [[entities/flashattention]] — IO-aware exact attention library (v1-v3): default in PyTorch/JAX; v3 reaches 740 TFLOPS FP16 and ~1.2 PFLOPS FP8 on H100.
- [[entities/retro]] — DeepMind's 7.5B model matching GPT-3 (185B) via 2T-token retrieval database with chunked cross-attention — decoupling memorization from reasoning.
- [[entities/neural-turing-machine]] — Graves 2014: foundational architecture coupling LSTM controller with differentiable external memory for algorithmic learning.
- [[entities/streamingllm]] — MIT HAN Lab framework: infinite-length generation by preserving attention sink tokens + rolling KV window; 22.2x speedup, no fine-tuning.

### Comparisons
- [[comparisons/transformers-vs-state-space-models]] — Databases vs brains: Transformers for tokenized text, SSMs for raw data, hybrids optimal.
- [[comparisons/encoder-only-vs-decoder-only-vs-encoder-decoder]] — BERT vs GPT vs T5: why decoder-only won.
- [[comparisons/dense-vs-moe-transformers]] — Dense (all params per token) vs MoE (sparse routing): MoE now default for frontier.
- [[comparisons/softmax-vs-linear-attention]] — Softmax (O(N^2*d), exact, sharp retrieval) vs linear (O(N*d^2), approximate, blurred): linear attention offers efficiency but loses injectivity and sharpness.
- [[comparisons/mha-vs-gqa-vs-mqa]] — Multi-Head (max quality) vs Grouped Query (near-MHA, 4-8x less KV) vs Multi-Query (fastest, quality loss): GQA dominant since 2023.
- [[comparisons/self-attention-vs-cross-attention]] — Self-attention (within-sequence) vs cross-attention (between sequences): self-attention dominates decoder-only LLMs; cross-attention essential for multimodal and retrieval.

## Sources (Claude & Anthropic Deep Dive)

- [[sources/wikipedia-claude-language-model]] — Complete Claude release history: Claude 1 (Mar 2023) through Claude 4.6 (Feb 2026), constitutional AI evolution from principles to 23K words.
- [[sources/wikipedia-anthropic]] — Anthropic founding by 7 ex-OpenAI researchers, PBC structure, $380B valuation, Amazon/Google/Microsoft partnerships.
- [[sources/anthropic-claude-models-overview]] — Official API docs: Opus 4.6 (1M/128K/$5/$25), Sonnet 4.6 (1M/64K/$3/$15), Haiku 4.5 (200K/64K/$1/$5).
- [[sources/anthropic-rsp-v3]] — RSP v3.0 (Feb 2026): separated unilateral/industry commitments, ASL framework, 17 security controls, Frontier Safety Roadmaps.
- [[sources/anthropic-extended-thinking-docs]] — Extended thinking API reference: adaptive vs manual modes, interleaved thinking, display options, caching behavior.
- [[sources/anthropic-claude-3-family-announcement]] — Claude 3 (Mar 2024): three-tier Opus/Sonnet/Haiku, first to surpass GPT-4, >99% Needle-in-Haystack.
- [[sources/anthropic-claude-4-announcement]] — Claude 4 (May 2025): extended thinking with tools, 72.5% SWE-bench, 65% fewer shortcuts, Claude Code GA.
- [[sources/dario-amodei-machines-of-loving-grace]] — 50-page essay: AI's transformative upside across biology, neuroscience, governance, economics, work.
- [[sources/improvado-claude-vs-chatgpt-vs-gemini-2026]] — 2026 comparison: Claude leads coding/writing, GPT leads reasoning, Gemini leads math; multi-model strategy.

## Concepts (Claude & Anthropic Deep Dive)

- [[concepts/claude-model-family-evolution]] — 17 releases from Claude 1 (9K context, Mar 2023) to Claude 4.6 (1M context, Feb 2026); context 111x, output 32x, Opus price 3x cheaper.
- [[concepts/extended-thinking]] — Claude's test-time compute: manual budget_tokens (Claude 4) to adaptive thinking (Claude 4.6); interleaved thinking between tool calls.
- [[concepts/responsible-scaling-policy]] — Anthropic's RSP with AI Safety Levels (ASL-1 to ASL-5); 6 versions since Sep 2023; influenced OpenAI, Google, EU AI Act.

## Comparisons (Claude & Anthropic Deep Dive)

- [[comparisons/claude-vs-gpt-vs-gemini]] — 2026: Claude Opus 4.6 leads coding/writing, GPT-5.4 leads general reasoning, Gemini 3.1 leads math; no single winner; multi-model recommended.

## Sources (Karpathy Deep Profile)

- [[sources/karpathy-wikipedia-biography]] — Comprehensive biography: Stanford PhD under Fei-Fei Li, OpenAI founding member, Tesla AI Director, Eureka Labs founder, AI education pioneer.
- [[sources/karpathy-software-2-0]] — 2017 essay: neural networks as new programming paradigm (Software 2.0), eight advantages, interpretability crisis warning.
- [[sources/karpathy-recipe-training-neural-networks]] — 2019 practical guide: six-stage recipe from data inspection to squeezing performance, "don't be a hero" philosophy.
- [[sources/karpathy-vibe-coding]] — Vibe coding origin (Feb 2025): Collins Word of Year, 25% YC startups 95% AI-generated, 1.7x more bugs, 19% dev slowdown.
- [[sources/karpathy-2025-llm-year-review]] — Year-end review: RLVR replaces RLHF, jagged intelligence, Cursor/Claude Code as app layer, benchmark skepticism.
- [[sources/karpathy-llm-os-concept]] — LLM as OS kernel: CPU (reasoning), RAM (context window), filesystem (RAG), Software 3.0 (prompts as code).
- [[sources/karpathy-eureka-labs]] — AI-native education company (July 2024): LLM101n course, Teacher + AI Teaching Assistant symbiosis.
- [[sources/karpathy-state-of-gpt]] — Microsoft Build 2023 keynote: canonical introduction to GPT training pipeline (pretraining -> SFT -> RLHF).
- [[sources/karpathy-educational-projects]] — micrograd (100-line autograd), nanoGPT (GPT-2 reproduction), minbpe (BPE tokenizer), llm.c (C/CUDA, 7% faster than PyTorch), Zero to Hero series.

## Concepts (Karpathy Deep Profile)

- [[concepts/llm-os]] — Karpathy's metaphor: LLMs as OS kernel (CPU=reasoning, RAM=context window, filesystem=RAG), with natural language as programming interface.
- [[concepts/ai-native-education]] — Education redesigned around AI: human instructors create curriculum, AI teaching assistants guide at scale -- Karpathy's Eureka Labs vision.

## Entities (Karpathy Deep Profile)

- [[entities/eureka-labs]] — Karpathy's AI-native education company (July 2024) building LLM101n with AI teaching assistants.
- [[entities/micrograd]] — Karpathy's 100-line autograd engine: scalar-level backpropagation for pedagogy, PyTorch-like API.
- [[entities/nanogpt]] — Karpathy's GPT training repo: reproduces GPT-2 (124M) in ~4 days on 8xA100.
- [[entities/llm-c]] — LLM training in pure C/CUDA: 3,000 lines, 7% faster than PyTorch, GPT-2 in 90 min for $20.
- [[entities/fei-fei-li]] — Stanford professor, ImageNet creator, Karpathy's PhD advisor.
- [[entities/tesla]] — EV/AI company where Karpathy served as Director of AI (2017-2022), leading Autopilot Vision.

## Sources (AI Code Generation & Code-to-Knowledge Shift)

- [[sources/karpathy-software-2-0]] -- Karpathy's foundational 2017 essay arguing neural networks are Software 2.0: datasets replace source code, training replaces compilation, data curation replaces instruction-writing.
- [[sources/wikipedia-vibe-coding]] -- Comprehensive Wikipedia overview of vibe coding: Karpathy's February 2025 coinage, Collins Word of the Year, quality crisis (2.74x more security vulns), evolution to agentic engineering.
- [[sources/greptile-state-of-ai-coding-2025]] -- Greptile telemetry data: PR size +93%, developer output tripled, CLAUDE.md in 75% of orgs, Anthropic SDK at 124M monthly downloads.
- [[sources/morphllm-coding-models-comparison-2026]] -- March 2026 model ranking: Opus 4.6 (80.8%), Gemini 3.1 Pro (80.6%), scaffold matters more than model weights (22-point swing).
- [[sources/morphllm-codex-vs-claude-code]] -- Head-to-head: Codex (speed, 77.3% Terminal-Bench, 1,000+ tok/s) vs Claude Code (depth, 80.8% SWE-bench, 1M context, Agent Teams).
- [[sources/osmani-ai-productivity-reality]] -- Osmani's meta-analysis of AI coding productivity: realistic 20-30% gains, DORA paradox (91% longer reviews, 9% more bugs), Sentry failure case.
- [[sources/swe-bench-leaderboard-2026]] -- SWE-bench evolution: 48.5% (GPT-4 Turbo, 2023) to 77.2% (Claude 4 Sonnet, 2025) -- 59% improvement in under 2 years, 70%+ considered production-ready.
- [[sources/osmani-llm-coding-workflow-addendum]] -- Osmani's practical workflow: spec.md planning, context packing (gitingest/repo2txt), multi-model review, CI/CD as safety net.

## Concepts (AI Code Generation & Code-to-Knowledge Shift)

- [[concepts/software-2-0]] -- Karpathy's 2017 paradigm: neural networks as new programming model where datasets replace source code, training replaces compilation, data curation replaces instruction-writing -- intellectual foundation for vibe coding and code-to-knowledge shift.
- [[concepts/vibe-coding]] -- Karpathy's February 2025 term for natural-language-driven development with minimal code review (Collins Word of the Year 2025), which followed a clear arc from excitement to "hangover" to Karpathy declaring it passe in favor of agentic engineering.
- [[concepts/ai-code-generation]] -- LLMs generating source code from natural language or context: ~46% of committed code, SWE-bench at 80.8%, scaffold matters more than model weights (22-point swing), models within 1.2% of each other at frontier.
- [[concepts/natural-language-programming]] -- Specifying software behavior in English rather than formal languages: from Karpathy's "English is the hottest programming language" to spec-driven development with LLM agents.
- [[concepts/automated-testing-for-ai-code]] -- Validating AI-generated code through agentic test generation, self-healing suites, AI-on-AI review, and CI/CD safety nets -- critical because 60% of AI-generated code requires intervention.

## Entities (AI Code Generation)

- [[entities/openai-codex]] -- OpenAI's agentic coding tool: cloud sandbox-based, 1,000+ tok/s on Cerebras, 56.8% SWE-bench Pro, 77.3% Terminal-Bench, excels at rapid prototyping and terminal workflows.
- [[entities/codestral]] -- Mistral AI's 22B open-weight coding model: fast local inference at 1.4s/response, scoring within 85-90% of frontier models on straightforward tasks.
- [[entities/swe-bench]] -- Princeton benchmark for AI software engineering agents: real GitHub issues from production Python repos, 59% improvement in 2 years, dominant evaluation standard.

## Comparisons (AI Code Generation)

- [[comparisons/codex-vs-claude-code]] -- The two dominant AI coding agents: Codex (speed, sandbox, terminal) vs Claude Code (depth, multi-agent, determinism) with recommended hybrid approach.
- [[comparisons/vibe-coding-vs-agentic-engineering]] -- Two successive AI programming philosophies by Karpathy: minimal-review natural-language coding (2025) vs disciplined agent orchestration (2026).

## Sources (Web Scraping, Content Extraction & Ingest Pipeline)

- [[sources/web-scraping-best-practices-2026]] — Comprehensive 2026 guide to web scraping: IP rotation, request timing, headers, honeypots, caching, distributed architecture, and ethical compliance.
- [[sources/mozilla-readability-algorithm]] — Deep technical explanation of Mozilla's Readability.js — the 7-heuristic, 6-stage pipeline that powers Firefox Reader View and underpins most modern content extraction tools.
- [[sources/trafilatura-web-extraction]] — Trafilatura: the most accurate open-source web text extraction library — combines jusText and Readability algorithms, outputs to markdown/JSON/XML-TEI, used by HuggingFace, IBM, Microsoft Research.
- [[sources/jina-reader-lm-html-to-markdown]] — Jina's Reader-LM (0.5B-1.5B params) outperforms GPT-4o at HTML-to-markdown conversion by treating it as a selective-copy task — a paradigm shift from heuristic to neural content extraction.
- [[sources/crawl4ai-llm-web-crawler]] — Crawl4AI (63K+ GitHub stars): open-source Playwright-based crawler producing dual markdown output (raw + BM25-filtered), with LLM/CSS/XPath extraction and anti-bot detection.
- [[sources/web-scraping-legality-ethics-2025]] — Web scraping legality: hiQ v. LinkedIn confirms public data access legal in US; GDPR EUR 20M fines for personal data; EU AI Act requires training data provenance.
- [[sources/python-scraping-tools-comparison]] — BeautifulSoup (lightweight), Scrapy (2,500 pages/min), Playwright (JS rendering, 800 pages/min) — systematic benchmarks and selection criteria.
- [[sources/schema-org-structured-data]] — Schema.org: 45M+ domains with pre-structured JSON-LD/Microdata enabling high-confidence extraction without heuristics.
- [[sources/web-archiving-warc-tools]] — WARC (ISO 28500) preservation standard, tools from Heritrix to ArchiveBox, protecting KB source provenance.

## Concepts (Web Scraping, Content Extraction & Ingest Pipeline)

- [[concepts/content-extraction]] — Extracting meaningful content from messy web pages — three generations: rule-based, heuristic (Readability/Trafilatura), neural (Reader-LM) — critical first step in KB ingest.
- [[concepts/boilerplate-removal]] — Removing navigation, ads, footers, sidebars via DOM scoring (Readability), block classification (jusText), or neural filtering (Reader-LM).
- [[concepts/html-to-markdown-conversion]] — Converting HTML to markdown — from Turndown/Pandoc to Reader-LM v2 (ROUGE-L 0.86) — the format bridge between web and LLM knowledge.
- [[concepts/web-scraping-ethics-and-law]] — Public data generally legal (hiQ v. LinkedIn); GDPR for PII; EU AI Act for training data; robots.txt compliance legally relevant.
- [[concepts/anti-bot-evasion]] — IP rotation, header randomization, stealth browsers, behavior mimicry — balanced against ethical obligations.
- [[concepts/structured-data-extraction]] — Pre-structured Schema.org data (JSON-LD, Microdata) from 45M+ domains — bypasses heuristic extraction for metadata and entities.
- [[concepts/web-archiving]] — WARC (ISO 28500) preservation for source permanence and provenance — from Heritrix to ArchiveBox.
- [[concepts/web-scraping-at-scale]] — (updated) Scrapy for throughput, Playwright for JS, Crawl4AI/Firecrawl for LLM-ready markdown.

## Entities (Web Scraping, Content Extraction & Ingest Pipeline)

- [[entities/mozilla-readability]] — Readability.js: 7-heuristic, 6-stage DOM scoring algorithm powering Firefox Reader View and Jina Reader API.
- [[entities/trafilatura]] — Most accurate open-source extraction library (ACL 2021), hybrid jusText + Readability, used by HuggingFace/IBM/Microsoft.
- [[entities/jina-reader]] — Jina Reader API: prefix r.jina.ai/ for clean markdown; Chrome + Readability + Turndown pipeline with optional ReaderLM v2.
- [[entities/reader-lm]] — Jina's 1.5B model for HTML-to-markdown: ROUGE-L 0.86 vs GPT-4o's 0.43, selective-copy task, 512K context, 29 languages.
- [[entities/crawl4ai]] — #1 open-source LLM crawler (63K stars), Playwright-based, BM25-filtered "fit markdown" output.
- [[entities/playwright]] — Microsoft's cross-browser automation: Chromium/Firefox/WebKit, auto-waiting, stealth mode, 800 pages/min.
- [[entities/scrapy]] — Python web crawling framework: 2,500 pages/min, 1,000 concurrent requests, Twisted async.
- [[entities/beautiful-soup]] — Python HTML parser: lightweight, handles malformed markup, common in hybrid Playwright+BS4 workflows.

## Comparisons (Web Scraping, Content Extraction & Ingest Pipeline)

- [[comparisons/heuristic-vs-neural-content-extraction]] — Heuristic (fast, free, 90%+ pages) vs neural (ROUGE-L 0.86, needs GPU) content extraction — hybrid recommended.
- [[comparisons/crawl4ai-vs-firecrawl]] — Open-source Crawl4AI (free, BM25 filtering) vs SaaS Firecrawl (managed, integrated).

## Sources (LLM Applications Beyond Code)

- [[sources/hbr-llms-unlock-creative-ideas]] -- HBR research: LLMs unlock creativity via persistence and flexibility, but group-level diversity paradoxically narrows; four AI ideation roles proposed.
- [[sources/assemblyai-llm-use-cases-2026]] -- Seven primary LLM use cases in 2026: spoken data analysis, content creation, customer support, translation, sentiment, education, cybersecurity — with 40-70% task time reductions.
- [[sources/frontiers-ai-lab-automation-scientific-discovery]] -- Hartung review: AI transitioning from co-pilot to lab-pilot — AlphaFold (Nobel Prize), halicin (novel antibiotic), ISM001-055 (first AI drug Phase II), autonomous labs.
- [[sources/pmc-llms-healthcare-medical-review]] -- Comprehensive review of 7 healthcare LLM domains; GPT-4 at 93.1% on USMLE; Med-PaLM 2 +19% on MultiMedQA; critical hallucination and bias challenges.
- [[sources/ai-deep-research-tools-2026]] -- Comparative review of 7 AI research tools: Perplexity, Elicit, Consensus, Scite (1.2B citations), Research Rabbit; best practice is multi-tool composition.
- [[sources/mergen-llm-data-analysis-automation]] -- PMC study on mergen R package: LLM code correctness drops from 88% (simple) to 0% (complex); self-correction loops improve by up to 52.5%.
- [[sources/emergentmind-llm-tutoring-solutions]] -- Survey of LLM tutoring systems: Physics-STAR (100% score increase), Tutorly (+15pp), AgentTutor (+24-30pp); IRT and Bayesian mastery tracking.
- [[sources/microsoft-research-ai-2026-frontiers]] -- Microsoft Research 20 AI frontiers for 2026: AI lab assistants, EvoDiff protein design, virtual patients, interactive storytelling, agentic media, inclusive innovation.
- [[sources/gavel-law-firm-llm-guide-2026]] -- Legal LLM adoption surged 19% to 79% in one year; three use cases (document review, drafting, research) with Everlaw, Luminance, Casetext.
- [[sources/science-advances-ai-creativity-diversity-paradox]] -- Science Advances: AI-assisted stories rated more creative but more similar to each other; individual improvement vs collective homogenization.

## Concepts (LLM Applications Beyond Code)

- [[concepts/llm-applications-beyond-code]] -- The expanding frontier of LLM applications across writing, research, education, science, healthcare, law — Karpathy's 'knowledge manipulation' shift applied to all professional domains.
- [[concepts/ai-scientific-discovery]] -- AI's transition from co-pilot to lab-pilot: AlphaFold (Nobel), halicin, ISM001-055, GNoME (380K crystals), autonomous laboratories.
- [[concepts/llm-healthcare-applications]] -- Seven healthcare LLM domains: clinical decision support, education, patient care, literature, drug discovery, radiology, documentation.
- [[concepts/llm-education-tutoring]] -- LLM tutoring systems achieving significant learning gains via IRT models, Bayesian mastery tracking, and multi-agent architectures.
- [[concepts/llm-creative-applications]] -- LLMs for creative writing, ideation, storytelling; Gemini 3 Pro #1 LM Arena creative writing; Claude Opus 4.6 tops Mazur Writing Benchmark.
- [[concepts/llm-legal-applications]] -- Legal AI adoption from 19% to 79% in one year; document review, drafting, research; lawyer role transformation mirrors developer shift.
- [[concepts/ai-creativity-paradox]] -- AI improves individual creative output while reducing collective diversity — empirically demonstrated in Science Advances with implications for all knowledge domains.
- [[concepts/llm-data-analysis]] -- LLMs for natural language to code translation; critical executability-correctness gap (88% correct simple, 0% complex); self-correction loops most effective.
- [[concepts/ai-research-assistants]] -- 2026 research tool ecosystem: Perplexity (discover), Elicit (synthesize), Consensus (validate), Scite (verify), Research Rabbit (explore).

## Entities (LLM Applications Beyond Code)

- [[entities/perplexity-ai]] -- AI research tool providing citation-backed answers with real-time web search; gold standard for fast multi-source discovery.
- [[entities/elicit]] -- AI literature review tool with customizable comparison tables and structured data extraction from peer-reviewed sources.
- [[entities/scite]] -- Citation analysis tool with 1.2B citation statements from 187M+ articles; Smart Citations classify as supporting/contrasting/mentioning.
- [[entities/alphafold]] -- DeepMind's Nobel Prize-winning protein structure prediction system; 200M+ predicted structures; landmark AI-for-science achievement.
- [[entities/med-palm]] -- Google's medical LLM family; Med-PaLM 2 +19% on MultiMedQA; first LLM to reach expert-level on medical licensing exams.
- [[entities/everlaw]] -- AI-powered e-discovery and document analysis platform for legal teams.

## Comparisons (LLM Applications Beyond Code)

- [[comparisons/coding-vs-knowledge-work-llm-applications]] -- Code generation vs knowledge work LLM applications: shared patterns (automation to orchestration), different maturity, convergence toward knowledge orchestration.

## Sources (World Models, Simulation & Physical AI)

- [[sources/ha-schmidhuber-world-models]] — Foundational 2018 paper: VAE + MDN-RNN + 867-parameter controller solving CarRacing by "learning inside a dream"; agents trained entirely in model-generated environments.
- [[sources/openai-video-world-simulators]] — OpenAI Sora technical report: spacetime patch diffusion transformer for video generation as world simulation; emergent 3D consistency at scale; Sora 2 improved physics; discontinued March 2026.
- [[sources/deepmind-genie-2]] — DeepMind's Genie 2: autoregressive latent diffusion generating interactive 3D worlds from single images; keyboard/mouse control, emergent physics, long-horizon memory; Genie 3 (Aug 2025) achieved real-time 24fps 720p.
- [[sources/meta-v-jepa-2]] — Meta's V-JEPA 2: 1.2B-param self-supervised world model on 1M+ hours video; SOTA action anticipation; zero-shot robot planning with 62 hours robot data; three new physical reasoning benchmarks.
- [[sources/jepa-deep-dive]] — Technical walkthrough of JEPA family: energy-based formulation, four training criteria without contrastive loss, I-JEPA/V-JEPA/H-JEPA/MC-JEPA variants, collapse prevention via EMA and Isotropic Gaussian regularization.
- [[sources/nvidia-cosmos-world-foundation]] — NVIDIA Cosmos: wavelet tokenizer (12x faster, +4dB), 7B-14B diffusion and 4B-13B autoregressive world models trained on 20M hours video, open license, 2M+ downloads, robotics/AV adoption.
- [[sources/world-models-race-2026]] — 2026 competitive landscape: AMI Labs ($1.03B seed), Genie 3 (24fps real-time), NVIDIA Cosmos (2M downloads), World Labs Marble ($230M); over $1.3B in funding.
- [[sources/llms-and-world-models-mitchell]] — Melanie Mitchell analysis: Sutskever vs LeCun on LLM world understanding; Orrery Spectrum (lookup-map-orrery-simulator); three criteria for genuine world models; community split 50-50.

## Concepts (World Models, Simulation & Physical AI)

- [[concepts/world-models]] — AI systems building internal representations of reality to simulate, predict, and plan — the emerging paradigm challenging LLMs with $1.3B+ in 2026 funding.
- [[concepts/jepa]] — Yann LeCun's Joint Embedding Predictive Architecture: predicts representations not pixels; I-JEPA, V-JEPA, V-JEPA 2, H-JEPA, LeWorldModel; foundation for AMI Labs.
- [[concepts/video-generation-as-world-simulation]] — Hypothesis that scaling video generation trains implicit world simulators — pioneered by Sora, challenged by gap between statistical prediction and true causal modeling.
- [[concepts/latent-world-models]] — World models compressing observations into compact representations for dynamics prediction — from 32-dim VAE to DreamerV3's RSSM to V-JEPA 2's 1.2B ViT.
- [[concepts/physical-ai]] — AI systems perceiving and acting in the physical world — requiring world models for physics, object permanence, and spatial reasoning.
- [[concepts/embodied-ai]] — AI agents with physical instantiation learning through world interaction; three-layer framework: perception, world modeling, policy generation.
- [[concepts/self-supervised-learning]] — Learning representations from unlabeled data: contrastive, generative, joint embedding (JEPA) — the training paradigm for world models.
- [[concepts/model-based-reinforcement-learning]] — RL that learns environment models for planning through imagination — Dyna (1990) to DreamerV3 (2025, Minecraft diamond).
- [[concepts/llm-world-understanding]] — Whether LLMs develop genuine world models: split 50-50; Sutskever yes, LeCun no; Orrery Spectrum as evaluation framework.

## Entities (World Models, Simulation & Physical AI)

- [[entities/yann-lecun]] — Turing Award winner, JEPA creator, AMI Labs founder ($1.03B seed at $3.5B); most prominent world models advocate.
- [[entities/ami-labs]] — LeCun's Paris-based $1.03B startup building JEPA-based world models; largest European seed round ever.
- [[entities/sora]] — OpenAI's text-to-video model; pioneered "video as world simulation"; discontinued March 2026.
- [[entities/genie]] — DeepMind's foundation world model: Genie 2 (3D interactive), Genie 3 (24fps real-time 720p).
- [[entities/nvidia-cosmos]] — World foundation model platform: 7B-14B models; 20M hours training; open license; 2M+ downloads.
- [[entities/dreamerv3]] — DeepMind general RL algorithm (Nature 2025): 150+ tasks, first Minecraft diamond from scratch.
- [[entities/world-labs]] — Fei-Fei Li's $230M startup; Marble platform for 3D world generation.
- [[entities/david-ha]] — Co-author of foundational World Models paper (2018).
- [[entities/jurgen-schmidhuber]] — LSTM co-inventor; World Models (2018) co-author.
- [[entities/melanie-mitchell]] — Santa Fe Institute; Orrery Spectrum; LLM world understanding analysis.

## Comparisons (World Models, Simulation & Physical AI)

- [[comparisons/world-models-vs-llms]] — World models vs LLMs as path to AGI; $1.3B+ bet on world models; convergence via hybrid architectures.
- [[comparisons/jepa-vs-generative-vs-contrastive]] — Three SSL paradigms: generative (pixels), contrastive (negatives), JEPA (representations).
- [[comparisons/world-model-platforms-comparison]] — AMI Labs vs Genie vs Cosmos vs World Labs: architecture, funding, applications.

## Sources (AI Geopolitics, US-China Race & Global Power Dynamics)

- [[sources/time-us-china-ai-race-graphs]] -- Data-driven analysis: US dominates with 93% of global LLM visits but China surging from 3% to 13% in two months; seven-month average quality gap narrowing; chip production asymmetry remains US advantage.
- [[sources/csis-deepseek-breakthrough-redefining-ai-race]] -- CSIS analysis: DeepSeek R1 achieves OpenAI o1-comparable results with far less compute; "not a Sputnik moment yet" but gap narrowing; advocates targeted export controls.
- [[sources/cfr-how-2026-decides-future-of-ai]] -- CFR: 2026 pivotal year; EU AI Act enforcement begins, US state regulations fragment, export control decisions could give China 2-3 year boost, 80%+ workers use unapproved AI.
- [[sources/cfr-china-ai-chip-deficit-huawei-nvidia]] -- CFR: US chips 5x more powerful (widening to 17x by 2027); Huawei produces 4-5% of Nvidia output; export controls working and should remain.
- [[sources/lawfare-china-ai-ecosystem-beyond-deepseek]] -- Lawfare deep dive: 2,100+ government guidance funds ($1.86T target), $137B direct investment, provincial competition, computing vouchers across 17 provinces.
- [[sources/nanonets-ai-warfare-pentagon-china-2026]] -- AI warfare: Project Maven ($480M), Operation Epic Fury (900 strikes in 12 hours), Pentagon AI systems, PLA pursuing fully autonomous combat decisions.
- [[sources/pernot-leplay-ai-regulation-china-eu-us]] -- Three-way comparison: EU (risk-based, rights-protective), US (sector-specific, innovation-first), China (agile, state-controlled, "develop hard, control tight").
- [[sources/crunchbase-q1-2026-record-ai-funding]] -- Q1 2026: $300B global VC ($242B in AI, 80% of total); OpenAI $122B, Anthropic $30B, xAI $20B; US captured 83% of global VC.
- [[sources/euronews-ai-brain-drain-europe]] -- Europe has 30% more AI talent per capita than US but net tech inflows halved; US salaries 30-70% higher; demand-supply ratio 3.2:1 globally.

## Concepts (AI Geopolitics, US-China Race & Global Power Dynamics)

- [[concepts/ai-geopolitics]] -- The intersection of AI development with international power dynamics: US-China competition, export controls, regulatory divergence, military AI, talent flows, sovereignty drives.
- [[concepts/us-china-ai-race]] -- The defining geopolitical competition: US leads in model quality (7-month gap), market share (93%), compute (5-17x), capital ($250B Q1 2026); China closing via efficiency, open source, state ecosystem.
- [[concepts/ai-chip-export-controls]] -- US restrictions on advanced AI chip exports; most potent policy lever; policy oscillating between restriction and relaxation; US chips 5-17x more powerful.
- [[concepts/ai-sovereignty]] -- A nation's ability to develop and control its own AI capabilities; 71% of executives call it existential; requires sovereignty across 6 layers; $600B market by 2030.
- [[concepts/open-source-vs-closed-ai]] -- Geopolitically charged debate: Chinese open-source usage surged from 1.2% to 30% in 2025; safety vs innovation; DeepSeek R1 MIT license; EU AI Act attempts middle path.
- [[concepts/ai-arms-race]] -- Escalating military AI competition: US has operational combat experience (Operation Epic Fury), China pursues fully autonomous combat decisions; no international treaty governs AI weapons.
- [[concepts/ai-regulation-landscape]] -- Three competing regulatory philosophies: EU (comprehensive, risk-based), US (fragmented, innovation-first), China (agile, state-controlled); race for global norms remains open.
- [[concepts/ai-talent-competition]] -- Global demand exceeds supply 3.2:1; Europe trains 30% more per capita but loses to 30-70% salary premiums; young scholars 100x more likely to leave academia.
- [[concepts/ai-industry-consolidation]] -- Extreme capital concentration: Q1 2026 $242B in AI VC; 4 companies captured 65% of all global VC; big tech infra spending approaching $700B.
- [[concepts/ai-industrial-policy]] -- Government AI strategies: China leads ($137B direct, 2,100+ funds); US relies on private sector ($500B Stargate); EU focuses on regulatory power.
- [[concepts/ai-military-applications]] -- Operational AI in combat by 2026: targeting (Gospel, Lavender), intelligence fusion (Maven), decision support (GenAI.mil), autonomous platforms.
- [[concepts/semiconductor-supply-chain]] -- Global AI chip supply chain centered on TSMC (Taiwan); SMIC constrained to 7nm creating 2+ generation gap; Taiwan geopolitically critical.
- [[concepts/brussels-effect]] -- EU regulations becoming de facto global standards through market power; AI Act may replicate GDPR success but outcome uncertain.

## Entities (AI Geopolitics)

- [[entities/nvidia]] -- Dominant AI chip company: 5-17x performance over Chinese competitors; 4.5M chips/year scaling to 10M+; lost $600B market value in one day after DeepSeek; H200 export controversy.
- [[entities/huawei]] -- China's leading AI chip maker: Ascend 910C at 60% of H100 performance; SMIC 7nm constraint; next-gen chip regresses; 4-5% of Nvidia production.

## Comparisons (AI Geopolitics)

- [[comparisons/us-vs-china-vs-eu-ai-regulation]] -- Three-way: EU (comprehensive, slow), US (fragmented, innovation-first), China (agile, state-controlled); no global standard has emerged.
- [[comparisons/us-vs-china-ai-military]] -- US has operational combat experience and integrated AI stack; China has efficiency advantage, domestic chips, and fully autonomous doctrine but zero combat testing.
- [[comparisons/nvidia-vs-huawei-ai-chips]] -- 5x current performance gap (widening to 17x by 2027), 20:1 production ratio; TSMC vs SMIC manufacturing constraint is binding.

## Sources (AGI, AI Economics, Compute Scaling & the Future of AI)

- [[sources/amodei-machines-of-loving-grace]] — Anthropic CEO's optimistic vision: powerful AI could compress a century of progress into 5-10 years across biology, mental health, economic development, and governance — if risks are managed.
- [[sources/aschenbrenner-situational-awareness]] — Former OpenAI researcher's influential essay arguing AGI by 2027 is "strikingly plausible," followed by rapid intelligence explosion to superintelligence, requiring trillion-dollar infrastructure and defense-grade security.
- [[sources/sutskever-ssi-safe-superintelligence]] — Ilya Sutskever declares the "age of scaling" over, pivots to research-driven breakthroughs at SSI — a $30B-valued company with 50 people, no products, and a singular mission to build safe superintelligence.
- [[sources/epoch-ai-scaling-limits-2030]] — Epoch AI projects 2e29 FLOP training runs feasible by 2030 — equivalent to another GPT-2→GPT-4 jump — with power as the binding constraint, followed by chip manufacturing capacity.
- [[sources/agi-timeline-predictions-2026]] — Comprehensive survey of AGI timeline predictions showing dramatic compression: median expert estimate moved from 2060-2070 (2020) to 2028-2033 (2026), with AI leaders predicting 2026-2027.
- [[sources/ai-economics-investment-2026]] — AI spending hits $2.52T in 2026 (Gartner); Big Tech CapEx at $700B; GDP contribution surpasses dot-com boom; but revenue gap and energy costs remain key risks.
- [[sources/ai-scaling-paradigm-shift-2026]] — The meaning of "scaling" has fundamentally shifted: from pre-training scale (2018-2023) to post-training (2023-2025) to test-time compute (2024+), with DeepSeek-R1 proving RL alone produces reasoning.

## Concepts (AGI, AI Economics, Compute Scaling & the Future of AI)

- [[concepts/path-to-agi]] — The convergence of scaling, algorithmic efficiency, and unhobbling gains suggests AGI between 2027-2033, with AI leaders predicting the earlier end and researchers the later — but definitions remain deeply contested.
- [[concepts/intelligence-explosion]] — The hypothesis that AGI could automate AI research itself, compressing decades of progress into months — producing superintelligence rapidly and creating the most consequential event in human history.
- [[concepts/compute-scaling]] — The multi-dimensional landscape of AI scaling: pre-training scaling shows diminishing returns, but test-time compute and algorithmic efficiency open new dimensions — constrained by power, chips, data, and capital.
- [[concepts/ai-optimism-and-abundance]] — The thesis that powerful AI could compress a century of human progress into 5-10 years — transforming biology, mental health, economics, and governance — articulated most fully by Dario Amodei.
- [[concepts/superalignment]] — The challenge of aligning AI systems that exceed human intelligence — requiring new approaches beyond RLHF, including scalable oversight, interpretability, and adversarial testing — with potentially civilization-level stakes.
- [[concepts/ai-economics]] — The trillion-dollar economics of AI: $2.52T global spending in 2026, $700B+ Big Tech CapEx, GDP impact surpassing the dot-com boom — but the revenue gap between investment and returns remains the central risk.
- [[concepts/ai-energy-and-infrastructure]] — Data centers consume 415 TWh (1.5% of global electricity) in 2024, doubling to 945 TWh by 2030 — with AI-driven servers growing at 30% annually, making power the binding constraint on AI scaling.
- [[concepts/data-wall]] — The looming exhaustion of high-quality training data — estimated by 2026-2028 — forcing the industry toward synthetic data, multimodal sources, and new learning paradigms.

## Entities (AGI, AI Economics, Compute Scaling & the Future of AI)

- [[entities/leopold-aschenbrenner]] — Former OpenAI superalignment researcher; author of "Situational Awareness" predicting AGI by 2027; founder of $1.5B+ hedge fund; one of the most influential voices shaping AI policy and investment discourse.
- [[entities/ilya-sutskever]] — Co-founder of OpenAI, architect of the scaling paradigm (AlexNet, GPT series); departed to found SSI in 2024; declared "the age of scaling is ending" in 2025, pivoting to research-driven breakthroughs for safe superintelligence.
- [[entities/safe-superintelligence-inc]] — Ilya Sutskever's AI lab: $30B valuation, ~50 employees, zero revenue, zero products — focused exclusively on building safe superintelligence with no commercial distractions.
- [[entities/epoch-ai]] — Research institute tracking AI compute trends, training data, and scaling limits — authors of the definitive analysis of whether AI scaling can continue through 2030.

## Comparisons (AGI, AI Economics, Compute Scaling & the Future of AI)

- [[comparisons/amodei-vs-aschenbrenner-vs-sutskever]] — Three influential AI thinkers offer divergent visions: Amodei (optimistic transformation), Aschenbrenner (urgent national security race), Sutskever (end of scaling, research-driven path).
- [[comparisons/scaling-vs-research-path-to-agi]] — The central debate: whether AGI comes from continued compute scaling (Aschenbrenner) or novel research breakthroughs (Sutskever) — with test-time compute as a possible third path.

## Sources (AI for Scientific Discovery)

- [[sources/alphafold-five-years-impact]] -- AlphaFold five-year retrospective: 3M+ researchers, 200M+ structures, 35K+ citations, Nobel Prize, AlphaFold 3 extends to all biomolecular interactions.
- [[sources/ai-drug-discovery-phase-iii-2026]] -- 173+ AI drug programs in clinical development; Insilico's 30-month timeline (vs 6-8yr); Phase I success 80-90% vs 52% historical; first approval projected 2026-2027.
- [[sources/gnome-materials-discovery]] -- GNoME: 2.2M crystals via graph neural networks, 380K stable, 52K graphene-like, 528 lithium conductors (25x). Berkeley A-Lab synthesized 41+ new materials.
- [[sources/funsearch-mathematical-discovery]] -- FunSearch: PaLM 2 + evaluator evolutionary loop solves cap set problem (largest advance in 20 years); interpretable code outputs.
- [[sources/gencast-weather-prediction]] -- GenCast: diffusion model outperforms ECMWF ENS on 97.2% of metrics; 15-day forecasts in 8 minutes on single TPU; used for humanitarian Anticipatory Action.
- [[sources/alphagenome-genomics]] -- AlphaGenome: 1M base-pair DNA input, predicts thousands of molecular properties, outperforms on 22/24 evaluations, covers non-coding 98% of genome.
- [[sources/alphaevolve-algorithm-discovery]] -- AlphaEvolve: Gemini-powered evolutionary agent; broke Strassen's 56-year matrix multiplication record; 0.7% Google compute savings; 20% improvement on 50+ open problems.
- [[sources/gemini-deep-think-scientific-discovery]] -- Gemini Deep Think: IMO gold (35/42), 4 Erdos conjectures solved, Aletheia agent, Vibe-Proving human-AI collaboration paradigm.
- [[sources/nobel-prizes-ai-2024]] -- 2024 Nobel Prizes: Physics (Hopfield, Hinton -- neural networks) and Chemistry (Baker -- protein design; Hassabis, Jumper -- AlphaFold). Both AI.
- [[sources/self-driving-labs-revolution]] -- Self-driving labs: AI + robotics automate entire scientific method; A-Lab (Berkeley), Periodic Labs (2025); cloud labs from $50K/month.
- [[sources/rfdiffusion3-protein-design]] -- RFdiffusion3 (Dec 2025): de novo protein design at atomic level; 10x faster than v2; atomically accurate antibodies; open-source.
- [[sources/ucsd-nine-ai-breakthroughs]] -- Nine AI breakthroughs: Alzheimer's gene causation, TB drug discovery, 25x faster climate modeling, AI wildfire detection.

## Concepts (AI for Scientific Discovery)

- [[concepts/ai-for-scientific-discovery]] -- AI's most transformative real-world impact: AlphaFold, GNoME, GenCast, AlphaEvolve, self-driving labs. Both 2024 Nobel Prizes went to AI researchers.
- [[concepts/ai-drug-discovery]] -- 173+ programs, 80-90% Phase I success (vs 52%), 30-month timelines (vs 6-8yr). 2026 Phase III results are the decisive test.
- [[concepts/ai-materials-science]] -- GNoME's 2.2M crystals (800yr equivalent); A-Lab autonomous synthesis; 528 lithium conductors, 52K graphene-like compounds.
- [[concepts/ai-mathematical-reasoning]] -- From struggling with arithmetic to IMO gold in 2 years; FunSearch cap sets, AlphaEvolve Strassen record, Deep Think Erdos conjectures.
- [[concepts/ai-protein-structure-prediction]] -- AlphaFold solved the 50-year protein folding problem; AF3 extends to all biomolecular interactions with 76% ligand accuracy.
- [[concepts/ai-protein-design]] -- De novo protein creation using diffusion models (RFdiffusion3); custom antibodies, enzymes, biosensors. David Baker Nobel 2024.
- [[concepts/ai-genomics]] -- AlphaGenome (non-coding 98%), AlphaMissense (coding 2%), Evo2 (128K+ genomes); from reading to designing genomes.
- [[concepts/ai-weather-climate]] -- GenCast outperforms ECMWF on 97%+; 8 min vs hours; operational at NOAA; Spherical DYffusion for 100-year climate projections.
- [[concepts/self-driving-labs]] -- AI + robotics autonomously design and execute experiments; A-Lab, Periodic Labs, Argonne; 10x throughput, months to days.
- [[concepts/nobel-prizes-ai-2024]] -- 2024 watershed: Physics (Hopfield, Hinton) and Chemistry (Baker, Hassabis/Jumper) both AI. Validates AI as fundamental scientific tool.
- [[concepts/llm-as-search-operator]] -- LLMs as creative candidate generators in evolutionary loops with automated verification; FunSearch and AlphaEvolve paradigm.
- [[concepts/generative-chemistry]] -- AI designs novel molecules from scratch; generative, physics-based, and retrosynthetic approaches; Insilico's 30-month timeline.

## Entities (AI for Scientific Discovery)

- [[entities/alphafold]] -- DeepMind's protein structure prediction: CASP14, 200M+ structures, 3M+ researchers, Nobel Prize, AF3 (76% ligand accuracy).
- [[entities/gnome]] -- Graph Networks for Materials Exploration: 2.2M crystals, 380K stable, 52K graphene-like, A-Lab integration.
- [[entities/funsearch]] -- DeepMind's LLM + evaluator for math discovery; cap set problem, bin packing; established LLM-as-search paradigm.
- [[entities/alphaevolve]] -- Gemini-powered evolutionary agent; Strassen record, 0.7% Google compute, kissing number, 50+ open problems.
- [[entities/gencast]] -- Diffusion weather model; 97.2% vs ECMWF ENS; 15-day in 8 minutes; tropical cyclones, wind energy.
- [[entities/alphagenome]] -- Non-coding genome AI (98%); 1M base-pair input; 22/24 evaluations superior; splicing, gene regulation.
- [[entities/rfdiffusion]] -- Baker Lab diffusion protein design; v3 (Dec 2025) all-atom, any molecule, 10x faster; atomically accurate antibodies.
- [[entities/demis-hassabis]] -- CEO Google DeepMind; 2024 Nobel Chemistry; founded Isomorphic Labs; AlphaFold architect.
- [[entities/david-baker]] -- UW Institute for Protein Design; 2024 Nobel Chemistry; Rosetta, RFdiffusion lineage.
- [[entities/geoffrey-hinton]] -- "Godfather of AI"; 2024 Nobel Physics; Boltzmann machines, backpropagation; AI safety advocate.
- [[entities/insilico-medicine]] -- Generative chemistry; rentosertib (IPF) 30-month target-to-Phase-I; Phase IIa positive.
- [[entities/recursion-pharmaceuticals]] -- Phenomics (2.2M experiments/week); merged with Exscientia (Jul 2025); 10+ programs.
- [[entities/isomorphic-labs]] -- Hassabis-founded (2021) drug discovery using AlphaFold; Alphabet subsidiary.

## Comparisons (AI for Scientific Discovery)

- [[comparisons/alphafold-vs-rfdiffusion]] -- Prediction vs design: AlphaFold tells you what exists; RFdiffusion creates what doesn't. Complementary Nobel Prize-winning approaches.
- [[comparisons/ai-scientific-domains-comparison]] -- Six domains compared on maturity: protein structure (Nobel) > weather (operational) > materials > genomics > math > drug approval.

## Sources (AI Robotics & Embodied Intelligence)

- [[sources/deloitte-physical-ai-humanoid-robots-2026]] -- Deloitte Tech Trends 2026: physical AI definition, VLA models, humanoid market ($30-50B by 2035), Waymo (10M+ rides), Amazon (1M robots), six deployment barriers.
- [[sources/google-deepmind-rt2-vla-model]] -- RT-2: pioneering VLA model (July 2023); PaLM-E/PaLI-X backbone; actions as text tokens; 62% novel scenario success (vs 32% RT-1); emergent reasoning from web pre-training.
- [[sources/physical-intelligence-pi0-foundation-model]] -- π0: 3B-param VLA with flow matching at 50Hz; trained on 8 robots, 68 tasks; 1.0 success on laundry folding where prior models score 0; open-sourced via Hugging Face.
- [[sources/llms-for-robotics-survey-2025]] -- Comprehensive 2025 survey: 4-pillar taxonomy (perception/decision/control/interaction); VLA evolution RT-1 to RT-2 to OpenVLA to π0 to GR00T; hallucination in planning and sub-300ms latency as key challenges.
- [[sources/saycan-grounding-language-robotic-affordances]] -- SayCan (Google 2022): LLM semantic scores x affordance functions; 84% plan success, 74% execution on 101 kitchen tasks; foundational for language-grounded robotics.
- [[sources/figure-ai-humanoid-robots]] -- Figure AI: $70M seed to $39B valuation in 3 years; three robot generations; OpenAI partnership ended for proprietary Helix VLA; BotQ factory targeting 12K units/year.
- [[sources/tesla-optimus-humanoid-robot]] -- Tesla Optimus: Gen 3 (22 DOF hands), FSD AI, summer 2026 production start; Rodney Brooks calls it "pure fantasy"; teleoperation-dependent demos criticized.
- [[sources/nvidia-isaac-groot-n1-foundation-model]] -- NVIDIA GR00T N1: first open humanoid foundation model; dual System 1/2 architecture; 780K synthetic trajectories in 11h (= 9 months human demo); adopted by Boston Dynamics, 1X, Agility.
- [[sources/nvidia-automate-sim-to-real-assembly]] -- AutoMate: sim-to-real assembly with only 4.2% gap; specialist 86.5% real success; generalist 84.5% (exceeded sim); assembly-by-disassembly trick.

## Concepts (AI Robotics & Embodied Intelligence)

- [[concepts/embodied-intelligence]] -- AI systems that perceive, reason, and physically act in the real world; three waves: classical, LLM-as-planner, end-to-end VLA; "the future of intelligent systems."
- [[concepts/vision-language-action-models]] -- Neural architectures unifying vision, language, and motor control; evolution from RT-2 (55B, text tokens) through π0 (3B, flow matching) to GR00T (dual system).
- [[concepts/foundation-models-for-robotics]] -- Pre-train broadly on internet + robot data, fine-tune with 1-20h demonstrations; π0, RT-2, GR00T, OpenVLA; VC investment $7.2B in 2025.
- [[concepts/humanoid-robots]] -- Human-shaped robots for infrastructure compatibility; UBS: 2M units by 2035, $30-50B TAM; Tesla ($20-30K), Figure ($39B valuation), Boston Dynamics ($140-150K).
- [[concepts/language-grounding-for-robots]] -- Connecting language to physical capabilities: affordance grounding (SayCan), scene graphs (SayPlan), closed-loop feedback, end-to-end VLAs.
- [[concepts/sim-to-real-transfer]] -- Training in simulation, deploying in reality; domain randomization, digital twins, massive synthetic data (780K trajectories in 11h); AutoMate at 4.2% gap.
- [[concepts/dexterous-manipulation]] -- Human-level hand skills for robots; π0 first to fold laundry (1.0 success); hardware frontier: 22 DOF hands, 3-gram tactile sensors.
- [[concepts/cross-embodiment-transfer]] -- One model controlling diverse robot morphologies; π0 spans 7-8 robot types; Open X-Embodiment pools 800K trajectories.
- [[concepts/robot-learning-from-demonstration]] -- Teaching via teleoperation, motion capture, human video, synthetic demos; π0 needs 1-20h per task; growing gig economy of remote teleoperators.
- [[concepts/autonomous-driving]] -- Most mature physical AI domain; end-to-end transition; Waymo (10M+ rides), NVIDIA Alpamayo-R1, DeepRoute 40B VLA.

## Entities (AI Robotics & Embodied Intelligence)

- [[entities/rt-2]] -- Google DeepMind's pioneering VLA (July 2023, 55B params); encodes actions as text tokens; emergent web knowledge transfer; chain-of-thought for robot planning.
- [[entities/pi0]] -- Physical Intelligence's 3B VLA with flow matching at 50Hz; trained on 8 robots, 68 tasks; first to fold laundry and assemble boxes; open-sourced via Hugging Face.
- [[entities/physical-intelligence]] -- SF robotics startup; raised $400M+; built π0, the first robot foundation model achieving complex dexterous tasks.
- [[entities/figure-ai]] -- Humanoid robot company ($39B valuation); three robot generations; pivoted from OpenAI to Helix VLA; BotQ targeting 12K units/year.
- [[entities/tesla-optimus]] -- Tesla's humanoid robot; Gen 3 (22 DOF hands), 125 lb; shares AI with FSD; production summer 2026; faces sustained skepticism.
- [[entities/nvidia-groot]] -- NVIDIA's open humanoid foundation model; dual System 1/2 architecture; adopted by Boston Dynamics, 1X, Agility, NEURA, Franka.
- [[entities/saycan]] -- Google's foundational language-to-affordance grounding (2022); 84% plan success; precursor to RT-2 and VLA paradigm.
- [[entities/helix-vla]] -- Figure AI's proprietary VLA replacing OpenAI partnership; full-body autonomy (Jan 2026); "high rate robot control" over language understanding.
- [[entities/boston-dynamics]] -- Pioneer robotics company; Electric Atlas for enterprise ($140-150K); DeepMind Gemini + NVIDIA GR00T partnerships.
- [[entities/waymo]] -- Alphabet's autonomous driving subsidiary; 10M+ paid robotaxi rides; most commercially advanced AV service.

## Comparisons (AI Robotics & Embodied Intelligence)

- [[comparisons/rt2-vs-pi0-vs-groot]] -- Three robot foundation models: RT-2 (pioneer, emergent reasoning), π0 (dexterous, open-source), GR00T (open platform, synthetic data ecosystem).
- [[comparisons/tesla-optimus-vs-figure-vs-atlas]] -- Three humanoid programs: Tesla (mass-market, FSD AI), Figure (fastest iteration, Helix VLA), Boston Dynamics (engineering depth, $140-150K).

## Sources (Neuroscience-Inspired AI & Biological Intelligence)

- [[sources/neuroai-catalyzing-next-gen-ai]] — Landmark NeuroAI consortium paper: neuroscience should guide next-gen AI through sample efficiency, sparse coding, complementary learning systems, embodied cognition.
- [[sources/ai-consciousness-evidence-debate]] — Assessment of AI consciousness evidence using 14 theory-derived indicators; 25-35% credence for frontier models; asymmetric risk in false negatives.
- [[sources/neuralink-bci-2026-status]] — Neuralink 2026: 12 patients implanted, high-volume production planned, tension between medical device focus and transhumanist ambitions.
- [[sources/free-energy-principle-unified-brain-theory]] — Karl Friston's free energy principle: unified brain theory connecting perception, action, learning to VAEs and generative AI via the ELBO.
- [[sources/sleep-replay-catastrophic-forgetting]] — Sleep Replay Consolidation (SRC): offline Hebbian phases recover first-task accuracy from 5% to 63% on CUB-200.
- [[sources/hippocampus-stability-plasticity-dilemma]] — Hippocampus-inspired approach to stability-plasticity: dual-process learning with SWR-BARR dynamics.
- [[sources/neuromorphic-computing-mainstream-2026]] — Neuromorphic computing goes mainstream: Intel Loihi 3 (8M neurons, 1.2W) and IBM NorthPole (72.7x GPU efficiency) enter commercial production.
- [[sources/biological-vs-artificial-neural-networks]] — Systematic comparison: biological (86B neurons, 20W, Hebbian) vs artificial (millions of params, kilowatts, backprop) across 10 dimensions.
- [[sources/memory-systems-brain-to-ai-agents]] — Comprehensive survey mapping biological memory (episodic, semantic, procedural, working) to AI agent architectures.
- [[sources/neuro-inspired-dynamic-sparsity-efficiency]] — Brain-inspired dynamic sparsity (spatial, temporal, activation, structural) for 10-1000x AI energy reduction.

## Concepts (Neuroscience-Inspired AI & Biological Intelligence)

- [[concepts/neuroai]] — The interdisciplinary field at the intersection of neuroscience and AI, arguing biological intelligence holds the key to next-gen AI.
- [[concepts/brain-inspired-ai]] — AI systems designed using biological brain principles: sparse coding, complementary learning, predictive processing, sleep consolidation, spiking networks.
- [[concepts/predictive-coding]] — The brain continuously generates top-down predictions and only processes bottom-up prediction errors — a hierarchical prediction machine that minimizes surprise.
- [[concepts/free-energy-principle]] — Karl Friston's mathematical framework: all adaptive systems minimize variational free energy; negative FE = ELBO, bridging neuroscience and generative AI.
- [[concepts/active-inference]] — Extension of the FEP to action: organisms minimize surprise by changing the world to match predictions, not just updating internal models.
- [[concepts/bayesian-brain]] — The brain represents information as probability distributions and performs approximate Bayesian inference, combining priors with sensory evidence.
- [[concepts/complementary-learning-systems]] — The brain's dual-system solution: fast hippocampus for rapid encoding, slow neocortex for long-term storage, sleep-mediated transfer between them.
- [[concepts/continual-learning]] — Learning new tasks without forgetting old ones — natural for brains, challenging for neural networks; addressed by replay, regularization, architecture.
- [[concepts/sleep-consolidation-ai]] — Implementing biological sleep-like offline phases in neural networks using Hebbian replay to consolidate memories and prevent catastrophic forgetting.
- [[concepts/sparse-coding]] — Only a small fraction of neurons active at any time — the brain's energy-efficient coding strategy, now applied for 10-1000x AI efficiency gains.
- [[concepts/efficient-coding-hypothesis]] — Barlow's 1961 principle: sensory neurons maximize information while minimizing redundancy and energy — the theoretical foundation for sparse and predictive coding.
- [[concepts/neuromorphic-computing]] — Brain-inspired hardware using spiking neural networks and event-driven processing; Intel Loihi 3 and IBM NorthPole go commercial in 2026.
- [[concepts/brain-computer-interfaces]] — Direct communication between brain and external devices; from medical restoration (paralysis) to potential cognitive enhancement.
- [[concepts/ai-consciousness]] — The debate over whether AI can have subjective experience; 14 theory-derived indicators, no proof but mounting signals and asymmetric risk.
- [[concepts/computational-functionalism]] — Consciousness depends on information-processing patterns, not substrate — if true, silicon AI could in principle be conscious.
- [[concepts/neurotechnology]] — Technologies interfacing with the nervous system: BCIs, neuromorphic chips, neural decoding, brain stimulation, neurodiagnostics.

## Entities (Neuroscience-Inspired AI & Biological Intelligence)

- [[entities/karl-friston]] — British neuroscientist at UCL; originator of the free energy principle; most cited neuroscientist; mathematical bridge between brain theory and VAEs.
- [[entities/neuralink]] — Elon Musk's BCI company: 12 patients, The Link implant, high-volume production planned 2026, medical vs transhumanist tension.
- [[entities/intel-loihi]] — Intel's neuromorphic processor family: Loihi 1 (2018) → Loihi 3 (2025, 8M neurons, 1.2W, first commercial), 100-1000x GPU efficiency.
- [[entities/ibm-northpole]] — IBM neuromorphic chip: 256 co-located memory-compute cores, 72.7x GPU efficiency for LLM inference, full production 2026.
- [[entities/david-chalmers]] — Philosopher; "hard problem of consciousness"; co-author of 14-indicator AI consciousness framework with Butlin, Long, and Bengio.

## Comparisons (Neuroscience-Inspired AI & Biological Intelligence)

- [[comparisons/biological-vs-artificial-neural-networks]] — Brain (86B neurons, 20W, Hebbian, continuous adaptation) vs AI (millions of params, kilowatts, backprop, train/deploy) across 10 dimensions.
- [[comparisons/neuromorphic-vs-gpu-computing]] — Neuromorphic (100-1000x efficiency, event-driven, edge) vs GPU (training, ecosystem, scale): complementary, not competitive.
