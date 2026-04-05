---
title: "OntoGPT: LLM-Based Ontological Extraction Tools"
source: "https://github.com/monarch-initiative/ontogpt"
author: "Caufield et al. (Monarch Initiative)"
date_published: 2024-02-01
date_ingested: 2026-04-05
tags: [ontology, information-extraction, SPIRES, zero-shot, biomedical, knowledge-graph]
type: repo
status: raw
discovered_via: search
---

# OntoGPT: LLM-Based Ontological Extraction Tools

Published in Bioinformatics (2024), DOI: 10.1093/bioinformatics/btae104.

## Overview

OntoGPT is a Python package for extracting structured information from text with large language models (LLMs), instruction prompts, and ontology-based grounding. It transforms unstructured biomedical and general text into organized, semantically meaningful data aligned with established ontologies.

## SPIRES Method

SPIRES (Structured Prompt Interrogation and Recursive Extraction of Semantics) is the underlying methodology. It is "a method for populating knowledge bases using zero-shot learning." The approach leverages instruction-based prompts combined with ontology constraints to systematically extract and validate information without requiring task-specific training data.

Key aspects of SPIRES:
- Zero-shot extraction (no labeled training data needed)
- Ontology-grounded: ensures extracted entities map to established ontology terms
- Recursive: can handle nested and hierarchical relationships
- Schema-driven: uses LinkML data models to define extraction targets

## Supported Models

Works with most APIs including OpenAI, Azure, Anthropic, Mistral, and Replicate. Also supports local models through Ollama (prefix model name with `ollama/`).

## Usage Example

```bash
pip install ontogpt
echo "One treatment for high blood pressure is carvedilol." > example.txt
ontogpt extract -i example.txt -t drug
```

## Architecture

- Built on LiteLLM for model abstraction
- Integrates with OAK (Ontology Access Kit) library for ontology access
- Outputs structured results with extracted objects
- Uses LinkML for data modeling and schema definition
- Web interface available via `web-ontogpt` command

## Significance

OntoGPT represents the ontology-grounded approach to information extraction: rather than free-form entity extraction, it constrains LLM outputs to match established biomedical ontologies. This dramatically improves precision for domain-specific extraction at the cost of flexibility.
