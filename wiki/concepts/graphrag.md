---
title: "GraphRAG"
type: concept
sources: ["[[sources/microsoft-graphrag]]", "[[sources/ragflow-rag-review-2025]]", "[[sources/graphrag-microsoft-research]]", "[[sources/rag-vs-kg-enterprise-phyvant]]", "[[sources/kg-vs-vector-db-glean]]", "[[sources/llm-kg-construction-survey]]"]
related: ["[[concepts/retrieval-augmented-generation]]", "[[concepts/knowledge-graph]]", "[[concepts/hybrid-search]]", "[[entities/microsoft-research]]", "[[concepts/hybrid-retrieval]]", "[[concepts/knowledge-graph-construction]]", "[[concepts/knowledge-extraction]]"]
last_compiled: 2026-04-05
summary: "Microsoft's graph-based RAG variant that constructs knowledge graphs from text, clusters them into communities with pre-generated summaries, enabling holistic and aggregate queries that baseline RAG cannot answer."
---

## Overview

GraphRAG is a structured, hierarchical approach to [[concepts/retrieval-augmented-generation]] developed by [[entities/microsoft-research]]. Unlike standard RAG, which retrieves individual text chunks based on vector similarity, GraphRAG constructs a [[concepts/knowledge-graph]] from the source corpus and uses graph machine learning to organize information into semantic communities at multiple abstraction levels.

The core motivation is that baseline RAG fails fundamentally on two types of queries: (1) connecting disparate pieces of information that share attributes but aren't co-located in text, and (2) holistic summarization queries that require understanding themes across an entire dataset. As Microsoft's research demonstrated, when asked to identify top themes in a news corpus, baseline RAG returned irrelevant topics while GraphRAG correctly identified the actual major themes.

## How It Works

GraphRAG follows a three-stage offline process:

**1. Entity and Relationship Extraction**: LLMs process the entire dataset, identifying entities (people, places, organizations, concepts) and the relationships between them. This creates a foundation knowledge graph where nodes are entities and edges are relationships, each with natural language descriptions.

**2. Community Detection**: Graph machine learning algorithms (typically Leiden clustering) perform bottom-up hierarchical clustering, organizing the knowledge graph into communities of related entities. This creates a multi-level hierarchy from granular entity groups up to broad thematic clusters.

**3. Community Summarization**: LLMs generate natural language summaries for each community at every level of the hierarchy. These pre-computed summaries enable the system to answer queries at different levels of abstraction without requiring real-time synthesis.

At query time, the system uses these community summaries alongside the graph structure for prompt augmentation, providing richer context than raw chunk retrieval.

## Performance vs. Baseline RAG

Microsoft's evaluation showed stark differences:

| Query Type | Baseline RAG | GraphRAG |
|---|---|---|
| Simple factual ("What is X?") | Adequate | Adequate |
| Connecting information ("What has X done?") | No results | Specific answers with evidence |
| Holistic themes ("Top themes in dataset?") | Irrelevant themes returned | Correct themes identified |

GraphRAG consistently outperforms on **comprehensiveness** (more complete answers), **human enfranchisement** (provides supporting evidence for verification), and **diversity** (surfaces multiple viewpoints). Faithfulness remains comparable to baseline RAG per SelfCheckGPT evaluation.

## Practical Challenges

Despite its power, GraphRAG has significant implementation challenges identified in real-world deployments:

- **Token consumption**: Knowledge graph extraction consumes several to dozens of times the original text in LLM tokens, making it expensive for large corpora
- **Quality gaps**: The quality of extracted entities and relationships often falls short of expectations, requiring careful prompt engineering and validation
- **Fragmented outputs**: Graph-extracted knowledge can be disjointed, requiring sophisticated LLM integration to produce coherent narratives
- **LazyGraphRAG**: Microsoft later introduced a lighter-weight variant that defers some processing to query time to reduce upfront costs

## Variants and Extensions

- **LazyGraphRAG**: Reduces upfront indexing costs by deferring some processing
- **Hybrid TreeRAG + GraphRAG**: Combining local semantic strengths (TreeRAG) with relational discovery (GraphRAG)
- **KAG (Knowledge-Augmented Generation)**: Integrates knowledge graphs with LLMs for logical reasoning in specialized domains

## Query Modes

GraphRAG provides multiple specialized search approaches:

- **Global Search**: Reasons about corpus-wide questions using community summaries across the hierarchy
- **Local Search**: Focuses on specific entities and their neighbors for entity-specific questions
- **DRIFT Search**: Combines local entity traversal with community context for richer answers
- **Basic Search**: Falls back to conventional vector retrieval when appropriate

## Relationship to Knowledge Graph Construction

GraphRAG's extraction stage is a form of [[concepts/knowledge-graph-construction]], and the [[sources/llm-kg-construction-survey]] places it within the broader taxonomy of LLM-driven KG construction methods. Notably, [[entities/kggen]] outperforms GraphRAG's extraction on the MINE benchmark (66% vs 48%), suggesting that GraphRAG's strength lies more in its retrieval/summarization architecture than in raw extraction quality.

The system can be combined with [[concepts/hybrid-retrieval]] approaches — for instance, Neo4j's LLM Knowledge Graph Builder integrates GraphRAG alongside vector search and Text2Cypher.

## Sources

- [[sources/microsoft-graphrag]] — original Microsoft Research blog post with evaluation
- [[sources/ragflow-rag-review-2025]] — practical challenges noted in real-world deployments
- [[sources/graphrag-microsoft-research]] — detailed documentation and query modes
- [[sources/rag-vs-kg-enterprise-phyvant]] — enterprise context for graph-enhanced RAG
- [[sources/kg-vs-vector-db-glean]] — hybrid architecture analysis
- [[sources/llm-kg-construction-survey]] — survey covering GraphRAG's extraction approach

## Related Concepts

- [[concepts/retrieval-augmented-generation]] — the baseline GraphRAG improves upon
- [[concepts/knowledge-graph]] — the underlying data structure
- [[concepts/knowledge-graph-construction]] — the extraction pipeline stage
- [[concepts/knowledge-extraction]] — entity/relation extraction
- [[concepts/hybrid-retrieval]] — combining graph and vector approaches
- [[concepts/raptor]] — alternative hierarchical retrieval approach (tree vs. graph)
- [[concepts/hybrid-search]] — can be combined with graph retrieval
