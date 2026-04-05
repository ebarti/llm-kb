---
title: "STORM"
type: entity
entity_type: paper
sources: ["[[sources/storm-automated-wiki-creation]]"]
related: ["[[concepts/automated-wiki-creation]]", "[[concepts/multi-agent-systems]]", "[[concepts/wiki-compilation]]", "[[entities/freshwiki]]", "[[comparisons/storm-vs-karpathy-workflow]]"]
last_compiled: 2026-04-06
summary: "A research system for automated Wikipedia-style article creation using multi-perspective question-asking and retrieval-based outline synthesis."
reading_time: "2 min"
---

## Overview

STORM (Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking) is a research system that automates the creation of Wikipedia-style articles by focusing on the pre-writing stage -- research and outline generation -- rather than assuming these already exist. Developed as an academic research project, STORM represents the most rigorous automated approach to wiki article creation, standing in contrast to Karpathy's interactive, accumulating knowledge base methodology.

The core insight behind STORM is that high-quality articles require diverse research perspectives, not just information retrieval. By simulating conversations between LLM agents playing distinct expert roles, STORM produces more comprehensive and balanced content than single-perspective generation approaches.

## Key Features

- **Perspective discovery**: STORM analyzes related Wikipedia articles' tables of contents to identify N distinct viewpoints relevant to the target topic. This ensures coverage of multiple angles rather than defaulting to a single narrative.

- **Multi-turn simulated conversations**: LLMs are personified with specific perspectives and conduct simulated expert discussions. Each perspective-agent asks different questions, breaks complex queries into searchable sub-queries, filters results against Wikipedia reliability guidelines, and synthesizes evidence-based responses.

- **Outline-first synthesis**: Rather than generating text directly, STORM first produces a structured outline from the simulated conversations, then uses the outline to guide full article generation. This mirrors the human writing process of research-before-drafting.

- **FreshWiki evaluation dataset**: STORM introduced [[entities/freshwiki]], a dataset of Wikipedia articles created after LLM training cutoffs, ensuring evaluation is not contaminated by memorization. Assessment uses heading/entity recall for outlines, ROUGE scores for articles, and expert rubrics from experienced Wikipedia editors.

## Role in LLM Knowledge Bases

STORM provides the key contrasting model to Karpathy's approach (see [[comparisons/storm-vs-karpathy-workflow]]). Where Karpathy builds a persistent, accumulating knowledge base that grows through the filing loop, STORM performs single-shot article generation from web search without maintaining a persistent knowledge store. STORM is better for producing standalone reference articles on well-defined topics; Karpathy's approach is better for building compounding research knowledge over time.

Both systems share the fundamental insight that LLMs can serve as research synthesizers rather than just text generators. STORM achieves this through multi-agent perspective simulation; Karpathy achieves it through incremental compilation and iterative Q&A.

## Mentioned In

- [[sources/storm-automated-wiki-creation]] -- full description of the system, methodology, evaluation, and comparison with Karpathy's approach
