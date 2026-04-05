---
title: "Matplotlib"
type: entity
entity_type: tool
sources: ["[[sources/karpathy-llm-knowledge-bases]]", "[[sources/antigravity-post-code-ai-workflow]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/obsidian-as-ide]]", "[[entities/marp]]", "[[entities/obsidian]]"]
last_compiled: 2026-04-06
summary: "A Python plotting library used in the LLM-KB workflow to generate data visualizations that are saved as images and viewed within Obsidian alongside wiki articles."
reading_time: "2 min"
---

## Overview

Matplotlib is the foundational plotting library for the Python scientific computing ecosystem. It provides comprehensive tools for creating static, animated, and interactive visualizations including line plots, bar charts, scatter plots, histograms, heatmaps, and more. Matplotlib is one of the most widely used libraries in data science and machine learning.

In Karpathy's LLM knowledge base workflow, Matplotlib serves as one of the multi-format output channels alongside markdown reports and [[entities/marp]] slide decks. When the LLM answers a query that benefits from visual representation -- comparative charts, timelines, distribution plots, relationship diagrams -- it generates Matplotlib code, executes it to produce image files, and saves those images within the wiki structure where they can be viewed in [[entities/obsidian]].

## Key Features

- **Comprehensive plotting**: Supports virtually any 2D visualization type, from simple line plots to complex multi-panel figures with custom layouts.

- **Programmatic generation**: Because Matplotlib is a Python library, LLMs can generate the code to produce visualizations directly. The LLM writes Python code, the code is executed, and the resulting image is saved to the wiki.

- **Image output**: Renders to PNG, SVG, PDF, and other formats. PNG images embed naturally in markdown files and display inline in Obsidian.

- **Customization**: Styles, colors, annotations, and layouts are all controllable through code, allowing the LLM to produce publication-quality figures tailored to the query.

## Role in LLM Knowledge Bases

Matplotlib exemplifies a broader principle of the LLM-KB workflow: the knowledge base is not limited to text. By generating visualizations and filing them back into the wiki, the LLM produces a richer, more navigable knowledge artifact than text alone could provide. A chart comparing RAG accuracy vs. fine-tuning accuracy (as referenced in [[sources/pebblous-cheap-ontology]]) communicates quantitative relationships faster than a paragraph of prose.

This multi-modal output capability is one of the advantages that distinguishes LLM-maintained wikis from traditional note-taking: the LLM can generate both the analysis and the visualization in a single pass, creating self-contained artifacts that combine prose, data, and imagery.

## Mentioned In

- [[sources/karpathy-llm-knowledge-bases]] -- listed as one of the output formats (markdown, Marp slides, matplotlib images) viewable in Obsidian
- [[sources/antigravity-post-code-ai-workflow]] -- included in the multi-format output step of the 6-step workflow
