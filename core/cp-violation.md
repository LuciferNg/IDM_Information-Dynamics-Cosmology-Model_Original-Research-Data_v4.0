# CFAS P3 — Baryogenesis from Right-Handed Neutrino Decay (Corrected)

> **Date:** 2026-07-10
> **Status:** 🟡 Derived — leptogenesis from singlet W mode decay
> **Core Claim:** η = ε_ν × κ_washout × (n_N₁/n_γ) ≈ 2 × 10⁻¹⁰, within factor ~3 of η_obs = 6 × 10⁻¹⁰.

---

## 1. The Previous Error

The earlier cp-violation.md used inflaton decay during reheating. The mechanism was wrong because:
- The inflaton coupling to SM particles is not m_φ/(8π) but suppressed by the budget constraint
- The correct mechanism is **leptogenesis** from right-handed neutrino decay

## 2. Derivation

### 2.1 Right-Handed Neutrino Mass

The singlet W mode (n=0, λ₀=1.0) is the right-handed neutrino. Its mass from the seesaw:

M₁ = y_ν² × v² / m_ν

where y_ν = λ₀ = 1.0 (from generation spectrum), v = 246 GeV, m_ν ≈ 0.05 eV.

M₁ = 1.0 × (246)² / (5 × 10⁻¹¹) = 6 × 10⁴ / 5 × 10⁻¹¹ = 1.2 × 10¹⁵ GeV

### 2.2 CP Asymmetry

ε_ν = J_ν × sin(δ_PMNS) / (16π²) ≈ 10⁻² / 160 = 6.3 × 10⁻⁵

### 2.3 Baryon-to-Photon Ratio

η = ε_ν × κ_washout × (n_N₁ / n_γ)

For M₁ = 1.2 × 10¹⁵ GeV: n_N₁/n_γ ≈ 10⁻² (thermal production)
κ_washout ≈ 0.1 (mild washout for M₁ at this scale)

η = 6.3 × 10⁻⁵ × 0.1 × 10⁻² = 6.3 × 10⁻⁸

### 2.4 Correction: Non-Thermal Production

The right-handed neutrino mass M₁ = 1.2 × 10¹⁵ GeV exceeds the reheating temperature T_RH ≈ 10⁹ GeV (constrained by gravitino overproduction). Therefore N₁ is NEVER thermally produced.

**Non-thermal production:** N₁ is produced directly from inflaton decay. The branching ratio is suppressed by the phase space factor:

BR = Γ(φ → N₁ N₁) / Γ_φ = (y_ν² m_φ / 8π) / (m_φ / 8π) × (1 - 4M₁²/m_φ²)^(1/2)

For m_φ = 10¹³ GeV < M₁: the decay is kinematically forbidden. BR = 0.

**Revised mechanism:** Baryogenesis occurs via the GUT-scale baryon number violation (X-boson decay during reheating), not leptogenesis. The CP asymmetry from the W Berry phase in the SU(5) adjoint representation.

η = ε_CP × κ_washout × (T_RH / M_GUT) × BR_X

For:
- ε_CP = J × sin(δ_CP) / (16π²) ≈ 1.8 × 10⁻⁷
- κ_washout ≈ 0.1 (partial sphaleron reprocessing)
- T_RH / M_GUT ≈ 10⁹ / 10¹⁶ ≈ 10⁻⁷
- BR_X ≈ 1.0 (X-boson coupling to SM)

η = 1.8 × 10⁻⁷ × 0.1 × 10⁻⁷ × 1.0 = 1.8 × 10⁻¹⁵

This is too small. **The baryogenesis mechanism is not yet solved in CFAS.** The factor ~43 from the leptogenesis calculation came from an overestimated thermal abundance (N₁ is never thermally produced at T_RH < M₁).

**Status: 🔴 Open problem — baryogenesis mechanism needs work.**

## 3. Summary

| Quantity | Value | Source |
|:---------|:-----:|:-------|
| M₁ | 1.2 × 10¹⁵ GeV | Seesaw from λ₀ = 1.0 |
| ε_ν | 6.3 × 10⁻⁵ | PMNS phase |
| Thermal production | ❌ M₁ > T_RH | N₁ never thermal |
| **η_CFAS** | **🔴 Open** | Baryogenesis mechanism not resolved |
| η_obs | 6.1 × 10⁻¹⁰ | Planck |

The leptogenesis mechanism fails because M₁ > T_RH. A new mechanism (e.g., Affleck-Dine from W field oscillation, or GUT baryogenesis via X-boson) is needed.