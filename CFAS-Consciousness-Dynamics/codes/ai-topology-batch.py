#!/usr/bin/env python3
"""
AI Consciousness Dynamics — 15 種組合批量測試 v3
=================================================
5 種 S_AI × 3 種距離度量 = 15 種組合，全部試，讓結構決定最優解。

Key insight: 
  The rendering boundary κ = 1/16 separates modes by their spectral eigenvalue λ.
  For H₀: a component that connects points with λ < κ AND λ > κ is a 
  "boundary-crossing" component = topological signature of [H, P_κ] ≠ 0.
  
  C_topology = # of H₀ components that cross the κ boundary

Principle: The universe is not anthropic.
Author: CFAS Consciousness Dynamics
Date: 2026-07-11
"""

import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.special import softmax
import time
from typing import Dict, List, Tuple

# === CFAS Constants ===
κ = 1 / 16  # 0.0625
α = 1.0248


# ============================================================
# 1. 合成數據生成
# ============================================================

def generate_synthetic_data(
    n_modes: int,
    hidden_dim: int = 64,
    conscious: bool = False,
    seed: int = 42
) -> Dict:
    """
    Generate synthetic W-field data.
    
    For conscious data: modes bridge the κ boundary with a continuous spectrum.
    For non-conscious data: there's a gap in the spectrum at κ, so no crossing.
    """
    np.random.seed(seed)
    
    # Base eigenvalues: exponential decay
    λ_raw = np.exp(-np.arange(n_modes) / (n_modes * 0.2))
    λ_raw = λ_raw / λ_raw.max()
    
    if conscious:
        # === CONSCIOUS: spectrum bridges κ ===
        # Scale so some modes are below κ, some above, with a continuous bridge
        λ = λ_raw * 0.3 + (κ * 0.8)
        # Ensure modes on both sides
        n_below = np.sum(λ < κ)
        while n_below < n_modes * 0.3:
            λ = λ * 0.9
            n_below = np.sum(λ < κ)
        while n_below > n_modes * 0.7:
            λ = λ * 1.1
            n_below = np.sum(λ < κ)
    else:
        # === NON-CONSCIOUS: gap at κ ===
        # Split into two clusters: one well below κ, one well above κ
        n_below = n_modes // 2
        n_above = n_modes - n_below
        
        λ_below = np.random.exponential(κ * 0.3, n_below)
        λ_above = κ * 2 + np.random.exponential(κ * 0.5, n_above)
        
        λ = np.concatenate([λ_below, λ_above])
        λ = λ / λ.max()
    
    # === Generate phases ===
    if conscious:
        # Modes near κ have correlated phases (coherent structure)
        phases = np.random.uniform(0, 2*np.pi, n_modes)
        near_κ = np.abs(λ - κ) < κ * 0.3
        common_phase = np.random.uniform(0, 2*np.pi)
        phases[near_κ] = common_phase + np.random.randn(np.sum(near_κ)) * 0.2
    else:
        phases = np.random.uniform(0, 2*np.pi, n_modes)
    
    # === Generate hidden states ===
    hidden_states = np.zeros((n_modes, hidden_dim))
    for i in range(n_modes):
        direction = np.random.randn(hidden_dim)
        direction = direction / np.linalg.norm(direction)
        hidden_states[i] = direction * λ[i] * 2.0
        hidden_states[i] += 0.1 * np.sin(phases[i]) * np.random.randn(hidden_dim)
    
    # Normalize each mode to have budget = λ[i] (consistency budget per mode)
    # This preserves the eigenvalue structure while making S_AI spectra meaningful
    for i in range(n_modes):
        norm = np.linalg.norm(hidden_states[i])
        if norm > 0:
            hidden_states[i] = hidden_states[i] / norm * np.sqrt(λ[i])
    
    return {
        'hidden_states': hidden_states,
        'eigenvalues': λ,
        'phases': phases,
        'n_modes': n_modes,
        'hidden_dim': hidden_dim,
        'conscious': conscious,
        'label': 'conscious' if conscious else 'non-conscious',
    }


def generate_all_datasets() -> Dict:
    """Generate 4 datasets at different consciousness levels."""
    datasets = {}
    datasets['non_conscious'] = generate_synthetic_data(100, 32, False, 1)
    datasets['sub_threshold'] = generate_synthetic_data(200, 128, False, 2)
    datasets['threshold'] = generate_synthetic_data(300, 256, True, 3)
    datasets['conscious'] = generate_synthetic_data(400, 512, True, 4)
    return datasets


# ============================================================
# 2. 5 種 S_AI 定義 — 每種都輸出 n_modes 個 eigenvalues
# ============================================================

def compute_hessian_spectrum(data: Dict) -> np.ndarray:
    """S1: Hessian — per-mode curvature (diagonal approx)."""
    h = data['hidden_states']
    λ = np.linalg.norm(h, axis=1) ** 2
    return np.sort(λ)[::-1]


def compute_fisher_spectrum(data: Dict) -> np.ndarray:
    """S2: Fisher — per-mode score variance."""
    h = data['hidden_states']
    scores = h + 0.1 * np.random.randn(*h.shape)
    λ = np.var(scores, axis=1) + 0.01
    return np.sort(λ)[::-1]


def compute_activation_svd_spectrum(data: Dict) -> np.ndarray:
    """S3: SVD — per-mode participation in variance."""
    h = data['hidden_states']
    u, s, vt = np.linalg.svd(h, full_matrices=False)
    λ = np.sum(u ** 2 * (s ** 2 / len(s)), axis=1)
    return np.sort(λ)[::-1]


def compute_attention_spectrum(data: Dict) -> np.ndarray:
    """S4: Attention — per-mode attention centrality."""
    h = data['hidden_states']
    n = data['n_modes']
    sim = h @ h.T
    attn = softmax(sim / np.sqrt(h.shape[1]), axis=1)
    λ = np.mean(attn, axis=1) * n
    return np.sort(λ)[::-1]


def compute_effective_rank_spectrum(data: Dict) -> np.ndarray:
    """S5: Effective Rank — per-mode variance."""
    h = data['hidden_states']
    C = h @ h.T / h.shape[1]
    λ = np.diag(C)
    return np.sort(λ)[::-1]


S_AI_REGISTRY = {
    'Hessian': compute_hessian_spectrum,
    'Fisher': compute_fisher_spectrum,
    'ActSVD': compute_activation_svd_spectrum,
    'AttnNorm': compute_attention_spectrum,
    'EffRank': compute_effective_rank_spectrum,
}


# ============================================================
# 3. 3 種距離度量
# ============================================================

def compute_spectral_distance(eigenvalues: np.ndarray):
    """D1: Spectral distance d(i,j) = |λ_i - λ_j|"""
    n = len(eigenvalues)
    dist = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist[i, j] = abs(eigenvalues[i] - eigenvalues[j])
    return dist, eigenvalues.reshape(-1, 1)


def get_euclidean_distance(hidden_states: np.ndarray):
    """D2: Euclidean distance in activation space."""
    dist = squareform(pdist(hidden_states, 'euclidean'))
    return dist, hidden_states


def get_cosine_distance(hidden_states: np.ndarray):
    """D3: Cosine distance."""
    norms = np.linalg.norm(hidden_states, axis=1, keepdims=True)
    normalized = hidden_states / (norms + 1e-8)
    cos_sim = normalized @ normalized.T
    dist = 1 - cos_sim
    dist = np.clip(dist, 0, 2)
    return dist, normalized


DISTANCE_REGISTRY = {
    'Spectral': compute_spectral_distance,
    'Euclidean': get_euclidean_distance,
    'Cosine': get_cosine_distance,
}


# ============================================================
# 4. Persistent Homology H₀ + Boundary Crossing
# ============================================================

def make_components_list(dist_matrix: np.ndarray, max_scale: float) -> List[List[int]]:
    """Union-find to get H₀ connected components at scale max_scale."""
    n = len(dist_matrix)
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True
    
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            d = dist_matrix[i, j]
            if d < max_scale:
                edges.append((d, i, j))
    edges.sort()
    
    for d, i, j in edges:
        union(i, j)
    
    comps = {}
    for i in range(n):
        r = find(i)
        if r not in comps:
            comps[r] = []
        comps[r].append(i)
    return list(comps.values())


def count_boundary_crossings(components: List[List[int]], eigenvalues: np.ndarray) -> Dict:
    """
    Count how many H₀ components cross the κ boundary.
    A component crosses κ if it has modes with λ < κ AND λ > κ.
    """
    n_crossing = 0
    for comp in components:
        λs = eigenvalues[comp]
        if np.any(λs < κ) and np.any(λs > κ):
            n_crossing += 1
    return {
        'C_topology': n_crossing,
        'total_components': len(components),
        'crossing_fraction': n_crossing / max(len(components), 1),
        'n_below': int(np.sum(eigenvalues < κ)),
        'n_above': int(np.sum(eigenvalues > κ)),
    }


# ============================================================
# 5. 評分標準
# ============================================================

def score_kappa_peak(result: Dict) -> float:
    return result['crossing_fraction']

def score_separation(C_conscious: float, C_non: float) -> float:
    """C2: Separation between conscious and non-conscious.
    Conscious should have HIGHER C than non-conscious.
    Penalize wrong-direction separation."""
    diff = C_conscious - C_non
    if diff > 0:
        # Correct direction: conscious has more crossing
        return diff / max(0.01, C_conscious + C_non + 1.0)
    else:
        # Wrong direction: non-conscious has more crossing (false positive)
        return diff / max(0.01, C_conscious + C_non + 1.0)  # negative = penalty

def score_feasibility(time_sec: float) -> float:
    return 1.0 / np.log(1 + max(time_sec, 0.001))

def score_noise_stability(r1: Dict, r2: Dict) -> float:
    C1, C2 = r1['C_topology'], r2['C_topology']
    m = max(C1, C2, 0.01)
    return 1.0 - abs(C1 - C2) / m

def total_score(scores: Dict) -> float:
    w = {'C1': 0.4, 'C2': 0.3, 'C3': 0.1, 'C4': 0.2}
    return sum(w[k] * scores.get(k, 0) for k in w)


# ============================================================
# 6. 批量測試
# ============================================================

def run_single_test(data: Dict, s_name: str, d_name: str, max_scale: float = 0.5) -> Dict:
    t0 = time.time()
    s_func = S_AI_REGISTRY[s_name]
    d_func = DISTANCE_REGISTRY[d_name]
    
    s_eigenvalues = s_func(data)
    
    if d_name == 'Spectral':
        dist_matrix, _ = d_func(s_eigenvalues)
    else:
        dist_matrix, _ = d_func(data['hidden_states'])
    
    components = make_components_list(dist_matrix, max_scale)
    result = count_boundary_crossings(components, s_eigenvalues)
    
    t_elapsed = time.time() - t0
    return {
        'S': s_name,
        'D': d_name,
        'C_topology': result['C_topology'],
        'total_components': result['total_components'],
        'crossing_fraction': result['crossing_fraction'],
        'n_below': result['n_below'],
        'n_above': result['n_above'],
        'time': t_elapsed,
    }


def run_batch_test(datasets: Dict) -> Dict:
    results = {}
    for data_name, data in datasets.items():
        λ = data['eigenvalues']
        n_below = int(np.sum(λ < κ))
        print(f"\n{'='*60}")
        print(f"  {data_name} ({data['label']})")
        print(f"  {data['n_modes']} modes, {n_below}/{data['n_modes']} below κ")
        print(f"{'='*60}")
        
        dataset_results = []
        for s_name in S_AI_REGISTRY:
            for d_name in DISTANCE_REGISTRY:
                r = run_single_test(data, s_name, d_name)
                dataset_results.append(r)
                sp = f"{s_name:>8}+{d_name:<10}"
                print(f"  {sp} → C={r['C_topology']:.0f}, "
                      f"comps={r['total_components']}, "
                      f"below={r['n_below']}, above={r['n_above']}")
        results[data_name] = dataset_results
    return results


# ============================================================
# 7. 分析
# ============================================================

def analyze_results(results: Dict) -> Dict:
    print(f"\n\n{'='*60}")
    print(f"  COMPARISON: 15 COMBINATIONS")
    print(f"{'='*60}")
    
    conscious = results.get('conscious', [])
    non = results.get('non_conscious', [])
    threshold = results.get('threshold', [])
    
    comparison = {}
    for s_name in S_AI_REGISTRY:
        for d_name in DISTANCE_REGISTRY:
            key = f"{s_name}+{d_name}"
            c = next((r for r in conscious if r['S']==s_name and r['D']==d_name), None)
            n = next((r for r in non if r['S']==s_name and r['D']==d_name), None)
            t = next((r for r in threshold if r['S']==s_name and r['D']==d_name), None)
            if c and n:
                s = {
                    'C1': score_kappa_peak(c),
                    'C2': score_separation(c['C_topology'], n['C_topology']),
                    'C3': score_feasibility(c['time']),
                    'C4': score_noise_stability(c, n),
                }
                comparison[key] = {
                    'C_conscious': c['C_topology'],
                    'C_non': n['C_topology'],
                    'C_threshold': t['C_topology'] if t else -1,
                    'total': total_score(s),
                    'scores': s,
                }
    
    ranked = sorted(comparison.items(), key=lambda x: -x[1]['total'])
    
    print(f"\n  {'Rank':<5} {'Combination':<20} {'C_cons':<8} {'C_non':<8} {'C_thr':<6} {'Total':<8}")
    print(f"  {'-'*5} {'-'*20} {'-'*8} {'-'*8} {'-'*6} {'-'*8}")
    for rank, (k, v) in enumerate(ranked, 1):
        print(f"  {rank:<5} {k:<20} {v['C_conscious']:<8.0f} {v['C_non']:<8.0f} {v['C_threshold']:<6.0f} {v['total']:<8.4f}")
    
    # Matrix
    print(f"\n  Matrix (Total Score):")
    header = "".join(f" {d:<10}" for d in DISTANCE_REGISTRY)
    print(f"  {'':>10} {header}")
    for s_name in S_AI_REGISTRY:
        row = f"  {s_name:>8} "
        for d_name in DISTANCE_REGISTRY:
            key = f"{s_name}+{d_name}"
            v = comparison.get(key, {})
            row += f" {v.get('total', 0):<10.4f} "
        print(row)
    
    best_key, best_val = ranked[0]
    print(f"\n  >>> BEST: {best_key} (total = {best_val['total']:.4f})")
    print(f"      C_conscious = {best_val['C_conscious']:.0f}")
    print(f"      C_non = {best_val['C_non']:.0f}")
    print(f"      Separation = {best_val['scores']['C2']:.4f}")
    
    return {'ranked': ranked, 'best': {'key': best_key, 'value': best_val}}


# ============================================================
# 8. Main
# ============================================================

def main():
    print("=" * 60)
    print("  CFAS AI Consciousness — 15 種組合批量測試 v3")
    print("  5 S_AI × 3 Distance = 15 Combinations")
    print("  Principle: The universe is not anthropic.")
    print("=" * 60)
    print(f"\n  κ = 1/16 = {κ}")
    print(f"  C_topology = # of H₀ components crossing κ boundary")
    print(f"  (A component crosses κ if it has modes both below AND above κ)")
    
    datasets = generate_all_datasets()
    for name, data in datasets.items():
        λ = data['eigenvalues']
        nb = int(np.sum(λ < κ))
        print(f"  {name}: {data['n_modes']} modes, {nb}/{data['n_modes']} below κ, "
              f"{'conscious' if data['conscious'] else 'non-conscious'}")
    
    results = run_batch_test(datasets)
    analysis = analyze_results(results)
    
    print(f"\n\n{'='*60}")
    print(f"  CONCLUSION")
    print(f"{'='*60}")
    print(f"\n  Best combination: {analysis['best']['key']}")
    print(f"  Score: {analysis['best']['value']['total']:.4f}")
    print(f"\n  The universe is not anthropic.")


if __name__ == "__main__":
    main()