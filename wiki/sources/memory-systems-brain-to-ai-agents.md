---
title: "Source: AI Meets Brain — Memory Systems from Cognitive Neuroscience to Autonomous Agents"
type: source-summary
source: "[[raw/memory-systems-brain-to-ai-agents]]"
related: ["[[concepts/complementary-learning-systems]]", "[[concepts/brain-inspired-ai]]", "[[concepts/agent-memory]]", "[[concepts/continual-learning]]"]
tags: [memory-systems, cognitive-neuroscience, ai-agents, hippocampus]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Comprehensive survey mapping biological memory (episodic, semantic, procedural, working) to AI agent architectures: parametric memory = semantic, context windows = working memory, external stores = long-term, with hippocampal-cortical consolidation parallels."
---

## Key Points

- Maps biological memory taxonomy to AI: parametric = semantic, context window = working memory, external = long-term
- Hippocampus functions as an indexing system that reactivates distributed cortical traces
- Agent memory follows four phases mirroring biology: encoding, consolidation, retrieval, reconsolidation
- Key AI architectures: Reflexion (contextual self-reflection), Memory Trees (hierarchical indexing), Cognitive Maps (graph-based relational memory)
- Ebbinghaus forgetting curve principles applied to adaptive AI information elimination
- Working memory managed through "context folding" — dynamic management within reasoning trajectories

## Detailed Summary

This arXiv survey provides the most comprehensive mapping between biological and artificial memory systems to date. It establishes a progressive framework from cognitive neuroscience through LLMs to autonomous agents.

Biological memory divides into short-term (sensory-frontoparietal networks, seconds to minutes) and long-term (hippocampal-neocortical coordination) categories, with long-term further split into episodic (events), semantic (facts), and procedural (skills). The survey maps these onto AI: parametric memory (model weights) corresponds to abstract semantic memory, context windows mirror working memory's limited capacity and positional bias, and external memory banks parallel long-term neocortical storage.

The [[concepts/complementary-learning-systems]] principle appears directly in agent architectures: encoding converts raw interactions into structured records, consolidation abstracts through reflection, retrieval uses similarity matching, and reconsolidation allows updating during "plasticity windows." Specific architectures include Reflexion (self-reflection in context rather than weight updates), Memory Trees (recursive summarization for navigation), Skill Libraries (procedural memory as executable programs), and Cognitive Maps (graph-based relational structures mirroring hippocampal-entorhinal systems).

The survey's treatment of [[concepts/agent-memory]] management as a lifecycle — extraction, updating, retrieval, application — provides a practical design pattern for building brain-inspired AI agents.

## Concepts Introduced or Discussed

- [[concepts/complementary-learning-systems]] — hippocampal-cortical memory framework
- [[concepts/agent-memory]] — memory in AI agent systems
- [[concepts/continual-learning]] — learning without forgetting

## Metadata

- **Author**: Multiple authors
- **Date Published**: 2025-12-30
- **Format**: paper (arXiv survey)
- **URL**: https://arxiv.org/html/2512.23343v1
