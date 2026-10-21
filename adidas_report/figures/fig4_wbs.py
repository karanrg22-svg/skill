"""Figure 4 - Work Breakdown Structure (level 1 project, level 2 deliverables, level 3 work packages).
WBS is the master list: costs in EUR thousand; Appendix E and Figure 2 budget are derived from it."""
import textwrap
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

WBS = {
    "1 Programme governance": [("1.1", "Charter and steering committee", 150), ("1.2", "Stakeholder and communication plan", 200),
                               ("1.3", "Risk management and reserve", 1200), ("1.4", "Benefits tracking and close-out", 150)],
    "2 Multi-tier visibility platform": [("2.1", "Requirements and vendor selection", 300), ("2.2", "Platform configuration and integration", 2000),
                                         ("2.3", "Tier 1 data onboarding", 900), ("2.4", "Tier 2 mill mapping", 1100)],
    "3 Second-source qualification": [("3.1", "Candidate factory selection", 200), ("3.2", "HREDD audits", 700),
                                      ("3.3", "Technical trials and sample approval", 1500), ("3.4", "Commercial agreements", 300)],
    "4 Switching playbook": [("4.1", "Style-factory capability matrix", 250), ("4.2", "Switching process design", 350),
                             ("4.3", "Simulated switch pilots", 500)],
    "5 Capability and change": [("5.1", "Sourcing team training", 250), ("5.2", "Supplier onboarding workshops", 350),
                                ("5.3", "Worker-voice integration", 300)],
    "6 Pilot, rollout, benefits": [("6.1", "Control tower go-live", 400), ("6.2", "Live switch rehearsal", 500),
                                   ("6.3", "KPI baseline and measurement", 250), ("6.4", "Lessons learned and handover", 150)],
}
BUDGET_K = 12000
assert sum(c for v in WBS.values() for *_, c in v) == BUDGET_K

if __name__ == "__main__":
    plt.rcParams["font.family"] = ["DejaVu Sans"]
    fig, ax = plt.subplots(figsize=(14, 7.5)); ax.set_xlim(0, 14); ax.set_ylim(0, 7.5); ax.axis("off")
    def box(x, y, w, h, t, fill, size=7.4, bold=False):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.06", fc=fill, ec="black", lw=1))
        ax.text(x + w / 2, y + h / 2, textwrap.fill(t, 60 if size >= 10 else (24 if bold else 26)), ha="center", va="center", fontsize=size, fontweight="bold" if bold else "normal", linespacing=1.15)
    box(4.5, 6.7, 5, 0.6, "0 Project FLEX: flexible sourcing programme (EUR 12.0m)", "#d9d9d9", 10, True)
    w = 2.2
    for i, (head, wps) in enumerate(WBS.items()):
        x = 0.1 + i * 2.3
        ax.plot([7, 7], [6.7, 6.45], color="black"); 
        ax.plot([x + w / 2, x + w / 2], [6.45, 6.2], color="black")
        box(x, 5.5, w, 0.7, head, "#bfbfbf", 7.8, True)
        for j, (wid, name, cost) in enumerate(wps):
            y = 4.75 - j * 0.95
            ax.plot([x + 0.05, x + 0.05], [5.5, y + 0.4], color="black", lw=0.8)
            ax.plot([x + 0.05, x + 0.15], [y + 0.4, y + 0.4], color="black", lw=0.8)
            box(x + 0.15, y, w - 0.15, 0.8, f"{wid} {name}", "white")
    ax.plot([0.1 + w / 2, 0.1 + 5 * 2.3 + w / 2], [6.45, 6.45], color="black")
    ax.text(7, 0.3, "Level 1 = project, level 2 = six deliverables, level 3 = 22 work packages. Numbers match the Gantt task IDs (Figure 5).",
            ha="center", fontsize=8.5, style="italic")
    plt.savefig("fig4_wbs.png", dpi=200, bbox_inches="tight", facecolor="white")
