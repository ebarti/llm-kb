---
title: "AlphaFold"
type: entity
entity_type: tool
url: "https://alphafold.ebi.ac.uk/"
related: ["[[concepts/ai-protein-structure-prediction]]", "[[concepts/ai-for-scientific-discovery]]", "[[concepts/ai-drug-discovery]]", "[[entities/demis-hassabis]]", "[[entities/google-deepmind]]"]
tags: [alphafold, protein-structure, deepmind, nobel-prize, drug-discovery]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Google DeepMind's protein structure prediction system. AlphaFold 2 solved the 50-year structure prediction problem (CASP 14, 2020); AF3 extends to all biomolecular interactions. 3M+ researchers, 200M+ structures, 35K+ citations, 2024 Nobel Prize in Chemistry."
---

## Overview

AlphaFold is [[entities/google-deepmind]]'s family of AI systems for predicting the 3D structure of proteins and other biomolecules from their amino acid sequences. It is widely considered one of the most significant AI achievements to date and a transformative contribution to biology. AlphaFold-2 achieved near-experimental accuracy in the CASP14 competition and earned the [[concepts/nobel-prizes-ai-2024|2024 Nobel Prize in Chemistry]], making it the landmark example of [[concepts/ai-for-scientific-discovery]].

## Key Facts

- **Type**: AI system / computational biology tool
- **Creator**: Google DeepMind (Demis Hassabis, John Jumper)
- **URL**: https://alphafold.ebi.ac.uk/
- **Notable for**: Solving the 50-year protein structure prediction problem; 2024 Nobel Prize in Chemistry

## Versions

### AlphaFold 1 (2018)
- Won CASP 13 but did not achieve experimental-level accuracy.
- Used distance prediction + optimization.

### AlphaFold 2 (2020)
- Solved CASP 14 with near-experimental accuracy.
- Evoformer + Structure Module architecture.
- 200M+ protein structures released (2022).
- 35,000+ citations; 200,000+ methodology incorporations.

### AlphaFold 3 (2024)
- Diffusion-based "Pairformer" architecture.
- Predicts proteins, DNA, RNA, small molecules, ions, modified residues jointly.
- 76% accuracy on ligand binding poses (2x competing methods).
- 9,000+ citations within 18 months.

### AlphaFold Server
- Web interface for researchers.
- 8+ million structure predictions generated.

## Ecosystem

| Tool | Focus | Relationship |
|------|-------|-------------|
| AlphaMissense | Mutation pathogenicity | Protein-coding regions (2% of genome) |
| [[entities/alphagenome]] | Gene regulation | Non-coding regions (98% of genome) |
| AlphaProteo | Protein binder design | De novo design using AlphaFold physics |
| [[entities/isomorphic-labs]] | Drug design | Commercial drug discovery engine |

## Impact

- 3+ million researchers across 190+ countries.
- 1+ million users from low- and middle-income countries.
- 30%+ of AlphaFold research focuses on disease mechanisms.
- 40%+ increase in novel protein structure submissions by AlphaFold users.
- 2x more likely to be cited in clinical articles.
- Honeybee conservation (Vitellogenin), heart disease (Apolipoprotein B100), Alzheimer's research.

## Mentioned In

- [[sources/alphafold-five-years-impact]] — five-year retrospective
- [[sources/nobel-prizes-ai-2024]] — Nobel Prize recognition
- [[sources/ai-drug-discovery-phase-iii-2026]] — role in drug target understanding
- [[concepts/ai-protein-structure-prediction]] — core capability
- [[concepts/ai-for-scientific-discovery]] — paradigmatic example

## External References

- [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk/)
- [Nature paper (AlphaFold 2)](https://www.nature.com/articles/s41586-021-03819-2)
- [Nature paper (AlphaFold 3)](https://www.nature.com/articles/s41586-024-07487-w)
