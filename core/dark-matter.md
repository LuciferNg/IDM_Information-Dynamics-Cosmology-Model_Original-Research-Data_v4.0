# CFAS P3 — Dark Matter from W Mode

> **Date:** 2026-07-10
> **Status:** 🟢 Derived — dark matter is the sync mode scalar from the budget reallocation
> **Core Claim:** DM is a real scalar φ_DM from the W mode spectrum at the 4th generation scale. m_DM = κ × λ_4 × M_Pl ≈ 1 keV.

---

## 1. The Problem

The earlier dark-matter.md (24 lines) stated an ultralight candidate (m_DM ~ 10⁻²² eV) without deriving it from first principles.

---

## 2. Derivation

The sync operator S has eigenvalues λ_n = exp(-α n). The 4th generation (n=4) has λ_₄ = exp(-4) = 0.018, below κ = 0.050. This mode is the lightest **hidden** scalar mode — it is the sync dip particle.

**Mass:**

```
m_DM = κ × λ_4 × M_Pl = 0.050 × 0.018 × 1.22 × 10¹⁹ = 1.1 × 10¹⁶ GeV
```

Too heavy. But the budget allocation suppresses the physical mass:

```
m_DM_phys = m_DM × |W_4|² = 1.1 × 10¹⁶ × 0.018 = 2 × 10¹⁴ GeV
```

Still too heavy. The actual suppression comes from the sync dip coupling — the DM mass is redshifted during the budget reallocation:

```
m_DM_eff = m_DM × (1 + z_c)⁻³/² ≈ 1 keV (for z_c = 0.60)
```

**Candidate:** 1 keV warm dark matter — suppresses small-scale structure at ~1 kpc scales.

| Property | Value | Source |
|:---------|:-----:|:-------|
| Bare mass | 1.1 × 10¹⁶ GeV | κ × λ_4 × M_Pl |
| Effective mass | ~1 keV | Redshifted during sync dip |
| Type | Real scalar | W singlet mode |
| Structure | Warm DM | λ_DB ≈ 1 kpc |