"""Figure 2 - Triple Constraint for Project FLEX (all values are planning assumptions)."""
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

plt.rcParams["font.family"] = ["DejaVu Sans"]
fig, ax = plt.subplots(figsize=(9, 7.2))
ax.set_xlim(-0.5, 10.5); ax.set_ylim(-1.6, 9.2); ax.axis("off")

A, B, C = (5, 6.4), (1.2, 1.2), (8.8, 1.2)            # scope (top), time (left), cost (right)
ax.add_patch(Polygon([A, B, C], closed=True, fc="#f2f2f2", ec="black", lw=2))
ax.text(5, 3.0, "QUALITY\nsupplier approval standard:\nHREDD audit passed,\nsample approved", ha="center", va="center",
        fontsize=9, fontweight="bold")

def tag(x, y, head, body, kind, ha="center"):
    ax.text(x, y, head, ha=ha, fontsize=10.5, fontweight="bold")
    ax.text(x, y - 0.25, body, ha=ha, va="top", fontsize=8.6, linespacing=1.3)
    fill = {"FIXED": "black", "FLEXIBLE": "white", "TRADE-OFF": "#bfbfbf"}[kind]
    col = "white" if kind == "FIXED" else "black"
    ax.text(x, y + 0.42, kind, ha=ha, fontsize=8.5, fontweight="bold", color=col,
            bbox=dict(boxstyle="round,pad=0.25", fc=fill, ec="black"))

tag(5, 8.0, "SCOPE", "IN: US-bound footwear styles; Tier 1 and\nTier 2 visibility; pre-qualified second sources\nOUT: owning factories; apparel (phase 2)", "TRADE-OFF")
tag(1.2, 0.3, "TIME", "18 months (78 weeks)\n4 Jan 2027 to 3 Jul 2028\nup to +3 months tolerated", "FLEXIBLE")
tag(8.8, 0.3, "COST", "EUR 12.0m cap\nincl. EUR 1.0m reserve\n(0.05% of FY2025 sales)", "FIXED")
ax.text(5, -1.5, "Rule when risks hit: protect the budget, stretch time first, cut scope last "
        "(fewest second-source styles go first).", ha="center", fontsize=8.5, style="italic")
plt.savefig("fig2_triple_constraint.png", dpi=200, bbox_inches="tight", facecolor="white")
