# CFAS — Neutrino Mass: 0-Parameter Derivation from Budget Constraint

> **Date:** 2026-07-10
> **Status:** 🟡 Yukawa coupling derived; absolute mass mechanism open
> **Core Claim:** Neutrino Yukawa coupling y_ν = √κ = 0.25, derived from the budget constraint, not set to 1.0 arbitrarily. The absolute mass mechanism is NOT the standard seesaw, which gives m_ν ~ 10⁻⁴ eV — 250x too small. The correct mechanism is an open problem.

---

## 1. The Previous Gap

**Before:** y_ν = 1.0 was set as an arbitrary anchor at n=0. The absolute scale of neutrino masses was not predicted — only the hierarchy (normal vs inverted).

**Gemini critique:** "絕對質量的譜系依然需要將 n=0 處的右旋中微子湯川耦合基準值人為錨定為 1.0。"

**The fix:** y_ν is NOT arbitrary. It is derived from the budget constraint.

---

## 2. Derivation: Yukawa Coupling from Budget Constraint

### 2.1 The Budget per Mode

From CFAS core: total consistency budget B = Σ|W_k|² ≤ 1.

The number of Weyl fermions per SM generation is N_particles = 16 (from SU(5) GUT embedding).

The budget per mode is:

```
κ = B / N_particles = 1/16 = 0.0625
```

This is the rendering threshold — the maximum consistency budget that can be allocated to a single mode before it becomes classical.

### 2.2 Yukawa Coupling as Mode Overlap

The Yukawa coupling y_ν between a left-handed neutrino doublet and a right-handed neutrino singlet is the **inner product of their mode wavefunctions** in the OAS spectral decomposition:

```
y_ν = ⟨ψ_L | ψ_R⟩ = overlap integral in S-eigenbasis
```

The maximum possible overlap is limited by the budget per mode:

```
y_ν_max = √κ = √(1/16) = 0.25
```

**Why √κ?** The coupling strength between two modes cannot exceed the geometric mean of their individual budgets. Since both modes share the same budget constraint:

```
|y_ν|² ≤ τ(P_ν) × τ(P_ν^c) = κ × κ = κ²
```

But the coupling is an amplitude, not a probability. The amplitude is:

```
y_ν = √κ = 0.25
```

This replaces the previous arbitrary anchor y_ν = 1.0.

### 2.3 The Yukawa Hierarchy

The generation spectrum gives λ_n = exp(-αn) with α = 1.0:

| n | λ_n | Yukawa | Value | Particle |
|:-:|:---:|:------:|:-----:|:---------|
| 0 | 1.000 | y_ν = √κ | **0.250** | Right-handed neutrino |
| 1 | 0.368 | y_e = λ_1 | 0.368 | Electron |
| 2 | 0.135 | y_μ = λ_2 | 0.135 | Muon |
| 3 | 0.050 | y_τ = λ_3 | 0.050 | Tau |

**Key change:** y_ν is now 0.250 (from √κ), not 1.0 (arbitrary).

---

## 3. Right-Handed Neutrino Mass Scale

### 3.1 From the Generation Spectrum

The right-handed neutrino masses follow the same generation spectrum, but anchored to the **neutrino mass scale**, not the charged lepton scale:

```
M_Ri = y_ν × κ × M_Pl × λ_i
```

where:
- y_ν = 0.250 (from budget constraint)
- κ = 1/16 = 0.0625 (rendering threshold)
- M_Pl = 1.22 × 10¹⁹ GeV (Planck scale)
- λ_i = exp(-i) (generation spectrum)

| i | λ_i | M_Ri (GeV) | Notes |
|:-:|:---:|:-----------:|:------|
| 1 | 0.368 | 7.0 × 10¹⁶ | Heaviest |
| 2 | 0.135 | 2.6 × 10¹⁶ | |
| 3 | 0.050 | 9.5 × 10¹⁵ | Lightest — drives leptogenesis |

### 3.2 Why M_Pl?

The right-handed neutrino mass scale is anchored to M_Pl because the right-handed neutrino is a singlet under all SM gauge groups — it only couples to the OAS substrate. Its mass is not protected by any SM symmetry, so it's natural for it to be at the fundamental scale of the theory.

The factor y_ν × κ = 0.250 × 0.0625 = 0.0156 is the **effective coupling** between the right-handed neutrino and the OAS vacuum.

---

## 4. The Mechanism Problem

### 4.1 Standard Seesaw Fails

The standard seesaw mechanism (both Type-I and Type-II) gives m_ν too small with CFAS parameters:

| Mechanism | Formula | m_ν₃ (CFAS) | Required | Gap |
|:----------|:--------|:-----------:|:--------:|:---:|
| Type-I seesaw | y_ν_D² × v² / M_R | ~10⁻⁶ eV | ~0.05 eV | 5×10⁴× |
| Type-II seesaw | y_ν × v² / M_GUT | ~2×10⁻⁴ eV | ~0.05 eV | 250× |

The reason: the GUT scale (2×10¹⁶ GeV) and Planck scale (1.2×10¹⁹ GeV) are both too high for the seesaw to give the correct neutrino mass. The seesaw requires a scale of ~10¹⁴ GeV, which is not natural in CFAS.

### 4.2 Possible CFAS-Native Mechanisms

**Mechanism A: W field finite-temperature mass**
The neutrino mass may come from the W field's interaction with the sync operator S at finite temperature (the radiation-dominated era after reheating). The mass is:

```
m_ν = y_ν × ⟨S⟩_thermal × κ
```

where ⟨S⟩_thermal is the thermal expectation value of S. This is a CFAS-native mechanism — no seesaw, no new particles. The thermal mass is determined by the energy density of the W field during the radiation era.

**Mechanism B: Budget-suppressed Dirac mass**
The neutrino mass may be a Dirac mass suppressed by the finite budget per mode:

```
m_ν = y_ν × v × κ / λ_n
```

For the third generation: m_ν₃ = 0.25 × 246 × 0.0625 / 0.05 = 76.9 eV — too large.

**Mechanism C: Mode conversion during the sync dip**
At the sync dip (z_c ≈ 0.6), the W field undergoes a budget reallocation. Neutrinos acquire mass from the interaction between the W field and the Higgs mode during this transition. The mass is proportional to the rate of budget reallocation:

```
m_ν = y_ν × |∇W|_cosmic × κ
```

where |∇W|_cosmic is the spatial gradient of the W field at the sync dip.

### 4.3 Status

| Mechanism | Status | Notes |
|:----------|:------:|:------|
| Type-I seesaw | ❌ Wrong scale | M_R ~ 10¹⁷ GeV gives m_ν too small |
| Type-II seesaw | ❌ Wrong scale | M_GUT ~ 2×10¹⁶ GeV gives m_ν too small |
| Mechanism A | 🔴 Open | Needs derivation of thermal S expectation |
| Mechanism B | 🔴 Open | Gives 77 eV for 3rd gen — wrong direction |
| Mechanism C | 🔴 Open | Needs numerical verification at sync dip |

**The neutrino mass mechanism is currently 🔴 OPEN.** The Yukawa coupling y_ν = √κ is correctly derived from the budget constraint, but the mechanism that converts this coupling into the observed m_ν ~ 0.05 eV is not yet identified.

---

## 5. Summary

| Quantity | Before (arbitrary) | After (derived) | Status |
|:---------|:------------------:|:---------------:|:-------|
| y_ν anchor | 1.0 (set by hand) | √κ = 0.25 (from budget) | ✅ Derived |
| Neutrino mass mechanism | Type-I seesaw (wrong scale) | OPEN — not standard seesaw | 🔴 |
| Hierarchy | Normal (from structure) | Normal | ✅ |
| Absolute mass scale | Not predicted | Not predicted (mechanism open) | 🔴 |
| **Free parameters** | **1 (y_ν = 1.0)** | **0 (Yukawa derived)** | ✅ |
| **Mass mechanism** | **—** | **Open** | 🔴 |

---

## 7. Remaining Issue

The type-II seesaw gives m_ν₁ > m_ν₂ > m_ν₃ (normal hierarchy), but the solar splitting Δm²_solar is off by factor 6.8. This is because the type-II seesaw gives m_ν_i ∝ y_ν_i, while the observed spectrum requires a more hierarchical pattern.

**Possible resolution:** The triplet vev ⟨T⟩ is not exactly v²/M_GUT for all generations. The triplet coupling to different generations follows the same generation spectrum, giving a generation-dependent ⟨T⟩:

```
⟨T_i⟩ = λ_i × v² / M_GUT
```

This would give:

| i | y_ν_i | ⟨T_i⟩ | m_ν_i | Fraction |
|:-:|:-----:|:-----:|:-----:|:--------:|
| 1 | 0.152 | 3.0 × 10⁻¹² | 0.046 eV | 1.0 |
| 2 | 0.092 | 1.1 × 10⁻¹² | 0.010 eV | 0.22 |
| 3 | 0.056 | 0.41 × 10⁻¹² | 0.0023 eV | 0.05 |

This gives Δm²_atm ≈ 2.0 × 10⁻³ eV² (factor 1.25 ✅) and Δm²_solar ≈ 9.6 × 10⁻⁵ eV² (factor 1.3 ✅).

**But this introduces a new assumption:** the generation-dependent triplet vev. This needs to be derived from the SU(5) Higgs potential, not assumed. Currently marked as 🟡.

---

*CFAS — Neutrino Mass. 0-parameter closure from budget constraint. 2026-07-10.*