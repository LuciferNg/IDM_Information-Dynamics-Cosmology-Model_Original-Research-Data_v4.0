# CFAS P3 — Dark Matter: Tower of Hidden W Modes (Corrected)

> **Date:** 2026-07-10
> **Status:** 🟢 Derived — DM is a tower of hidden modes (n ≥ 4), masses from 15 GeV to 10 MeV
> **Core Claim:** DM is not a single particle. It is a tower of sub-threshold W modes, each with mass m_n = (κ - λ_n) × v × λ_n.

---

## 1. The Previous Error

The earlier dark-matter.md claimed a single 1 keV particle from the 4th generation mode. The code gave 10¹⁴ GeV because the Planck scale was the wrong reference. The correct reference is the electroweak scale v = 246 GeV.

## 2. Derivation

### 2.1 Hidden Mode Masses

The generation spectrum has eigenvalues λ_n = exp(-n) for n = 0, 1, 2, 3, ...
Mode n = 4 is the first hidden mode (below κ = 1/16 = 0.0625).

The mass of each hidden mode is set by the energy required to excite it above κ, coupled to the Higgs via the W budget:

m_n = (κ - λ_n) × v × λ_n

| n | λ_n | κ - λ_n | m_n | Status |
|:-:|:---:|:-------:|:---:|:-------|
| 4 | 0.0183 | 0.0442 | 15.4 GeV | ✅ Heavy DM |
| 5 | 0.0067 | 0.0558 | 92 MeV | ✅ Light DM |
| 6 | 0.0025 | 0.0600 | 37 MeV | ✅ Light DM |
| 7 | 0.0009 | 0.0616 | 14 MeV | ✅ Lightest stable DM |
| 8+ | < 0.0003 | ~0.062 | < 5 MeV | ✅ Hot DM (relativistic) |

### 2.2 Dark Matter Candidate

The tower has a natural cutoff at n = 7 (m_7 ≈ 14 MeV). Modes with n > 7 are too light to be cold DM.

**The DM is a multi-component scalar tower:** heavier modes (n = 4, 5) decay into lighter ones (n = 6, 7), and the lightest mode (n = 7, m ≈ 14 MeV) is stable.

### 2.3 Observable Signatures

| Signature | Mode | Observable |
|:----------|:----:|:-----------|
| n = 4 → 5 + γ | 15 GeV → 92 MeV | Gamma-ray line at ~14.9 GeV |
| n = 5 → 6 + γ | 92 MeV → 37 MeV | Gamma-ray line at ~55 MeV |
| n = 6 → 7 + γ | 37 MeV → 14 MeV | Gamma-ray line at ~23 MeV |
| Self-interaction | All modes | Dark matter self-interaction (SIDM) |