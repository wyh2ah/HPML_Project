import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# ========= Trainium 硬件参数 =========
P_peak = 190.0   # TFLOP/s
B_peak = 820.0   # GB/s
I_int = P_peak * 1000.0 / B_peak   # memory/compute 交点

# ========= 四个 batch 的实验数据 =========
intensities = np.array([69.75, 94.82, 108.42, 117.88, 128.23])  # FLOPs/Byte
performances = np.array([12.16, 17.55, 22.25, 24.50, 26.58])   # TFLOP/s
labels = [" 8", " 16", " 32", " 48", " 64"]

# ========= x 轴范围 =========
I_min = intensities.min() / 20
I_max = I_int * 10
I_vals = np.logspace(np.log10(I_min), np.log10(I_max), 400)

# ========= Roofline =========
mem_roof = (B_peak * I_vals) / 1000.0
comp_roof = np.full_like(I_vals, P_peak)
roof = np.minimum(mem_roof, comp_roof)

plt.figure(figsize=(9,6))

# Roofline 曲线
plt.plot(I_vals, roof, '--', linewidth=2, label="Roofline", color="orange")

# 四个实验点
plt.scatter(intensities, performances, s=70, color="blue")
for x, y, lab in zip(intensities, performances, labels):
    plt.text(x*1.12, y*1.05, lab, fontsize=10)

# ========= 用箭头连接四个点 =========
for i in range(len(intensities)-1):
    x1, y1 = intensities[i], performances[i]
    x2, y2 = intensities[i+1], performances[i+1]
    plt.annotate("",
                 xy=(x2, y2),
                 xytext=(x1, y1),
                 arrowprops=dict(arrowstyle="-", lw=1.8, color="black"))

# 交点竖线
plt.axvline(I_int, linestyle=':', linewidth=1, color="gray",
            label=f"Intersection I={I_int:.1f}")

# 坐标轴设置
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Arithmetic Intensity (FLOPs / Byte)")
plt.ylabel("Performance (TFLOP/s)")
plt.title("Roofline Model - Trainium (Batch Scaling)")
plt.legend()
plt.grid(True, which="both", linestyle="--", alpha=0.3)

plt.tight_layout()
plt.show()
