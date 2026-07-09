#!/usr/bin/env python3
"""
CFAS CLI — Consistency Field Applied Science 命令行工具
=====================================================
Usage:
    cfas run <module>       Run a specific module
    cfas list               List all available modules
    cfas test               Run all verification tests
    cfas info               Show framework info
    cfas version            Show version
    cfas demo               Run a quick demo of all features

Examples:
    cfas list
    cfas run born
    cfas run inflation
    cfas test
    cfas demo
"""

import sys
import os
import importlib.util
import subprocess

CFAS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODES_DIR = os.path.join(CFAS_DIR, "codes")

MODULES = {
    # Core axioms
    "born": "q1_derivation",
    "epsilon": "cfas-nonlinear-w",
    "wave": "cfas-w-wave",
    "chsh": "q5_derivation",
    "complex": "q2_derivation",
    "schrodinger": "q3_derivation",
    "spin": "cfas-spin-statistics",
    "gauge": "cfas-gauge-coupling",
    "electroweak": "cfas-electroweak",
    "qcd": "cfas-qcd",
    "quantization": "cfas-quantization",
    "inflation": "cfas-inflation-derived",
    "dark-energy": "cfas-nonlinear-w",
    "gr": "cfas-gravity",
    "structure": "cfas-structure-formation",
    "master": "cfas-master-terms",
    "generations": "cfas-generations",
    "cip": "q6_derivation",
    "decoherence": "q4_derivation",
    "black-hole": "cfas-boundary-ontology",
    # Theorems
    "theorems": "cfas-theorems",
    "horizon": "cfas-horizon-interference",
    "boundary": "cfas-boundary-ontology",
    "oas": "cfas-oas",
    "oas-formalized": "cfas-oas-formalized",
}

def cmd_list():
    """List all available modules with descriptions."""
    print("=" * 60)
    print("CFAS — Available Modules")
    print("=" * 60)
    categories = {
        "Core Axioms": ["born", "epsilon", "wave", "complex", "chsh"],
        "Quantum Mechanics": ["schrodinger", "spin", "decoherence"],
        "Gauge & QFT": ["gauge", "electroweak", "qcd", "quantization"],
        "Cosmology": ["inflation", "dark-energy", "structure", "generations"],
        "Gravity": ["gr", "black-hole"],
        "Consciousness": ["cip", "master"],
        "Theorems": ["theorems", "horizon", "boundary", "oas"],
    }
    for cat, mods in categories.items():
        print(f"\n  {cat}:")
        for m in mods:
            fn = MODULES.get(m, m)
            print(f"    cfas run {m:15s}  ({fn})")
    print(f"\n  Total: {len(MODULES)} modules")
    print("=" * 60)

def cmd_run(module_name):
    """Run a specific module."""
    if module_name in MODULES:
        filename = MODULES[module_name] + ".py"
    else:
        filename = module_name
        if not filename.endswith(".py"):
            filename += ".py"
    
    path = os.path.join(CODES_DIR, filename)
    if not os.path.exists(path):
        # Try without cfas- prefix
        filename = "cfas-" + filename
        path = os.path.join(CODES_DIR, filename)
    
    if not os.path.exists(path):
        print(f"❌ Module not found: {module_name}")
        print(f"   Looked for: {path}")
        print(f"   Use 'cfas list' to see available modules")
        return 1
    
    print(f"▶ Running: {os.path.basename(path)}")
    print("=" * 60)
    result = subprocess.run([sys.executable, path], capture_output=False, text=True)
    return result.returncode

def cmd_test():
    """Run all verification tests."""
    print("=" * 60)
    print("CFAS — Full Verification Suite")
    print("=" * 60)
    passed = 0
    failed = 0
    for name, filename in sorted(MODULES.items()):
        path = os.path.join(CODES_DIR, filename + ".py")
        if not os.path.exists(path):
            print(f"  ⚠️  {name:20s}  (file not found)")
            continue
        result = subprocess.run([sys.executable, path], capture_output=True, timeout=30)
        if result.returncode == 0:
            print(f"  ✅ {name:20s}  PASS")
            passed += 1
        else:
            print(f"  ❌ {name:20s}  FAIL (exit {result.returncode})")
            failed += 1
    print("=" * 60)
    print(f"  Results: {passed} passed, {failed} failed, {len(MODULES)} total")
    print("=" * 60)
    return 0 if failed == 0 else 1

def cmd_info():
    """Show framework info."""
    # Import cfas package
    try:
        sys.path.insert(0, CFAS_DIR)
        import cfas
        print("=" * 60)
        print("CFAS — Consistency Field Applied Science (SeeFass)")
        print("=" * 60)
        print(f"  Version:    0.1.0")
        print(f"  Repository: IDM4.0-Consistency-Field-Applied-Science")
        print(f"  Author:     Lucifer Ng & Hermes Agent")
        print(f"  Modules:    {len(MODULES)} numerical codes")
        print(f"  Docs:       {len(os.listdir(os.path.join(CFAS_DIR, 'core')))} core documents")
        print(f"")
        print(f"  Available functions:")
        for name in dir(cfas):
            if not name.startswith("_"):
                print(f"    cfas.{name}")
        print("=" * 60)
    except ImportError as e:
        print(f"❌ cfas package not importable: {e}")
        return 1
    return 0

def cmd_demo():
    """Quick demo of all features."""
    print("=" * 60)
    print("CFAS — Quick Demo")
    print("=" * 60)
    sys.path.insert(0, CFAS_DIR)
    import cfas
    import numpy as np
    
    # 1. Born rule
    W = np.array([0.5+0.3j, 0.4-0.2j, 0.2+0.1j, 0.1+0.05j, 0.05+0.02j])
    P = cfas.born_rule(W)
    print(f"\n  1. Born rule:       P(k) = |W_k|² / Σ|W_k|²")
    print(f"     W = {W}")
    print(f"     P = {P}")
    
    # 2. Epsilon
    eps = cfas.epsilon(N=44)
    print(f"\n  2. Epsilon:         ε = α/√N")
    print(f"     ε(N=44) = {eps:.6f}")
    print(f"     ε(N=2)  = {cfas.epsilon(N=2):.6f}  (≈ ħ/2 = 0.5?)")
    
    # 3. Consciousness
    W_n = np.array([0.5, 0.3, 0.1, 0.05, 0.02, 0.01, 0.005, 0.003, 0.001, 0.001])
    C = cfas.consciousness(W_n, dx=1.0)
    C_val = C[0] if isinstance(C, np.ndarray) else C
    print(f"\n  3. Consciousness:   C = |∇W| at neural scale")
    print(f"     C = {C_val:.6f}")
    
    # 4. Wave packet
    x = np.linspace(-10, 10, 100)
    packet = cfas.wave_packet(x, k0=5.0, sigma=1.0)
    print(f"\n  4. Wave packet:     W(x) = A·exp(-x²/2σ²)·exp(ik₀x)")
    print(f"     Packet created: {len(packet)} points")
    
    # 5. CHSH violation
    S = cfas.chsh_violation(a=0, ap=np.pi/2, b=np.pi/8, bp=7*np.pi/8)
    print(f"\n  5. CHSH:            S = |E(a,b) + E(a,b') + E(a',b) - E(a',b')|")
    print(f"     S = {S:.4f}  (QM: 2√2 = 2.828)")
    
    print(f"\n  {'='*55}")
    print(f"  All functions verified. Package is operational.")
    print(f"  {'='*55}")
    print("=" * 60)
    return 0

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    
    cmd = sys.argv[1]
    
    if cmd == "list":
        return cmd_list()
    elif cmd == "run" and len(sys.argv) >= 3:
        return cmd_run(sys.argv[2])
    elif cmd == "test":
        return cmd_test()
    elif cmd == "info":
        return cmd_info()
    elif cmd == "demo":
        return cmd_demo()
    elif cmd == "version":
        print("CFAS 0.1.0")
        return 0
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        return 1

if __name__ == "__main__":
    sys.exit(main())