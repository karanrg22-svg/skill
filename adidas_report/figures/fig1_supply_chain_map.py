"""Figure 1 - Adidas supply chain map (physical, information and financial flows)."""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.family"] = ["DejaVu Sans"]
fig, ax = plt.subplots(figsize=(13, 6.6))
ax.set_xlim(0, 13); ax.set_ylim(-0.2, 6.7); ax.axis("off")

def box(x, y, w, h, text, fill="white", bold=False, size=8.5, ls="-"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                fc=fill, ec="black", lw=1.1, ls=ls))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size,
            fontweight="bold" if bold else "normal", linespacing=1.25)

def arrow(p, q, style="phys", rad=0.0):
    ls, lw = {"phys": ("-", 2.0), "info": ((0, (5, 3)), 1.3), "fin": ((0, (1, 2)), 1.5)}[style]
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=12, lw=lw, ls=ls,
                                 color="black", connectionstyle=f"arc3,rad={rad}"))

# Stage headers
for x, t in [(0.9, "UPSTREAM"), (4.35, "MANUFACTURE (outsourced)"), (7.55, "DISTRIBUTE"),
             (9.85, "SELL"), (12.1, "")]:
    ax.text(x, 6.05, t, ha="center", fontsize=9, fontweight="bold", color="#444444")

# Control centre (what Adidas keeps)
box(2.2, 5.1, 7.4, 0.8, "adidas HQ: brand, design, demand planning, sourcing\n(what Adidas controls)", fill="#d9d9d9", bold=True, size=9)

# Upstream
box(0.1, 2.3, 1.6, 1.9, "Raw materials\nand Tier 2 mills\n(textiles, rubber,\nchemicals)\nlimited visibility", fill="#f2f2f2")

# Tier 1 country boxes
box(2.55, 1.0, 3.6, 3.7, "", fill="white")
ax.text(4.35, 4.35, "Tier 1 independent manufacturing partners\n(almost 100% of production; largest factory about 6%)",
        ha="center", fontsize=8.3, fontweight="bold")
rows = [("Vietnam 27%", 3.35), ("Indonesia 18%", 2.8), ("China 16%", 2.25),
        ("Other Asia 31%", 1.7), ("Outside Asia 8%", 1.15)]
for t, y in rows:
    box(2.75, y, 3.2, 0.45, t, fill="#bfbfbf" if "Outside" not in t else "white", size=8.5)
ax.text(4.35, 0.78, "Asia total 92% of volume (Annual Report 2025)", ha="center", fontsize=8, style="italic")

# DCs
box(6.65, 2.3, 1.8, 1.9, "60 distribution\ncentres\n21 owned\n39 partner-run\nmainly sea freight", fill="#f2f2f2")

# Channels
box(9.2, 3.6, 1.35, 0.8, "Wholesale", fill="#f2f2f2")
box(9.2, 2.6, 1.35, 0.8, "Own retail", fill="#f2f2f2")
box(9.2, 1.6, 1.35, 0.8, "E-commerce\n(returns loop)", fill="#f2f2f2")

# Consumer
box(11.4, 2.3, 1.4, 1.9, "Consumer", fill="#d9d9d9", bold=True, size=9.5)

# Physical flow (left to right)
arrow((1.7, 3.25), (2.55, 3.25))
arrow((6.15, 3.25), (6.65, 3.25))
for y in (4.0, 3.0, 2.0):
    arrow((8.45, 3.25), (9.2, y), rad=0.0)
    arrow((10.55, y), (11.4, 3.25), rad=0.0)
# Returns (reverse physical)
arrow((9.2, 1.75), (8.0, 2.3), rad=-0.35)

# Information flow (demand signals right to left, dashed)
arrow((12.1, 4.2), (9.6, 5.5), style="info", rad=0.2)
arrow((2.2, 5.5), (0.9, 4.2), style="info", rad=0.2)
arrow((4.35, 5.1), (4.35, 4.7), style="info")

# Financial flow (payments flow back, dotted)
ax.annotate("", xy=(5.0, 0.35), xytext=(10.0, 0.35),
            arrowprops=dict(arrowstyle="-|>", ls=(0, (1, 2)), lw=1.5, color="black"))
ax.text(7.5, 0.45, "payments back to Tier 1 partners", ha="center", fontsize=8)

# Legend
ax.plot([0.1, 0.8], [0.5, 0.5], color="black", lw=2); ax.text(0.9, 0.5, "Physical flow", va="center", fontsize=8)
ax.plot([0.1, 0.8], [0.25, 0.25], color="black", lw=1.3, ls=(0, (5, 3))); ax.text(0.9, 0.25, "Information flow (orders, forecasts, sales data)", va="center", fontsize=8)
ax.plot([0.1, 0.8], [0.0, 0.0], color="black", lw=1.5, ls=(0, (1, 2))); ax.text(0.9, 0.0, "Financial flow", va="center", fontsize=8)

ax.text(6.5, 6.45, "Adidas supply chain: asset-light and Asia-concentrated", ha="center", fontsize=11, fontweight="bold")
plt.savefig("fig1_supply_chain_map.png", dpi=200, bbox_inches="tight", facecolor="white")
