from __future__ import annotations

import csv
import random
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA_DIR = BASE / "data"
NODES_PATH = DATA_DIR / "mock_data_nodes.csv"
EDGES_PATH = DATA_DIR / "mock_data_edges.csv"
OUTPUTS = BASE / "sprints" / "sprint1" / "outputs"
DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUTS.mkdir(parents=True, exist_ok=True)

SEED = 5228
random.seed(SEED)

TEAMS = [
    "Information Management",
    "Data Engineering",
    "Solution Architecture",
    "Client Services",
    "Platform Engineering",
    "Analytics & BI",
]
SENIORITIES = ["Junior", "Mid-level", "Senior"]
FREQS = ["Daily", "Weekly", "Monthly", "Rarely"]
# Granovetter (1973) ordinal tie strength for ONA-literature alignment.
FREQ_WEIGHTS = {"Daily": 4, "Weekly": 3, "Monthly": 2, "Rarely": 1}
# Exponential-decay decimal weights (schema v1.2.0). Used for algorithmic inputs
# such as network edge weights, Isolation Score sub-components, and pyvis layout.
FREQ_WEIGHT_DECIMAL = {"Daily": 1.00, "Weekly": 0.67, "Monthly": 0.33, "Rarely": 0.10}
# Interaction_Type enumeration (schema v1.2.0). Hard=1, Soft=0. Slots 2/3 reserved
# for future extension (e.g., Advice, Escalation) per codebook.
TYPE_CODE = {"Hard": 1, "Soft": 0}

NODE_COLUMNS = [
    "EMP_ID","Seniority","Team","Years_Exp","Profile_Type",
    "A1_PostgreSQL","A2_Linux","A3_Python","A4_Cloud","A5_InfoMgmt","A6_Networking",
    "A7_DataAnalytics","A8_API","A9_TechConsult",
    "B1_English","B2_German","B3_French","B4_OtherLang",
    "C1_ClientMeetings","C2_ScopingSessions","C3_IndustryAdvice",
    "D1_KnowledgeSessions","D2_MentoringCount","D3_CrossTeamContrib",
    "E1_TeamLeadCount","E2_EscalationsToMe","E3_UnblockCount",
    "F1_IncidentsCalled","F2_ProblemConsults","F3_InnovationsAdopted",
    "G1_MultiCountryProj","G2_CulturalBridging",
    "H1_StakeholderExplain","H2_DocsAuthored","H3_PresentationsGiven",
    "Isolation_Risk_Flag",
]

EDGE_COLUMNS = [
    "Source_EMP_ID",
    "Target_EMP_ID",
    "Interaction_Type",
    "Interaction_Type_Code",
    "Interaction_Frequency",
    "Interaction_Frequency_Weight",
    "Awareness_Score",
    "Energy_Score",
    "Nomination_Rank",
]


def clamp(v: int, lo: int = 0, hi: int = 5) -> int:
    return max(lo, min(hi, v))


def pick_profile() -> str:
    r = random.random()
    if r < 0.06:
        return "hub"
    if r < 0.14:
        return "broker"
    if r < 0.29:
        return "island"
    return "balanced"


def gen_node(emp_id: str, profile: str) -> dict[str, str]:
    if profile == "hub":
        seniority = random.choices(["Senior", "Mid-level"], weights=[0.7, 0.3])[0]
        years = random.randint(8, 22)
        hard_base, soft_base, consult = 4, 4, 5
        iso = 0
    elif profile == "broker":
        seniority = random.choices(["Mid-level", "Senior"], weights=[0.8, 0.2])[0]
        years = random.randint(5, 16)
        hard_base, soft_base, consult = 2, 4, 2
        iso = 0
    elif profile == "island":
        seniority = random.choices(["Junior", "Mid-level"], weights=[0.65, 0.35])[0]
        years = random.randint(1, 10)
        hard_base, soft_base, consult = 2, 1, 1
        iso = 1
    else:
        seniority = random.choices(SENIORITIES, weights=[0.25, 0.55, 0.2])[0]
        years = random.randint(2, 18)
        hard_base, soft_base, consult = 3, 3, 2
        iso = 0

    team = random.choice(TEAMS)

    row = {
        "EMP_ID": emp_id,
        "Seniority": seniority,
        "Team": team,
        "Years_Exp": str(years),
        "Profile_Type": profile,
    }

    for c in ["A1_PostgreSQL","A2_Linux","A3_Python","A4_Cloud","A5_InfoMgmt","A6_Networking","A7_DataAnalytics","A8_API"]:
        row[c] = str(clamp(int(round(random.gauss(hard_base, 1.0)))))
    row["A9_TechConsult"] = str(clamp(int(round(random.gauss(consult, 1.0)))))

    lang_base = 4 if profile in {"hub", "broker"} else (3 if profile == "balanced" else 2)
    row["B1_English"] = str(clamp(int(round(random.gauss(lang_base, 0.8)))))
    row["B2_German"] = str(clamp(int(round(random.gauss(2 if team in {"Client Services", "Solution Architecture"} else 1, 0.8)))))
    row["B3_French"] = str(clamp(int(round(random.gauss(1, 0.8)))))
    row["B4_OtherLang"] = str(clamp(int(round(random.gauss(1, 0.8)))))

    for c in ["C1_ClientMeetings","C2_ScopingSessions","C3_IndustryAdvice","D1_KnowledgeSessions","D2_MentoringCount","D3_CrossTeamContrib","E1_TeamLeadCount","E2_EscalationsToMe","E3_UnblockCount","F1_IncidentsCalled","F2_ProblemConsults","F3_InnovationsAdopted","G1_MultiCountryProj","G2_CulturalBridging","H1_StakeholderExplain","H2_DocsAuthored","H3_PresentationsGiven"]:
        row[c] = str(clamp(int(round(random.gauss(soft_base, 1.1)))))

    row["Isolation_Risk_Flag"] = str(iso)
    return row


def weighted_freq(profile: str, tie_type: str) -> str:
    if profile == "hub":
        weights = [0.45, 0.35, 0.15, 0.05]
    elif profile == "broker" and tie_type == "Soft":
        weights = [0.30, 0.45, 0.20, 0.05]
    elif profile == "island":
        weights = [0.05, 0.15, 0.35, 0.45]
    else:
        weights = [0.2, 0.4, 0.25, 0.15]
    return random.choices(FREQS, weights=weights)[0]


def score_from_freq(freq: str, profile: str, tie_type: str) -> tuple[int, int]:
    base = {"Daily": 5, "Weekly": 4, "Monthly": 3, "Rarely": 2}[freq]
    awareness = base + random.choice([-1, 0, 0, 1])
    energy = base + random.choice([-1, 0, 1])

    if profile == "broker" and tie_type == "Soft":
        energy += 1
    if profile == "island":
        awareness -= 1

    return clamp(awareness, 1, 5), clamp(energy, 1, 5)


def build_edges(nodes: list[dict[str, str]]) -> list[dict[str, str]]:
    emp_ids = [n["EMP_ID"] for n in nodes]
    profiles = {n["EMP_ID"]: n["Profile_Type"] for n in nodes}
    teams = {n["EMP_ID"]: n["Team"] for n in nodes}

    hubs = [n["EMP_ID"] for n in nodes if n["Profile_Type"] == "hub"]
    brokers = [n["EMP_ID"] for n in nodes if n["Profile_Type"] == "broker"]
    if len(hubs) < 3:
        hubs = emp_ids[:3]
    if len(brokers) < 5:
        brokers = emp_ids[3:8]

    edges: list[dict[str, str]] = []

    for src in emp_ids:
        p = profiles[src]

        if p == "hub":
            hard_n = random.randint(1, 2)
            soft_n = random.randint(1, 2)
        elif p == "broker":
            hard_n = random.randint(0, 1)
            soft_n = random.randint(2, 3)
        elif p == "island":
            hard_n = random.randint(0, 1)
            soft_n = random.randint(0, 1)
            if random.random() < 0.60:
                hard_n = 0
            if random.random() < 0.75:
                soft_n = 0
        else:
            hard_n = random.randint(1, 3)
            soft_n = random.randint(1, 3)

        # HARD nominations
        hard_candidates = [e for e in emp_ids if e != src]
        hard_targets = []
        if p != "island":
            if random.random() < 0.75:
                hard_targets.append(random.choice(hubs))
        while len(hard_targets) < hard_n:
            t = random.choice(hard_candidates)
            if t not in hard_targets:
                hard_targets.append(t)

        rank = 1
        for tgt in hard_targets[:3]:
            freq = weighted_freq(p, "Hard")
            a, e = score_from_freq(freq, p, "Hard")
            edges.append({
                "Source_EMP_ID": src,
                "Target_EMP_ID": tgt,
                "Interaction_Type": "Hard",
                "Interaction_Type_Code": str(TYPE_CODE["Hard"]),
                "Interaction_Frequency": freq,
                "Interaction_Frequency_Weight": f"{FREQ_WEIGHT_DECIMAL[freq]:.2f}",
                "Awareness_Score": str(a),
                "Energy_Score": str(e),
                "Nomination_Rank": str(rank),
            })
            rank += 1

        # SOFT nominations
        soft_targets = []
        if p in {"broker", "balanced", "hub"} and random.random() < 0.70:
            soft_targets.append(random.choice(brokers))

        soft_candidates = [e for e in emp_ids if e != src]
        while len(soft_targets) < soft_n:
            # prefer cross-team soft ties
            if random.random() < 0.65:
                pool = [e for e in soft_candidates if teams[e] != teams[src]]
                t = random.choice(pool if pool else soft_candidates)
            else:
                t = random.choice(soft_candidates)
            if t not in soft_targets:
                soft_targets.append(t)

        rank = 1
        for tgt in soft_targets[:3]:
            freq = weighted_freq(p, "Soft")
            a, e = score_from_freq(freq, p, "Soft")
            edges.append({
                "Source_EMP_ID": src,
                "Target_EMP_ID": tgt,
                "Interaction_Type": "Soft",
                "Interaction_Type_Code": str(TYPE_CODE["Soft"]),
                "Interaction_Frequency": freq,
                "Interaction_Frequency_Weight": f"{FREQ_WEIGHT_DECIMAL[freq]:.2f}",
                "Awareness_Score": str(a),
                "Energy_Score": str(e),
                "Nomination_Rank": str(rank),
            })
            rank += 1

    return edges


def write_csv(path: Path, rows: list[dict[str, str]], cols: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)


def dq_checks(nodes: list[dict[str, str]], edges: list[dict[str, str]]) -> dict[str, str]:
    issues = []

    # required non-empty
    for i, r in enumerate(edges, 2):
        for c in EDGE_COLUMNS:
            if r.get(c, "") == "":
                issues.append(f"row {i}: empty {c}")

    # domain checks
    valid_type = {"Hard", "Soft"}
    valid_freq = set(FREQS)
    for i, r in enumerate(edges, 2):
        if r["Interaction_Type"] not in valid_type:
            issues.append(f"row {i}: invalid Interaction_Type")
        if r["Interaction_Frequency"] not in valid_freq:
            issues.append(f"row {i}: invalid Interaction_Frequency")
        for s in ["Awareness_Score", "Energy_Score", "Nomination_Rank"]:
            try:
                v = int(r[s])
            except Exception:
                issues.append(f"row {i}: non-int {s}")
                continue
            if s in {"Awareness_Score", "Energy_Score"} and not (1 <= v <= 5):
                issues.append(f"row {i}: out-of-range {s}")
            if s == "Nomination_Rank" and not (1 <= v <= 3):
                issues.append(f"row {i}: invalid rank")

    # rank uniqueness within (source, type)
    seen = set()
    for i, r in enumerate(edges, 2):
        key = (r["Source_EMP_ID"], r["Interaction_Type"], r["Nomination_Rank"])
        if key in seen:
            issues.append(f"row {i}: duplicate rank within source/type")
        seen.add(key)

    # link consistency
    node_set = {n["EMP_ID"] for n in nodes}
    for i, r in enumerate(edges, 2):
        if r["Source_EMP_ID"] not in node_set or r["Target_EMP_ID"] not in node_set:
            issues.append(f"row {i}: unknown node reference")

    return {
        "nodes": str(len(nodes)),
        "edges": str(len(edges)),
        "dq_passed": "true" if not issues else "false",
        "issue_count": str(len(issues)),
        "issues_preview": " | ".join(issues[:10]) if issues else "none",
    }


def build_eda(nodes: list[dict[str, str]], edges: list[dict[str, str]]) -> None:
    node_map = {n["EMP_ID"]: n for n in nodes}
    indeg = Counter()
    outdeg = Counter()
    inw = Counter()
    outw = Counter()

    for e in edges:
        s, t = e["Source_EMP_ID"], e["Target_EMP_ID"]
        w = FREQ_WEIGHTS[e["Interaction_Frequency"]]
        outdeg[s] += 1
        indeg[t] += 1
        outw[s] += w
        inw[t] += w

    # per-node profile
    rows = []
    for n in nodes:
        eid = n["EMP_ID"]
        rows.append({
            "EMP_ID": eid,
            "Team": n["Team"],
            "Profile_Type": n["Profile_Type"],
            "Out_Degree": outdeg[eid],
            "In_Degree": indeg[eid],
            "Out_Strength": outw[eid],
            "In_Strength": inw[eid],
            "Isolation_Risk_Flag": n["Isolation_Risk_Flag"],
        })

    with (OUTPUTS / "eda_profile_v1.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # summary text
    by_profile = Counter(n["Profile_Type"] for n in nodes)
    by_type = Counter(e["Interaction_Type"] for e in edges)
    by_freq = Counter(e["Interaction_Frequency"] for e in edges)

    top_hubs = sorted(rows, key=lambda r: (r["In_Degree"], r["In_Strength"]), reverse=True)[:10]
    top_islands = sorted(rows, key=lambda r: (r["Out_Degree"], r["Out_Strength"]))[:10]

    with (OUTPUTS / "dq_gate_report.md").open("w", encoding="utf-8") as f:
        f.write("# Sprint 1 Data Quality Gate\n\n")
        dq = dq_checks(nodes, edges)
        f.write(f"- DQ Passed: **{dq['dq_passed']}**\n")
        f.write(f"- Nodes: **{dq['nodes']}**\n")
        f.write(f"- Edges: **{dq['edges']}**\n")
        f.write(f"- Issue count: **{dq['issue_count']}**\n")
        f.write(f"- Issues preview: {dq['issues_preview']}\n\n")

        f.write("## Distribution Snapshot\n")
        f.write(f"- Profile mix: {dict(by_profile)}\n")
        f.write(f"- Interaction type mix: {dict(by_type)}\n")
        f.write(f"- Frequency mix: {dict(by_freq)}\n\n")

        f.write("## Top 10 In-Degree (Hub Candidates)\n")
        for r in top_hubs:
            f.write(f"- {r['EMP_ID']}: in_degree={r['In_Degree']}, in_strength={r['In_Strength']}\n")

        f.write("\n## Top 10 Lowest Out-Degree (Silent-Island Candidates)\n")
        for r in top_islands:
            f.write(f"- {r['EMP_ID']}: out_degree={r['Out_Degree']}, out_strength={r['Out_Strength']}\n")


def draw_network(edges: list[dict[str, str]]) -> None:
    """Create a lightweight topology prototype PNG without matplotlib/networkx."""
    try:
        from PIL import Image, ImageDraw

        width, height = 1400, 900
        img = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(img)

        # Use a deterministic subset for readability.
        subset = edges[:300]
        node_ids = sorted({e["Source_EMP_ID"] for e in subset} | {e["Target_EMP_ID"] for e in subset})
        if not node_ids:
            img.save(OUTPUTS / "network_prototype_v1.png")
            return

        # Deterministic radial-ish placement by hash order.
        cx, cy = width // 2, height // 2
        radius = min(width, height) * 0.38
        positions = {}
        for i, n in enumerate(node_ids):
            angle = 2 * 3.1415926 * i / len(node_ids)
            x = int(cx + radius * (0.85 if i % 2 else 1.0) * (random.Random(n).random() * 0.4 + 0.6) * __import__("math").cos(angle))
            y = int(cy + radius * (0.85 if i % 3 else 1.0) * (random.Random(n + "_y").random() * 0.4 + 0.6) * __import__("math").sin(angle))
            positions[n] = (x, y)

        # Draw edges (weighted by frequency).
        for e in subset:
            s, t = e["Source_EMP_ID"], e["Target_EMP_ID"]
            x1, y1 = positions[s]
            x2, y2 = positions[t]
            w = FREQ_WEIGHTS[e["Interaction_Frequency"]]
            color = (120, 120, 120) if e["Interaction_Type"] == "Hard" else (80, 120, 180)
            draw.line((x1, y1, x2, y2), fill=color, width=max(1, w - 1))

        # Draw nodes.
        indeg = Counter(e["Target_EMP_ID"] for e in subset)
        for n, (x, y) in positions.items():
            r = 4 + min(14, indeg.get(n, 0))
            fill = (220, 90, 90) if indeg.get(n, 0) >= 8 else (90, 140, 220)
            draw.ellipse((x - r, y - r, x + r, y + r), fill=fill, outline=(40, 40, 40))

        draw.text((20, 20), "Sprint 1 Network Topology Prototype v1", fill=(20, 20, 20))
        draw.text((20, 50), "Hard ties: gray | Soft ties: blue | Larger nodes: higher inbound", fill=(50, 50, 50))
        img.save(OUTPUTS / "network_prototype_v1.png")
    except Exception:
        # Last-resort tiny valid PNG header (transparent pixel)
        raw = (
            b"\\x89PNG\\r\\n\\x1a\\n\\x00\\x00\\x00\\rIHDR\\x00\\x00\\x00\\x01\\x00\\x00\\x00\\x01"
            b"\\x08\\x06\\x00\\x00\\x00\\x1f\\x15\\xc4\\x89\\x00\\x00\\x00\\x0bIDATx\\x9cc\\x00\\x01\\x00\\x00\\x05\\x00\\x01"
            b"\\x0d\\n\\x2d\\xb4\\x00\\x00\\x00\\x00IEND\\xaeB`\\x82"
        )
        (OUTPUTS / "network_prototype_v1.png").write_bytes(raw)


def main() -> None:
    n_nodes = 300
    nodes = []
    for i in range(1, n_nodes + 1):
        emp_id = f"EMP_{i:03d}"
        profile = pick_profile()
        nodes.append(gen_node(emp_id, profile))

    edges = build_edges(nodes)

    write_csv(NODES_PATH, nodes, NODE_COLUMNS)
    write_csv(EDGES_PATH, edges, EDGE_COLUMNS)

    build_eda(nodes, edges)
    draw_network(edges)

    # concise generation notes (written into project-level docs/)
    notes = BASE / "docs" / "data_generation_notes.md"
    notes.parent.mkdir(parents=True, exist_ok=True)
    profile_counts = Counter(n["Profile_Type"] for n in nodes)
    with notes.open("w", encoding="utf-8") as f:
        f.write("# Data Generation Notes (schema v1.2.0)\n\n")
        f.write(f"- Seed: `{SEED}`\n")
        f.write(f"- Nodes generated: `{len(nodes)}`\n")
        f.write(f"- Edges generated: `{len(edges)}`\n")
        f.write(f"- Profile mix: `{dict(profile_counts)}`\n")
        f.write(
            "- Edge schema: `Source_EMP_ID, Target_EMP_ID, Interaction_Type, "
            "Interaction_Type_Code, Interaction_Frequency, Interaction_Frequency_Weight, "
            "Awareness_Score, Energy_Score, Nomination_Rank`\n"
        )
        f.write("- Tie-strength mapping (Granovetter ordinal): Daily=4, Weekly=3, Monthly=2, Rarely=1\n")
        f.write(
            "- Tie-strength mapping (v1.2.0 algorithmic, exponential decay): "
            "Daily=1.00, Weekly=0.67, Monthly=0.33, Rarely=0.10\n"
        )
        f.write("- Interaction_Type_Code mapping (v1.2.0): Hard=1, Soft=0 (slots 2/3 reserved)\n")
        f.write("- Archetype logic: hub (high inbound), broker (cross-team soft ties), island (low outbound)\n")


if __name__ == "__main__":
    main()
