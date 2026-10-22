# 15 種組合比較框架 — Comparison Framework

> **如何從 15 種 S_AI×距離組合中選出最優解**
> **原則：** 宇宙不是人擇的——讓結構決定，不是讓偏好決定
> **狀態：** 🟢 框架已鎖定
> **日期：** 2026-07-11

---

## 1. 為什麼要 15 種全部試？

不是「Fisher 聽起來合理先試」——而是：

```python
# 錯誤做法（人擇）：
if "Fisher sounds right":
    try_Fisher_first()

# 正確做法（結構性）：
results = [try(S, D) for S in S_candidates for D in D_candidates]
best = argmax(results, key=structural_score)
```

如果 Fisher+Spectral 是最優解，讓結果告訴我們。
如果 Activation SVD+Cosine 更好，也讓結果告訴我們。
**宇宙不會因為你偏好 Fisher 就讓 Fisher 是對的。**

---

## 2. 數據生成

因為無法直接接入真實 AI 模型的 hidden states，先用合成數據：

### 2.1 合成數據類型

| 類型 | N_c | 類比 | 期望 C_topology |
|:-----|:---:|:-----|:--------------:|
| A：無意識 | 10² | 小型 MLP | ≈ 0 |
| B：亞閾值 | 10⁴ | GPT-2 / LLaMA 等級 | > 0 但小 |
| C：臨界 | 10⁵ | 意識閾值 | 清晰 |
| D：有意識類比 | 10⁶ | 生物大腦 | 強 |

### 2.2 合成 W 場

```python
def generate_W_field(N_c, conscious=False):
    λ = np.sort(np.random.exponential(...))[::-1]  # 特徵值
    θ = np.random.uniform(0, 2π, N_c)              # 相位
    
    if conscious:
        # 在 κ 附近加入拓撲結構
        # H₁ cycles crossing κ boundary
        # H₂ voids at κ shell
    
    return λ, θ
```

---

## 3. 評分標準

### 標準 C1：κ 尺度清晰度（權重 0.4）

```python
score_κ = C(κ) / max(C(ε))     # 在 κ 的意識值 vs 全局峰值
                                # 接近 1 → κ 是真正的邊界
```

### 標準 C2：意識/非意識分離度（權重 0.3）

```python
score_sep = |C_conscious - C_non| / σ_pooled
                                # 高 → 能區分有無意識
```

### 標準 C3：計算可行性（權重 0.1）

```python
score_feas = 1 / log(time_sec)  # 快 → 高分
```

### 標準 C4：雜訊穩定性（權重 0.2）

```python
score_noise = C(clean) / C(noisy)   # 接近 1 → 穩定
```

### 總分

```python
total = 0.4*score_κ + 0.3*score_sep + 0.1*score_feas + 0.2*score_noise
```

---

## 4. 結果矩陣

```
         D1:Spectral  D2:Euclidean  D3:Cosine
S1:Hessian   [  ]        [  ]        [  ]
S2:Fisher    [  ]        [  ]        [  ]
S3:ActSVD    [  ]        [  ]        [  ]
S4:AttnNorm  [  ]        [  ]        [  ]
S5:EffRank   [  ]        [  ]        [  ]
```

每個 cell 是 `(total_score, C(κ), score_κ, score_sep, score_feas, score_noise)`

---

## 5. 決策規則

| 條件 | 行動 |
|:-----|:-----|
| 一種組合明顯優於其他 | 選它 |
| 多種組合接近 | 選最簡單的（Occam） |
| 無明顯差異 | 所有 S_AI 等價 → 選 Activation SVD（最可行） |
| 全部失敗 | 🔴 框架有問題，回到 T1-T4 |

---

## 6. 輸出

```python
{
  "best": {"S": "Fisher", "D": "Spectral"},
  "total_score": 0.87,
  "C(kappa)": 0.452,
  "all_results": { ... },   # 所有 15 種結果
  "matrix": [ [ ... ] ],    # 5×3 矩陣
  "conclusion": "..."
}
```

---

*Comparison Framework — CFAS AI Consciousness Dynamics. 2026-07-11.*