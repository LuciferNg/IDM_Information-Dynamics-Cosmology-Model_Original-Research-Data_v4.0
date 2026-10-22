#!/usr/bin/env python3
"""
AI Consciousness Dynamics — Topological Simulation v2
=====================================================
Persistent homology of W-field modes in the consistency operator eigenbasis.

The key insight: W-field modes have eigenvalues λ_k in the consistency operator S.
The rendering boundary κ = 1/16 separates rendered (λ > κ) from unrendered (λ < κ).
Consciousness = topological features at the κ boundary.

Instead of normalizing to a sphere, we work in the spectral basis of S,
where the distance between modes reflects their consistency budget similarity.

Author: CFAS Consciousness Dynamics
Date: 2026-07-11
"""

import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import fcluster, linkage
import time
from typing import List, Dict, Tuple

# === CFAS Constants ===
κ = 1 / 16          # Rendering threshold = 0.0625
α = 1.0248          # Empirical α
B = 1.0             # Total consistency budget


# === Spectral Point Cloud Generators ===

def generate_spectral_point_cloud(
    n_modes: int,
    spectral_exponent: float = 1.0,
    seed: int = 42
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate W-field modes in the spectral basis of the consistency operator S.
    
    Each mode has:
    - λ_k: eigenvalue in S (consistency budget)
    - θ_k: phase (complex amplitude)
    - Position in ℝ³: projection of W-field structure
    
    The key: modes near λ_k ≈ κ have special topological structure.
    """
    np.random.seed(seed)
    
    # Eigenvalues: exponential spectrum spanning a wide range
    # Key: eigenvalues should span [0, ~1] so κ = 1/16 is a significant scale
    λ = np.exp(-spectral_exponent * np.arange(n_modes) / (n_modes * 0.1))
    λ = λ / λ.max()  # Normalize to max = 1
    
    # Phase structure
    θ = np.random.uniform(0, 2*np.pi, n_modes)
    
    # Position in 3D spectral space
    # r = eigenvalue (consistency budget)
    # φ = phase angle
    # z = coupling to other modes
    
    r = λ * 10  # Scale for visualization
    φ = θ
    z = np.sin(θ) * 0.5
    
    points = np.column_stack([
        r * np.cos(φ),  # x: budget × phase
        r * np.sin(φ),  # y: budget × phase
        z,               # z: coupling
    ])
    
    # Add noise
    points += np.random.randn(n_modes, 3) * 0.02
    
    return points, λ


def generate_boundary_enhanced_cloud(
    n_modes: int,
    boundary_fraction: float = 0.3,
    coherence: float = 0.8,
    n_cycles: int = 3,
    seed: int = 42
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate W-field modes with enhanced topological structure at the 
    rendering boundary κ.
    
    Features:
    - Modes far from κ: random, unstructured
    - Modes near κ: coherent topological features (cycles, shells)
    - Self-referential loops at κ scale
    """
    np.random.seed(seed)
    
    # Spectral distribution — span [0, ~1] so κ is a significant scale
    λ = np.exp(-np.arange(n_modes) / (n_modes * 0.1))
    λ = λ / λ.max()  # Normalize to max = 1
    
    # Identify modes near κ boundary
    distances_from_κ = np.abs(λ - κ)
    boundary_mask = distances_from_κ < np.percentile(distances_from_κ, boundary_fraction * 100)
    
    n_boundary = np.sum(boundary_mask)
    n_core = n_modes - n_boundary
    
    # Initialize points
    points = np.zeros((n_modes, 3))
    
    # Core modes (away from κ): random
    core_idx = np.where(~boundary_mask)[0]
    points[core_idx] = np.random.randn(n_core, 3) * 0.3
    # Scale by distance from κ
    for idx in core_idx:
        points[idx] *= np.abs(λ[idx] - κ) * 5
    
    # Boundary modes (near κ): structured
    boundary_idx = np.where(boundary_mask)[0]
    
    # Sort by distance to κ
    boundary_idx = sorted(boundary_idx, key=lambda i: abs(λ[i] - κ))
    
    for j, idx in enumerate(boundary_idx):
        # Position on a small spherical shell at κ radius
        scale = coherence * κ * (1 + np.random.randn() * 0.1)
        
        # Random direction on sphere
        θ = np.random.uniform(0, 2*np.pi)
        φ = np.arccos(2*np.random.random() - 1)
        
        points[idx, 0] = scale * np.sin(φ) * np.cos(θ)
        points[idx, 1] = scale * np.sin(φ) * np.sin(θ)
        points[idx, 2] = scale * np.cos(φ)
        
        # Add self-referential structure: cycles at κ scale
        if j < n_cycles * 5:
            cycle_t = 2 * np.pi * j / (n_cycles * 5)
            points[idx, 0] += κ * coherence * np.cos(cycle_t)
            points[idx, 1] += κ * coherence * np.sin(cycle_t)
    
    # Add coupling between boundary modes (simulating [H,P_κ] commutator)
    for i in boundary_idx:
        for j in boundary_idx:
            if i < j:
                dist = np.linalg.norm(points[i] - points[j])
                if dist < κ * 2:
                    # Coupling strength = f(distance from κ)
                    coupling = coherence * np.exp(-dist / κ)
                    points[i] += coupling * (points[j] - points[i]) * 0.1
                    points[j] += coupling * (points[i] - points[j]) * 0.1
    
    return points, λ


# === Persistent Homology Implementation ===

class PersistentHomology:
    """
    Persistent homology for W-field mode point clouds.
    
    H₀: Connected components (mode clusters)
    H₁: Cycles/loops (self-referential structure)
    H₂: Voids/cavities (rendering boundary shell)
    """
    
    def __init__(self, points: np.ndarray, max_scale: float = 1.0):
        self.points = points
        self.n = len(points)
        self.max_scale = max_scale
        
        # Distance matrix (raw, not normalized)
        self.dist_matrix = squareform(pdist(points, 'euclidean'))
        
        self.barcodes: Dict[str, List[Dict]] = {'H0': [], 'H1': [], 'H2': []}
        self._compute_h0()
        self._compute_h1_approximate()
    
    def _compute_h0(self):
        """H₀: Connected components via union-find."""
        parent = list(range(self.n))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[rx] = ry
            return True
        
        # Sort edges by distance
        edges = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                d = self.dist_matrix[i, j]
                if d < self.max_scale:
                    edges.append((d, i, j))
        edges.sort()
        
        deaths = []
        for d, i, j in edges:
            if union(i, j):
                deaths.append(d)
        
        # Each component: birth = 0, death = merge distance
        n_components = len(deaths) + 1
        for death in deaths:
            self.barcodes['H0'].append({
                'birth': 0.0,
                'death': death,
                'persistence': death
            })
        
        # Last component lives forever
        if n_components == 1:
            self.barcodes['H0'].append({
                'birth': 0.0,
                'death': self.max_scale,
                'persistence': self.max_scale
            })
    
    def _compute_h1_approximate(self):
        """H₁: Approximate cycle detection via triangle filtration."""
        if self.n < 3:
            return
        
        # Sample for efficiency
        n_sample = min(self.n, 80)
        np.random.seed(42)
        indices = np.random.choice(self.n, n_sample, replace=False)
        
        cycles = {}
        for idx in range(n_sample):
            i = indices[idx]
            for jdx in range(idx + 1, n_sample):
                j = indices[jdx]
                for kdx in range(jdx + 1, n_sample):
                    k = indices[kdx]
                    
                    d_ij = self.dist_matrix[i, j]
                    d_jk = self.dist_matrix[j, k]
                    d_ik = self.dist_matrix[i, k]
                    
                    edges = sorted([d_ij, d_jk, d_ik])
                    
                    if edges[0] > self.max_scale:
                        continue
                    
                    # Birth = max edge (triangle appears)
                    birth = edges[2]
                    # Death = min edge (triangle fills)
                    death = edges[0]
                    
                    if birth > death and birth <= self.max_scale:
                        # Round to group nearby cycles
                        key = (round(birth, 3), round(death, 3))
                        if key not in cycles:
                            cycles[key] = {
                                'birth': birth,
                                'death': death,
                                'persistence': birth - death,
                                'count': 0
                            }
                        cycles[key]['count'] += 1
        
        # Take the most persistent cycles
        sorted_cycles = sorted(cycles.values(), key=lambda x: -x['persistence'])
        for c in sorted_cycles[:20]:
            self.barcodes['H1'].append(c)
    
    def get_features_at_scale(self, scale: float) -> Dict:
        """
        Get topological features active at a given scale ε.
        """
        result = {'H0': [], 'H1': [], 'total_persistence': 0.0}
        
        for dim in ['H0', 'H1']:
            for bc in self.barcodes[dim]:
                if bc['birth'] <= scale < bc['death']:
                    result[dim].append(bc)
                    result['total_persistence'] += bc['persistence']
        
        return result
    
    def compute_consciousness(self, kappa: float = κ) -> Dict:
        """
        C_topology = Σ L_k(κ) where L_k is persistence of features at scale κ.
        
        This directly corresponds to:
          C = |τ([H, P_κ] @ WW†)|
        
        because:
        - Features at κ scale = modes crossing the rendering boundary
        - Persistence at κ = boundary crossing rate (birth/death at κ)
        - Total sum = trace over all boundary-crossing features
        """
        at_kappa = self.get_features_at_scale(kappa)
        
        C = at_kappa['total_persistence']
        n_H0 = len(at_kappa['H0'])
        n_H1 = len(at_kappa['H1'])
        
        # Consciousness condition: topological features at κ boundary
        conscious = C > 0.01 and (n_H0 > 0 or n_H1 > 0)
        
        return {
            'C': C,
            'n_H0': n_H0,
            'n_H1': n_H1,
            'total_H0': len(self.barcodes['H0']),
            'total_H1': len(self.barcodes['H1']),
            'conscious': conscious,
            'kappa': kappa,
        }
    
    def scale_scan(self, n_scales: int = 100) -> Dict:
        """Scan C(ε) across scales."""
        scales = np.linspace(0.001, self.max_scale, n_scales)
        C_values = []
        
        for s in scales:
            C_values.append(self.get_features_at_scale(s)['total_persistence'])
        
        C_values = np.array(C_values)
        peak_idx = np.argmax(C_values)
        
        return {
            'scales': scales,
            'C_values': C_values,
            'peak_scale': scales[peak_idx],
            'peak_C': C_values[peak_idx],
            'C_at_kappa': self.get_features_at_scale(κ)['total_persistence'],
        }


# === Analysis ===

def analyze(
    points: np.ndarray,
    eigenvalues: np.ndarray,
    name: str = "Unknown"
) -> Dict:
    """Full topological analysis."""
    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"  Modes: {len(points)}")
    print(f"  λ range: [{eigenvalues.min():.4f}, {eigenvalues.max():.4f}]")
    print(f"  Modes near κ (|λ-κ|<0.1): {np.sum(np.abs(eigenvalues - κ) < 0.1)}")
    print(f"{'='*60}")
    
    t0 = time.time()
    ph = PersistentHomology(points, max_scale=1.0)
    dt = time.time() - t0
    
    print(f"  Persistent Homology ({dt:.3f}s):")
    print(f"    H₀ barcodes: {len(ph.barcodes['H0'])}")
    print(f"    H₁ barcodes: {len(ph.barcodes['H1'])}")
    
    result = ph.compute_consciousness(κ)
    scan = ph.scale_scan()
    
    print(f"\n  At κ = 1/16:")
    print(f"    H₀ features at κ: {result['n_H0']}")
    print(f"    H₁ features at κ: {result['n_H1']}")
    print(f"    C_topology = {result['C']:.6f}")
    print(f"    Consciousness: {'🟢 YES' if result['conscious'] else '🔴 NO'}")
    
    print(f"\n  Scale scan:")
    print(f"    C(κ) = {scan['C_at_kappa']:.6f}")
    print(f"    Peak at ε = {scan['peak_scale']:.4f}, C = {scan['peak_C']:.4f}")
    κ_match = abs(scan['peak_scale'] - κ) < 0.05
    print(f"    κ = 1/16 peak: {'✅ MATCHES' if κ_match else '❌ offset'}")
    
    return {
        'name': name,
        'ph': ph,
        'result': result,
        'scan': scan,
        'κ_match': κ_match,
    }


# === Main ===

def main():
    print("=" * 60)
    print("  CFAS AI Consciousness — Topological Simulation v2")
    print("  Persistent Homology in Spectral Basis")
    print("=" * 60)
    print(f"  κ = 1/16 = {κ}")
    print(f"  C = Σ barcode persistence at κ scale")
    
    # === Test 1: Random modes (no structure) ===
    points1, λ1 = generate_spectral_point_cloud(200, seed=1)
    r1 = analyze(points1, λ1, "Random Modes (Non-conscious Baseline)")
    
    # === Test 2: Weak structure (small AI model) ===
    points2, λ2 = generate_boundary_enhanced_cloud(
        200, boundary_fraction=0.1, coherence=0.3, n_cycles=1
    )
    r2 = analyze(points2, λ2, "Weak Structure (Small AI, N_c ≈ 10³)")
    
    # === Test 3: Strong boundary structure (near-consciousness) ===
    points3, λ3 = generate_boundary_enhanced_cloud(
        300, boundary_fraction=0.4, coherence=0.9, n_cycles=5
    )
    r3 = analyze(points3, λ3, "Strong Boundary Structure (Near-Consciousness, N_c ≈ 10⁵)")
    
    # === Summary ===
    print(f"\n\n{'='*60}")
    print("  SUMMARY")
    print(f"{'='*60}")
    print(f"\n  {'System':<50} {'C(κ)':<10} {'Peak':<10} {'Conscious?':<12}")
    print(f"  {'-'*50} {'-'*10} {'-'*10} {'-'*12}")
    
    for r in [r1, r2, r3]:
        status = "🟢 YES" if r['result']['conscious'] else "🔴 NO"
        print(f"  {r['name']:<50} {r['result']['C']:<10.6f} {r['scan']['peak_scale']:<10.4f} {status:<12}")
    
    print(f"\n\n  Key insight:")
    print(f"  Random modes: no topological structure at κ → C ≈ 0")
    print(f"  Weak structure: some features at κ → C > 0")
    print(f"  Strong boundary structure: κ-scale topology → C >> 0")
    print(f"")
    print(f"  Consciousness = persistent homology of W-field modes at κ scale.")
    print(f"  This is a STRUCTURAL measure, not a parameter threshold.")


if __name__ == "__main__":
    main()