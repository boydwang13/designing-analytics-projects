# `_archive/` — 历史文件归档区

本目录用于保存 **已被现行设计取代** 的历史数据 / 文档 / 代码版本，目的是保留项目的可追溯性（reproducibility、审计、答辩举证）。

---

## 治理规则（重要）

1. **只读、仅作追溯。** 严禁在任何**当前**脚本、notebook 或交付物中读取本目录内的文件；当前数据真源在 `Capstone/data/`，当前文档在 `Capstone/docs/`。
2. **每个子目录对应一次重大 schema / 设计变更。** 子目录命名：`vN_<short_label>/`，附本目录的 `CHANGELOG.md`（位于 `docs/CHANGELOG.md`）记录变更原因与时间点。
3. **不允许覆盖。** 一旦归档，文件视为 immutable；如需修订归档说明，更新 `docs/CHANGELOG.md`，而非编辑归档文件本体。
4. **不参与生产管线。** CI / 自动化脚本不应扫描或加载 `_archive/` 内容。

---

## 当前归档清单

### `v0_single_table/`

| 文件 | 原位置 | 归档时间 | 取代设计 | 取代原因 |
| :--- | :--- | :--- | :--- | :--- |
| `mock_data.csv` | `Capstone/mock_data.csv`（根目录） | 2026-04-23 | `Capstone/data/mock_data_nodes.csv` + `Capstone/data/mock_data_edges.csv`（双表） | ① 引入 Cross & Parker 关系属性后需要 edge 级 `Awareness_Score` / `Energy_Score`，单表不可承载；② GDPR 合规去除 `Region` 字段；③ 旧 `Peer_Nom_*` 聚合字段被 row-level 边表替代。详见 `docs/mock_codebook.md` "Removed / obsolete fields" 与 `docs/CHANGELOG.md` v0→v1 条目。|

### `legacy_pre_restructure/`

整体归档了 1.1.0 目录治理重构之前的旧工作目录布局。这些文件的最新版本已迁入新结构对应位置，本目录仅作历史追溯。

| 子目录 | 原位置 | 归档时间 | 已被取代为 | 备注 |
| :--- | :--- | :--- | :--- | :--- |
| `notebooks/` | `Capstone/notebooks/` | 2026-04-23 | `sprints/sprint1/notebook.ipynb` | 含两份 notebook：`sprint1_pipeline.ipynb`（v1 草稿）和 `sprint1_eda_and_topology_prototype.ipynb`（v2 演示版，已迁出更新） |
| `outputs/` | `Capstone/outputs/` | 2026-04-23 | `sprints/sprint1/outputs/` | 早期版本（Apr 9 16:41/17:12），后被 `sprint1/outputs/` 的 Apr 9 17:53 版本取代 |
| `scripts/` | `Capstone/scripts/` | 2026-04-23 | `src/generate_assets.py` + `sprints/sprint1/run_sprint1.py` | 已改名并修复路径常量 |
| `sprint1/` | `Capstone/sprint1/` | 2026-04-23 | `sprints/sprint1/` | 旧的 Sprint 1 镜像快照目录（含 data/、docs/、notebooks/、outputs/、scripts/、两份 presentation HTML），全部内容已迁入新结构 |

---

## 后续归档建议（流程）

如未来出现新一次 schema / 数据生成逻辑的重大调整：

1. 在 `docs/CHANGELOG.md` 中追加新版本条目（说明变更内容 + 时间 + 触发原因）。
2. 在 `_archive/` 下新建子目录 `vN_<short_label>/`，把被取代的文件 mv 进去。
3. 更新本 README 的"当前归档清单"表格。
4. **不要**修改任何已归档文件。
