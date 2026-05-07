# Sprint 1 — Data Generation & Initial Topology Prototype

**周次**：Weeks 1–2
**状态**：✅ 完成
**对应 PID 计划**：[`docs/PID.md`](../../docs/PID.md) "Sprint 1 (Weeks 1-2): Data Generation & Initial Prototype"

---

## Definition of Done（已全部满足）

| # | 工作项 | 产出 | 完成证据 |
| :-- | :-- | :-- | :-- |
| 1 | Schema 冻结 + 问卷 / 字典对齐 | `docs/mock_survey.md`、`docs/mock_codebook.md` | 双表 schema 定稿，Section I/J 与导出字段一致 |
| 2 | 大规模合成数据生成（archetype 注入） | `data/mock_data_nodes.csv`（300）、`data/mock_data_edges.csv`（1042） | seed=5228 可复现；profile mix balanced/island/broker/hub = 222/41/29/8 |
| 3 | 数据质量门禁（DQ Gate） | [`outputs/dq_gate_report.md`](outputs/dq_gate_report.md) | **PASS**（0 issues） |
| 4 | EDA：分布、度profile | [`outputs/eda_profile_v1.csv`](outputs/eda_profile_v1.csv)、[`outputs/sprint1_freq_type_distribution.csv`](outputs/sprint1_freq_type_distribution.csv)、[`outputs/sprint1_node_degree_profile.csv`](outputs/sprint1_node_degree_profile.csv) | Hard 490 / Soft 552；Weekly 主导；in-degree top hub 候选可识别 |
| 5 | 网络拓扑原型（全量 + sandbox） | [`outputs/network_prototype_v1.png`](outputs/network_prototype_v1.png)、[`outputs/sprint1_topology_sandbox.png`](outputs/sprint1_topology_sandbox.png) | 全量 + 69-node 子图各一张 |
| 6 | 可复现 notebook + 自动化 runner + 评审包 | [`notebook.ipynb`](notebook.ipynb)、[`run_sprint1.py`](run_sprint1.py)、[`outputs/sprint1_summary_report.md`](outputs/sprint1_summary_report.md)、[`outputs/sprint1_review_pack.md`](outputs/sprint1_review_pack.md)、[`presentation.html`](presentation.html) | Sponsor 双语评审页已交付 |

---

## 文件索引

```
sprints/sprint1/
├── README.md                          ← 本文件
├── notebook.ipynb                     演示 notebook（路径已更新到新结构）
├── run_sprint1.py                     一键执行：DQ + EDA + sandbox 渲染 + 摘要
├── outputs/
│   ├── dq_gate_report.md              DQ Gate 详细报告
│   ├── eda_profile_v1.csv             EDA 节点 profile
│   ├── sprint1_node_degree_profile.csv
│   ├── sprint1_freq_type_distribution.csv
│   ├── sprint1_topology_sandbox.png   sandbox 子图（69 nodes / 125 edges）
│   ├── network_prototype_v1.png       全量原型
│   ├── sprint1_summary_report.md      Sprint 摘要
│   └── sprint1_review_pack.md         Sponsor 评审包
├── data_snapshot/                     Sprint 1 时点冻结的数据（仅追溯，不参与当前管线）
│   ├── mock_data_nodes.csv
│   └── mock_data_edges.csv
├── presentation.html                  Sponsor 评审页（中英双语，完整版）
└── presentation_v2_short.html         Sponsor 评审页（精简版）
```

---

## 如何复现 Sprint 1

```bash
cd Capstone

# 一键执行（读 data/ 下当前数据，写本目录 outputs/）
python sprints/sprint1/run_sprint1.py
```

预期输出：
```
{'nodes': 300, 'edges': 1042, 'sandbox_nodes': 69, 'sandbox_edges': 125, 'dq_pass': True}
```

如需重新生成底层数据再跑 Sprint 1：
```bash
python src/generate_assets.py        # 重新生成 data/*.csv（seed=5228）
python sprints/sprint1/run_sprint1.py
```

---

## 关键量化结果

| 指标 | 值 |
| :-- | :-- |
| Nodes（全量） | 300 |
| Edges（全量） | 1042 |
| Sandbox nodes / edges | 69 / 125 |
| DQ Gate | **PASS**（0 issues） |
| Profile mix | balanced 222 / island 41 / broker 29 / hub 8 |
| Interaction type mix | Hard 490 / Soft 552 |
| Frequency mix | Weekly 409 / Monthly 259 / Daily 240 / Rarely 134 |
| Top in-degree (hub 候选) | EMP_159 (33), EMP_126 (33), EMP_198 (32), EMP_166 (29), EMP_247 (24) |
| Out-degree = 0 (silent 候选) | 10+ 个 EMP_ID（详见 `outputs/dq_gate_report.md`） |

---

## 与 Sprint 2 的衔接

Sprint 2 将在以下基线上推进：

1. **数据输入**：直接使用 `Capstone/data/mock_data_*.csv`（live snapshot）
2. **核心任务**：In-degree / Out-degree / Betweenness centrality → Isolation Score → 静默名单 v1 → 拓扑图叠加中心性着色
3. **风险控制**：优先分层名单而非单一硬阈值；先在 sandbox 校验后再发布全量

详细 Sprint 2 计划将在前置清理任务（包括教授意见处理）完成后另行制定。
