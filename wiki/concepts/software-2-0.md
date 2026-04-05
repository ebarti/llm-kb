---
title: "Software 2.0"
type: concept
sources: ["[[sources/karpathy-software-2-0]]", "[[sources/wikipedia-vibe-coding]]"]
related: ["[[concepts/vibe-coding]]", "[[concepts/ai-code-generation]]", "[[concepts/post-code-ai-workflow]]", "[[concepts/agentic-coding]]", "[[concepts/natural-language-programming]]", "[[entities/andrej-karpathy]]"]
tags: [paradigm-shift, neural-networks, software-engineering, karpathy]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Karpathy's 2017 paradigm: neural networks as a new programming model where datasets replace source code, training replaces compilation, and data curation replaces instruction-writing -- the intellectual foundation for vibe coding and the code-to-knowledge shift."
---

## Overview

Software 2.0 is the term [[entities/andrej-karpathy]] coined in a 2017 essay to describe the paradigm shift where neural networks replace hand-written code as the dominant way to build software. In Software 1.0, programmers write explicit instructions in languages like Python or C++. In Software 2.0, they curate datasets, design architectures, and let optimization discover the program (in the form of learned weights). Training is "compiling the dataset into the binary."

This concept is the intellectual ancestor of [[concepts/vibe-coding]], [[concepts/agentic-coding]], and the broader [[concepts/post-code-ai-workflow]] shift from code manipulation to knowledge manipulation. Understanding Software 2.0 is essential for grasping why AI is transforming programming -- it explains the *why*, not just the *how*.

## The Three-Stage Arc

Karpathy's thinking has evolved across three stages, each representing a deepening of the paradigm:

| Stage | Era | Core Idea | Human Role |
|-------|-----|-----------|------------|
| **Software 1.0** | Pre-2012 | Explicit code | Write instructions |
| **Software 2.0** | 2012-2023 | Learned weights | Curate datasets, design architectures |
| **Software 3.0** | 2023-present | LLM-generated code + natural language specs | Specify intent, review output, orchestrate agents |

Software 3.0 -- sometimes called "the LLM layer" -- is where LLMs bridge the gap between 1.0 and 2.0 by generating Software 1.0 code from natural language prompts while themselves being Software 2.0 artifacts.

## Key Ideas

### Datasets as Source Code
The most radical claim: in Software 2.0, the dataset *is* the source code. The neural net architecture is the rough skeleton ("identifies a subset of program space to search"), and training discovers the actual program. This reframes quality control from code review to **data curation** -- a direct ancestor of [[concepts/data-quality-bottleneck]].

### Computational Homogeneity
Unlike Software 1.0's heterogeneous instruction sets, Software 2.0 reduces to matrix multiplications and ReLU operations. This homogeneity enables custom silicon (TPUs, neuromorphic chips), predictable performance, and cross-platform portability.

### The Infrastructure Gap
In 2017, Karpathy identified critical missing tools: IDEs for dataset curation, GitHub-equivalents for data versioning, and package managers for trained models. By 2026, platforms like Hugging Face, Weights & Biases, and DVC have partially filled these gaps, but the data-centric toolchain remains less mature than the code-centric one.

### Progressive Domain Takeover
Software 2.0 conquered domains one by one: vision (ImageNet/ConvNets), speech recognition, speech synthesis (WaveNet), machine translation, games (AlphaGo), and databases (learned indexes). By 2026, LLMs represent the culmination -- Software 2.0 systems that can generate Software 1.0 code, creating a recursive loop.

## The Code-to-Knowledge Shift

Software 2.0 provides the intellectual framework for understanding why [[concepts/post-code-ai-workflow]] matters:

1. **Software 1.0**: Programmers manipulate *code* (instructions)
2. **Software 2.0**: Programmers manipulate *data* (datasets, labels)
3. **Software 3.0**: Programmers manipulate *knowledge* (specifications, context, prompts)

This is exactly the shift Karpathy described when he moved from advocating [[concepts/vibe-coding]] ("forget the code exists") to [[concepts/agentic-coding]] ("orchestrate agents who write the code"). The competitive advantage is no longer in writing code -- it's in specifying what the code should do and curating the knowledge that informs it.

This directly connects to the [[concepts/llm-knowledge-base]] concept: if manipulating knowledge is the new programming, then a well-maintained knowledge base is the new codebase.

## Limitations and Critiques

- **Interpretability**: Software 2.0 programs (neural networks) are opaque. You can verify *what* they do but not *why*.
- **Adversarial vulnerability**: Small perturbations can cause catastrophic failures in ways impossible with Software 1.0.
- **Silent failure**: Unlike explicit code which fails loudly, neural networks can produce confident-sounding wrong answers -- the same concern underlying [[concepts/hallucination-contamination]].
- **Not a complete replacement**: Software 2.0 excels where data is abundant and evaluation is cheap, but explicit logic, formal verification, and provable correctness remain Software 1.0's domain.

## Open Questions

- Will Software 2.0 ultimately subsume 1.0 entirely, or will there always be a core of formally verified, hand-written code?
- How does the interpretability problem scale as Software 2.0 systems become more capable?
- Does the recursive loop (LLMs generating code that trains LLMs) accelerate or destabilize the paradigm?

## Sources

- [[sources/karpathy-software-2-0]] -- the original 2017 essay
- [[sources/wikipedia-vibe-coding]] -- documents the evolution from Software 2.0 to vibe coding to agentic engineering
