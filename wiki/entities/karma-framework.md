---
title: "KARMA"
type: entity
entity_type: paper
sources: ["[[sources/karma-multi-agent-knowledge-graph]]", "[[sources/llm-kg-construction-survey]]"]
related: ["[[concepts/knowledge-graph-construction]]", "[[concepts/multi-agent-systems]]", "[[concepts/knowledge-extraction]]", "[[concepts/knowledge-fusion]]"]
last_compiled: 2026-04-05
summary: "NeurIPS 2025 Spotlight paper: 9-agent LLM framework for automated knowledge graph enrichment from unstructured text, achieving 83.1% accuracy and 38,230 new entities from 1,200 PubMed papers."
---

## Overview

KARMA (Knowledge Automated Reasoning and Multi-Agent framework) is a NeurIPS 2025 Spotlight paper presenting a multi-agent LLM architecture for automated [[concepts/knowledge-graph]] enrichment from unstructured scientific text.

## Architecture

Nine collaborative LLM agents handle specialized tasks:
- Entity discovery agents
- Relation extraction agents
- Schema alignment agents
- Conflict resolution agents
- Validation agents

## Performance

- **83.1% accuracy** on knowledge graph enrichment
- **38,230 new entities** extracted from 1,200 PubMed papers
- **18.6% conflict reduction** through multi-agent conflict resolution
- Schema-guided extraction ensuring consistency with existing ontology

## Significance

KARMA represents the multi-agent approach to [[concepts/knowledge-graph-construction]], demonstrating that specialized agent roles improve extraction quality over monolithic LLM prompting. The [[sources/llm-kg-construction-survey]] classifies it as a schema-based extraction method with multi-agent architecture for schema-guided task execution.

## Mentioned In

- [[sources/karma-multi-agent-knowledge-graph]] — primary paper
- [[sources/llm-kg-construction-survey]] — classified within schema-based extraction taxonomy
