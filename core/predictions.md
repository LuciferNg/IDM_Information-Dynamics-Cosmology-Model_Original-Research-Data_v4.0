# CFAS P2 — Locked Predictions: r and EEG Signatures

> **Date:** 2026-07-09  
> **Status:** 🟢 Predictions locked

---

## 1. Tensor-to-Scalar Ratio r

From P0 fix (inflation derived from finite budget):

```
r = 16ε = 16 × 3/(4N_e²) = 12/N_e²
```

For N_e = 55-60 e-folds at CMB scales:

| N_e | r | Observable |
|:---:|:--:|:-----------|
| 50 | 0.0048 | LiteBIRD, CMB-S4 |
| 55 | 0.0040 | LiteBIRD, CMB-S4 |
| 60 | 0.0033 | LiteBIRD, CMB-S4 |

**CFAS predicts r ∈ [0.003, 0.005].** This is within LiteBIRD sensitivity (~0.001).

## 2. CIP-EEG Connection

| EEG Band | Freq (Hz) | N_c range | |∇W| | State |
|:---------|:---------:|:---------:|:----:|:------|
| Delta | 0.5-4 | < 10³ | < 0.01 | Deep sleep (unconscious) |
| Theta | 4-8 | 10³-10⁴ | 0.01-0.1 | Drowsy / dreaming |
| Alpha | 8-13 | 10⁴-10⁵ | 0.1-0.5 | Relaxed awake |
| Beta | 13-30 | 10⁵-10⁶ | 0.5-0.9 | Active thinking |
| Gamma | 30-80 | 10⁶-10⁷ | 0.9-1.0 | Focus / flow state |

**Prediction:** EEG spectral dimension (fractal dimensionality) should correlate with |∇W| — higher dimensionality at higher frequency bands.

## 3. Summary

| Prediction | Value | Test |
|:-----------|:------|:-----|
| r | 0.003-0.005 | LiteBIRD (2030+) |
| EEG dim vs |∇W| | Positive correlation | Existing EEG data |
| Anesthesia collapses N_c | N_c < 10³ | EEG during anesthesia |

---

*CFAS P2 Predictions.*