---
title: "DCLM (DataComp-LM)"
type: entity
entity_type: dataset
sources: ["[[sources/dclm-datacomp-language-models]]", "[[sources/nemotron-cc-nvidia]]"]
related: ["[[concepts/training-data-curation]]", "[[concepts/model-based-filtering]]", "[[entities/common-crawl]]", "[[entities/fineweb]]"]
last_compiled: 2026-04-05
summary: "Benchmark and dataset from Apple/UW for controlled training data experiments — provides 240T-token Common Crawl pool, 53 evaluations, and the DCLM-Baseline (2T tokens) achieving 64% MMLU on a 7B model."
---

## Overview

DCLM (DataComp for Language Models) is both a benchmark for comparing dataset curation strategies and the resulting DCLM-Baseline dataset. Created by researchers at Apple, University of Washington, and collaborators.

## Key Contributions

1. **Standardized benchmark**: 5 competition scales (412M to 7B parameters), 53 downstream evaluations, two tracks (filtering and mixing)
2. **DCLM-Pool**: 240 trillion tokens from Common Crawl (200B documents, 370TB compressed)
3. **DCLM-Baseline**: ~2T tokens filtered to top 10% by fastText quality — enables 64% MMLU on 7B model with 6.6x less compute than Llama 2
4. **Definitive filtering comparison**: fastText classifiers decisively outperform 6 alternative approaches

## Impact

- Demonstrated that model-based filtering is the most important curation technique
- Showed quality rankings transfer reliably across model scales (r=0.885-0.919)
- Proved that mixing curated sources into filtered data can degrade performance
- DCLM classifier became a component of [[entities/nemotron-cc]]'s ensemble approach
- Available at https://www.datacomp.ai/dclm/

## Mentioned In

- [[sources/dclm-datacomp-language-models]] — primary source
- [[sources/nemotron-cc-nvidia]] — used as baseline and ensemble component
