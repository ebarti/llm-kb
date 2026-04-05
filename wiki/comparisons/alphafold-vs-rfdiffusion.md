---
title: "AlphaFold vs RFdiffusion: Prediction vs Design"
type: comparison
subjects: ["[[entities/alphafold]]", "[[entities/rfdiffusion]]"]
sources: ["[[sources/alphafold-five-years-impact]]", "[[sources/rfdiffusion3-protein-design]]", "[[sources/nobel-prizes-ai-2024]]"]
last_compiled: 2026-04-05
summary: "AlphaFold predicts structures of existing proteins; RFdiffusion designs entirely new proteins. Complementary tools from the two 2024 Chemistry Nobel laureate teams (Hassabis/Jumper and Baker), both using deep learning but for inverse problems."
---

## Overview

[[entities/alphafold]] and [[entities/rfdiffusion]] represent the two sides of AI protein science: prediction (what does a known protein look like?) and design (can we create a new protein that does X?). Both are transformative tools, both were recognized with the [[concepts/nobel-prizes-ai-2024|2024 Nobel Prize in Chemistry]], and both use deep learning — but they solve inverse problems.

## Comparison Table

| Dimension | AlphaFold | RFdiffusion |
|-----------|-----------|-------------|
| **Problem** | Structure prediction | Structure design |
| **Direction** | Sequence to structure | Function to structure |
| **Input** | Amino acid sequence | Desired interaction/function |
| **Output** | Predicted 3D structure | Novel protein sequence + structure |
| **Architecture** | Evoformer + diffusion (AF3) | Diffusion on atom positions |
| **Creator** | DeepMind (Hassabis, Jumper) | Baker Lab (David Baker) |
| **Scope** | All known proteins (200M+) | Novel proteins that don't exist in nature |
| **Latest version** | AlphaFold 3 (2024) | RFdiffusion3 (Dec 2025) |
| **Molecular scope** | Proteins, DNA, RNA, ligands (AF3) | Proteins, DNA, RNA, ligands (v3) |
| **Commercial arm** | Isomorphic Labs | Institute for Protein Design spin-offs |
| **Openness** | Server + limited code | Fully open-source |
| **Nobel Prize** | Chemistry 2024 (one half) | Chemistry 2024 (other half) |

## When to Use Each

### AlphaFold
- Understanding the structure of a known protein.
- Predicting how a drug will interact with a known target.
- Analyzing genetic variant effects on protein structure (via AlphaMissense).
- Rapid structural hypothesis generation for experimental validation.

### RFdiffusion
- Designing a new protein to bind a specific target.
- Creating custom antibodies for therapeutics.
- Engineering enzymes for industrial applications.
- Designing biosensors for diagnostics.

### Together
The most powerful approach combines both: use AlphaFold to understand the target's structure, then use RFdiffusion to design a protein that interacts with it in the desired way. This is the foundation of modern [[concepts/ai-drug-discovery]].

## Shared Characteristics

- Both use deep learning on protein structural data.
- Both are open/semi-open for academic research.
- Both recognized by the 2024 Nobel Prize in Chemistry.
- Both have expanded from proteins to broader biomolecular interactions.
- Both are advancing toward all-atom, multi-molecule modeling.

## Sources

- [[sources/alphafold-five-years-impact]] — AlphaFold capabilities and impact
- [[sources/rfdiffusion3-protein-design]] — RFdiffusion3 design capabilities
- [[sources/nobel-prizes-ai-2024]] — Both teams' Nobel recognition
