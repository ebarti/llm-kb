---
title: "AI Protein Structure Prediction"
type: concept
sources: ["[[sources/alphafold-five-years-impact]]", "[[sources/nobel-prizes-ai-2024]]"]
related: ["[[concepts/ai-for-scientific-discovery]]", "[[concepts/ai-drug-discovery]]", "[[concepts/ai-protein-design]]", "[[entities/alphafold]]", "[[entities/demis-hassabis]]"]
tags: [protein-structure, alphafold, structural-biology, casp]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Predicting 3D protein structure from amino acid sequence — solved by AlphaFold 2 at CASP 14 (2020). AlphaFold 3 extends to all biomolecular interactions (76% accuracy on ligand binding). 200M+ structures released, 3M+ researchers served, Nobel Prize awarded 2024."
---

## Overview

Protein structure prediction is the computational determination of a protein's 3D shape from its amino acid sequence. This was one of biology's grand challenges for 50 years: the amino acid sequence determines the structure, but the folding process involves an astronomical number of possible configurations (Levinthal's paradox).

[[entities/alphafold]] 2's solution at CASP 14 (2020) is widely considered one of the most significant scientific achievements of the 21st century, recognized with the [[concepts/nobel-prizes-ai-2024|2024 Nobel Prize in Chemistry]].

## Technical Evolution

### AlphaFold 1 (2018)
- Won CASP 13 but did not achieve experimental-level accuracy.
- Used distance prediction + optimization.

### AlphaFold 2 (2020)
- Solved the problem at CASP 14 with near-experimental accuracy.
- End-to-end architecture: Evoformer (attention over sequences and structures) + Structure Module.
- Predicted structures for 200M+ proteins (released 2022).

### AlphaFold 3 (2024)
- Substantially updated diffusion-based architecture.
- Predicts joint structure of complexes: proteins, DNA, RNA, small molecules, ions, modified residues.
- 76% accuracy on ligand binding poses (2x any competing method).
- Introduced the "Pairformer" architecture.
- 9,000+ direct citations within 18 months.

## Impact Metrics

| Metric | Value |
|--------|-------|
| Researchers served | 3+ million across 190+ countries |
| LMIC users | 1+ million |
| Direct citations | 35,000+ |
| Methodology incorporations | 200,000+ papers |
| Server predictions | 8+ million |
| Disease-focused research | 30%+ of AlphaFold papers |

## Downstream Applications

- **Drug discovery**: Understanding drug-target interactions ([[concepts/ai-drug-discovery]]).
- **Disease mechanisms**: Alzheimer's (PHGDH gene structure), heart disease (Apolipoprotein B100), honeybee conservation (Vitellogenin).
- **Protein design**: Foundation for [[concepts/ai-protein-design]] tools like [[entities/rfdiffusion]].
- **Genomics**: AlphaMissense uses structural context to assess mutation impact.

## Open Questions

- Can protein dynamics (not just static structures) be predicted?
- How will AlphaFold 3's accuracy improve for disordered regions?
- Will structure prediction integrate with molecular dynamics simulations?

## Sources

- [[sources/alphafold-five-years-impact]] — Five-year retrospective and impact metrics
- [[sources/nobel-prizes-ai-2024]] — Nobel recognition

## Related Concepts

- [[concepts/ai-for-scientific-discovery]] — AlphaFold as paradigmatic example
- [[concepts/ai-drug-discovery]] — downstream application
- [[concepts/ai-protein-design]] — complementary capability
