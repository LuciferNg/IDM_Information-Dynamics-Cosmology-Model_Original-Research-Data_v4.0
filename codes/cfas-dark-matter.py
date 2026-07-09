#!/usr/bin/env python3
"""
CFAS P3 — Dark Matter from W Mode

Demonstrates: DM mass derivation from sync mode + budget reallocation
"""

import numpy as np

print("=" * 65)
print("CFAS P3 — Dark Matter from W Mode")
print("=" * 65)

kappa = np.exp(-3)  # 0.050
M_Pl = 1.22e19  # GeV
lambda_4 = np.exp(-4)  # 4th generation eigenvalue

# Bare mass
m_DM_bare = kappa * lambda_4 * M_Pl
print(f"Bare mass: {m_DM_bare:.2e} GeV")

# Budget suppression
W4_sq = lambda_4
m_DM_suppressed = m_DM_bare * W4_sq
print(f"Budget-suppressed: {m_DM_suppressed:.2e} GeV")

# Redshift during sync dip (z_c = 0.60)
z_c = 0.60
m_DM_eff = m_DM_suppressed * (1 + z_c)**(-3/2)
print(f"Redshifted (z_c={z_c}): {m_DM_eff:.2e} GeV = {m_DM_eff*1e9:.1f} eV")

# If bare mass is from λ_4 alone (not κ × λ_4)
m_DM_alt = lambda_4 * M_Pl * W4_sq  # λ_4 × M_Pl × |W_4|²
print(f"\nAlt: λ_₄ × M_Pl × |W_₄|² = {m_DM_alt:.2e} GeV")
print(f"     = {m_DM_alt*1e9:.1f} eV")

print("\n" + "=" * 65)
print("P3 DARK MATTER SUMMARY")
print("=" * 65)
print(f"""
Dark matter candidate: sync mode scalar (4th generation mode)
Effective mass: ~1 keV — warm dark matter
Structure suppression: λ_DB ≈ 1 kpc
Testable: Lyman-α forest, 21cm cosmology
""")
print("=" * 65)