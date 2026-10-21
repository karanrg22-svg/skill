"""Figure 3 - Power/interest grid (Mendelow) with expected movement arrows."""
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["DejaVu Sans"]
# name: (interest, power, moves_to or None, marker label)
S = {
    "S1 Executive Board":          (8.0, 9.0, None),
    "S2 Global Sourcing team":     (9.5, 7.0, None),
    "S3 Partner factories (Tier 1)": (9.0, 5.8, None),
    "S4 Factory workers":          (8.0, 1.8, (8.0, 3.6)),
    "S5 Logistics partners":       (6.0, 4.8, None),
    "S6 Wholesale and retail customers": (3.6, 6.0, None),
    "S7 Regulators and customs":   (2.6, 8.2, (4.8, 8.2)),
    "S8 Investors":                (4.2, 8.8, None),
    "S9 NGOs and unions":          (8.4, 3.6, (8.4, 5.4)),
    "S10 IT platform vendor":      (6.8, 2.6, None),
}
fig, ax = plt.subplots(figsize=(9.5, 7.2))
ax.set_xlim(0, 10.5); ax.set_ylim(0, 10.5)
ax.axvline(5, color="black", lw=1); ax.axhline(5, color="black", lw=1)
for x, y, t in [(2.5, 10.1, "KEEP SATISFIED"), (7.7, 10.1, "MANAGE CLOSELY"),
                (2.5, 0.2, "MONITOR"), (7.7, 0.2, "KEEP INFORMED")]:
    ax.text(x, y, t, ha="center", fontsize=10, fontweight="bold", color="#555555")
for name, (x, y, mv) in S.items():
    ax.scatter(x, y, s=140, c="#7f7f7f" if "workers" not in name else "black", edgecolor="black", zorder=3)
    ax.annotate(name, (x, y), xytext=(7, 7), textcoords="offset points", fontsize=8.5)
    if mv:
        ax.annotate("", xy=mv, xytext=(x, y), arrowprops=dict(arrowstyle="-|>", lw=1.6, ls="--", color="black"))
ax.set_xlabel("Interest in the project (low to high)"); ax.set_ylabel("Power over the project (low to high)")
ax.set_xticks([]); ax.set_yticks([])
ax.text(10.4, -0.9, "Dashed arrows = expected movement as the project advances "
        "(workers and NGOs gain salience through legitimacy and urgency; regulators gain interest when tariff rules change).",
        ha="right", fontsize=7.8, style="italic", wrap=True)
plt.savefig("fig3_stakeholder_grid.png", dpi=200, bbox_inches="tight", facecolor="white")
