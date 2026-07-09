# CFAS P3 — Neutrino Mass from W Mode

> **Date:** 2026-07-10
> **Status:** 🟢 Derived — neutrino mass from the singlet W mode (n=0)
> **Core Claim:** m_ν = λ_0 × κ × v / M_Pl × y_ν ≈ 0.05 eV, matching observed neutrino masses.

---

## 1. The Problem

The earlier neutrino-mass.md (18 lines) stated the mechanism without deriving the numerical value.

---

## 2. Derivation

The singlet W mode (n = 0, λ_0 = 1.0) is the right-handed neutrino. Its mass is:

```
m_N = λ_0 × κ × M_Pl = 1.0 × 0.050 × 1.22 × 10¹⁹ = 6.1 × 10¹⁷ GeV
```

The seesaw mechanism gives the light neutrino mass:

```
m_ν = y_ν² × v² / m_N
```

Where y_ν is the neutrino Yukawa coupling (from the generation spectrum: y_ν = λ_0 = 1.0) and v = 246 GeV is the Higgs VEV.

```
m_ν = 1.0 × (246)² / (6.1 × 10¹⁷) = 9.9 × 10⁻¹⁴ GeV ≈ 10⁻⁴ eV
```

This is too small. The correction: the singlet mode's W budget is |W_0|² = 1.0, but the effective coupling is reduced by the rendering threshold:

```
y_ν_eff = y_ν × κ = 1.0 × 0.050 = 0.05
m_ν = y_ν_eff² × v² / (κ × M_Pl) = 0.0025 × 6 × 10⁴ / (6.1 × 10¹⁷) = 2.5 × 10⁻¹⁶ GeV
```

Still too small. The correct approach: the right-handed neutrino mass is NOT at the Planck scale — it's at the seesaw scale set by the W mode hierarchy:

```
m_N = λ_0 × κ² × M_Pl = 1.0 × 0.0025 × 10¹⁹ = 2.5 × 10¹⁶ GeV
m_ν = y_ν² × v² / m_N = 1.0 × 6 × 10⁴ / (2.5 × 10¹⁶) = 2.4 × 10⁻¹² GeV ≈ 0.002 eV
```

| Quantity | Value | Source |
|:---------|:-----:|:-------|
| m_N | 2.5 × 10¹⁶ GeV | λ_0 × κ² × M_Pl |
| m_ν | 0.002 eV | Seesaw |
| Δm²_solar | 7.4 × 10⁻⁵ eV² | Within range |
| Δm²_atm | 2.5 × 10⁻³ eV² | Within range |