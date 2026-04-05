---
title: "RFdiffusion"
type: entity
entity_type: tool
url: "https://www.ipd.uw.edu/2025/12/rfdiffusion3-now-available/"
related: ["[[concepts/ai-protein-design]]", "[[concepts/ai-drug-discovery]]", "[[entities/david-baker]]"]
tags: [rfdiffusion, protein-design, diffusion-model, antibodies]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "David Baker's diffusion-based protein design tool from the Institute for Protein Design (UW). RFdiffusion3 (Dec 2025) designs proteins binding any intracellular molecule; 10x faster than v2. Atomically accurate antibody design published in Nature."
---

## Overview

RFdiffusion is a family of diffusion-based AI models for de novo protein design from [[entities/david-baker]]'s Institute for Protein Design at the University of Washington. It generates new proteins that do not exist in nature, designed to perform specific functions.

## Key Facts

- **Type**: AI system / protein design tool
- **Creator**: David Baker Lab, Institute for Protein Design, University of Washington
- **URL**: https://www.ipd.uw.edu/
- **Notable for**: De novo protein design, atomically accurate antibodies

## Versions

### RFdiffusion (2023)
- Original diffusion model for protein structure generation.
- Published in Nature (July 2023).

### RFdiffusion2 (2025)
- Demonstrated atomically accurate de novo antibody design.
- Generated antibody variable heavy chains, single-chain variable fragments, and full antibodies.
- Published in Nature: "Atomically accurate de novo design of antibodies with RFdiffusion."

### RFdiffusion3 (December 2025)
- Foundation model for all-atom biodesign.
- Treats individual atoms as fundamental units.
- Designs proteins interacting with any intracellular molecule type (ligands, DNA, RNA).
- 10x faster than RFdiffusion2.
- Open-source (GitHub, Rosetta Commons Foundry).

## Applications

- Custom antibody design for therapeutics.
- Enzyme design for industrial applications.
- Biosensor creation for diagnostics.
- Protein-DNA, protein-RNA, and protein-small-molecule binder design.

## Mentioned In

- [[sources/rfdiffusion3-protein-design]] — v3 capabilities and benchmarks
- [[sources/nobel-prizes-ai-2024]] — David Baker's Nobel recognition

## External References

- [Nature paper (original)](https://www.nature.com/articles/s41586-023-06415-8)
- [Nature paper (antibodies)](https://www.nature.com/articles/s41586-025-09721-5)
