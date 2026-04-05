---
title: "AI Across Scientific Domains: Maturity and Impact Comparison"
type: comparison
subjects: ["[[concepts/ai-protein-structure-prediction]]", "[[concepts/ai-materials-science]]", "[[concepts/ai-mathematical-reasoning]]", "[[concepts/ai-weather-climate]]", "[[concepts/ai-drug-discovery]]", "[[concepts/ai-genomics]]"]
sources: ["[[sources/alphafold-five-years-impact]]", "[[sources/gnome-materials-discovery]]", "[[sources/funsearch-mathematical-discovery]]", "[[sources/gencast-weather-prediction]]", "[[sources/ai-drug-discovery-phase-iii-2026]]", "[[sources/alphagenome-genomics]]"]
last_compiled: 2026-04-05
summary: "Comparison of AI's maturity, validation level, and real-world impact across six scientific domains — from fully proven (protein structure) to early-stage (drug approval). Each domain has distinct AI methods, timelines, and challenges."
---

## Overview

AI is transforming multiple scientific domains simultaneously, but the maturity, validation level, and practical impact vary enormously. This comparison assesses six major areas where AI is making scientific contributions.

## Comparison Table

| Dimension | Protein Structure | Materials Science | Mathematics | Weather/Climate | Drug Discovery | Genomics |
|-----------|------------------|------------------|-------------|-----------------|---------------|----------|
| **Maturity** | Mature | Growing | Rapid advance | Operational | Clinical testing | Growing |
| **Key system** | [[entities/alphafold]] | [[entities/gnome]] | [[entities/alphaevolve]] / Deep Think | [[entities/gencast]] | Multiple companies | [[entities/alphagenome]] |
| **AI method** | Transformers + diffusion | Graph neural networks | LLM + evolutionary search | Diffusion models | Generative / physics-based | Conv + transformers |
| **Validation** | Nobel Prize, 3M+ users | 736 external syntheses | Peer-reviewed proofs | Operational at NOAA | Phase III trials (2026) | Benchmarks + case studies |
| **Speed advantage** | Millions of years compressed | 800 years equivalent | Minutes vs months | 8 min vs hours | 30 months vs 6-8 years | Real-time variant analysis |
| **Scale** | 200M+ structures | 2.2M crystals | 50+ open problems | Global 15-day forecasts | 173+ programs | 1M base-pair sequences |
| **Real-world use** | Routine in biology | Emerging | Early adoption | Operational forecasting | Clinical trials | Research tool |
| **Key risk** | Dynamic structures missed | False positive syntheses | Unverified proofs | Unprecedented events | Phase III failures | Regulatory uncertainty |
| **Nobel Prize** | Chemistry 2024 | No (yet) | No (yet) | No (yet) | No (yet) | No (yet) |

## Maturity Spectrum

```
Most Mature ←──────────────────────────────────────→ Least Validated

Protein Structure > Weather > Materials > Genomics > Mathematics > Drug Approval
  (Nobel Prize)    (Operational)  (Validated)  (Benchmarks)  (Proofs)    (Phase III)
```

## Key Patterns

### What Makes a Domain AI-Ready?
1. **Large, clean datasets**: Protein structures (PDB), weather (ERA5), crystals (ICSD).
2. **Objective evaluation**: DFT validation, forecast accuracy, proof verification.
3. **Computable search spaces**: Crystal structures, molecular configurations.

### What Remains Hard?
1. **Drug discovery**: Biological complexity means early-stage success does not predict late-stage outcomes.
2. **Climate**: Non-linear tipping points outside training distribution.
3. **Mathematics**: Generating genuinely new mathematical theories (vs solving known problems).

## When to Use Each

- **Need to understand a protein**: AlphaFold 3.
- **Need to design a new material**: GNoME + A-Lab.
- **Need to optimize an algorithm**: AlphaEvolve.
- **Need a weather forecast**: GenCast / WeatherNext 2.
- **Need to find a drug candidate**: Insilico / Recursion / Schrodinger.
- **Need to interpret a genetic variant**: AlphaGenome + AlphaMissense.

## Sources

- [[sources/alphafold-five-years-impact]] — protein structure maturity
- [[sources/gnome-materials-discovery]] — materials discovery scale
- [[sources/alphaevolve-algorithm-discovery]] — mathematical achievements
- [[sources/gencast-weather-prediction]] — weather prediction operational status
- [[sources/ai-drug-discovery-phase-iii-2026]] — drug discovery pipeline
- [[sources/alphagenome-genomics]] — genomics capabilities
