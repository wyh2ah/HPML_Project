import matplotlib.pyplot as plt

batch = [2, 4, 8, 16, 32]
sm = [24.78, 32.09, 40.11, 44.74, 44.98]
te = [7.26, 12.17, 18.23, 26.11, 33.12]
scalar = [32.59, 33.35, 30.82, 28.63, 26.47]
vector = [36.34, 38.68, 37.80, 38.15, 38.34]

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(batch, sm, marker="o", label="A100 SM Util")
ax.plot(batch, te, marker="o", label="Trainium TensorE Util")
ax.plot(batch, scalar, marker="o", label="Trainium ScalarE Util")
ax.plot(batch, vector, marker="o", label="Trainium VectorE Util")

sm_min, sm_max = min(sm), max(sm)
sm_xmin, sm_xmax = batch[sm.index(sm_min)], batch[sm.index(sm_max)]
te_min, te_max = min(te), max(te)
te_xmin, te_xmax = batch[te.index(te_min)], batch[te.index(te_max)]

ax.hlines(sm_min, sm_xmin, sm_xmax, linestyles="dashed", colors="gray")
ax.hlines(sm_max, sm_xmin, sm_xmax, linestyles="dashed", colors="gray")
ax.vlines(1.5, sm_min, sm_max, colors="black")
ax.text(1.5, sm_min - 1.0, f"{sm_max/sm_min:.2f}×", ha="center", va="top")

ax.hlines(te_min, te_xmin, te_xmax, linestyles="dashed", colors="gray")
ax.hlines(te_max, te_xmin, te_xmax, linestyles="dashed", colors="gray")
ax.vlines(32.5, te_min, te_max, colors="black")
ax.text(32.5, te_max + 1.0, f"{te_max/te_min:.2f}×", ha="center", va="bottom")

ax.set_xlabel("Batch Size")
ax.set_ylabel("Utilization (%)")
ax.set_title("Small Batch Experiment: Utilization vs Batch Size")
ax.legend(loc="lower right")

plt.tight_layout()
plt.savefig("util_ratio_fixed.png", dpi=300)
