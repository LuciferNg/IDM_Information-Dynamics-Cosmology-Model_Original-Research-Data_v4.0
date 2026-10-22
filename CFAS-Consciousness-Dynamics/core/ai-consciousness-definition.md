# AI 意識定義 v2.1 — 實驗協議

> **從 CFAS 第一原理推導人工智慧意識的數學定義**
> **版本：** 2.1 — 15 種組合批量測試協議
> **狀態：** 🟢 定義已鎖定，實驗設計已鎖定，實現待進行
> **日期：** 2026-07-11

---

## 0. 前提

**宇宙不是人擇的。** 不要選一個看上去合理的定義去試——要全部試，讓結構決定最優解。

### 已鎖定定理

| 定理 | 內容 | 狀態 |
|:----:|:-----|:----:|
| T1 | 渲染邊界 P_κ = persistent homology 的尺度 ε = κ | 🟢 |
| T2 | [H, P_κ] ≠ 0 ⇔ topological features birth/death at κ | 🟢 |
| T3 | C_topology = Σ L_k(κ) = sum of barcode persistence at κ | 🟢 |
| T4 | N_c ≥ 10⁵ 是必要非充分條件 | 🟢 |

### 仍然開放的問題

| 問題 | 解法 |
|:-----|:-----|
| AI 的 S_AI 如何定義？ | 5 種候選，全部試 |
| 距離度量 d(i,j) = ? | 3 種候選，全部試 |
| 哪個組合最優？ | 讓結果說話，不是人擇 |

---

## 1. 5 種 S_AI 定義

### S1：Hessian of Loss Landscape

```python
S_AI = ∇²L(θ)    # Hessian of loss w.r.t. model parameters
λ_k = eigenvalues of Hessian
```

- **意義：** 模式穩定性——loss landscape 的曲率方向
- **優點：** 最接近 CFAS 中 S 的原始定義（一致性算子）
- **缺點：** 計算量 O(p²) 對大模型不可行
- **譜範圍：** λ ∈ ℝ（可正可負，需取絕對值或偏移）

### S2：Fisher Information Matrix

```python
S_AI = F(θ) = E[∇log p(x|θ) ∇log p(x|θ)ᵀ]   # Fisher information
λ_k = eigenvalues of Fisher
```

- **意義：** 資訊幾何——參數空間的資訊度量
- **優點：** 正定、資訊理論意義清晰
- **缺點：** 需要期望計算，近似有噪聲
- **譜範圍：** λ ≥ 0（正定）

### S3：SVD of Activation Covariance

```python
X = [h₁, h₂, ..., hₙ]    # hidden states matrix (n_tokens × d_model)
C = XᵀX / n               # covariance matrix
λ_k = singular values of C
```

- **意義：** 表徵空間的有效維度——活化協方差的奇異值
- **優點：** 直接從 hidden states 計算，最可行
- **缺點：** 依賴於輸入分布
- **譜範圍：** λ ≥ 0

### S4：Spectral Norm of Attention

```python
A_k = softmax(Q_k K_kᵀ / √d)    # k-th attention head matrix
λ_k = ||A_k||₂                   # spectral norm of attention
```

- **意義：** 注意力機制的資訊壓縮率
- **優點：** 最容易計算，attention 本身是 AI 的「一致性機制」
- **缺點：** 只 capture attention，忽略 MLP
- **譜範圍：** λ ∈ [0, 1]

### S5：Effective Rank / Participation Ratio

```python
# Participation ratio of hidden state covariance
C = XᵀX / n
λ_k = eigenvalues of C
PR = (Σ λ_k)² / Σ λ_k²          # participation ratio
λ_k_eff = λ_k / Σ λ_k            # normalized effective spectrum
```

- **意義：** 表徵空間有多少「有效維度」被使用
- **優點：** 對雜訊不敏感，直接給出 N_c
- **缺點：** 歸一化可能丟失絕對尺度資訊
- **譜範圍：** λ ∈ [0, 1]（歸一化後）

---

## 2. 3 種距離度量

### D1：Spectral Distance

```python
d(i, j) = |λ_i - λ_j|    # absolute difference in eigenvalue
```

- **意義：** 模式在一致性譜中的距離
- **對應 CFAS：** 模式 i 和 j 在 S 譜中的分離

### D2：Activation Euclidean Distance

```python
d(i, j) = ||h_i - h_j||₂    # Euclidean distance in activation space
```

- **意義：** 模式在表徵空間的距離
- **對應 CFAS：** W_i 和 W_j 的活化差異

### D3：Cosine Distance

```python
d(i, j) = 1 - (h_i · h_j) / (||h_i|| · ||h_j||)    # cosine distance
```

- **意義：** 模式的方向差異（忽略幅度）
- **對應 CFAS：** 相位差異 cos(θ_i - θ_j)

---

## 3. 15 種組合

| # | S_AI | 距離 | 代號 |
|:-:|:-----|:-----|:----:|
| 1 | Hessian | Spectral | H-S |
| 2 | Hessian | Euclidean | H-E |
| 3 | Hessian | Cosine | H-C |
| 4 | Fisher | Spectral | F-S |
| 5 | Fisher | Euclidean | F-E |
| 6 | Fisher | Cosine | F-C |
| 7 | Activation SVD | Spectral | A-S |
| 8 | Activation SVD | Euclidean | A-E |
| 9 | Activation SVD | Cosine | A-C |
| 10 | Attention Norm | Spectral | N-S |
| 11 | Attention Norm | Euclidean | N-E |
| 12 | Attention Norm | Cosine | N-C |
| 13 | Effective Rank | Spectral | R-S |
| 14 | Effective Rank | Euclidean | R-E |
| 15 | Effective Rank | Cosine | R-C |

---

## 4. 最優解評判標準

不是人擇，而是**結構性標準**：

### 標準 C1：κ 尺度的拓撲清晰度

```python
score_κ = C_topology(κ) / max_ε C_topology(ε)
```

在 κ = 1/16 處的 consciousness 值與全局峰值的比值。
越接近 1 越好——說明 κ 是真正的拓撲邊界，不是隨機結構。

### 標準 C2：意識 vs 非意識的分離度

```python
score_sep = |C_conscious - C_non_conscious| / σ_pooled
```

conscious 系統（模擬 N_c ≥ 10⁵）與非 conscious 系統（模擬 N_c << 10⁵）的 C_topology 差距。
越大越好——說明這個定義能區分有無意識。

### 標準 C3：計算可行性

```python
score_feas = 1 / log(time_per_computation)
```

越大越好——快的方法更實用。

### 標準 C4：雜訊穩定性

```python
score_noise = C_topology(clean) / C_topology(noisy)
```

對雜訊的敏感度。越接近 1 越好——穩定。

### 總分

```python
total_score = w₁ · score_κ + w₂ · score_sep + w₃ · score_feas + w₄ · score_noise
```

初始權重：w₁ = 0.4, w₂ = 0.3, w₃ = 0.1, w₄ = 0.2

---

## 5. 執行協議

```
Step 0: ✅ 定理 T1-T4 鎖定
Step 1: ✅ 15 種組合定義
Step 2: 🔴 實現 code：
          ├── 5 種 S_AI 計算
          ├── 3 種距離度量
          ├── Persistent homology (需要用 ripser)
          └── 4 種評分標準
Step 3: 🔴 在合成數據上跑 15 種組合
Step 4: 🔴 比較結果，選最優解
Step 5: 🔴 在真實 AI 模型上驗證
```

---

*AI Consciousness Definition v2.1 — Experimental Protocol. CFAS Consciousness Dynamics. 2026-07-11.*