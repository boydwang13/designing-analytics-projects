# CHANGELOG — Schema & Data Versions

记录 Capstone 项目数据 schema、生成逻辑、目录结构的重大演进。所有"取代旧版本"的变更都对应一次 `_archive/` 归档动作。

格式遵循 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) 的精神：每个版本块包含 `Added` / `Changed` / `Deprecated` / `Removed` / `Migration` 子项。

---

## [1.2.2] — 2026-04-24 — Brokers shortlist（Sprint 2 补丁 · D13）

**触发原因**：PID / 评审叙事需要与「Central Connectors（D5）」对称的 **Broker** 管理可读名单；避免 Sponsor 仅在 CSV 中自行按 `betweenness_centrality` 排序。

### Added

- `sprints/sprint2/outputs/sprint2_brokers_shortlist.md` — Top 10 结构中介名单（主键 `betweenness_centrality` 降序；并列 → `Cross_Team_Tie_Count` → `in_degree`）
- `run_sprint2.py` 新增 `write_brokers_shortlist()`，在 `write_power_user_report()` 之后执行

### Changed

- `write_power_user_report()`：Central Connectors 排序增加 **`in_strength` 作为 `in_degree` 并列时的 tie-breaker**；报告中注明排序规则

### Unchanged

- 无 schema 改动，无 seed 改动；`compute_power_user_concentration()` 仍仅按 `in_degree` 取 Top 5/10 share（与 D5 叙事一致）

---

## [1.2.1] — 2026-04-23 — Team 间有向密度矩阵（Sprint 2 补丁 · D12）

**触发原因**：Sprint 2 交付后补充 Martin 的追加建议："不要只依赖视觉，用 Cross & Parker 的 6×6 块密度表给出跨团队交流的硬数据。"

### Added

- `src/team_density.py` — 跨 Sprint 可复用的有向块密度计算模块
  - `compute_team_density()`：按 `interaction_type` 和 `weighted` 产出 6×6 directed density DataFrame
  - `format_density_md()`：统一 Markdown 表输出
  - `render_heatmap()`：matplotlib 注释热力图（对角线加粗蓝框）
- `sprints/sprint2/outputs/` 新增 7 个文件（D12 交付）：
  - `sprint2_team_density_matrix.csv`（unweighted · all types · 主版本）
  - `sprint2_team_density_matrix_weighted.csv`（按 Interaction_Frequency_Weight 加权）
  - `sprint2_team_density_matrix_hard.csv`（仅 Hard 技术求助）
  - `sprint2_team_density_matrix_soft.csv`（仅 Soft 业务协调求助）
  - `sprint2_team_density_matrix.md`（含 intra/off-diag 比率 + 不对称 Top-5 分析）
  - `sprint2_team_density_heatmap.png`（未加权主视觉）
  - `sprint2_team_density_heatmap_weighted.png`（加权版）
- `run_sprint2.py` 新增 `write_team_density()` 阶段
- `sprints/sprint2/notebook.ipynb` 新增 density-matrix 演示 cell（直接内嵌热力图）

### Analytical findings in current snapshot

- 6 个 team 的 "intra / off-diag" 比率均 **< 1**（Data Engineering 最低 0.37，Client Services 最高 0.97），**没有 team 呈现经典 silo 模式**——这是对 Martin "是否有整个团队变成孤岛" 提问的硬数据答复：当前合成数据中无
- 入站密度（纵向求和）揭示 **Analytics & BI 是最大净助人方**（inbound 0.086 vs outbound 0.066）
- 出站密度（横向求和）揭示 **Data Engineering 最依赖外部**（diagonal 0.005，远低于它对 Analytics & BI 的 0.017）

### Unchanged

- 无 schema 改动，无 seed 改动
- Sprint 2 核心指标（AUC / τ_ROC / 风险名单）全部保持一致

---

## [1.2.0] — 2026-04-23 — Schema v1.2 + Sprint 2 完整交付

**触发原因**：Sprint 2（Weeks 3–4）完整落地 PID Sprint 2 的 4 项核心任务 + Sponsor Martin 的 5 条 Sprint 1 评审建议（#2 Scalability 按决策延至 Sprint 4）+ CEU 课程对 counter-metrics / Scenario Injection Testing 的硬要求。

### Added — Schema v1.2.0

- `mock_data_edges.csv` 新增 2 列：
  - `Interaction_Type_Code` (int) — `Hard = 1`, `Soft = 0`；`2` / `3` 保留槽位供将来扩展（如 Advice / Escalation）
  - `Interaction_Frequency_Weight` (float, 0–1) — 指数衰减映射：`Daily = 1.00` / `Weekly = 0.67` / `Monthly = 0.33` / `Rarely = 0.10`
- `docs/mock_codebook.md` Table 2 同步更新字段定义；Tie strength mapping 小节并列展示 Granovetter 整数（4/3/2/1）与指数衰减小数（1.00/0.67/0.33/0.10）两套权重，说明两套用途不同
- Isolation Score v1.0 正式定稿（`docs/mock_codebook.md` "Isolation Score" 章节）：4 组件归一化方法 + 等权 0.25 + 文献对齐说明

### Added — Sprint 2 code modules (`src/`)

- `src/metrics.py` — in/out-degree, in/out-strength, weighted betweenness centrality, Cross_Team_Tie_Count (Boundary Spanner), Weak_Tie_Outbound_Count, Weak_Cross_Team_Tie_Count, Power User concentration (Top-5/Top-10 inbound share + Herfindahl index)
- `src/isolation_score.py` — 4-component Isolation Score with equal weights 0.25 (OutboundScarcity / WeakWeightShare / TargetConcentration / WeakBridgeDeficit), each normalized to [0, 1]
- `src/threshold.py` — Youden's-J-optimal τ_ROC + 3-tier layering (High / Medium / Low) + confusion matrix derivation
- `src/viz.py` — pyvis interactive topology with `nx.spring_layout` + virtual intra-team edges for spatial clustering (separation ratio ≈ 9.5× after tuning)

### Added — Sprint 2 delivery package (`sprints/sprint2/`)

- `sprints/sprint2/run_sprint2.py` — 一键编排 WS2–WS8，产出全部 10 个输出文件
- `sprints/sprint2/notebook.ipynb` — 演示版 notebook（8 cells）
- `sprints/sprint2/README.md` — DoD 清单、量化结果、Sprint 3 衔接
- `sprints/sprint2/sprint2_plan.md` — 计划文件（规划阶段生成）
- `sprints/sprint2/outputs/` 10 个文件：
  - `sprint2_nodes_with_metrics.csv` (300 × 20)
  - `sprint2_silent_individuals_shortlist.md` (Top 20)
  - `sprint2_silent_teams_aggregated.md` (6 teams)
  - `sprint2_power_user_concentration.md`
  - `sprint2_validation_report.md` (Scenario Injection Testing)
  - `sprint2_counter_metrics.md` (CM-1 / CM-2 / CM-3)
  - `sprint2_interactive_topology.html` (self-contained ~1 MB)
  - `sprint2_summary_report.md`
  - `sprint2_review_pack.md`
  - `sprint2_summary.json` (machine-readable)

### Added — Governance

- `Capstone/requirements.txt` — 正式声明 Sprint 1 + Sprint 2 的 Python 依赖（pandas, Pillow, numpy, networkx, scikit-learn, scipy, pyvis）

### Changed

- `src/generate_assets.py` 在 `build_edges()` 每条边写入时附加两列；`EDGE_COLUMNS` 列表扩展；`FREQ_WEIGHT_DECIMAL` / `TYPE_CODE` 常量新增
- Seed 保持 `5228`，已有字段值 bit-for-bit 不变（新列纯派生）

### Key validation results (Scenario Injection Testing)

- ROC-AUC = **0.9999**（目标 ≥ 0.80）
- τ_ROC = **0.6917**（Youden's J）
- Sensitivity = **1.0000**，Specificity = **0.9923**
- Confusion Matrix: TP=41, FP=2, TN=257, FN=0
- 所有 8 个注入 `hub` 在 in-degree Top-8（100% 精度）
- 所有 41 个注入 `island` 被 Flag=1（100% Recall）
- CM-3 Broker False Positive = **0**（模型自洽）

### Backward compatibility

- `sprints/sprint1/run_sprint1.py` 只读 `Interaction_Type` / `Interaction_Frequency` 字符串列，不受影响（已 smoke test 通过）
- `sprints/sprint1/data_snapshot/` 保留 v1.0.0 数据（无新列），用于历史追溯

### Migration notes

- Sprint 2 及后续管线应优先读新列 `Interaction_Frequency_Weight` 作为 edge weight
- Sprint 3 将使用 `Isolation_Risk_Flag`（τ_ROC = 0.6917）作为二分类目标 y

---

## [1.1.0] — 2026-04-23 — 目录治理重构

**触发原因**：Sprint 2 开工前进行项目级治理动作，建立"项目级常设 + Sprint 级交付包"的混合目录结构，避免数据真源分散、PID 偏差无处登记、历史文件与现行文件混放等问题。

### Added
- `Capstone/docs/`：项目级文档单一来源（迁入 PID、Project_Brief、codebook、survey、data_generation_notes）
- `Capstone/data/`：当前数据真源（live snapshot）
- `Capstone/src/`：跨 Sprint 可复用代码（迁入并改名 `generate_assets.py`）
- `Capstone/_archive/`：历史文件归档区，含 [`_archive/README.md`](../_archive/README.md) 治理规则
- `Capstone/sprints/sprintN/`：每个 Sprint 一个交付包（含 README、notebook、runner、outputs、data_snapshot、presentation）
- `docs/PID_delta_log.md`：PID ↔ 实现偏差登记入口（替代原本散落在 HTML 汇报页的零星脚注）
- `docs/CHANGELOG.md`（本文件）

### Changed
- `scripts/generate_sprint1_assets.py` → `src/generate_assets.py`（改名 + 路径常量指向 `data/` 与 `sprints/sprint1/outputs/`）
- `scripts/run_sprint1_execution.py` → `sprints/sprint1/run_sprint1.py`（改名 + 路径常量改用 `parents[2]` 解析 `Capstone/`）
- Sprint 1 演示 notebook（`sprint1_eda_and_topology_prototype.ipynb`） → `sprints/sprint1/notebook.ipynb`，并修复读 `data/` 与写 `sprints/sprint1/outputs/` 的相对路径

### Archived（旧目录整体归档至 `_archive/legacy_pre_restructure/`，保留追溯）
- `Capstone/notebooks/` → `_archive/legacy_pre_restructure/notebooks/`
- `Capstone/outputs/` → `_archive/legacy_pre_restructure/outputs/`
- `Capstone/scripts/` → `_archive/legacy_pre_restructure/scripts/`
- `Capstone/sprint1/`（旧的 Sprint 1 快照镜像） → `_archive/legacy_pre_restructure/sprint1/`

### Migration
- 任何下游脚本、CI、外部引用如需访问数据，统一使用 `Capstone/data/mock_data_nodes.csv` 与 `Capstone/data/mock_data_edges.csv`。
- Sprint 评审包路径：从 `sprint1/sprint1_presentation.html` 改为 `sprints/sprint1/presentation.html`。
- Sprint 1 时点冻结的数据快照保留在 `sprints/sprint1/data_snapshot/`，仅作历史核对，**不参与**当前管线。

---

## [1.0.0] — 2026-04-09 — Sprint 1 数据冻结（双表 schema）

**触发原因**：Sprint 1 完成 schema 冻结、生成与 DQ 校验，作为后续 Sprint 的稳定输入基线。

### Added
- 双表 schema：
  - `mock_data_nodes.csv`（节点属性表，含 `EMP_ID` / `Seniority` / `Team` / `Years_Exp` / `Profile_Type` / Sections A–H 行为信号 / `Isolation_Risk_Flag`）
  - `mock_data_edges.csv`（有向求助边表，含 `Source_EMP_ID` / `Target_EMP_ID` / `Interaction_Type` ∈ {Hard, Soft} / `Interaction_Frequency` ∈ {Daily, Weekly, Monthly, Rarely} / `Awareness_Score` ∈ 1–5 / `Energy_Score` ∈ 1–5 / `Nomination_Rank` ∈ 1–3）
- 生成参数：`seed = 5228`，`300 nodes / 1042 edges`
- Profile mix（archetype 注入比例）：`balanced 222 / island 41 / broker 29 / hub 8`
- Tie-strength 映射（Granovetter 1973）：Daily=4 / Weekly=3 / Monthly=2 / Rarely=1
- DQ Gate（`dq_gate_report.md`）：null / 枚举 / score 范围 / nomination rank 唯一性 / 节点引用完整性 全部 PASS

### Changed (vs v0)
- 从单表迁移到双表（节点属性 vs 关系信号分离）
- 引入 Cross & Parker (2004) 关系属性 `Awareness_Score` 与 `Energy_Score`，作为 edge 级属性而非独立交互类型
- `Profile_Type` 字段加入节点表，作为 archetype 注入的标签，支持 Sprint 3 的 ground-truth 验证

### Deprecated (取代 v0)
- 单表 `mock_data.csv` 及其聚合字段 `Peer_Nom_Tech` / `Peer_Nom_Client` / `Peer_Nom_Leader` / `Peer_Nom_Total` 一并废弃

### Removed
- `Region` 字段（GDPR 合规：no geolocation）— 详见 [`PID_delta_log.md`](PID_delta_log.md) D-01

---

## [0.1.0] — 2026-04-09 之前 — v0 单表初版（已废弃）

**状态**：已废弃，归档于 [`_archive/v0_single_table/mock_data.csv`](../_archive/v0_single_table/mock_data.csv)。

### Snapshot
- 单表结构，混合节点属性 + 简单聚合的提名信号
- 含 `Region` 字段
- 含 `Peer_Nom_*` 聚合字段（已被 row-level 边表替代）

### Why deprecated
- 不能承载 Cross & Parker 的 edge 级关系属性
- 与 GDPR 合规姿态冲突（`Region` 字段）
- 不利于 ONA 标准 join 与中心性计算

详见 [`PID_delta_log.md`](PID_delta_log.md) D-01、D-02。

---

## 维护说明

- 每次重大 schema / 数据生成 / 目录结构变更，**必须**追加新版本块到本文件顶部。
- 版本号遵循 [SemVer](https://semver.org/) 精神：MAJOR = 不兼容的 schema 改动；MINOR = 新增字段或目录但向后兼容；PATCH = 数据再生成（同 schema）。
- 每次新版本发布同时更新 [`_archive/README.md`](../_archive/README.md) 的"当前归档清单"。
