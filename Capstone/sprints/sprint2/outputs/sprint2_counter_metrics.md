# Sprint 2 — Counter-Metrics Declaration

**Purpose**: Prevent Goodhart's Law failure modes. Every primary metric is paired with counter-metrics monitoring *quality*, classified as **Guardrail** (must not worsen) or **Tradeoff** (may worsen within bounds).

---

## CM-1 — New-Hire False Positive Rate

**Risk**: Employees with `Years_Exp < 1` have structurally low outbound volume due to onboarding; falsely flagging them would erode model trust.
**Classification**: **Guardrail**.
**Measurement**: `count(Years_Exp<1 AND Flag=1) / count(Years_Exp<1)`.
**Target ceiling**: ≤ 10%.
**Current value**: Undefined (0 / 0; no new hires in synthetic data).
**Status**: Deferred to real-data wave (synthetic data has no true new hires).

---

## CM-2 — Non-English Primary Users High-Risk Rate

**Risk**: Employees whose B2/B3/B4 score ≥ 3 may appear structurally isolated in an English-dominant referral network despite being connected in their linguistic sub-community (PID §42 intercultural limitation).
**Classification**: **Guardrail**.
**Measurement**: `count((B2>=3 OR B3>=3 OR B4>=3) AND Flag=1) / count(B2>=3 OR B3>=3 OR B4>=3)`.
**Target ceiling**: ≤ 10% absolute; ≤ network-baseline (14.33%) + 2pp.
**Current value**: 3 / 35 = **8.57%** — below both thresholds.
**Status**: PASS.

---

## CM-3 — Broker False Positive Count

**Risk**: A node with high betweenness and high Cross_Team_Tie_Count is a Cross & Parker boundary spanner; flagging them as isolated is self-contradictory.
**Classification**: **Tradeoff** (target = 0).
**Measurement**: `count(betweenness > p75 AND Flag=1)` where p75 = 0.015516.
**Current value**: **0** — matches target.
**Status**: PASS.

---

## Counter-Metric Summary Table

| CM | Type | Target | Current Value | Status |
| :-- | :-- | :-- | :-- | :-- |
| CM-1 New-Hire FP Rate | Guardrail | ≤ 10% | Undefined (0 / 0; no new hires in synthetic data) | Deferred |
| CM-2 Non-English High-Risk Rate | Guardrail | ≤ 10% absolute | 8.57% | PASS |
| CM-3 Broker FP Count | Tradeoff | = 0 | 0 | PASS |

---

## Future expansion (Sprint 3+)

- **CM-4**: Predictive-model-vs-Isolation-Score disagreement rate.
- **CM-5**: Positive-class share stability across retrains (≤ 5 pp drift).

## References

- PID §42 (intercultural limitation) drives CM-2.
- CEU counter-metrics / Goodhart's Law framework.
- Cross & Parker (2004) — boundary spanner definition underpinning CM-3.