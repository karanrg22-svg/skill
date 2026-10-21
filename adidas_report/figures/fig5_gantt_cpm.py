"""Figure 5 - Gantt chart with critical path (CPM computed in code), PERT range for task 3.3."""
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

START = dt.date(2027, 1, 4)
# id: (name, duration_weeks, predecessors)
T = {
    "1.1": ("Charter and steering committee", 4, []),
    "1.2": ("Stakeholder and communication plan", 4, ["1.1"]),
    "2.1": ("Requirements and vendor selection", 10, ["1.1"]),
    "2.2": ("Platform configuration and integration", 16, ["2.1"]),
    "2.3": ("Tier 1 data onboarding", 12, ["2.2"]),
    "2.4": ("Tier 2 mill mapping", 20, ["2.3"]),
    "3.1": ("Candidate factory selection", 6, ["1.1"]),
    "3.2": ("HREDD audits", 10, ["3.1"]),
    "3.3": ("Technical trials and sample approval", 24, ["3.2"]),
    "1.3B": ("Schedule buffer (supplier approval risk)", 4, ["3.3"]),
    "3.4": ("Commercial agreements", 8, ["1.3B"]),
    "4.1": ("Style-factory capability matrix", 8, ["3.1"]),
    "4.2": ("Switching process design", 10, ["4.1"]),
    "4.3": ("Simulated switch pilots", 6, ["4.2", "3.3"]),
    "5.1": ("Sourcing team training", 6, ["2.2"]),
    "5.2": ("Supplier onboarding workshops", 6, ["2.3"]),
    "5.3": ("Worker-voice integration", 6, ["3.2"]),
    "6.1": ("Control tower go-live", 4, ["2.3", "5.1"]),
    "6.2": ("Live switch rehearsal", 6, ["4.3", "3.4", "6.1"]),
    "6.3": ("KPI baseline and measurement", 10, ["6.2"]),
    "6.4": ("Lessons learned and handover", 4, ["6.3", "2.4"]),
    "1.4": ("Benefits tracking and close-out", 2, ["6.4"]),
}
MILESTONES = {"M1 Gate: platform live": "6.1", "M2 Gate: second sources approved": "3.4", "M3 Project complete": "1.4"}

def cpm(T):
    order, seen = [], set()
    def visit(k):
        if k in seen: return
        for p in T[k][2]: visit(p)
        seen.add(k); order.append(k)
    for k in T: visit(k)
    ES, EF = {}, {}
    for k in order:
        ES[k] = max([EF[p] for p in T[k][2]], default=0); EF[k] = ES[k] + T[k][1]
    end = max(EF.values()); LS, LF = {}, {}
    for k in reversed(order):
        succ = [s for s in T if k in T[s][2]]
        LF[k] = min([LS[s] for s in succ], default=end); LS[k] = LF[k] - T[k][1]
    return ES, EF, LS, LF, {k: LS[k] - ES[k] for k in T}, end

def date(w): return START + dt.timedelta(weeks=w)

if __name__ == "__main__":
    plt.rcParams["font.family"] = ["DejaVu Sans"]
    ES, EF, LS, LF, FL, END = cpm(T)
    ids = sorted(T, key=lambda k: (ES[k], k)); n = len(ids)
    fig, ax = plt.subplots(figsize=(13, 8))
    for i, k in enumerate(ids):
        y = n - i; crit = FL[k] == 0
        ax.barh(y, T[k][1], left=ES[k], height=0.6, color="black" if crit else "#bfbfbf", edgecolor="black",
                hatch="" if crit else "", zorder=3)
        if FL[k] > 0:
            ax.barh(y, FL[k], left=EF[k], height=0.25, color="white", edgecolor="black", hatch="////", zorder=2)
    ax.set_yticks([n - i for i in range(n)]); ax.set_yticklabels([f"{k}  {T[k][0]}" for k in ids], fontsize=8)
    # level-of-effort bar for monthly risk and tariff reviews (1.3)
    ax.barh(n + 1, END, left=0, height=0.35, color="white", edgecolor="black", hatch="..", zorder=3)
    ax.text(END / 2, n + 1, "1.3 Risk and tariff reviews (monthly, level of effort)", ha="center", va="center", fontsize=8,
            bbox=dict(fc="white", ec="none", pad=1), zorder=4)
    ax.set_yticks(list(ax.get_yticks()) + [n + 1]); ax.set_yticklabels(list(ax.get_yticklabels()[:-1]) + ["1.3  Risk management"], fontsize=8)
    for lab, k in MILESTONES.items():
        ax.scatter(EF[k], n + 0.2, marker="D", s=60, c="white", edgecolor="black", zorder=5)
        ax.axvline(EF[k], color="black", lw=0.6, ls=":", zorder=1)
        ax.text(EF[k] - 0.5 if k == "1.4" else EF[k] + 0.5, n + 0.55, lab.split(":")[0], fontsize=8, fontweight="bold", ha="right" if k == "1.4" else "left")
    ticks = list(range(0, END + 1, 13))
    ax.set_xticks(ticks); ax.set_xticklabels([f"wk {t}\n{date(t):%b %Y}" for t in ticks], fontsize=8)
    ax.set_xlim(0, END + 3); ax.set_ylim(0.2, n + 1.8); ax.grid(axis="x", color="#dddddd", zorder=0)
    ax.legend(handles=[Patch(fc="black", ec="black", label="Critical path (zero float)"),
                       Patch(fc="#bfbfbf", ec="black", label="Non-critical task"),
                       Patch(fc="white", ec="black", hatch="////", label="Float (slack)"),
                       Patch(fc="white", ec="black", hatch="..", label="Level of effort")], loc="upper center", bbox_to_anchor=(0.5, -0.09), ncol=4, fontsize=8, frameon=False)
    ax.set_title(f"Project FLEX: {END} weeks, {date(0):%d %b %Y} to {date(END):%d %b %Y}. "
                 "PERT for 3.3: O=18, M=24, P=36, expected 25 weeks, sd 3", fontsize=9.5)
    plt.tight_layout(); plt.savefig("fig5_gantt_cpm.png", dpi=200, facecolor="white")
    print("END", END, [k for k in ids if FL[k] == 0])
