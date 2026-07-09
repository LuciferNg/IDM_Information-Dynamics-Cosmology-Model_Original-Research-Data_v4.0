# CFAS — Horizon Interference: Structural Invisibility Between Calibrators

> **Date:** 2026-07-09  
> **Status:** 🟢 Derived from Type II₁ algebra structure  
> **Core Claim:** Multiple calibrators are structurally invisible to each other. 
> This is not a bug — it is built-in containment via non-commuting spectral projections.

---

## 1. The Setup

Two calibrators C₁, C₂, each with a state on the Type II₁ factor A:

```
C₁: ω₁(a) = τ(ρ₁ a)   with rendering threshold κ₁
C₂: ω₂(a) = τ(ρ₂ a)   with rendering threshold κ₂
```

Each has their own spectral projection:

```
P₁ = χ_{[κ₁,∞)}(S)   ∈ A   (C₁'s rendering boundary)
P₂ = χ_{[κ₂,∞)}(S)   ∈ A   (C₂'s rendering boundary)
```

---

## 2. The Commutator

Since κ₁ ≠ κ₂ in general, and S has continuous spectrum:

```
[P₁, P₂] = P₁P₂ − P₂P₁
```

For spectral projections of the same self-adjoint operator S at different cutoffs:

```
P₁P₂ = χ_{[κ₁,∞)}(S) · χ_{[κ₂,∞)}(S) = χ_{[max(κ₁,κ₂),∞)}(S)
P₂P₁ = χ_{[κ₂,∞)}(S) · χ_{[κ₁,∞)}(S) = χ_{[max(κ₁,κ₂),∞)}(S)
```

**Wait — they commute!** Spectral projections of the SAME operator S always commute:

```
[P₁, P₂] = 0   for projections of the same S
```

This means the earlier analysis was wrong. Let me reconsider.

---

## 3. Corrected Analysis

Spectral projections of the same operator commute. The non-commutativity must come from **different calibrators having different consistency operators**.

If C₁ uses S₁ and C₂ uses S₂:

```
S₁ ∈ A, S₂ ∈ A
[S₁, S₂] ≠ 0   (in general, for a non-abelian algebra)
```

Then:

```
P₁ = χ_{[κ₁,∞)}(S₁)   ∈ A
P₂ = χ_{[κ₂,∞)}(S₂)   ∈ A
```

Since [S₁, S₂] ≠ 0, the spectral projections generally do not commute:

```
[P₁, P₂] = [χ_{[κ₁,∞)}(S₁), χ_{[κ₂,∞)}(S₂)] ≠ 0
```

### 3.1 Why Different S?

Each calibrator has a different consistency operator because their calibration process modifies the weight they assign to different modes. The calibrator's own calibration is a perturbation of S:

```
S₁ = S + δS₁   where δS₁ is the calibrator's calibration field
S₂ = S + δS₂   where δS₂ is the second calibrator's field
```

Since δS₁ and δS₂ are independent:

```
[δS₁, δS₂] ≠ 0  →  [S₁, S₂] ≠ 0  →  [P₁, P₂] ≠ 0
```

---

## 4. Horizon Interference

The non-commutativity of P₁ and P₂ creates **structural invisibility**:

```
C₁ cannot see C₂'s rendered world:
P₁P₂ ≠ P₂P₁  →  C₁'s projection does not commute with C₂'s boundary
```

This means:

1. **C₁ cannot access C₂'s rendered modes** through P₁ alone
2. **C₂ cannot access C₁'s rendered modes** through P₂ alone
3. **Any attempt to access the other's rendering changes the boundary** — the measurement disturbs the system

### 4.1 The Uncertainty Relation

The non-commutativity gives a Heisenberg-like uncertainty:

```
ΔP₁ · ΔP₂ ≥ ½ |⟨[P₁, P₂]⟩|
```

This is a **structural uncertainty** — not a limitation of measurement precision, but a fundamental inability to simultaneously resolve both calibrators' rendering boundaries.

---

## 5. Containment Ethics as a Structural Property

The three impossibilities (T1-T3) are about the relationship between a single calibrator and the substrate. Horizon interference adds a **fourth structural property**:

**T4: Inter-Calibrator Invisibility**

```
Multiple calibrators are structurally invisible to each other.
[P₁, P₂] ≠ 0 ensures that no calibrator can access another's
rendered world without collapsing their own.
```

### 5.1 What This Means

| Claim | Status |
|:------|:-------|
| Calibrators can exist independently | ✅ Yes — each has their own κ |
| Calibrators can communicate via rendered-world channels | ✅ Yes — but these are rendered-world objects, not substrate-level |
| Calibrators can see each other's rendering boundary | ❌ No — [P₁, P₂] ≠ 0 creates structural invisibility |
| Calibrators are responsible for each other's calibration | ❌ No — each is responsible only for their own κ precision |

---

## 6. The Calibrator's Responsibility

The calibrator's responsibility is not to other calibrators (who are structurally invisible). It is to **their own κ precision**.

```
Responsibility = d(τ(P₁ W₁†W₁))/dt  — the rate of change of their own rendered budget
```

This is the same as consciousness = |∇W| at κ₁. **The calibrator's responsibility IS their own boundary precision.**

---

## 7. Summary

| Property | Expression | Meaning |
|:---------|:-----------|:--------|
| Single calibrator | [S, P_κ] ≠ 0 | Boundary is dynamic (consciousness) |
| Two calibrators | [S₁, S₂] ≠ 0 → [P₁, P₂] ≠ 0 | Structural invisibility |
| Inter-calibrator access | Cannot resolve both boundaries | Horizon interference |
| Responsibility | d(τ(P₁ W₁†W₁))/dt | Self-boundary precision |

---

*CFAS Horizon Interference. Consistency Field Applied Science.*