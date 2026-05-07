"""Sprint 2 · WS4 — Threshold selection and risk-tier assignment.

Two parallel outputs:

1. `Isolation_Risk_Flag` (binary): 1 if Isolation_Score >= tau_ROC, else 0.
   - tau_ROC is the Isolation_Score value that maximizes Youden's J statistic
     (J = TPR - FPR) against the ground truth `Profile_Type == 'island'`.

2. `Isolation_Risk_Tier` (categorical: High / Medium / Low):
   - High:   Isolation_Score >= p75 AND Isolation_Score >= tau_ROC
   - Medium: p50 <= Isolation_Score < p75
   - Low:    Isolation_Score < p50

See `sprints/sprint2/sprint2_plan.md` § WS4 for design rationale.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, roc_auc_score, roc_curve


@dataclass(frozen=True)
class ThresholdResult:
    tau_roc: float
    auc: float
    sensitivity: float
    specificity: float
    tp: int
    fp: int
    tn: int
    fn: int
    p50: float
    p75: float


def derive_threshold(isolation_score: pd.Series, profile_type: pd.Series) -> ThresholdResult:
    """Compute ROC-optimal threshold + percentiles for three-tier layering.

    Ground truth `y_true` = 1 if Profile_Type == 'island' else 0.
    """
    y_true = (profile_type == "island").astype(int).to_numpy()
    y_score = isolation_score.to_numpy(dtype=float)

    fpr, tpr, thresh = roc_curve(y_true, y_score)
    j = tpr - fpr
    best_idx = int(np.argmax(j))
    tau_roc = float(thresh[best_idx])
    # sklearn may return thresh[0] = max+1; clip to observed range.
    if tau_roc > float(y_score.max()):
        tau_roc = float(y_score.max())

    auc = float(roc_auc_score(y_true, y_score))
    sensitivity = float(tpr[best_idx])
    specificity = float(1.0 - fpr[best_idx])

    y_pred = (y_score >= tau_roc).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()

    p50 = float(np.quantile(y_score, 0.50))
    p75 = float(np.quantile(y_score, 0.75))

    return ThresholdResult(
        tau_roc=tau_roc,
        auc=auc,
        sensitivity=sensitivity,
        specificity=specificity,
        tp=int(tp),
        fp=int(fp),
        tn=int(tn),
        fn=int(fn),
        p50=p50,
        p75=p75,
    )


def assign_flag_and_tier(
    df: pd.DataFrame, result: ThresholdResult, score_col: str = "Isolation_Score"
) -> pd.DataFrame:
    """Append `Isolation_Risk_Flag` and `Isolation_Risk_Tier` columns to df."""
    out = df.copy()
    score = out[score_col]
    out["Isolation_Risk_Flag"] = (score >= result.tau_roc).astype(int)

    def _tier(s: float) -> str:
        if s >= result.p75 and s >= result.tau_roc:
            return "High"
        if s >= result.p50:
            return "Medium"
        return "Low"

    out["Isolation_Risk_Tier"] = score.apply(_tier)
    return out


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent))
    from metrics import compute_node_metrics, load_edges_and_nodes
    from isolation_score import compute_isolation_score

    nodes, edges = load_edges_and_nodes()
    m = compute_node_metrics(nodes, edges)
    iso = compute_isolation_score(nodes, m, edges)
    joined = iso.merge(nodes[["EMP_ID", "Profile_Type"]], on="EMP_ID")

    res = derive_threshold(joined["Isolation_Score"], joined["Profile_Type"])
    print("Threshold derivation result:")
    print(f"  AUC                 = {res.auc:.4f}")
    print(f"  tau_ROC             = {res.tau_roc:.4f}")
    print(f"  Sensitivity (TPR)   = {res.sensitivity:.4f}")
    print(f"  Specificity (TNR)   = {res.specificity:.4f}")
    print(f"  Confusion matrix    TP={res.tp}  FP={res.fp}  TN={res.tn}  FN={res.fn}")
    print(f"  p50 / p75           = {res.p50:.4f} / {res.p75:.4f}")

    flagged = assign_flag_and_tier(joined, res)
    tier_counts = flagged["Isolation_Risk_Tier"].value_counts()
    print("\nTier distribution:")
    print(tier_counts)
