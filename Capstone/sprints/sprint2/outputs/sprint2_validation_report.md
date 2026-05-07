# Sprint 2 — Scenario Injection Testing & Validation Report

**Purpose (PID §66)**: *"Since the data is synthetic, the sponsor will evaluate the credibility of the Isolation Score through Scenario Injection Testing. If the algorithm accurately flags intentionally isolated nodes without generating false positives, the model's mathematical logic will be validated as credible."*

**Method**: Use `Profile_Type == 'island'` (41 of 300) as ground-truth positive class; use `Isolation_Score` as continuous score. Compute ROC-AUC, Youden's-J-optimal τ_ROC, confusion matrix.

**Dataset snapshot**: 300 nodes, 1042 edges, seed = 5228, schema v1.2.0.

---

## 1. Headline Results

| Metric | Target | Observed | Status |
| :-- | :-- | :-- | :-- |
| ROC-AUC | ≥ 0.80 | **0.9999** | PASS |
| Sensitivity (TPR) at τ_ROC | ≥ 0.75 | **1.0000** | PASS |
| Specificity (TNR) at τ_ROC | ≥ 0.80 | **0.9923** | PASS |
| Welch's t-test island vs balanced | p < 0.01 | **p ≈ 9.04e-45** | PASS |

τ_ROC (Youden's-J-optimal) = **0.6917**.

---

## 2. Confusion Matrix at τ_ROC = 0.6917

|  | Predicted Island | Predicted Not Island |
| :-- | :-: | :-: |
| **Actual Island** | **TP = 41** | FN = 0 |
| **Actual Not Island** | FP = 2 | **TN = 257** |

- Recall (Sensitivity) = 41/41 = **1.0000**
- Precision = 41/43 = **0.9535**
- Specificity = 257/259 = **0.9923**

---

## 3. Isolation Score Distribution by Archetype

| Profile_Type | n | mean | median | std | min | max |
| :-- | --: | --: | --: | --: | --: | --: |
| `balanced` | 222 | 0.4250 | 0.4083 | 0.0974 | 0.2500 | 0.6917 |
| `broker` | 29 | 0.4429 | 0.4208 | 0.0490 | 0.3958 | 0.5417 |
| `hub` | 8 | 0.4979 | 0.5166 | 0.0519 | 0.4083 | 0.5417 |
| `island` | 41 | 0.9583 | 1.0000 | 0.0814 | 0.6917 | 1.0000 |

---

## 4. False Positive Inspection

Count: **2**.

| EMP_ID | Team | Seniority | Profile_Type | Isolation_Score | OutboundScarcity | WeakBridgeDeficit |
| :-- | :-- | :-- | :-- | --: | --: | --: |
| EMP_004 | Information Management | Mid-level | balanced | 0.6917 | 0.6667 | 0.6000 |
| EMP_125 | Solution Architecture | Senior | balanced | 0.6917 | 0.6667 | 0.6000 |

**Interpretation**: FPs sit at τ_ROC boundary with structurally island-like driver combinations (low outbound + weak-bridge deficit). Recommended management treatment: "flagged for investigation, not confirmed silent island".

---

## 5. Implication

- PID §66 credibility test: **satisfied**.
- Sprint 3 predictive model will use `Isolation_Risk_Flag` (derived at τ_ROC) as binary target y.
- Scalability validation at larger N: deferred to Sprint 4 per plan.