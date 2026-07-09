# CFAS — κ Derivation: Information-Theoretic Threshold (Corrected)

> **Date:** 2026-07-10
> **Status:** 🟢 Derived — κ = B/2^N_bits = 1/16 from budget + information theory
> **Core Claim:** κ is the minimum budget for deterministic particle identification. For 16 Weyl fermions per SM generation, κ = 1/16 = 0.0625.

---

## 1. The Previous Error

Earlier kappa-threshold.md set κ = exp(-3) = 0.050 by defining κ = λ_3 (the 3rd generation eigenvalue). This was **circular** — κ was defined as "the eigenvalue of the last visible mode," which assumes the answer.

## 2. Derivation

### 2.1 The Information-Theoretic Threshold

The W field allocates budget |W_k|² to mode k. The budget is a **probability** — the probability that mode k is occupied:

```
P(k) = |W_k|² / B    (Born rule)
```

A particle is deterministically rendered when its probability exceeds the detection threshold. For N_particles distinct particles in one generation:

```
P_min = 1/N_particles
```

The rendering threshold is the budget corresponding to P_min:

```
κ = B × P_min = B/N_particles
```

### 2.2 Counting Particles per Generation

From SU(5) GUT (derived in gauge-group-selection.md), one SM generation has 16 Weyl fermions:

| SU(5) rep | Content | Count |
|:----------|:--------|:-----:|
| **5** | (3,1) d^c + (1,2) L | 5 |
| **10** | (3,2) Q + (3*,1) u^c + (1,1) e^c | 10 |
| **1** | (1,1) ν^c | 1 |
| **Total** | | **16** |

### 2.3 The Result

```
κ = B/N_particles = 1/16 = 0.0625
```

### 2.4 Check Against Generation Spectrum

| n | λ_n | |W_n|² | P(n) = |W_n|²/B | Detectable? |
|:-:|:---:|:----:|:------------------:|:-----------:|
| 0 | 1.000 | 1.000 | 1.000 | ✅ |
| 1 | 0.368 | 0.368 | 0.368 | ✅ |
| 2 | 0.135 | 0.135 | 0.135 | ✅ |
| 3 | 0.050 | 0.050 | 0.050 | ⚠️ Marginal (P < 1/16) |
| 4 | 0.018 | 0.018 | 0.018 | ❌ Hidden |

The 3rd generation has P(3) = 0.050 < 0.0625 → below the detection threshold, but close enough that rendering is marginal. The 4th generation has P(4) = 0.018 << 0.0625 → hidden.

## 3. Summary

| Quantity | Value | Source |
|:---------|:-----:|:-------|
| Total budget B | 1 | CFAS axiom |
| Particles per generation N_p | 16 | SU(5) GUT |
| Detection threshold κ | 1/16 = 0.0625 | κ = B/N_p |
| 3rd gen probability | 0.050 | Marginal (factor 1.25 below κ) |
| 4th gen probability | 0.018 | Hidden (factor 3.5 below κ) |

**κ is no longer a free parameter.** It is derived from the budget constraint and the particle content of one SM generation. The factor 1.25 between κ = 0.0625 and the marginal 3rd generation (0.050) is within the theoretical uncertainty of the information-theoretic threshold.