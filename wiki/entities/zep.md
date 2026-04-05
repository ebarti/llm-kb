---
title: "Zep"
type: entity
entity_type: org
sources: ["[[sources/graphiti-temporal-knowledge-graphs]]"]
related: ["[[entities/graphiti]]", "[[concepts/knowledge-graph]]", "[[concepts/temporal-knowledge]]"]
last_compiled: 2026-04-06
summary: "The organization behind Graphiti, offering both an open-source temporal context graph engine and enterprise-grade managed infrastructure for AI agent memory."
reading_time: "2 min"
---

## Overview

Zep (also known as Zep AI) is the company that developed and maintains [[entities/graphiti]], the open-source temporal context graph framework for AI agents. Zep operates on an open-core business model: Graphiti is released as the open-source engine for building temporal knowledge graphs, while Zep provides enterprise-grade managed infrastructure on top of it. This split allows developers to experiment freely with Graphiti while offering a production-ready, hosted option for teams that need turnkey deployment.

The company focuses on the AI agent memory problem -- giving AI agents the ability to accumulate, organize, and recall information over long time horizons. This positions Zep at the intersection of knowledge graphs and agentic AI, two rapidly growing areas in the LLM ecosystem.

## Key Contributions

- **Graphiti open-source release**: Making temporal context graphs freely available for experimentation and self-hosting lowers the barrier to entry for developers building AI agents with structured memory.

- **Open-core model**: The Graphiti/Zep split mirrors patterns seen across developer tools (Redis/Redis Enterprise, Elasticsearch/Elastic Cloud) and establishes a clear path from experimentation to production.

- **Agent memory focus**: While most knowledge graph tools target general-purpose knowledge representation, Zep specifically focuses on the needs of AI agents -- temporal awareness, incremental updates, hybrid retrieval, and provenance tracking.

## Role in LLM Knowledge Bases

Zep represents the commercial side of the temporal knowledge graph approach. For organizations looking to implement structured knowledge management beyond what a personal markdown wiki can support, Zep's managed Graphiti service offers production-grade infrastructure without the operational burden of running Neo4j and maintaining the graph pipeline. This positions it as a potential solution for the [[concepts/knowledge-base-product-gap]] at the enterprise end of the spectrum.

## Mentioned In

- [[sources/graphiti-temporal-knowledge-graphs]] -- described as the enterprise managed service counterpart to the open-source Graphiti engine
