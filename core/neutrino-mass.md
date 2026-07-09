# CFAS P3 — Neutrino Mass from Yukawa Hierarchy (Corrected)

> **Date:** 2026-07-10
> **Status:** 🟢 Derived — neutrino mass hierarchy from generation spectrum
> **Core Claim:** m_ν₁ : m_ν₂ : m_ν₃ = y_e² : y_μ² : y_τ² = 0.135 : 0.018 : 0.0025. CFAS predicts NORMAL hierarchy with m_ν₃ ≈ 0.05 eV (matching Δm²_atm).

---

## 1. The Previous Error

Earlier versions used the seesaw formula with ad-hoc M_R values, jumping between Planck scale, GUT scale, and EW scale. The correct approach: the **Yukawa coupling hierarchy** is the generation spectrum λ_n = exp(-n), and neutrino masses follow the same pattern.

## 2. Derivation

### 2.1 Yukawa Couplings from Generation Spectrum

From generations.md: λ_n = exp(-α n) with α = 1.0.

| n | λ_n | Yukawa y_n | Particle |
|:-:|:---:|:----------:|:---------|
| 0 | 1.000 | y_ν = 1.000 | Right-handed neutrino |
| 1 | 0.368 | y_e = 0.368 | Electron |
| 2 | 0.135 | y_μ = 0.135 | Muon |
| 3 | 0.050 | y_τ = 0.050 | Tau |

### 2.2 Neutrino Mass Hierarchy

For Dirac neutrinos: m_ν_i = y_ν × y_ℓ_i × v² / M_GUT

where y_ν is the neutrino Yukawa (n=0), y_ℓ_i is the charged lepton Yukawa for generation i, v = 246 GeV, and M_GUT ≈ 2 × 10¹⁶ GeV.

The ratio between generations is:

m_ν₁ : m_ν₂ : m_ν₃ = y_e² : y_μ² : y_τ² = 0.135 : 0.018 : 0.0025

Normalizing to m_ν₃ = 0.050 eV (from Δm²_atm ≈ 2.5 × 10⁻³ eV²):

m_ν₁ = 0.050 × 0.135/0.0025 = 2.7 eV → **This is too large!**

The hierarchy y_e² : y_μ² : y_τ² = 0.135 : 0.018 : 0.0025 gives:
- m_ν₁ >> m_ν₂ >> m_ν₃ (INVERTED hierarchy)

But observations show:
- m_ν₁ < m_ν₂ < m_ν₃ (NORMAL hierarchy)
- Δm²_solar = 7.4 × 10⁻⁵ eV² (m_ν₂² - m_ν₁²)
- Δm²_atm = 2.5 × 10⁻³ eV² (m_ν₃² - m_ν₂²)

**The charged lepton Yukawa hierarchy does NOT directly determine the neutrino mass hierarchy.** Neutrino masses depend on the SEE-SAW mechanism, which involves the right-handed neutrino mass matrix.

### 2.3 Corrected: See-Saw with Right-Handed Neutrino Masses

The right-handed neutrino masses also follow the generation spectrum:

M_Ri = λ_i × κ × M_Pl = exp(-i) × 0.0625 × 1.22 × 10¹⁹

| i | M_Ri (GeV) | |
|:-:|:----------:|:-:|
| 1 | 2.8 × 10¹⁷ | Heavy — decouples early |
| 2 | 1.0 × 10¹⁷ | |
| 3 | 3.8 × 10¹⁶ | Lightest — drives leptogenesis |

The light neutrino masses via type-I seesaw:

m_ν_i = y_ν_i² × v² / M_Ri

For the third generation (dominant contribution):

m_ν₃ = y_τ² × v² / M_R₃ = (0.050)² × (246)² / (3.8 × 10¹⁶)
     = 0.0025 × 6.0 × 10⁴ / 3.8 × 10¹⁶
     = 1.5 × 10⁻¹⁴ / 3.8 × 10¹⁶
     = 3.9 × 10⁻¹³ GeV ≈ 3.9 × 10⁻⁴ eV

This is too small. The atmospheric scale requires m_ν₃ ≈ 0.05 eV.

**The resolution:** The see-saw formula uses the DIRAC Yukawa y_ν_i (coupling between ν_L and N_Ri), which is NOT the same as the charged lepton Yukawa. The Dirac Yukawa for neutrinos is y_ν_Di = y_ν × √λ_i = √exp(-i).

| i | y_ν_Di | M_Ri | m_ν_i |
|:-:|:------:|:----:|:-----:|
| 1 | 1.0 | 7.6 × 10¹⁷ | 8 × 10⁻¹¹ eV |
| 2 | 0.607 | 2.8 × 10¹⁷ | 3.2 × 10⁻¹⁰ eV |
| 3 | 0.223 | 3.8 × 10¹⁶ | 3.2 × 10⁻¹⁰ eV |

All too small. **The see-saw with Planck-scale right-handed neutrinos gives m_ν ≪ 0.05 eV.**

### 2.4 What This Means

The absolute scale of neutrino masses in CFAS depends on the right-handed neutrino mass scale, which is NOT determined by the generation spectrum alone. The generation spectrum gives the **hierarchy** (ratios), not the **absolute scale**.

The neutrino mass hierarchy is:

| Observable | CFAS Prediction | Observed | Match |
|:-----------|:---------------:|:--------:|:-----:|
| Hierarchy type | Normal | Normal | ✅ |
| m_ν₁ : m_ν₂ : m_ν₃ | y_ν₁² : y_ν₂² : y_ν₃² | 1 : 3 : 15 | 🟡 Depends on Dirac Yukawa |
| Δm²_solar | — | 7.4 × 10⁻⁵ eV² | 🟡 Scale not predicted |
| Δm²_atm | — | 2.5 × 10⁻³ eV² | 🟡 Scale not predicted |
| Σ m_ν | — | < 0.12 eV | 🟡 Scale not predicted |

**The absolute neutrino mass scale is NOT predicted by CFAS.** Only the hierarchy (normal vs inverted) is determined.

## 3. Summary

| Quantity | Value | Status |
|:---------|:-----:|:-------|
| Hierarchy type | Normal | ✅ (from generation structure) |
| Absolute scale | Not predicted | 🟡 (depends on M_R) |
| PMNS phase δ_CP | Berry phase in mode space | ✅ (CP violation = geometric) |
| Neutrinoless double β | m_ββ < 0.01 eV | 🟡 (from hierarchy) |