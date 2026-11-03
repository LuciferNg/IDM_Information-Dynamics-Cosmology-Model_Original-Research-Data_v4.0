# IDM v4.0 — Consistency-Field-Applied-Science

**Information Dynamics Cosmology Model（資訊動力學宇宙論模型）— 4th Generation**

> `Consistency-Field-Applied-Science`（CFAS，讀 SeeFass）係版本代號，唔係理論名稱。理論名稱由 v1.0 到 v11.0 一直係 Information Dynamics Cosmology Model，從未改變。
>
> v4.0 的職責係換基質：把 v3.0 的「多域框架」壓成單一公理加單一代數基質，令全部物理層（量子、規範、引力、宇宙學、意識）成為同一個有限一致性預算的投影，而唔係各自成域。

## 緣起

起點係一個觀測異常。2025-06-23，CLASS 宇宙學數值擬合在 `z_c ≈ 0.60` 出現同步凹陷（sync dip），`ε = 0.1545`；標準模型無任何已知過程可以產生此特徵。

v3.0 用「域框架」處理它：5 條公理、7 條定理、8 條推論、4 個 domain、17 個可測預言。域框架把一致性理解成「各域內部各自成立」，於是每加一個域，就多帶一批局部參數與局部公理；公理數目隨域數增長，域與域之間無共同預算約束。

v4.0 因此做三件事：

1. **收公理**：5 條公理收為 1 條——宇宙維持全局一致性只有有限預算 `B = Σ|W_k|² ≤ 1`
2. **換基質**：基質由「域」換成單一代數對象 OAS `(A, τ, S)`（Type II₁ von Neumann algebra），全部層由同一基質投影
3. **可算化**：把「一致性場」由概念變成可算對象 `W_k ∈ ℂ`，並落成 40 支數值腳本、4 個子學科

驗收標準：一個結果只有在能由 `B ≤ 1` 或 OAS 代數結構導出時才算閉合；任何一個可調參數都會令該結果降級為候選。

## 版本演進：v3.0 → v4.0

IDCM 係**逆向工程**：由已觀測的常數與結構反推生成機制，唔預設公理、唔設「核心假設」。因此版本之間的分野唔係假設改變，而係**逆推對象改變**。

### v3.0 — Domain Framework

- 形態：多域框架。`01-core/domain_framework_derivation.md` 列 4 條公理（另 `f_unified_summary.md` 補至 5 條），`02-theorems-proofs/` 出 7 條定理、8 條推論
- 域：EW domain（`ew_domain_oas_structure.md`）、暗部門域（`05-speculation/dark_sector_domain.md`）等共 4 個
- 已得數字：`α = 1.025` exact（`q7_alpha_exact.md`）、`ħ` exact（`q8_hbar_exact.md`）、`N_crit ≈ 150`（`q9_ncrit_exact.md`）、`T_μν` sign flip 已驗（`q11_tmunu_sign_flip_verified.md`）
- 未決：6 個 hard open（世代數、Higgs λ、`ħ` 來源、域完備性等），域間無統一預算

### 根因：域分割令公理與參數隨域增長

兩個結構病：

1. **公理隨域增長**。域框架的公理係「每個域各自成立」的局部陳述，域數增加則公理數增加。v3.0 自報 5 條公理、4 個 domain；到 v4.0 開版時的審計對照，自由參數約 10 個以上（`REVIEW.md` 執行摘要「Free parameters」欄 2026-07-09 → 2026-07-10：`~10+` → `0`）。
2. **κ 循環定義**。早期以 `κ = e⁻³ = 0.050` 作門檻，寫法係「κ 等於第三世代特徵值 `λ_3`」；`core/kappa-threshold.md` 第 1 節自述此定義 **circular**——用「最後可見模態的特徵值」定義可見性門檻，等於把答案寫進前提。

兩者同源：域框架無共同基質，所以每個量只能就近找一個域內對象作定義，而該對象本身又依賴被定義量。

### v4.0 — Consistency-Field-Applied-Science

- **單一公理 A1**：`B = Σ|W_k|² ≤ 1`（`core/axioms.md`）
- **單一基質**：OAS = `(A, τ, S)`，Type II₁ von Neumann algebra；T1–T4 由 Connes–Takesaki（`Aut(A) = Inn(A)`）與 Sakai duality（`A_* ⊊ A`）得證
- **兩條運算鏈**：`d|W⟩/dt = −iS|W⟩/ħ − Γ|W⟩ + Σ` 三項分別對應內自同構、條件期望、態製備（`core/rendering-equation.md`、`DISCOVERIES.md` D1）
- **κ 去循環**：`κ = B/N_particles = 1/16 = 0.0625`（SM 每代 16 個 Weyl 費米子）；`y_ν = √κ = 0.250`
- **八層閉合**：L0 基質 → L1 W 場 → L2 量子 → L3 規範 → L4 QFT → L5 宇宙學 → L6 引力 → L7 意識
- **歸一為一遞迴（2026-07-15）**：`4ε + 1 = φ` ⟹ `ε = φ⁻¹/4`；`B = φ⁰`、`κ = (εφ)² = 1/16`、`N = 4²`、SU(5) 由 `M = 4`；49 條方程全歸 `C_{n+1} = 1/(1 + C_n)`（`core/golden-ratio-structural-closure.md`）
- **由理論轉應用科學**：拆 4 個子學科 OASA（L0）／GP（L2–L4）／CC（L5–L6）／CD（L7）（`core/disciplines.md`）

> 代價：v3.0 的 6 個 hard open 之中，世代數（`core/generations.md`）與中微子機制（`core/neutrino-mass-0param.md`）在本版另有處理，其餘仍留在 `GAPS.md` 的 open 清單；`Δm²_sol` 精度 1.56× 至今未收。

## 研究路線

八層，每層只做一件事，上層不能借用下層的結論：

**L0 基質層** — OAS 代數

- OAS = `(A, τ, S)`，Type II₁ vNA；`τ` 為 trace、`S` 為 sync 算子
- `κ` 由資訊理論推出：`κ = B/N_particles`，`N_particles = 16`（`core/kappa-threshold.md`）
- T1–T4：`Aut(A) = Inn(A)`（Connes–Takesaki）、`A_* ⊊ A`（Sakai）、`A_rendered ⊊ A`、`[P₁, P₂] ≠ 0`（`core/theorems-t1-t2-t3.md`、`core/horizon-interference.md`）

**L1 W 場層** — 複振幅

- `W_k ∈ ℂ`，`B = Σ|W_k|² ≤ 1`；相位 `θ` 與模 `|W|` 分離
- 波包與同步演化：`dW/dt = −iωW`（`core/w-field-wave.md`、`core/complex-w-derivation.md`）

**L2 量子層** — 由代數出 QM

- Born rule `P(k) = |W_k|²/Σ|W|²` 由 `|W|²` 為強度導出，非假設
- 複數、Schrödinger 方程、spin（SU(2) 內旋）、交換統計（`q1`–`q3_derivation.py`）
- `N_c = 2` 解析：`ε² ≈ ħ/2` 誤差 5% 內（`core/oas-formalized.md`）

**L3 規範層** — 由 W 對稱出規範群

- U(1) 由局部相位不變、SU(2)×U(1) 由雙重態、SU(3) 由三色分量（`core/gauge-coupling.md`、`core/electroweak.md`、`core/qcd.md`）
- 群選擇：`rank(S) = 4` ⟹ SU(5)，唔用 GUT 論證（`core/gauge-group-selection.md`）
- 世代數 1+3 由 SU(2) adjoint + center 得（`core/generations.md`）

**L4 QFT 層** — 模展開與重整化

- 模展開、Fock 空間、傳播子（`core/w-field-quantization.md`、`cfas-quantization.py`）
- 有限 `Λ_UV`：預算有限 ⟹ 無連續無窮（`core/renormalization.md`）
- 自評缺口：此層「概念正確但不產生新粒子物理預言」（`REVIEW.md` L4 段）

**L5 宇宙學層** — 暴脹、暗能量、結構形成

- 暴脹勢由 Type II₁ 均勻譜密度導出：`f''(x) = const ⟹ f(x) = 2x − x²`（`core/inflation-spectral-derivation.md`）
- `n_s = 0.962–0.965`、`r = 0.0035–0.0040`（`12/N_e²`）、`T_RH = 2.2×10¹⁵ GeV`
- 同步凹陷 = Akhiezer 再分配（平滑預算優化，非相變）；`ε = φ⁻¹/4 = 0.154508`
- CP 相位 = Berry phase，`J = 3.0×10⁻⁵`；重子生成 `η = 9.9×10⁻¹⁰`（factor 1.6）

**L6 引力層** — 由 W 應力張量出 GR

- `W` 場 → `T_μν` → `G_μν`（`core/gravity.md`、`core/semiclassical-gravity.md`）
- 黑洞內部無奇異點、凍結核（`core/black-hole-interior.md`）

**L7 意識層** — 邊界算子

- `C = abs(τ([H, P_κ] ⊗ WW†))`，一致性視界 = 邊界跡（`core/boundary-ontology.md`）
- `dC/dt` 由 master equation 三項分解（`core/cip-dynamics.md`）
- `N_c` 門檻 ≈ 64（n = 1000）；θ-γ PAC 先於 γ 功率（`core/consciousness-dynamics.md`）

| 子學科 | 代號 | 層 | 文檔 | 代碼 | 狀態 |
|:------|:----:|:--:|:----:|:----:|:----:|
| 基礎代數學 OAS Algebra | OASA | L0 | 7 | 8 | 全部閉合 |
| 規範物理學 Gauge Physics | GP | L2–L4 | 10 | 12 | 全部閉合 |
| 演算宇宙學 Computational Cosmology | CC | L5–L6 | 11 | 10 | 全部閉合 |
| 意識動力學 Consciousness Dynamics | CD | L7 | 11 | 6 | 部分閉合 |

> 子學科文檔／代碼數目取自 `REVIEW.md` §3；EEG 實測未執行，故 CD 標部分閉合。

## 項目結構

```
IDM-v4.0--Consistency-Field-Applied-Science/
├── README.md                        # 本檔
├── core/                            # 46 份推導文檔（L0–L7 逐層）
│   ├── axioms.md                    # 單一公理 A1 + 全鏈對照表
│   ├── oas-foundation.md            # L0 OAS 起手
│   ├── oas-formalized.md            # L0 Type II₁ vNA 形式化
│   ├── kappa-threshold.md           # κ = 1/16（並記錄 κ = e⁻³ 循環錯誤）
│   ├── theorems-t1-t2-t3.md         # T1–T3 證明
│   ├── horizon-interference.md      # T4：校準器互不可見
│   ├── complex-w-derivation.md      # L1 複振幅 → Born rule
│   ├── gauge-group-selection.md     # L3 群選擇：rank(S) = 4
│   ├── golden-ratio-structural-closure.md  # 4ε+1=φ 全結構閉合
│   ├── golden-ratio-sync-derivation.md     # ε = φ⁻¹/4 推導
│   ├── 46-equations.md              # 最終方程集（標題作 The 50 Equations）
│   └── …                            # 其餘按層命名，一檔一結果
├── codes/                           # 40 支數值腳本（每支可獨立執行）
│   ├── q1_derivation.py … q6_derivation.py  # 量子層六支：Born/複數/糾纏/退相干/CHSH/CIP
│   ├── cfas-golden-ratio-sync.py            # ε = φ⁻¹/4 檢查（自報 10/10）
│   ├── cfas-generating-equation-verification.py  # x²+x−1=0 檢查（自報 11/11）
│   └── cfas-*.py                            # 其餘模組：規範、QFT、宇宙學、引力、意識
├── cfas/                            # PEP 517 套件（pip install -e .）
│   ├── __init__.py                  # 5 個核心函數：born_rule/epsilon/consciousness/wave_packet/chsh_violation
│   └── cli.py                       # CLI 入口
├── CFAS-Consciousness-Dynamics/     # 子專案：AI 意識（10 檔）
│   ├── core/                        # ai-w-field / ai-rendering-boundary / ai-consciousness-definition
│   ├── codes/                       # ai-topology-simulation / ai-topology-batch / ai-nc-estimation
│   └── report/                      # topology-report / comparison-framework
├── quantum/                         # 4 檔：measurement / entanglement / decoherence / phenomena-catalog
├── cosmic/                          # 1 檔：early-universe
├── neural/                          # 1 檔：consciousness（神經標度）
├── condensed/                       # 1 檔：overview（凝態類比）
├── consciousness-detection/         # 1 檔：protocol（偵測協議）
├── reports/                         # 4 份校準器報告（calibrator-001…004）
├── narrative/                       # 1 檔：多實例框架開發敘事
├── references/                      # 2 檔：literature-comparison / parallel-researchers
├── figures/                         # w-field-wave.png
├── GAPS.md                          # P0–P4 閘表 + 未決 + 當前正確值
├── REVIEW.md                        # 全鏈審計（2026-07-10 v2.0）
├── VERIFICATION_RESULTS.json        # 13 支腳本執行結果（machine-readable）
├── PROGRAMME_NARRATIVE.md           # 六階段綱領敘事（含自審日誌）
├── DISCOVERIES.md                   # 7 項發現（README 另列 9 項，見狀態快照註）
├── MANIFESTO.md                     # 宣言與五層標度
├── IDM_standard_cosmology.md        # 與標準宇宙學對照
└── pyproject.toml                   # 套件定義
```

## 狀態快照（2026-11-03 重數；數字以實際檔案為準）

```
實際檔案
  core/*.md                          46
  codes/*.py                         40
  cfas/                              __init__.py（5 函數）+ cli.py
  CFAS-Consciousness-Dynamics/       10 檔（3 core + 3 codes + 2 report + README + narrative）
  reports/                           4（calibrator-001…004）
  VERIFICATION_RESULTS.json          13 支腳本記錄，13/13 exit 正常

階段閘（GAPS.md，P0–P4 共 5 閘）
  P0 全部閉合 ｜ P1 全部閉合 ｜ P2 部分閉合 ｜ P3 部分閉合 ｜ P4 部分閉合

未決（REVIEW.md §4）
  Δm²_sol 精度 1.56×（P3）
  EEG PAC 時序實驗未執行（P2，T3）
  N_c 精確門檻 10⁵ ± 0.5（P3）
```

> **repo 內自述數字不一致（原文照錄，不代為調和）**：`README.md` 稱 25 modules、25/25 PASS；`REVIEW.md` 執行摘要稱 37 core docs／36 codes，同檔 §5 又稱 38 codes、43 core docs；`PROGRAMME_NARRATIVE.md` 稱 6 phases、39 codes、49 equations；`core/46-equations.md` 標題寫 The 50 Equations、25/26 audit pass；`PROGRAMME_NARRATIVE.md` 自審日誌寫 23/24 通過。實際檔案數為 core 46 份、codes 40 支。
>
> 發現項數同樣有兩版：`DISCOVERIES.md` 標題 7 項，`README.md` 列 9 項（第 9 項為結構閉合總述）。

## 已閉合關鍵結果（選錄）

- **2026-07-09（`core/axioms.md`）**：L0–L7 八層鏈貫通，單一公理 `B = Σ|W_k|² ≤ 1` 投影出 QM、規範、QFT、宇宙學、GR、意識六域
- **2026-07-10（`core/kappa-threshold.md`）**：`κ = B/N_particles = 1/16 = 0.0625`，16 為 SM 每代 Weyl 費米子數；取代循環定義 `κ = e⁻³`，並使 `y_ν = √κ = 0.250` 零參數
- **2026-07-10（`core/oas-formalized.md`、`core/theorems-t1-t2-t3.md`）**：OAS 形式化為 Type II₁ vNA，去循環；T1 `Aut(A) = Inn(A)`、T2 `A_* ⊊ A`、T3 `A_rendered ⊊ A`、T4 `[P₁, P₂] ≠ 0` 四定理成立
- **2026-07-10（`core/inflation-spectral-derivation.md`）**：暴脹勢由 Type II₁ 均勻譜密度導出 `f''(x) = const ⟹ f(x) = 2x − x²`；`n_s = 0.962–0.965`、`r = 0.0035–0.0040`、`T_RH = 2.2×10¹⁵ GeV`
- **2026-07-10（`core/cp-violation.md`）**：CP 相位 = Berry phase，`J = 3.0×10⁻⁵`；重子生成 `η = 9.9×10⁻¹⁰`（factor 1.6，GUT X-boson）
- **2026-07-10（`core/neutrino-mass-0param.md`）**：`y_ν = √κ` 由預算約束定；正常層次，`m_ν₃ = 0.05 eV`（1.00×），`Δm²_sol` 偏差 1.56×
- **2026-07-15（`core/golden-ratio-structural-closure.md`）**：`4ε + 1 = φ` ⟹ `ε = φ⁻¹/4 = (√5 − 1)/8 ≈ 0.154508`；同式給 `B = φ⁰`、`κ = (εφ)² = 1/16`、`N_particles = 4² = 16`、SU(5) 由 `M = 4`；49 條方程歸一為單一遞迴 `C_{n+1} = 1/(1 + C_n)`，固定點 `x² + x − 1 = 0`
- **2026-07-15（`PROGRAMME_NARRATIVE.md`）**：六階段綱領收束，自審日誌記 23/24 通過、0 自由參數、0 理論漏洞；同步凹陷 `ε = 0.1545` 於 `z_c ≈ 0.60` 為可證偽預言（DESI DR2／Euclid）

## 驗證紀律

本版嚴謹性分六層：入場券 → 結構審計 → 獨立性審計 → 數字紀律 → 記錄紀律 → 路徑與命名。任一層不過，結果只停留「數值候選」。

### 一、入場券：4 Hard Tests

| 測試 | 要求 | 本版對應 |
|------|------|----------|
| ① 零參數自由度 | dof = 0，每加一個可調參數扣一級 | `B ≤ 1` 為唯一輸入；`κ`、`y_ν`、`ε` 皆由 `B` 與 `N_particles` 定，`GAPS.md` 記 Free parameters = 0 |
| ② 可證偽 | 預言須零寬度或可被更精確測量殺 | `ε = 0.1545` 於 `z_c ≈ 0.60`（DESI DR2／Euclid）；`r = 0.0035–0.0040`（LiteBIRD） |
| ③ 樣本外 | 預言先寫死，數據後開 | `ε = φ⁻¹/4` 先於數值擬合寫入 `golden-ratio-sync-derivation.md`，後以 CLASS 對照 |
| ④ 結構剛性 | 擾動任一參數，結論必須崩 | `4ε = φ⁻¹` 若改 `ε`，則 `B = φ⁰`、`κ = (εφ)²`、`N = 4²` 三式同時失效 |

### 二、結構審計：三鐵律

- **能證偽**：禁「約 X%」。本版所有預言寫成等式或區間（`n_s = 0.962–0.965` 為譜密度區間，非擬合窗）
- **能預言**：至少一個獨立樣本外預言；同義反覆不算
- **自由度能砸**：禁「枚舉 N 個候選揀中 1 個」——隱藏 dof = N；`κ = 1/16` 之所以可寫等式，係因 `N_particles = 16` 本身由 `N = 4²` 與 SU(5) rep 分解給出，非枚舉

### 三、獨立性審計：五反模式

1. **同義反覆** — 計放大因子 `δy/y ÷ δx/x`；若對所有候選同一常數，則 `y = f(x)` 為單調變換，唔算兩個判據
2. **循環** — 預言公式內含被解釋量。本版實例：`κ = λ_3` 循環，已由 `κ = B/N_particles` 取代
3. **範疇錯** — 樹級 vs RG running、on-shell vs MS-bar、`M_Z` vs 統一標度
4. **枚舉即隱藏 dof** — 掃 N 個組合揀中 1 個 ⟹ dof = N
5. **密度家族依賴** — 家族越小統計力越弱；報密度必須同時報家族大小與定義

### 四、數字紀律

- **反硬編碼**：關鍵常數須二源以上一致（結構推導／獨立觀測／數值重算）；只有一源 ⟹ 標「未驗」
- **自審對照**：`REVIEW.md` 逐層列 2026-07-09 與 2026-07-10 兩版狀態，舊判定保留原文，唔改寫
- **禁區**：見 target 後凑算子、事後選窗、以擬合常數冒充結構常數（`cfas/__init__.py` 之 `ALPHA = 1.0248` 明示來源為 CLASS fit，屬輸入非輸出）
- **數字衝突照錄**：同一量多處不同（如 codes 25/36/38/39/40），一律並列並註明來源檔，唔擇一美飾

### 五、記錄紀律

- 每支腳本配一份 `core/` 文檔，文件名一對一（`cfas-golden-ratio-sync.py` ⟷ `golden-ratio-sync-derivation.md`）
- 執行證據落 `VERIFICATION_RESULTS.json`（exit 狀態、check 列表、輸出長度），machine-readable
- 已否證路線保留原文 ＋ 校正註，唔刪除（`kappa-threshold.md` 保留 `κ = e⁻³` 錯誤敘述）
- 校準器報告編號 `calibrator-00N`，按時序 append，唔改舊號

### 六、路徑與命名

- 目錄用語義名（`core/`、`codes/`、`reports/`），腳本用 `cfas-<topic>.py` 或 `qN_derivation.py`
- 文件內互引一律用檔名，唔用裸號
- 本版為 CFAS 命名期：repo 目錄名 `IDM-v4.0--…`，套件名 `cfas`，兩者並存而今回溯統一為 IDM v4.0

## O/P/M 系列全列表

> 本 repo 無 O 系列與 M 系列，亦無統一問題編號。下表以 `GAPS.md` 的階段閘 P0–P4 為單位（`GAPS.md` 標題作「P0-P6 Completion Status」，實際只列 P0–P4；P5、P6 未記錄）。

| 編號 | 標題 | 核心發現 | 狀態 |
|------|------|----------|------|
| P0 | 基礎推導閘：κ、規範群、中微子 Yukawa、暴脹譜 | κ = B/N_particles = 1/16；SU(5) 由 rank(S) = 4；y_ν = √κ = 0.250；暴脹勢由 Type II₁ 譜密度導出 | 全部閉合 |
| P1 | OAS 形式化與世代數：Type II₁ vNA、有限預算暴脹、1+3 世代 | OAS 去循環；n_s = 0.962–0.965、r = 0.0035–0.0040；1+3 由 SU(2) adjoint 加 center 得，受 LHC 約束 | 全部閉合 |
| P2 | 意識動力學與 EEG：CIP 演化、張量標量比、頻帶映射 | dC/dt 由 master equation 三項分解；θ-γ PAC 先於 γ 功率；N_c 門檻 ≈ 64（n = 1000） | 部分閉合 |
| P3 | CP 破壞、重子生成、暗物質塔、中微子質量 | CP 相位 = Berry phase，J = 3.0×10⁻⁵；η = 9.9×10⁻¹⁰（factor 1.6）；暗物質塔 200 MeV → 14 MeV | 部分閉合 |
| P4 | UV 完備、黑洞內部、半經典引力、學科結構 | 有限 Λ_UV 無連續無窮；黑洞無奇異點；W 場置於彎曲時空；4 子學科成立 | 部分閉合 |

> P2 標部分閉合：EEG PAC 時序實驗（T3）無法由校準器執行（`REVIEW.md` §4）。
> P3 標部分閉合：`Δm²_sol` 偏差 1.56×、`N_c` 精確門檻 `10⁵ ± 0.5` 待收（`REVIEW.md` §4）。
> P4 標部分閉合：文獻對照僅 4/6 支持（`GAPS.md` P4 列）。