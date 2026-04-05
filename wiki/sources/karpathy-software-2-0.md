---
title: "Source: Software 2.0"
type: source-summary
source: "[[raw/karpathy-software-2-0]]"
related: ["[[concepts/software-2-0]]", "[[concepts/ai-code-generation]]", "[[concepts/post-code-ai-workflow]]", "[[entities/andrej-karpathy]]"]
tags: [software-2.0, neural-networks, paradigm-shift]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Karpathy's foundational 2017 essay arguing that neural networks represent a new programming paradigm where programs are defined by learned weights rather than explicit code, with datasets as the new source code."
---

## Key Points

- Software 1.0 = explicit code in Python/C++; Software 2.0 = neural network weights learned via optimization
- The "source code" of Software 2.0 is the dataset + neural net architecture; training is "compiling the dataset into the binary"
- Data labelers become the primary "2.0 programmers"; infrastructure specialists maintain training systems
- Software 2.0 has already displaced 1.0 in visual recognition, speech recognition/synthesis, machine translation, games, and databases
- Key advantages: computational homogeneity, silicon-friendliness, portability, agility, and system-wide optimization via backpropagation
- Critical limitation: interpretability crisis -- networks work but we don't understand why
- Missing infrastructure: no Software 2.0 IDEs, no GitHub-for-datasets, no package managers for trained models

## Detailed Summary

Written in November 2017, this essay is the foundational articulation of the paradigm shift that would later inform Karpathy's [[concepts/vibe-coding]] concept and his broader vision of developers as knowledge curators rather than code writers. Karpathy observes that across domain after domain -- vision, speech, translation, games -- neural networks trained on data have systematically replaced hand-engineered algorithms.

The core insight is architectural: Software 1.0 programmers write explicit step-by-step instructions, while Software 2.0 "programmers" curate datasets and design training pipelines. The actual program (the weights) emerges from optimization. This reframes programming from instruction-writing to data-curation and objective-specification.

Karpathy identifies a crucial infrastructure gap: the tooling ecosystem (IDEs, version control, package managers) remains built for Software 1.0. He predicts that whoever builds the equivalent tools for Software 2.0 -- dataset versioning, mislabel detection, model package managers -- will capture enormous value. By 2026, platforms like [[entities/hugging-face]] and tools like [[entities/weights-and-biases]] have partially fulfilled this prediction.

## Concepts Introduced or Discussed

- [[concepts/software-2-0]] -- the core paradigm
- [[concepts/ai-code-generation]] -- logical extension of the paradigm to LLMs generating code
- [[concepts/post-code-ai-workflow]] -- Karpathy's later refinement of the shift from code to knowledge manipulation
- [[concepts/data-quality-bottleneck]] -- implicit in the "dataset as source code" framing

## Quotes & Evidence

> "Software 2.0 is written in neural network weights. No human is involved in writing this code because there are a lot of weights (typical networks might have millions), and coding directly in weights is kind of hard."

> "The 2.0 stack can fail in unintuitive and embarrassing ways, or worse, they can 'silently fail'."

> "Who is going to develop the first Software 2.0 IDEs, which help accumulate and visualize datasets, spot outliers, label incorrectly, flag duplicates?"

## Metadata

- **Author**: Andrej Karpathy
- **Date Published**: 2017-11-11
- **Format**: article (Medium)
- **URL**: https://karpathy.medium.com/software-2-0-a64152b37c35
