---
title: "AI Protein Design"
type: concept
sources: ["[[sources/rfdiffusion3-protein-design]]", "[[sources/nobel-prizes-ai-2024]]", "[[sources/alphafold-five-years-impact]]"]
related: ["[[concepts/ai-for-scientific-discovery]]", "[[concepts/ai-drug-discovery]]", "[[concepts/ai-protein-structure-prediction]]", "[[entities/rfdiffusion]]", "[[entities/david-baker]]"]
tags: [protein-design, de-novo, diffusion-models, antibodies]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "De novo protein design uses AI (especially diffusion models like RFdiffusion3) to create entirely new proteins with specified functions — from custom antibodies to industrial enzymes. David Baker won the 2024 Nobel Prize for this work."
---

## Overview

AI protein design creates entirely new proteins that do not exist in nature, engineered to perform specific functions. This is the inverse of [[concepts/ai-protein-structure-prediction]]: rather than predicting the structure of a known sequence, protein design starts with a desired function or interaction and generates the protein to achieve it.

[[entities/david-baker]] pioneered this field over two decades, culminating in the [[concepts/nobel-prizes-ai-2024|2024 Nobel Prize in Chemistry]]. The latest tool, [[entities/rfdiffusion]] 3 (December 2025), represents the state of the art.

## Methods

### Diffusion-Based Design (RFdiffusion)
- Treats atoms as fundamental units.
- Applies diffusion (starting from noise, iteratively refining toward valid structures).
- Generates proteins in the context of target molecules (ligands, DNA, RNA, other proteins).
- RFdiffusion3: 10x faster than v2; handles any intracellular molecule type.

### AlphaProteo
- Designs novel protein binders for specific targets.
- Part of [[entities/google-deepmind]]'s AlphaFold ecosystem.
- Targets include cancer and diabetes-relevant proteins.

### Rosetta Suite
- [[entities/david-baker]]'s original computational design platform.
- Foundation for RFdiffusion and related tools.
- 20+ years of continuous development.

## Key Achievements

- **Atomically accurate antibodies**: RFdiffusion2 generates antibody variable heavy chains, single-chain variable fragments, and full antibodies binding to user-specified epitopes with atomic-level precision (published in Nature).
- **De novo enzymes**: RFdiffusion3 designs functional enzymes for industrial and therapeutic applications.
- **Custom binders**: AlphaProteo designs novel protein binders for cancer targets.
- **Biosensors**: Designed proteins that detect specific molecules for diagnostics.

## Applications

| Domain | Application | Tool |
|--------|------------|------|
| Therapeutics | Custom antibodies, protein drugs | RFdiffusion2/3 |
| Diagnostics | Biosensors detecting disease markers | AlphaProteo |
| Industrial | Enzymes for manufacturing, bioremediation | RFdiffusion3 |
| Agriculture | Crop resistance, pest management proteins | Rosetta-derived |
| Sustainability | Plastic-degrading enzymes | De novo design |

## Relationship to Structure Prediction

Protein design and structure prediction are complementary:
- [[concepts/ai-protein-structure-prediction|Structure prediction]] (AlphaFold) tells you what a natural protein looks like.
- **Protein design** (RFdiffusion) creates new proteins that nature never made.
- AlphaFold's understanding of protein physics directly informs design tools.

## Open Questions

- Can designed proteins achieve the stability and specificity of natural proteins?
- Will AI-designed therapeutics face unique regulatory challenges?
- How rapidly can designed proteins move from computation to clinical use?

## Sources

- [[sources/rfdiffusion3-protein-design]] — RFdiffusion3 capabilities and benchmarks
- [[sources/nobel-prizes-ai-2024]] — David Baker's Nobel Prize
- [[sources/alphafold-five-years-impact]] — AlphaProteo and ecosystem

## Related Concepts

- [[concepts/ai-protein-structure-prediction]] — complementary capability
- [[concepts/ai-drug-discovery]] — therapeutic applications
- [[concepts/ai-for-scientific-discovery]] — broader context
