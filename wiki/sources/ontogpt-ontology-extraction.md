---
title: "Source: OntoGPT — LLM-Based Ontological Extraction Tools"
type: source-summary
source: "[[raw/ontogpt-ontology-extraction]]"
related: ["[[concepts/schema-guided-extraction]]", "[[concepts/information-extraction]]", "[[concepts/zero-shot-information-extraction]]", "[[entities/ontogpt]]"]
last_compiled: 2026-04-05
summary: "OntoGPT's SPIRES method uses zero-shot LLM extraction grounded in biomedical ontologies, producing structured output aligned to established terminologies without training data."
reading_time: "2 min"
---

## Key Points

- Python package for ontology-grounded information extraction using LLMs
- SPIRES method: zero-shot extraction constrained by ontology terms
- Supports OpenAI, Anthropic, Mistral, Replicate, and local models via Ollama
- Uses LinkML for data modeling and schema definition
- Published in Bioinformatics (2024)

## Detailed Summary

[[entities/ontogpt]] represents the ontology-grounded approach to [[concepts/information-extraction]]. Rather than free-form entity extraction (where the LLM invents entity labels), SPIRES (Structured Prompt Interrogation and Recursive Extraction of Semantics) constrains LLM outputs to match established ontology terms.

This is a zero-shot method — no labeled training data is needed. The system leverages instruction-based prompts combined with ontology constraints to systematically extract entities and relationships. The ontology grounding step maps extracted mentions to canonical terms, dramatically improving precision for domain-specific extraction.

The architecture integrates with OAK (Ontology Access Kit) for ontology access, uses LinkML for schema definition, and supports LiteLLM for model abstraction. This makes it relevant as a reference implementation for [[concepts/schema-guided-extraction]] — one of the key approaches in the [[concepts/knowledge-graph]] construction taxonomy.

## Related Concepts

- [[concepts/schema-guided-extraction]] — OntoGPT is the canonical example
- [[concepts/zero-shot-information-extraction]] — no training data needed
- [[concepts/entity-linking]] — ontology grounding is a form of entity linking
- [[concepts/knowledge-graph]] — extraction populates KG structures
