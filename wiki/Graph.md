---
title: "Graph Analysis"
type: reference
last_updated: 2026-04-05
reading_time: "5 min"
---

# Graph Analysis

Static analysis of the wiki's internal link graph, computed from [[_meta/links]].

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
| 1 | [[concepts/llm-knowledge-base]] | 24 | 5 | 29 | Central hub -- every source and concept links here |
| 2 | [[concepts/rag-vs-index-based-retrieval]] | 10 | 2 | 12 | Key infrastructure concept |
| 3 | [[concepts/wiki-compilation]] | 8 | 2 | 10 | Core pipeline concept |
| 4 | [[concepts/knowledge-graph]] | 6 | 4 | 10 | Bridge between formal KG and markdown approaches |
| 5 | [[concepts/personal-knowledge-management]] | 5 | 4 | 9 | Human workflow hub |
| 6 | [[concepts/hallucination-contamination]] | 5 | 4 | 9 | Central risk concept |
| 7 | [[concepts/linting-and-health-checks]] | 5 | 2 | 7 | Quality assurance hub |
| 8 | [[concepts/obsidian-as-ide]] | 5 | 2 | 7 | Tooling hub |
| 9 | [[concepts/multi-agent-systems]] | 4 | 3 | 7 | Multi-agent architecture hub |
| 10 | [[concepts/data-quality-bottleneck]] | 3 | 4 | 7 | Risk/quality hub |

---

## Bridge Nodes

Articles that connect otherwise separate topic clusters. Removing these would fragment the graph.

| Bridge Node | Clusters Connected |
|-------------|-------------------|
| [[concepts/knowledge-graph]] | Connects the formal KG cluster (KARMA, Graphiti, Gallagher) to the markdown wiki cluster |
| [[concepts/rag-vs-index-based-retrieval]] | Bridges retrieval infrastructure debates (vector DBs, HN debate) to the core LLM-KB system |
| [[concepts/hallucination-contamination]] | Connects risk/quality cluster to the vault-separation and linting topics |
| [[concepts/personal-knowledge-management]] | Bridges the human workflow side (second brain, product gap) to the technical system |
| [[concepts/cheap-ontology]] | Links ontology/knowledge-representation theory to practical markdown implementation |
| [[concepts/multi-agent-systems]] | Connects KARMA and STORM (academic systems) to the broader KB concepts |

---

## Cluster Identification

### Cluster 1: Core LLM-KB System
The densest cluster, centered on [[concepts/llm-knowledge-base]].
- [[concepts/wiki-compilation]]
- [[concepts/obsidian-as-ide]]
- [[concepts/llm-qa-over-documents]]
- [[concepts/linting-and-health-checks]]
- [[concepts/post-code-ai-workflow]]
- [[concepts/markdown-as-universal-interface]]

### Cluster 2: Retrieval & Infrastructure
Focused on how knowledge is retrieved and stored.
- [[concepts/rag-vs-index-based-retrieval]]
- [[concepts/vector-databases]]
- [[sources/hn-vector-database-debate]]
- [[sources/decodingai-second-brain-rag]]

### Cluster 3: Knowledge Graphs & Multi-Agent
Formal knowledge representation and automated systems.
- [[concepts/knowledge-graph]]
- [[concepts/multi-agent-systems]]
- [[concepts/automated-wiki-creation]]
- [[concepts/temporal-knowledge]]
- [[sources/karma-multi-agent-knowledge-graph]]
- [[sources/storm-automated-wiki-creation]]
- [[sources/graphiti-temporal-knowledge-graphs]]

### Cluster 4: Risk & Quality
Focused on failure modes and mitigations.
- [[concepts/hallucination-contamination]]
- [[concepts/data-quality-bottleneck]]
- [[concepts/vault-separation]]
- [[concepts/linting-and-health-checks]]

### Cluster 5: Human Workflow & PKM
Human-facing knowledge management evolution.
- [[concepts/personal-knowledge-management]]
- [[concepts/second-brain]]
- [[concepts/knowledge-base-product-gap]]
- [[sources/gallagher-second-brain-knowledge-graphs]]
- [[sources/glenrhodes-karpathy-workflow]]

### Cluster 6: Ontology & Representation
Knowledge representation theory.
- [[concepts/cheap-ontology]]
- [[concepts/markdown-as-universal-interface]]
- [[sources/pebblous-cheap-ontology]]

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

[[concepts/llm-knowledge-base]] exhibits a strong star pattern: nearly every other article links to it, making it the gravitational center. This is expected for the core concept, but suggests that:

1. **Adding more mid-tier hub nodes** would improve navigability (e.g., split "llm-knowledge-base" into sub-concepts if it grows too large)
2. **Cross-cluster links** are primarily mediated through this single node -- creating direct links between peripheral clusters would improve resilience

---

## Leaf Nodes (Fewest Connections)

| Article | Incoming | Outgoing | Total |
|---------|----------|----------|-------|
| [[concepts/post-code-ai-workflow]] | 1 | 2 | 3 |
| [[concepts/temporal-knowledge]] | 2 | 2 | 4 |
| [[concepts/vault-separation]] | 2 | 3 | 5 |
| [[concepts/automated-wiki-creation]] | 2 | 3 | 5 |

These are candidates for further development and cross-linking.

---

## Source Coverage

Every source links to [[concepts/llm-knowledge-base]]. Source-to-source links are absent (by design -- sources link to concepts, not to each other).

| Source | Concepts Linked |
|--------|----------------|
| [[sources/karpathy-llm-knowledge-bases]] | 6 |
| [[sources/antigravity-post-code-ai-workflow]] | 6 |
| [[sources/pebblous-cheap-ontology]] | 5 |
| [[sources/dairai-llm-knowledge-bases-architecture]] | 5 |
| [[sources/glenrhodes-karpathy-workflow]] | 5 |
| [[sources/gallagher-second-brain-knowledge-graphs]] | 4 |
| [[sources/storm-automated-wiki-creation]] | 4 |
| [[sources/decodingai-second-brain-rag]] | 4 |
| [[sources/graphiti-temporal-knowledge-graphs]] | 4 |
| [[sources/karma-multi-agent-knowledge-graph]] | 3 |
| [[sources/hn-vector-database-debate]] | 2 |

---

*This analysis was computed statically from the link graph on 2026-04-05. Re-run the analysis after adding new articles to keep it current.*
