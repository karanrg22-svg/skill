"""Figure 6 - 5x5 probability-impact heat map with inherent (circle) and residual (square) positions.
Probability score to % : 1=10, 2=25, 3=40, 4=60, 5=80. EMV = probability % x cost impact (EUR m)."""
import matplotlib.pyplot as plt

PROB = {1: .10, 2: .25, 3: .40, 4: .60, 5: .80}
# id: (risk, P, I, residual P, residual I, cost impact EUR m, owner, response, linked task)
R = {
    "R1":  ("Second-source trials slip or fail", 4, 4, 2, 4, 1.5, "Head of Sourcing", "Extra candidates; 4-week buffer", "3.3, 1.3B"),
    "R2":  ("Factories resist data sharing", 4, 4, 2, 4, 1.0, "Supplier Relations", "Contract clause; workshops; incentives", "2.3, 5.2"),
    "R3":  ("US tariff rules change mid-project", 3, 5, 2, 5, 1.8, "Trade Compliance", "Monthly review; scope reserve", "1.3, 4.2"),
    "R4":  ("Platform integration overruns", 3, 4, 2, 4, 0.8, "IT Programme Lead", "Phased go-live; fixed-price build", "2.2"),
    "R5":  ("New factory fails labour audit", 3, 4, 2, 4, 0.7, "Sustainability Lead", "Audit before trial; remediation plan", "3.2"),
    "R6":  ("Sourcing team capacity or change fatigue", 3, 3, 2, 3, 0.4, "HR Business Partner", "Backfill; training", "5.1"),
    "R7":  ("Platform vendor fails or locks in", 2, 4, 1, 4, 0.6, "Procurement", "Escrow; exit clause", "2.1"),
    "R8":  ("Sensitive supplier data breach", 2, 5, 1, 5, 0.9, "CISO", "Access controls; audit", "2.2"),
    "R9":  ("Audit and trial cost inflation", 3, 3, 2, 3, 0.4, "Finance Partner", "Fixed-price audits; reserve", "1.3"),
    "R10": ("Freight disruption delays trial shipments", 3, 3, 2, 3, 0.4, "Logistics Lead", "Air-freight samples; buffer stock", "3.3"),
}
def emv(r, residual=False):
    p, i = (r[3], r[4]) if residual else (r[1], r[2]); return PROB[p] * r[5]
def score(r): return r[1] * r[2]

if __name__ == "__main__":
    plt.rcParams["font.family"] = ["DejaVu Sans"]
    fig, ax = plt.subplots(figsize=(8.5, 7.2))
    shades = {range(1, 5): "#f2f2f2", range(5, 10): "#d9d9d9", range(10, 15): "#a6a6a6", range(15, 26): "#595959"}
    for p in range(1, 6):
        for i in range(1, 6):
            s = p * i; c = next(v for k, v in shades.items() if s in k)
            ax.add_patch(plt.Rectangle((i - .5, p - .5), 1, 1, fc=c, ec="white", lw=2))
            ax.text(i + .4, p - .42, str(s), ha="right", va="bottom", fontsize=7, color="white" if s >= 15 else "#333333")
    from collections import defaultdict
    def place(idx, which):
        cell = defaultdict(list)
        for k, r in R.items(): cell[(r[idx[0]], r[idx[1]])].append(k)
        for (i, p), ks in cell.items():
            for n, k in enumerate(ks):
                x = i + (n - (len(ks) - 1) / 2) * 0.24
                if which == "inh":
                    ax.scatter(x, p + .12, s=300, marker="o", fc="white", ec="black", lw=1.4, zorder=4)
                    ax.text(x, p + .12, k[1:], ha="center", va="center", fontsize=7.5, fontweight="bold", zorder=5)
                else:
                    ax.scatter(x, p - .25, s=260, marker="s", fc="black", ec="white", zorder=4)
                    ax.text(x, p - .25, k[1:], ha="center", va="center", fontsize=7, fontweight="bold", color="white", zorder=5)
    place((2, 1), "inh"); place((4, 3), "res")
    ax.set_xlim(.5, 5.5); ax.set_ylim(.5, 5.5); ax.set_xticks(range(1, 6)); ax.set_yticks(range(1, 6))
    ax.set_xlabel("Impact (1 low to 5 severe)"); ax.set_ylabel("Probability (1 rare to 5 almost certain)")
    ax.set_title("Risk heat map: circles = inherent (R1 to R10), black squares = residual after response", fontsize=9.5)
    top = sorted(R, key=lambda k: -score(R[k]))[:3]
    txt = "Top 3 (EMV, EUR m): " + "; ".join(f"{k} {emv(R[k]):.2f} -> {emv(R[k], True):.2f}" for k in top)
    fig.text(0.5, 0.0, txt, ha="center", fontsize=8.5, style="italic")
    plt.savefig("fig6_risk_heatmap.png", dpi=200, bbox_inches="tight", facecolor="white")
    print(txt, "| residual EMV top3:", round(sum(emv(R[k], True) for k in top), 3))
