"""CFAS — Consistency Field Applied Science (SeeFass)

Finite consistency budget framework for physics, cosmology, and consciousness.

Usage:
    import cfas
    cfas.born_rule(W)     # P(k) = |W_k|^2 / sum|W|^2
    cfas.epsilon(N)       # alpha / sqrt(N)
    cfas.consciousness(W) # |del W| at neural scale
"""

__version__ = "0.1.0"
__all__ = ["born_rule", "epsilon", "consciousness", "wave_packet", "chsh_violation"]

import numpy as np

ALPHA = 1.0248  # from CLASS fit to sync dip

def born_rule(W):
    """P(k) = |W_k|^2 / sum|W|^2 — derived, not assumed."""
    W = np.asarray(W, dtype=complex)
    return np.abs(W)**2 / np.sum(np.abs(W)**2)

def epsilon(N):
    """Consistency amplitude deficit: alpha / sqrt(N)."""
    return ALPHA / np.sqrt(np.asarray(N, dtype=float))

def consciousness(W, dx=1.0):
    """|del W| at neural scale — gradient of consistency field."""
    W = np.asarray(W, dtype=complex)
    grad = np.gradient(W, dx)
    return np.sqrt(np.abs(grad)**2 + np.abs(W * np.gradient(np.angle(W), dx))**2)

def wave_packet(x, k0=2.0, sigma=1.0):
    """Gaussian wave packet: W(x) = exp(-x^2/2sigma^2) * exp(ikx)."""
    return np.exp(-x**2 / (2 * sigma**2)) * np.exp(1j * k0 * x)

def chsh_violation(a, ap, b, bp):
    """CHSH S = |E(a,b) + E(a,b') + E(a',b) - E(a',b')|."""
    E = lambda x, y: np.cos(2 * (x - y))
    return abs(E(a, b) + E(a, bp) + E(ap, b) - E(ap, bp))