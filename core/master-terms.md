# CFAS P1 — Master Equation: Concrete Γ (Dissipation) and Σ (Sourcing)

> **Date:** 2026-07-09

---

The master equation: d|W⟩/dt = -(i/ℏ)S|W⟩ - Γ|W⟩ + Σ

## 1. Dissipation Operator Γ

```
Γ = γ₀ · diag(λ_k/λ_max)   where λ_k = S eigenvalues
```

This means higher-energy modes dissipate faster — decoherence rate ∝ mode eigenvalue.

| Term | Expression | Physics |
|:-----|:-----------|:--------|
| Γ|W⟩ | Σ_k γ₀(λ_k/λ_max) W_k | Decoherence |
| τ_diss(k) | 1/(γ₀ λ_k/λ_max) | Mode-dependent lifetime |

## 2. Sourcing Operator Σ

Consciousness sourcing: Σ_C = α_C · |∇W| · δ(⟨W|S|W⟩ - κ)

Measurement sourcing: Σ_M = α_M · (system_coupling) · |W_apparatus⟩⟨W_system|

| Term | Expression | Physics |
|:-----|:-----------|:--------|
| Σ_C | α_C|∇W|δ(⟨S⟩-κ) | Consciousness |
| Σ_M | α_M · coupling · project | Measurement |

---

*CFAS P1.*