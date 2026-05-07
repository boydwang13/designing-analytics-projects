# Capstone — Social Telemetry: Seeing the Silent Teams

**项目**：Detecting Hidden Support Needs in Canon EMEA Professional Services
**学生**：Bo Wang · MS Business Analytics · CEU
**Sponsor**：Martin Brüggemann · Canon EMEA Solution Consultant
**Manager**：Eduardo Arino de la Rubia
**当前状态**：Sprint 1 完成，进入 Sprint 2 前置清理阶段

---

## 项目概览

通过 ONA（组织网络分析）识别 EMEA Professional Services 内部的"silent teams"（沉默团队）与"central hubs"（过度依赖的中心节点）。GDPR 合规约束下，使用 Python 生成的合成数据建模，采用 Cross & Parker (2004) 关系属性框架与 Granovetter (1973) 强弱连接理论，最终交付：(1) 网络拓扑可视化图、(2) Isolation Score 与名单、(3) 基于个人属性的孤立风险预测模型。

详细方法、范围、Sprint 计划见 [`docs/PID.md`](docs/PID.md)。

---

## 目录结构

```
Capstone/
├── README.md                    ← 本文件
│
├── docs/                        项目级文档（长期、权威、单一来源）
│   ├── PID.md                   已签署 Project Initiation Document（只读）
│   ├── Project_Brief.md         课程 Analytics Project Brief 框架应用
│   ├── mock_codebook.md         数据字典（nodes + edges 双表）
│   ├── mock_survey.md           行为信号问卷（Sections A–H + I + J）
│   ├── data_generation_notes.md 数据生成参数与逻辑摘要
│   ├── PID_delta_log.md         PID ↔ 实现偏差登记（审计入口）
│   └── CHANGELOG.md             schema / 数据 / 目录版本演进
│
├── data/                        当前数据真源（live snapshot）
│   ├── mock_data_nodes.csv      300 nodes
│   └── mock_data_edges.csv      1042 edges
│
├── src/                         跨 Sprint 可复用代码
│   └── generate_assets.py       数据生成器（seed=5228）
│
├── _archive/                    历史文件归档区（只读、严禁脚本读取）
│   ├── README.md                归档治理规则
│   └── v0_single_table/         已废弃的单表 schema
│       └── mock_data.csv
│
└── sprints/                     每个 Sprint 一个交付包
    └── sprint1/
        ├── README.md            Sprint 1 DoD 清单 + 文件索引
        ├── notebook.ipynb       演示 notebook
        ├── run_sprint1.py       一键执行脚本
        ├── outputs/             DQ 报告 / EDA / 网络图 / 摘要
        ├── data_snapshot/       Sprint 1 时点冻结的数据（仅追溯）
        ├── presentation.html    Sponsor 评审页（双语）
        └── presentation_v2_short.html
```

---

## 如何在本项目上工作

| 你想做什么 | 应该看 / 改哪里 |
| :-- | :-- |
| 了解项目背景 / 范围 / 时间线 | [`docs/PID.md`](docs/PID.md) |
| 查 schema 字段定义 | [`docs/mock_codebook.md`](docs/mock_codebook.md) |
| 查问卷题目原文 | [`docs/mock_survey.md`](docs/mock_survey.md) |
| 检查 PID 与实际实现的偏差 | [`docs/PID_delta_log.md`](docs/PID_delta_log.md) |
| 跟踪 schema / 目录的演进史 | [`docs/CHANGELOG.md`](docs/CHANGELOG.md) |
| 在分析中读数据 | `Capstone/data/mock_data_nodes.csv` 和 `mock_data_edges.csv`（**唯一真源**） |
| 重新生成数据 | `python src/generate_assets.py`（seed=5228 保证可复现） |
| 看某次 Sprint 的演示交付 | `sprints/sprintN/`（注意：当前仅存在 sprint1） |
| 看历史废弃文件 | `_archive/`（**只读**，不要在脚本中读取） |

---

## 复现指引

```bash
cd Capstone

# 重新生成数据（覆盖 data/ 下的 CSV）
python src/generate_assets.py

# 跑 Sprint 1 全流程（DQ + EDA + 子图渲染 + 汇总报告）
python sprints/sprint1/run_sprint1.py
```

依赖声明：见 [`requirements.txt`](requirements.txt)。Python ≥ 3.10。核心库：`pandas`、`networkx`、`scikit-learn`、`scipy`、`pyvis`、`Pillow`。

---

## 当前状态与里程碑

| Sprint | 周次 | 状态 | 交付 |
| :-- | :-- | :-- | :-- |
| Sprint 0 | – | ✅ 完成 | PID 签署 |
| Sprint 1 | Weeks 1–2 | ✅ 完成 | 数据生成 + EDA + 静态拓扑原型，详见 [`sprints/sprint1/`](sprints/sprint1/) |
| Sprint 2 | Weeks 3–4 | ✅ 完成 | Centrality + Isolation Score v1.0 + 静默名单 + 交互式拓扑图 + Scenario Injection Testing（AUC 0.9999），详见 [`sprints/sprint2/`](sprints/sprint2/) |
| **Sprint 3** | **Weeks 5–6** | 🔄 准备中 | 预测模型（Logistic Regression + Random Forest） |
| Sprint 4 | Weeks 7–8 | ⏳ 未开始 | Final report + presentation（含 Scalability 章节） |
