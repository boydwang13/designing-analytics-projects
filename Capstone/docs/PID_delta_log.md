# PID ↔ Implementation Delta Log

**目的**：PID 是已签署的项目契约文件，**不可改动**。在执行过程中，细节实现会与 PID 文字描述存在偏差。本文件**显式登记**这些偏差，便于 Sponsor、Faculty Supervisor、Capstone Manager 以及答辩委员会**一目了然地审计**：哪些是有意为之、哪些不影响项目大方向、哪些理由站得住。

**适用范围**：本登记只覆盖**实现细节偏差**；如果偏差大到改变 Key Problem / Objective / Primary Deliverable，则必须升级为 PID 修订流程，而不是登记到本文件。

**版本控制**：每条偏差都标注首次记录日期；如后续有进一步偏移或回归，追加新条目而非覆盖原条目。

---

## 偏差登记表

| # | PID 原文/承诺 | 实际实现 | 偏差类型 | 偏差理由 | 对 Key Problem / Objective / Primary Deliverable 的影响 | 首次记录日期 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **D-01** | Sprint 1 描述："incorporating node attributes (e.g., skills, tenure, **region**) and connections" （第 82 行附近） | 数据 schema **删除** `Region` 字段；改用 `Team` / `Seniority` 作为子群体代理。详见 [`docs/mock_codebook.md`](mock_codebook.md) "Removed / obsolete fields" 章节。 | 字段删减 | (1) 严格 GDPR 合规要求："no geolocation"；(2) Sponsor (Martin) 在 Sprint 0 评审中明确同意去掉地理标识。`Team` 已能覆盖大部分子群体差异需求。 | **无影响**。Key Problem 关注 silent teams 的识别（基于网络结构而非地理），Objective 的 ONA 拓扑可直接基于 `Team` 维度分析；Primary Deliverable（拓扑图）不依赖 region 维度。 | 2026-04-23 |
| **D-02** | PID 第 82–83 行 Sprint 1 表述："Generate a large-scale synthetic dataset (Mock Data) … incorporating node attributes … and connections" — 未明确表示双表结构 | 实际采用 **双表 schema**：`mock_data_nodes.csv`（节点属性） + `mock_data_edges.csv`（有向 Hard/Soft 求助边 + per-edge `Awareness_Score` / `Energy_Score`）。详见 [`docs/mock_codebook.md`](mock_codebook.md) Tables 1 & 2。 | 数据建模增强 | 单表无法承载 Cross & Parker (2004) 的关系属性（Awareness / Energy 必须在 edge 级），且节点属性与连接信号混在一张表会破坏 ONA 的标准 join 模式。双表是 ONA 行业标准。 | **强化 Objective**。原 Objective 要求"build a network topology visualization map"，双表 schema 让中心性、Isolation Score、broker 分析在 Sprint 2/3 可直接执行，无须返工改表。 | 2026-04-23 |
| **D-03** | PID 第 51 行 "Data Source": 仅说"generating a synthetic dataset (Mock Data) using Python/AI" | 引入 **archetype 注入机制**：`balanced` / `hub` / `broker` / `island` 四种行为画像按比例（222 / 8 / 29 / 41）注入，配合随机扰动生成。详见 [`docs/data_generation_notes.md`](data_generation_notes.md)。 | 方法细化 | 为 Sponsor 在 PID 第 66 条要求的 **Scenario Injection Testing**（"intentionally inject known behavioral archetypes…"）提供可控基线；同时为 Sprint 3 预测模型提供 ground-truth 用于验证。 | **支持 Sponsor Validation**。本偏差是为了实现 PID 中"Validation of Accuracy & Credibility"段落明确要求的 scenario injection；属于实现 PID 而非偏离 PID。 | 2026-04-23 |
| **D-04** | PID 第 43 行 "Interim Deliverables: Bi-weekly progress updates presented directly via Jupyter Notebooks" | 除 Notebook 外，额外交付**双语（中英）HTML 评审页**（[`sprints/sprint1/presentation.html`](../sprints/sprint1/presentation.html)） | 交付增强 | Notebook 适合技术演示，但 Sponsor 双周评审需要更结构化、可分享、可打印的叙事载体；双语版本同时方便 Sponsor (Martin) 与 Faculty Supervisor 阅读。 | **无影响、纯增量**。Notebook 仍是主交付，HTML 是补充。 | 2026-04-23 |
| **D-05** | PID 第 80 行 Sprint 0 描述："Draft and sign the Project Initiation Document" — 隐含 PID 是 Sprint 0 的唯一交付 | 项目初期实际产出还包括 [`docs/Project_Brief.md`](Project_Brief.md)（沿用课程 Analytics Project Brief 框架）和 [`docs/mock_survey.md`](mock_survey.md)（行为信号问卷设计） | 交付增强 | 课程要求每位学生用 Analytics Project Brief 完成 scenario 作业；问卷设计是数据生成的前置文件，等同于"测量工具规约"。两者强化项目可审计性。 | **无影响、纯增量**。 | 2026-04-23 |

---

## 大方向一致性自检

下表逐项验证：当前实现是否仍然在 PID 大方向之内（一致 = OK；偏离 = NEED-REVIEW）。

| PID 大方向条目 | 当前实现是否一致？ | 证据 |
| :-- | :-- | :-- |
| **Key Problem**：识别 silent teams / hidden support needs | ✅ OK | Sprint 2 完成 Isolation Score v1.0 + Top 20 静默名单 + Team 级聚合表。 |
| **Objective**：ONA 拓扑 + 静默孤岛识别 + 个人风险预测 | ✅ OK | Sprint 2 完成前两项；Sprint 3 进入预测建模。 |
| **Primary Deliverable**：Network Topology Visualization Map | ✅ OK + 升级 | Sprint 1 交付静态 PNG（[`sprints/sprint1/outputs/network_prototype_v1.png`](../sprints/sprint1/outputs/network_prototype_v1.png)）；Sprint 2 升级为交互式 pyvis HTML（[`sprints/sprint2/outputs/sprint2_interactive_topology.html`](../sprints/sprint2/outputs/sprint2_interactive_topology.html)），支持 Team 空间聚类 + hover tooltip。 |
| **MVP Fallback**：Ranked List of Silent Teams | ✅ OK | Sprint 2 交付 [`sprint2_silent_individuals_shortlist.md`](../sprints/sprint2/outputs/sprint2_silent_individuals_shortlist.md)（Top 20 个人）+ [`sprint2_silent_teams_aggregated.md`](../sprints/sprint2/outputs/sprint2_silent_teams_aggregated.md)（6 个 team 聚合）。 |
| **GDPR 合规**："no production email or live IT system data" | ✅ OK + 强化 | 不仅未触碰真实数据，schema 层面也去掉了 `Region` 字段（D-01）。 |
| **Sponsor Validation**：Scenario Injection Testing | ✅ OK + 强验证 | Sprint 2 正式跑完 Scenario Injection Testing：AUC = **0.9999**，Sensitivity = 1.0，Specificity = 0.99（[`sprint2_validation_report.md`](../sprints/sprint2/outputs/sprint2_validation_report.md)）。 |
| **Methodology**：ONA + Power User + Broker + Failure Analysis | ✅ OK | Sprint 2 全覆盖：Power User（集中度报告）+ Broker（betweenness + Cross_Team_Tie_Count）+ Failure Analysis（Isolation Score + 静默名单）。 |
| **Predictive Model**：Logistic Regression + Random Forest | ⏳ 待启动 | 计划在 Sprint 3 落地，y = `Isolation_Risk_Flag`（τ_ROC = 0.6917 已定）。 |

**结论**：截至 Sprint 2 结束，所有 PID 大方向条目依然一致或已升级。无 NEED-REVIEW 项。

---

## 维护说明

- 每发现一处新的 PID ↔ 实现偏差，**立即**追加新行（`D-NN`）到上方表格。
- 偏差升级判定：如果某条偏差影响"大方向一致性自检"中任一行从 OK 变为 NEED-REVIEW，则必须停下来与 Sponsor / Capstone Manager 讨论，决定是修订 PID 还是回归实现。
- 本文件随 [`docs/CHANGELOG.md`](CHANGELOG.md) 一起作为 Sprint 评审、答辩、handoff 三类场景的**标准审计入口**。
