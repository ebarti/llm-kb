---
title: "Source: RFdiffusion3 — Foundation Model for Protein Biodesign"
type: source-summary
source: "[[raw/rfdiffusion3-protein-design]]"
related: ["[[concepts/ai-protein-design]]", "[[concepts/ai-for-scientific-discovery]]", "[[entities/david-baker]]", "[[entities/rfdiffusion]]"]
tags: [rfdiffusion, protein-design, ai-biology, diffusion-models]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "David Baker's lab releases RFdiffusion3 (Dec 2025): open-source diffusion model for de novo protein design treating atoms as fundamental units. 10x faster than v2, designs proteins binding any intracellular molecule type, atomically accurate antibody generation."
---

## Key Points

- Open-source foundation model generating proteins that interact with any molecule commonly found inside cells.
- Treats individual atoms as fundamental units, applying diffusion to create new atomic arrangements.
- 10x faster than RFdiffusion2 (released earlier in 2025).
- Matched or outperformed prior tools on protein-protein, protein-DNA, protein-small-molecule binding, and enzyme design.
- RFdiffusion2 demonstrated atomically accurate de novo antibody design (published in Nature).

## Detailed Summary

[[entities/rfdiffusion]] 3, released from [[entities/david-baker]]'s Institute for Protein Design at UW, represents the state of the art in [[concepts/ai-protein-design]]. The diffusion-based approach generates protein structures in the context of ligands, nucleic acids, and other non-protein molecular complexes, producing intricate chemical interactions with unprecedented precision.

The tool's significance lies in its generality: previous protein design tools were often specialized for specific interaction types. RFdiffusion3 handles the full range of intracellular molecular interactions — a capability critical for designing therapeutics, biosensors, and industrial enzymes.

The antibody design application is particularly impactful. Using RFdiffusion2, researchers demonstrated de novo generation of antibody variable heavy chains, single-chain variable fragments, and full antibodies binding to user-specified epitopes with atomic-level precision — published in Nature as "Atomically accurate de novo design of antibodies with RFdiffusion."

## Concepts Introduced or Discussed

- [[concepts/ai-protein-design]] — core capability
- [[concepts/ai-drug-discovery]] — antibody therapeutics
- [[concepts/ai-for-scientific-discovery]] — broader implications

## Metadata

- **Author**: Institute for Protein Design, University of Washington
- **Date Published**: December 2025
- **Format**: article
- **URL**: https://www.ipd.uw.edu/2025/12/rfdiffusion3-now-available/
