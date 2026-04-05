---
title: "Data Quality Bottleneck"
type: concept
sources: ["[[sources/pebblous-cheap-ontology]]", "[[sources/decodingai-second-brain-rag]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/hallucination-contamination]]", "[[concepts/wiki-compilation]]"]
last_compiled: 2026-04-05
summary: "In LLM knowledge base pipelines, data quality at the raw input stage — not model capability — is the decisive factor: low-quality ingestion cascades into contaminated wiki content and flawed fine-tuning."
---

## Overview

As LLM capability has grown, the bottleneck in knowledge management systems has shifted from "can the LLM understand this?" to "is the input data good enough for the LLM to build on?" Data quality at the pipeline entry point determines everything downstream.

## Key Ideas

**The cascade:**
Low-quality raw data → contaminated wiki entries → polluted synthetic Q&A generation → permanently flawed fine-tuned models

**Research evidence:**
- Microsoft phi-1 (2023): "data quality matters more than model scale" — a 1.3B parameter model trained on textbook-quality synthetic data achieved competitive results against far larger models
- Gretel (2024): +73.6% performance improvement using high-quality synthetic data vs. human-curated baseline
- Amazon Science (2024): small amounts of high-quality data consistently outperformed large quantities of low-quality data
- Hybrid approaches (real + synthetic data) outperformed either alone

**Practical implications for LLM-KB:**
- Curate sources aggressively before ingestion — don't just dump all web content into `raw/`
- Prefer primary sources (papers, official docs) over summaries of summaries
- Use LLM quality scoring during ETL (as in the Decoding AI FTI pipeline) to filter low-quality content
- Never ingest from sources you wouldn't trust as authoritative

**The "garbage in, garbage out" amplification:**
Unlike traditional databases where bad data is contained, in LLM-maintained wikis bad data gets synthesized, cross-linked, and potentially used to generate training data. The contamination amplifies rather than stays local.

## Sources
- [[sources/pebblous-cheap-ontology]] — identifies data quality as the decisive bottleneck; cites phi-1, Gretel, Amazon Science studies
- [[sources/decodingai-second-brain-rag]] — implements quality scoring via LLMs during ETL as practical mitigation

## Related Concepts
- [[concepts/hallucination-contamination]] — the downstream consequence
- [[concepts/wiki-compilation]] — where quality determines output
- [[concepts/llm-knowledge-base]] — the system affected
- [[concepts/linting-and-health-checks]] — detection mechanism
