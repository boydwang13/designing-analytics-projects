# Sprint 2 — Core ONA, Isolation Score & Interactive Topology

**周次**：Weeks 3–4
**状态**：✅ 完成（10 个 Workstream 全部交付）
**对应 PID 计划**：[`docs/PID.md`](../../docs/PID.md) "Sprint 2 (Weeks 3-4): Core ONA & Descriptive Analysis"
**Sponsor 反馈对齐**：Martin Sprint 1 评审 5 条建议（#1 Boundary Spanning / #3 Numeric mapping / #4 Team clustering / #5 Interactivity；#2 Scalability 按计划延至 Sprint 4）

---

## Definition of Done（全部满足）

| # | 交付物 | 位置 |
| :-- | :-- | :-- |
| D1 | Schema v1.2.0：`Interaction_Type_Code` + `Interaction_Frequency_Weight` 两列 | [`data/mock_data_edges.csv`](../../data/mock_data_edges.csv)、[`docs/mock_codebook.md`](../../docs/mock_codebook.md)、[`docs/CHANGELOG.md`](../../docs/CHANGELOG.md) |
| D2 | 节点指标总表（centrality + Isolation Score + Risk Flag + Tier） | [`outputs/sprint2_nodes_with_metrics.csv`](outputs/sprint2_nodes_with_metrics.csv) |
| D3 | 个人静默名单 Top 20 | [`outputs/sprint2_silent_individuals_shortlist.md`](outputs/sprint2_silent_individuals_shortlist.md) |
| D4 | 团队静默聚合视图 | [`outputs/sprint2_silent_teams_aggregated.md`](outputs/sprint2_silent_teams_aggregated.md) |
| D5 | Power User 集中度 | [`outputs/sprint2_power_user_concentration.md`](outputs/sprint2_power_user_concentration.md) |
| **D13** | **Brokers（中介 / 边界跨越者）Top 10**（`betweenness` 主序 + 破同分） | [`outputs/sprint2_brokers_shortlist.md`](outputs/sprint2_brokers_shortlist.md) |
| D6 | Scenario Injection Testing 验证报告 | [`outputs/sprint2_validation_report.md`](outputs/sprint2_validation_report.md) |
| D7 | Counter-metrics 声明 | [`outputs/sprint2_counter_metrics.md`](outputs/sprint2_counter_metrics.md) |
| D8 | 交互式拓扑图（pyvis，self-contained） | [`outputs/sprint2_interactive_topology.html`](outputs/sprint2_interactive_topology.html) |
| D9 | 汇总 + 评审包 | [`outputs/sprint2_summary_report.md`](outputs/sprint2_summary_report.md)、[`outputs/sprint2_review_pack.md`](outputs/sprint2_review_pack.md) |
| D10 | 一键执行 + notebook + 本 README | [`run_sprint2.py`](run_sprint2.py)、[`notebook.ipynb`](notebook.ipynb) |
| D11 | 治理更新 | [`docs/CHANGELOG.md`](../../docs/CHANGELOG.md) v1.2.0 + v1.2.1 + v1.2.2、[`Capstone/requirements.txt`](../../requirements.txt) |
| **D12** | **Team 间有向密度矩阵**（Cross & Parker 块密度，6×6，含 unweighted / weighted / Hard / Soft 四种 + 热力图 PNG） | [`outputs/sprint2_team_density_matrix.md`](outputs/sprint2_team_density_matrix.md)、[`outputs/sprint2_team_density_heatmap.png`](outputs/sprint2_team_density_heatmap.png) |

---

## 关键量化结果

| 指标 | 值 | 评价 |
| :-- | :-- | :-- |
| Nodes / Edges | 300 / 1042 | 与 Sprint 1 一致 |
| ROC-AUC | **0.9999** | 远超计划 0.80 门槛 |
| τ_ROC（Youden's-J 最优） | **0.6917** | |
| Sensitivity / Specificity | **1.0000 / 0.9923** | 两项均 PASS |
| Confusion Matrix | TP=41 / FP=2 / TN=257 / FN=0 | 零漏报 |
| Risk Tier 分布 | High=43 / Medium=126 / Low=131 | High 占 14.3% |
| Top-5 Hub Inbound Share | **14.49%** | PID §34 preferential attachment 证据 |
| Top-10 Hub Inbound Share | **23.32%** | 3.3% 员工承接 23.3% 求助 |
| CM-3 Broker False Positive | **0** | 模型自洽 |
| Team 空间聚类 separation ratio | **9.5×** | Martin #4 落地成功 |

Archetype 回收：所有 8 个注入 `hub` 出现在 Central Connectors 表 Top-8（主序 `in_degree`、`in_strength` 破并列；精度 100%），所有 41 个注入 `island` 被 Flag=1（Recall 100%）。

---

## 如何复现 Sprint 2

一键执行（从 Capstone 目录运行）：

```bash
cd Capstone
PYTHONPATH=../.venv_lib python3 sprints/sprint2/run_sprint2.py
```

预期机器可读输出（JSON）：

```json
{
  "nodes": 300, "edges": 1042,
  "auc": 0.9999058291741219, "tau_roc": 0.6917,
  "sensitivity": 1.0, "specificity": 0.9922779922779923,
  "confusion": {"tp": 41, "fp": 2, "tn": 257, "fn": 0},
  "tier_counts": {"Low": 131, "Medium": 126, "High": 43}
}
```

若数据需要重新生成（同样 seed=5228，schema v1.2.0）：

```bash
python3 src/generate_assets.py
python3 sprints/sprint2/run_sprint2.py
```

---

## 代码依赖图

```
run_sprint2.py（本目录）
        │
        ▼
src/metrics.py  ────▶  src/isolation_score.py  ────▶  src/threshold.py
                                                          │
                                                          ▼
                                                     src/viz.py (pyvis)
```

所有 `src/*.py` 模块都有自己的 `__main__` 块，可独立调试：

```bash
PYTHONPATH=../.venv_lib python3 src/metrics.py          # WS2 独立验证
PYTHONPATH=../.venv_lib python3 src/isolation_score.py  # WS3 独立验证
PYTHONPATH=../.venv_lib python3 src/threshold.py        # WS4 独立验证
PYTHONPATH=../.venv_lib python3 src/viz.py              # WS7 独立验证
```

---

## Sponsor 评审建议路径（30 分钟）

按 [`outputs/sprint2_review_pack.md`](outputs/sprint2_review_pack.md) 的 5 步流程进行：

1. 打开 `sprint2_interactive_topology.html`（Team 聚类 + hover tooltip 验证）· 5 min
2. 走 `sprint2_silent_teams_aggregated.md`（团队级风险热图）· 5 min
3. 走 `sprint2_silent_individuals_shortlist.md` Top 20 · 5 min
4. 走 `sprint2_validation_report.md`（AUC / 混淆矩阵 / τ_ROC）· 10 min
5. `sprint2_counter_metrics.md` + `sprint2_power_user_concentration.md` · 5 min

---

## 与 Sprint 3 的衔接

Sprint 3 将以下面为基线：
- **y = `Isolation_Risk_Flag`**（二分类目标，τ_ROC = 0.6917 已定）
- **x = 节点属性**：`Seniority` / `Team`（编码）/ `Years_Exp` / `A1`–`H3` 行为信号
- **模型**：Logistic Regression（可解释）+ Random Forest（非线性）
- **评估**：AUC / Brier Score / Confusion Matrix；80/20 holdout + 5-fold CV

详细 Sprint 3 计划将在 Sprint 2 Sponsor 评审完成后另行制定。
