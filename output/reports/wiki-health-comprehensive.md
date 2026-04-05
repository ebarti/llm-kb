---
title: "Wiki Health Comprehensive Audit"
type: report
generated: 2026-04-05
wiki_snapshot: 2026-04-06 00:55
---

# Wiki Health: Comprehensive Audit Report

## Executive Summary

This wiki is a substantial, well-structured LLM knowledge base containing **854 markdown files** totaling approximately **347,000 words** across 14 topic domains. It demonstrates the viability of the Karpathy-style LLM-maintained wiki at a scale that significantly exceeds the original ~100-article, ~400K-word benchmark. The wiki has strong cross-linking (8,069 wikilinks, averaging ~9.4 per article), comprehensive coverage across its declared domains, and consistent article structure.

Key findings:
- **Strengths**: Excellent topical breadth, consistent frontmatter, high link density, well-maintained metadata infrastructure
- **Weaknesses**: All content compiled on a single date (2026-04-05), 12 orphan articles, root-level navigation files have unknown compilation dates, some topics significantly deeper than others
- **Recommendation**: Prioritize temporal diversity (ongoing ingestion), deepen thin entity articles, resolve orphan links, and begin freshness-based maintenance cycles

---

## 1. Overall Statistics

### File Counts

| Directory | File Count | Percentage |
|-----------|-----------|------------|
| sources/ | 300 | 35.1% |
| concepts/ | 321-322 | 37.6% |
| entities/ | 166 | 19.4% |
| comparisons/ | 53-54 | 6.3% |
| Root (navigation) | 9 | 1.1% |
| _meta/ | 5 | 0.6% |
| **Total** | **854** | **100%** |

### Word Counts

| Directory | Word Count | Avg Words/Article | Min | Max |
|-----------|-----------|-------------------|-----|-----|
| sources/ | 91,821 | 306 | 180 | 547 |
| concepts/ | ~178,455 | 560 | 233 | 1,127 |
| entities/ | 45,331 | 277 | 120 | 804 |
| comparisons/ | 29,018 | 545 | 324 | 816 |
| **Total content** | **~347,000** | **~410** | - | - |

Source: `wiki/_meta/stats.json` and direct word count analysis.

### Top Articles by Length

| Article | Words | Type |
|---------|-------|------|
| Reading-List.md | 6,525 | Navigation |
| _meta/links.md | 2,398 | Meta |
| [[concepts/retrieval-augmented-generation]] | 780 | Concept |
| [[concepts/synthetic-data-generation]] | 682 | Concept |
| [[concepts/text-embeddings]] | 682 | Concept |
| [[concepts/fine-tuning]] | 626 | Concept |
| [[concepts/vector-search]] | 569 | Concept |
| [[concepts/plain-text-longevity]] | 518 | Concept |
| [[entities/andrej-karpathy]] | 498 | Entity |
| [[sources/forte-building-second-brain]] | 482 | Source |

### Link Density

| Metric | Value |
|--------|-------|
| Total wikilinks (across content directories) | 8,069 |
| Average wikilinks per article | ~9.4 |
| Articles in backlink graph (_meta/links.md) | Comprehensive coverage |

The link density is strong. At 9.4 wikilinks per article on average, the wiki forms a well-connected knowledge graph even without a formal graph database layer. This validates the [[concepts/cheap-ontology]] thesis that wikilinks provide meaningful structure without formal ontology engineering.

---

## 2. Coverage Analysis: Topic Depth

### Topic Distribution

Based on the summaries in `wiki/_meta/summaries.md`, the wiki covers 14 major topic areas:

| Topic Domain | Sources | Concepts | Entities | Comparisons | Total | Depth Rating |
|-------------|---------|----------|----------|-------------|-------|-------------|
| LLM Knowledge Bases (core) | 11 | 15 | 18 | 8 | 52 | Deep |
| Context Windows & Memory | 11 | 10 | 3 | 1 | 25 | Deep |
| Data Pipelines & Document Processing | 9 | 7 | 10 | 3 | 29 | Deep |
| Embeddings, Vector Search & Retrieval | 10 | 14 | 6 | 3 | 33 | Deep |
| Knowledge Graphs & Graph Databases | 10 | 11 | 4 | 3 | 28 | Deep |
| Prompt Engineering | 11 | 13 | 6 | 3 | 33 | Deep |
| Multimodal AI & Vision | 8 | 8 | 3 | 1 | 20 | Moderate |
| Markdown & Plain Text | 8 | 7 | 8 | 1 | 24 | Moderate |
| Synthetic Data & Fine-Tuning | 8 | 11 | 2 | 2+ | 23+ | Moderate |
| Information Extraction | 6 | 9 | 6 | 1 | 22 | Moderate |
| Agentic AI & Tool Use | 11 | 11 | 3 | 2 | 27 | Deep |
| Open-Source LLMs & Local Inference | 12 | 8 | 10 | 4 | 34 | Deep |
| AI Safety, Governance & Evaluation | (multiple) | (multiple) | (multiple) | (multiple) | est. 40+ | Moderate |
| AI UX & Product Design | (multiple) | (multiple) | (multiple) | (multiple) | est. 20+ | Thin-Moderate |

### Deep Topics (Strong Coverage)

These topics have 10+ sources, multiple concept articles, entity profiles, and comparison pieces:

1. **LLM Knowledge Bases (core)**: 11 sources, 15 concepts, 18 entities, 8 comparisons. This is the wiki's centerpiece and is comprehensively covered.
2. **Embeddings & Vector Search**: 10 sources, 14 concepts. Excellent technical depth from embedding theory to HNSW to production vector databases.
3. **Prompt Engineering**: 11 sources, 13 concepts. Covers the full spectrum from basic techniques to meta-prompting and automated optimization.
4. **Agentic AI**: 11 sources, 11 concepts. Good coverage of agent architecture, tool use, MCP, and multi-agent collaboration.
5. **Open-Source LLMs**: 12 sources, 8 concepts, 10 entities. Strong landscape coverage with benchmarks and comparisons.

### Thin Topics (Need Deepening)

1. **Multimodal AI**: Only 1 comparison article. Needs more comparative analysis and practical integration guides.
2. **Information Extraction**: Only 6 sources. The extraction pipeline is critical for wiki compilation but under-sourced.
3. **AI UX & Product Design**: Referenced in [[concepts/knowledge-base-product-gap]] but coverage is scattered. Could benefit from consolidation.

---

## 3. Quality Assessment

### Cross-Linking Quality

**Well-linked articles** (high incoming + outgoing links):

| Article | Incoming Links | Outgoing Links | Assessment |
|---------|---------------|----------------|------------|
| [[concepts/llm-knowledge-base]] | 50+ | 6 | Hub article, excellent connectivity |
| [[concepts/knowledge-graph]] | 25+ | 10 | Well-connected across domains |
| [[concepts/rag-vs-index-based-retrieval]] | 25+ | 3 | Heavily referenced, could link out more |
| [[concepts/wiki-compilation]] | 22+ | 7 | Core concept, well-linked |
| [[concepts/hallucination-contamination]] | 15+ | 7 | Important topic, well-linked |
| [[entities/andrej-karpathy]] | 3 incoming | 15 outgoing | Entity hub with strong outgoing links |

**Poorly linked articles** (orphans with 0 incoming wikilinks):

| Orphan Article | Type | Issue |
|---------------|------|-------|
| sources/speculative-decoding-bentoml | Source | Not referenced by any concept or comparison |
| comparisons/heuristic-vs-model-based-filtering | Comparison | Not referenced from parent concepts |
| comparisons/vllm-vs-sglang | Comparison | Not linked from entity or concept articles |
| comparisons/ragas-vs-deepeval | Comparison | Not linked from evaluation concepts |
| comparisons/llm-judge-vs-human-evaluation | Comparison | Not linked from evaluation concepts |
| comparisons/conversational-vs-structured-vs-hybrid-ai-ui | Comparison | Not linked from UX concepts |
| comparisons/manual-vs-ai-pkm | Comparison | Duplicate of manual-pkm-vs-llm-pkm? |
| comparisons/static-vs-dynamic-benchmarks | Comparison | Not linked from benchmark concepts |
| comparisons/zettelkasten-vs-basb | Comparison | Not linked from PKM concepts |
| comparisons/personal-vs-enterprise-knowledge-systems | Comparison | Not linked from KB concepts |
| comparisons/fineweb-vs-dclm-vs-nemotron-cc | Comparison | Not linked from data concepts |
| comparisons/consensus-vs-federated-vs-ai-knowledge | Comparison | Not linked from collective intelligence concepts |

**Total orphans identified**: 12 articles (1.4% of total). This is a reasonable rate for a wiki of this size, but each orphan represents a missed connection.

### Frontmatter Consistency

Based on sampling, articles consistently include:
- `title`: Present in all sampled articles
- `type`: Present (source-summary, concept, comparison, entity)
- `sources`: Present in concept articles (linking back to source summaries)
- `related`: Present in most articles
- `last_compiled`: Present in most articles (2026-04-05)
- `summary`: Present in most articles (one-line description)
- `reading_time`: Present in some articles

**Assessment**: Frontmatter is consistent and well-structured. The YAML schema serves as a lightweight ontology, confirming the [[concepts/cheap-ontology]] approach.

### Article Structure Consistency

Source summaries follow a consistent template:
1. YAML frontmatter
2. Key Points (bullet list)
3. Detailed Summary
4. Notable Quotes
5. Related Concepts

Concept articles follow:
1. YAML frontmatter
2. Overview
3. Key Ideas
4. Sources
5. Related Concepts
6. Related Entities
7. Related Comparisons

**Assessment**: Template adherence is high, making the wiki navigable and predictable. This is a direct benefit of LLM-authored content following explicit instructions.

---

## 4. Metadata Infrastructure Assessment

### _meta/summaries.md

- **Status**: Comprehensive. Covers all topic domains with one-line summaries.
- **Length**: ~800 words of summaries (18,747 tokens total with formatting)
- **Assessment**: This is the primary index for [[concepts/rag-vs-index-based-retrieval|index-based retrieval]]. At 854 articles, it is approaching the upper bound of what can fit in a single context window for some models. Consider hierarchical indexes (topic-level summaries pointing to article-level) for continued scaling.

### _meta/links.md

- **Status**: Comprehensive backlink graph
- **Coverage**: All major articles mapped with incoming and outgoing links
- **Assessment**: Well-maintained. Enables rapid identification of hub articles, orphans, and connection patterns.

### _meta/manifest.md

- **Status**: Tracks 100 compiled raw files
- **Assessment**: All entries show compilation date of 2026-04-05. The manifest is functional but would benefit from tracking compilation version/prompt to enable re-compilation with improved prompts.

### _meta/stats.json

- **Status**: Single snapshot (2026-04-06 00:55)
- **Assessment**: Currently only one history entry. Designed for growth tracking but needs ongoing snapshots to show trajectory.

### _meta/citation-report.md

- **Status**: Identified 2 potential unsourced claims
- **Assessment**: Very clean. Only 2 flagged claims out of 854 articles suggests high provenance discipline.

### _meta/freshness-report.md

- **Status**: 9 root/navigation files show "unknown" compilation date (score 0.15). All content articles show 2026-04-05 (score 0.65).
- **Assessment**: The uniform compilation date means the freshness score is uninformative currently. It will become valuable as articles are updated at different times.

---

## 5. Growth Trajectory

### Current State

| Metric | Value |
|--------|-------|
| Total files | 854 |
| Total words | ~347,000 |
| Total wikilinks | 8,069 |
| Topic domains | 14 |
| Raw files compiled | 100 |
| Compilation date | 2026-04-05 (single batch) |

### Observations

1. **Single-batch compilation**: The entire wiki was compiled in a single pass on 2026-04-05. This means the wiki has not yet demonstrated the incremental compilation capability that is a core feature of the Karpathy workflow ([[concepts/wiki-compilation]]).

2. **Scale validation**: At 854 files and ~347K words, the wiki exceeds Karpathy's ~100-article benchmark by 8.5x. This demonstrates that the approach scales beyond personal scale, though it raises the question of whether index-based retrieval remains sufficient at this size.

3. **Compilation ratio**: 100 raw files produced 854 wiki articles — an ~8.5x expansion ratio. This is high, indicating thorough extraction of concepts, entities, and comparisons from each source.

4. **Word efficiency**: Average article length of 410 words is appropriate for a wiki — detailed enough to be useful, concise enough to be scannable.

---

## 6. Recommendations

### Priority 1: Begin Incremental Ingestion (Critical)

The wiki was compiled in a single batch. To realize the self-reinforcing "filing loop" ([[sources/glenrhodes-karpathy-workflow]]), begin regular ingestion of new sources:

- Ingest 2-3 new sources per week
- Run incremental compilation after each batch
- Verify that new articles are properly cross-linked to existing content
- Track compilation dates in manifest for freshness reporting

### Priority 2: Resolve Orphan Articles (High)

The 12 identified orphan articles (especially in `comparisons/`) should be linked from their parent concept or entity articles. Specific actions:

| Orphan | Link From |
|--------|-----------|
| comparisons/vllm-vs-sglang | [[entities/vllm]], [[concepts/local-llm-inference]] |
| comparisons/ragas-vs-deepeval | [[concepts/rag-evaluation]] |
| comparisons/llm-judge-vs-human-evaluation | [[concepts/rag-evaluation]] |
| comparisons/zettelkasten-vs-basb | [[concepts/personal-knowledge-management]] |
| comparisons/manual-vs-ai-pkm | Review for duplication with manual-pkm-vs-llm-pkm |
| comparisons/static-vs-dynamic-benchmarks | [[concepts/benchmark-saturation]] |
| comparisons/consensus-vs-federated-vs-ai-knowledge | [[concepts/collaborative-knowledge-building]] |

### Priority 3: Deepen Entity Articles (Medium)

Entity articles average only 277 words (vs. 560 for concepts). Many entities serve as simple stubs. Prioritize deepening:

- Entities with high incoming link counts (they are referenced frequently but may lack detail)
- Tool entities that would benefit from usage examples and integration patterns
- Person entities that would benefit from publication lists and contribution summaries

### Priority 4: Create Topic-Level Indexes (Medium)

At 854 articles, the flat `summaries.md` approach is reaching scale limits. Create topic-level index files:

```
wiki/_meta/indexes/
  knowledge-bases.md      <- Index for core KB topic
  retrieval.md            <- Index for RAG, vector search, etc.
  agents.md               <- Index for agentic AI topics
  ...
```

This enables hierarchical navigation: topic index -> article summaries -> full articles.

### Priority 5: Establish Health Check Cadence (Medium)

Set up regular automated health checks ([[concepts/linting-and-health-checks]]):

- **Weekly**: Orphan detection, broken link scan
- **Monthly**: Freshness report, coverage gap analysis, stats snapshot
- **Quarterly**: Full citation audit, contradiction scan, schema consistency check

### Priority 6: Address Coverage Gaps (Low-Medium)

Identified thin areas that would benefit from additional source ingestion:

1. **Multimodal knowledge integration**: How to incorporate images, diagrams, and visual content into a markdown wiki
2. **Evaluation frameworks**: Standardized approaches to measuring KB quality
3. **Collaborative knowledge building**: Multi-user wiki workflows
4. **AI governance for knowledge bases**: Compliance, access control, audit trails
5. **Practical MCP integration**: How to expose the wiki as an MCP resource for LLM agents

### Priority 7: Implement Growth Tracking (Low)

The `stats.json` file has history support but only one snapshot. Automate periodic snapshots to track:

- Article count over time (growth rate)
- Word count over time
- Link density over time
- Topic distribution shifts
- Quality metrics (orphan rate, freshness scores)

---

## 7. Risk Assessment

| Risk | Severity | Current Status | Mitigation |
|------|----------|---------------|------------|
| [[concepts/hallucination-contamination]] | High | 2 unsourced claims flagged | Regular citation audits |
| Scale ceiling for index-based retrieval | Medium | At ~347K words, approaching limits | Plan hierarchical indexes or RAG addition |
| Single-point-of-failure (one compilation batch) | Medium | All articles same date | Begin incremental compilation |
| Entity article thinness | Low | Avg 277 words | Prioritize deepening high-traffic entities |
| Orphan articles | Low | 12 orphans (1.4%) | Link resolution pass |

---

## 8. Comparison to Best Practices

| Best Practice | This Wiki | Assessment |
|--------------|-----------|------------|
| Raw sources preserved as source of truth | Yes (raw/ directory) | Excellent |
| LLM-authored, not human-edited | Yes | Excellent |
| Consistent frontmatter schema | Yes (YAML with type, sources, related) | Excellent |
| Wikilink cross-referencing | Yes (8,069 links) | Excellent |
| Backlink graph maintained | Yes (_meta/links.md) | Excellent |
| Compilation manifest | Yes (_meta/manifest.md) | Good |
| One-line summaries index | Yes (_meta/summaries.md) | Good (approaching scale limit) |
| Incremental compilation | Not yet demonstrated | Needs implementation |
| Regular health checks | Citation report exists, freshness report exists | Good infrastructure, needs cadence |
| Vault separation | Yes (wiki/ is separate from any personal notes) | Excellent |
| Filing loop (outputs filed back) | output/ directory exists | Needs active use |
| Freshness tracking | Infrastructure exists | Needs temporal diversity |

---

## 9. Summary Scorecard

| Dimension | Score (1-10) | Notes |
|-----------|-------------|-------|
| **Coverage breadth** | 9 | 14 topic domains, 854 articles |
| **Coverage depth** | 7 | Deep in core topics, thin in some areas |
| **Cross-linking quality** | 8 | 8,069 links, 9.4 avg per article, 12 orphans |
| **Article consistency** | 9 | Uniform templates, consistent frontmatter |
| **Metadata infrastructure** | 8 | All key meta files present and maintained |
| **Freshness** | 4 | Single compilation date, no temporal diversity |
| **Incremental capability** | 3 | Infrastructure exists but not yet exercised |
| **Health check maturity** | 5 | Reports exist but no established cadence |
| **Overall** | **7/10** | Strong foundation, needs operational maturity |

---

## 10. Sources for This Report

### Metadata Files Analyzed
- `wiki/_meta/stats.json` — file and word count statistics
- `wiki/_meta/summaries.md` — article summaries and topic categorization
- `wiki/_meta/links.md` — backlink graph
- `wiki/_meta/manifest.md` — compilation tracking
- `wiki/_meta/citation-report.md` — unsourced claim detection
- `wiki/_meta/freshness-report.md` — article freshness scores

### Wiki Concept Articles Referenced
- [[concepts/llm-knowledge-base]] — core system definition
- [[concepts/wiki-compilation]] — compilation pipeline
- [[concepts/linting-and-health-checks]] — maintenance methodology
- [[concepts/rag-vs-index-based-retrieval]] — retrieval scaling decision
- [[concepts/hallucination-contamination]] — primary risk
- [[concepts/cheap-ontology]] — cost disruption framing
- [[concepts/data-quality-bottleneck]] — quality as decisive factor

### Source Articles Referenced
- [[sources/karpathy-llm-knowledge-bases]] — original workflow
- [[sources/dairai-llm-knowledge-bases-architecture]] — four-phase architecture
- [[sources/glenrhodes-karpathy-workflow]] — filing loop
- [[sources/pebblous-cheap-ontology]] — scaling context
