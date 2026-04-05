---
title: "Multi-Agent Systems for Knowledge Management"
type: concept
sources: ["[[sources/karma-multi-agent-knowledge-graph]]", "[[sources/storm-automated-wiki-creation]]"]
related: ["[[concepts/knowledge-graph]]", "[[concepts/automated-wiki-creation]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "Using networks of specialized LLM agents (rather than a single LLM) to build and maintain knowledge systems — exemplified by KARMA's 9-agent KG enrichment pipeline and STORM's perspective-simulating article creation system."
---

## Overview

Multi-agent approaches to knowledge management divide the pipeline into specialized roles, each handled by a distinct LLM agent. This improves quality through specialization and enables conflict resolution between agents.

## KARMA's 9-Agent Architecture

Roles in KARMA's knowledge graph enrichment pipeline:
1. Document parser
2. Entity discoverer
3. Relation extractor
4. Schema aligner
5. Conflict detector
6. Conflict resolver
7. Knowledge integrator
8. Verifier
9. Schema validator

Each agent focuses on one task; agents pass results to each other and can challenge each other's outputs. The conflict resolution mechanism (18.6% edge conflict reduction) is only possible because distinct agents independently assess the same facts.

## STORM's Perspective-Simulating Agents

STORM uses a different multi-agent pattern: each agent role-plays a distinct *perspective* (identified from Wikipedia ToC analysis). These agents conduct simulated expert conversations, asking questions from their viewpoint. This produces more balanced, comprehensive coverage than a single-perspective research pass.

## When Multi-Agent > Single LLM

- **Conflict detection**: When two agents disagree, that's a signal worth surfacing
- **Scale**: Large document collections that exceed single context windows
- **Specialization**: When entity extraction, relation extraction, and schema validation have different requirements
- **Quality assurance**: Verification agent checks the primary extraction agent's work

## Contrast with Karpathy's Single-LLM Approach

Karpathy's system uses a single LLM in each phase (compilation, Q&A, linting) — simpler architecture, sufficient at personal scale (~100 articles). Multi-agent systems become justified at research-paper scale (thousands of documents) or when formal schema validation is required.

## Sources
- [[sources/karma-multi-agent-knowledge-graph]] — 9-agent KG enrichment (NeurIPS 2025 Spotlight)
- [[sources/storm-automated-wiki-creation]] — perspective-based article creation agents

## Related Concepts
- [[concepts/knowledge-graph]] — what KARMA builds
- [[concepts/automated-wiki-creation]] — STORM's output
- [[concepts/llm-knowledge-base]] — the single-LLM alternative
