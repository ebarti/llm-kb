---
title: "Andrej Karpathy"
type: entity
entity_type: person
sources: ["[[sources/karpathy-llm-knowledge-bases]]", "[[sources/dairai-llm-knowledge-bases-architecture]]", "[[sources/glenrhodes-karpathy-workflow]]", "[[sources/antigravity-post-code-ai-workflow]]", "[[sources/pebblous-cheap-ontology]]", "[[sources/karpathy-minbpe-lecture]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/post-code-ai-workflow]]", "[[concepts/wiki-compilation]]", "[[concepts/obsidian-as-ide]]", "[[entities/obsidian]]", "[[entities/marp]]", "[[concepts/tokenization]]", "[[concepts/byte-pair-encoding]]", "[[entities/minbpe]]"]
last_compiled: 2026-04-06
summary: "AI researcher and former Tesla/OpenAI lead who pioneered the LLM-maintained personal knowledge base workflow using markdown wikis and Obsidian."
reading_time: "3 min"
---

## Overview

Andrej Karpathy is a prominent AI researcher and educator known for his work at OpenAI and as the former head of AI at Tesla. In the context of this knowledge base, he is the originator of the LLM-maintained personal knowledge base methodology that serves as the central framework for the entire wiki. On April 2, 2026, Karpathy published a Twitter thread describing his workflow for using LLMs to build and maintain structured markdown wikis from raw ingested sources, sparking widespread discussion and analysis across the AI community.

Karpathy's background in deep learning research and engineering gives him a unique vantage point on how LLMs can be applied beyond code generation. His observation that "a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge" captures a broader shift in how AI practitioners relate to their tools.

## Key Contributions

- **LLM Knowledge Base Methodology**: Defined the raw-to-wiki compilation pipeline where an LLM ingests source documents and incrementally compiles them into a structured, cross-linked markdown wiki. The human acts as curator and questioner while the LLM handles all authoring and maintenance.

- **The Filing Loop**: Articulated the compounding knowledge pattern where query outputs are filed back into the wiki, making every exploration additive. As Glen Rhodes summarized: "His explorations accumulate. The knowledge base grows from use."

- **Post-Code AI Workflow**: Framed the intellectual trajectory from vibe coding (Feb 2025) through agentic engineering (Jan 2026) to knowledge orchestration (Apr 2026), arguing that once LLMs solve code generation, the bottleneck shifts to domain understanding.

- **Product Vision**: Acknowledged the current implementation is "a hacky collection of scripts" and identified the opportunity for a polished product, helping to define the [[concepts/knowledge-base-product-gap]].

- **Index-Based Retrieval**: Demonstrated that at personal scale (~100 articles, ~400K words), LLM-maintained index files and one-line summaries replace the need for vector database RAG entirely, a finding that challenged prevailing assumptions about retrieval infrastructure requirements.

## Role in LLM Knowledge Bases

Karpathy is the central figure in this knowledge base. His April 2026 thread is the primary source document, and virtually every other source in the wiki either directly analyzes his approach (DAIR.AI, Glen Rhodes, Antigravity Codes, Pebblous) or provides contrasting systems that are compared against his methodology ([[entities/storm]], [[entities/karma]], [[entities/graphiti]]). His design choices -- markdown as substrate, Obsidian as viewer, LLM as sole author, filing loop for compounding -- define the reference architecture against which all alternatives are measured.

His intellectual trajectory also illustrates the broader theme of [[concepts/post-code-ai-workflow]]: the shift from using AI to write code toward using AI to compile and manage knowledge.

## Mentioned In

- [[sources/karpathy-llm-knowledge-bases]] -- original Twitter thread describing the full workflow
- [[sources/dairai-llm-knowledge-bases-architecture]] -- Elvis Saravia's system architecture analysis of Karpathy's approach
- [[sources/glenrhodes-karpathy-workflow]] -- Glen Rhodes' technical walkthrough emphasizing the filing loop and product gap
- [[sources/antigravity-post-code-ai-workflow]] -- Antigravity Codes' broadest analysis placing Karpathy's work in the vibe-coding-to-knowledge trajectory
- [[sources/pebblous-cheap-ontology]] -- Pebblous positions Karpathy's approach within 50 years of ontology history as "Cheap Ontology"
- [[sources/karpathy-minbpe-lecture]] -- 2h13m lecture building a GPT tokenizer from scratch, demonstrating BPE and cataloging LLM problems traceable to tokenization
