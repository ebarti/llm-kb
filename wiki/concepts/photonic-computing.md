---
title: "Photonic Computing"
type: concept
sources: ["[[sources/photonic-computing-ai-2026]]"]
related: ["[[concepts/ai-hardware-landscape]]", "[[concepts/ai-data-center-energy]]", "[[concepts/ai-accelerators]]"]
tags: [photonic-computing, optical, emerging-hardware, energy-efficiency]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Computing with photons instead of electrons: 100x speed/energy efficiency demonstrated in labs (MIT, LightGen); three manufacturing platforms (InP, SiN, SiPh); commercial revolution unrealistic before 2030; near-term value in optical interconnects and co-packaged optics."
---

## Overview

Photonic computing replaces electrons with photons as the computational medium. The physics are compelling for AI workloads: matrix multiplications — the dominant operation in neural networks — can be performed through wave interference rather than sequential arithmetic, potentially achieving orders-of-magnitude improvements in speed and energy efficiency. Optical signals carry no charge, generate no resistive heat, and travel at light speed.

However, the gap between laboratory demonstrations and commercial deployment remains wide. Photonic computing in 2026 is where quantum computing was circa 2020: transformative potential with limited practical deployment. The near-term value is in optical interconnects (replacing electrical links between GPU clusters) rather than photonic compute itself.

## Key Ideas

### How Photonic Computing Works

Matrix multiplications can be performed optically through the interference of light waves passing through programmable optical elements (Mach-Zehnder interferometers). The light's intensity and phase encode the matrix values, and the physical propagation of light through the circuit performs the multiplication at the speed of light with near-zero energy.

Three manufacturing platforms compete:
- **Indium phosphide (InP)**: High performance, expensive, used for active components (lasers, modulators)
- **Silicon nitride (SiN)**: Low loss, good for sensing and passive components
- **Silicon photonics (SiPh)**: Compatible with existing CMOS fabs, best for data communication at scale

### Key Demonstrations (2024-2026)

- **LightGen** (Science, 2026): All-optical chip for vision generation with 100x speed and energy efficiency over electronic chips, integrating millions of photonic neurons
- **MIT photonic processor** (2024): DNN computations in under half a nanosecond with 92%+ accuracy — fully integrated on-chip
- **Neurophos**: First commercial photonic processor running ResNet, BERT, and Atari RL algorithms — proving the architecture works for real neural networks
- **China** (Nature, 2026): Heavy investment in photonic AI chips as a route around US semiconductor export controls

### Near-Term: Optical Interconnects

The most practical photonic application in 2026 is data center optical interconnects. As GPU clusters scale to thousands of chips, the bandwidth and energy cost of electrical interconnects becomes prohibitive. The transition from pluggable optics to co-packaged optics (CPOs) was the top discussion topic at the Optical Fiber Conference (OFC) 2026.

[[entities/google-tpu]] v4 already uses optical circuit switching (OCS) for dynamic reconfiguration of its interconnect fabric — a production-scale deployment of photonic networking for AI.

Lightmatter is building photonic interconnects specifically for AI data centers, positioning between pure optical compute and pure electrical compute.

### Limitations

- **Manufacturing complexity**: Nanometre-scale precision in specialized clean facilities
- **Integration challenges**: Combining photonic and electronic components on one chip remains difficult
- **Talent shortage**: Far fewer photonic engineers than semiconductor engineers
- **Standardization**: No industry standards — each vendor uses proprietary approaches
- **Digital precision**: Optical analog computation is inherently less precise than digital; error accumulation limits network depth

### Timeline

Conservative estimates project approximately 300 million photonic units by 2030 and 1 billion by 2040. A complete computing revolution by 2026 is unrealistic. The progression will likely be:
1. **2024-2026**: Optical interconnects in data centers (happening now)
2. **2027-2029**: Hybrid photonic-electronic accelerators for specific AI workloads
3. **2030+**: Potentially standalone photonic AI processors at commercial scale

## How It Connects

Photonic computing addresses the two biggest constraints on [[concepts/ai-hardware-landscape]] growth: [[concepts/ai-data-center-energy]] (100x efficiency potential) and the [[concepts/memory-bandwidth-wall]] (optical interconnects bypass electrical bandwidth limits). It represents a potential paradigm shift beyond the [[concepts/ai-accelerators]] designs of 2026, all of which are fundamentally electronic.

## Open Questions

- Will photonic interconnects become the critical bottleneck-breaker before photonic compute matures?
- Can China's investment in photonic computing create an effective workaround for US chip export controls?
- Will hybrid photonic-electronic architectures emerge, or must the transition be all-or-nothing?
- How will analog precision limitations affect real-world neural network accuracy at scale?

## Sources

- [[sources/photonic-computing-ai-2026]] — comprehensive status assessment
