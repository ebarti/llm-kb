---
title: "OntoGPT"
type: entity
entity_type: tool
sources: ["[[sources/ontogpt-ontology-extraction]]"]
related: ["[[concepts/schema-guided-extraction]]", "[[concepts/zero-shot-information-extraction]]", "[[concepts/information-extraction]]", "[[concepts/knowledge-graph]]"]
last_compiled: 2026-04-05
summary: "Python package for ontology-grounded information extraction using LLMs and the SPIRES zero-shot method — extracts structured data aligned to established biomedical ontologies."
---

## Overview

OntoGPT is a Python package developed by the Monarch Initiative for extracting structured information from text with LLMs, instruction prompts, and ontology-based grounding. Published in Bioinformatics (2024), DOI: 10.1093/bioinformatics/btae104.

## SPIRES Method

SPIRES (Structured Prompt Interrogation and Recursive Extraction of Semantics) is the core methodology:
- Zero-shot knowledge base population (no labeled training data)
- Ontology-constrained: extracted entities map to established ontology terms
- Recursive: handles nested and hierarchical relationships
- Uses LinkML for schema definition

## Architecture

- Built on LiteLLM for model abstraction
- Integrates with OAK (Ontology Access Kit) for ontology access
- Supports OpenAI, Anthropic, Mistral, Replicate, Ollama
- CLI and web interface available

## Significance

OntoGPT represents the [[concepts/schema-guided-extraction]] paradigm at its most structured: rather than letting the LLM invent entity labels, SPIRES constrains outputs to match established ontologies. This dramatically improves precision for domain-specific extraction.

## Mentioned In

- [[sources/ontogpt-ontology-extraction]] — full overview, SPIRES methodology, architecture
