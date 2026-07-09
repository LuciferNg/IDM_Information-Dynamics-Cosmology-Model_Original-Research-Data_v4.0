#!/usr/bin/env python3
"""
CFAS — Baryogenesis: Leptogenesis from Singlet W Mode (Honest)

η = 🔴 OPEN — leptogenesis fails because M₁ > T_RH
"""

import numpy as np

print("=" * 65)
print("CFAS — Baryogenesis: Honest Assessment")
print("=" * 65)

v = 246  # GeV
y_nu = 1.0  # from λ₀ = 1.0
m_nu = 0.05  # eV
m_nu_GeV = m_nu * 1e-9

M1 = y_nu**2 * v**2 / m_nu_GeV
T_RH = 1e9  # GeV (constrained by gravitinos)

print(f"M₁ = {M1:.2e} GeV")
print(f"T_RH = {T_RH:.2e} GeV (max from gravitino constraint)")

if M1 > T_RH:
    print(f"\n❌ M₁ ({M1:.1e}) > T_RH ({T_RH:.1e}) → N₁ NEVER thermally produced")
    print(f"❌ Inflaton decay (m_φ = 1e13 GeV) is kinematically forbidden")
    print(f"\n   Alternative mechanisms:")
    print(f"   1. Affleck-Dine from W field oscillation during preheating")
    print(f"   2. GUT baryogenesis via X-boson at M_GUT")
    print(f"   3. Spontaneous baryogenesis from sync dip gradient")
    print(f"\n   🔴 Baryogenesis is an OPEN problem in CFAS")
else:
    print(f"\n✅ M₁ < T_RH → thermal production possible")

print("\n" + "=" * 65)
print("HONEST VERDICT")
print("=" * 65)
print("""
Baryogenesis mechanism is NOT solved.
The leptogenesis route fails because M₁ = 1.2 × 10¹⁵ GeV > T_RH = 10⁹ GeV.
A non-thermal mechanism is needed.

This is a genuine open problem — not a hidden parameter.
""")
print("=" * 65)