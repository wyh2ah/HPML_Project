import matplotlib.pyplot as plt

configs = [
    (2e-5,   "0.95", 131.05, 92.55, 0.4778),
    (5e-5,   "0.95", 130.10, 94.15, 0.3182),
    (8e-5,   "0.95", 130.20, 94.40, 0.2721),
    (1.5e-4, "0.95", 129.55, 94.65, 0.2514),
    (1.5e-4, "0.90", 131.51, 94.10, 0.2766),
    (3e-4,   "0.95", 131.52, 93.85, 0.2820),
    (3e-4,   "0.90", 131.00, 94.40, 0.2666),
    (2e-5,   "none", 124.45, 92.90, 0.4126),
    (5e-5,   "none", 123.89, 94.30, 0.2833),
    (8e-5,   "none", 125.03, 94.65, 0.2554),
    (1.5e-4, "none", 124.88, 94.40, 0.2600),
]

decays = ["none", "0.95", "0.90"]
decay_labels = {"none": "No LLRD", "0.95": "LLRD=0.95", "0.90": "LLRD=0.90"}

def plot_metric(index, ylabel, title, filename):
    plt.figure(figsize=(7,4))
    for d in decays:
        xs = [c[0] for c in configs if c[1] == d]
        ys = [c[index] for c in configs if c[1] == d]
        if xs:
            plt.plot(xs, ys, marker="o", label=decay_labels[d])
    plt.xscale("log")
    plt.xlabel("Learning Rate")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=300)

plot_metric(2, "Train Time (s)", "Train Time vs Learning Rate", "lr_time.png")
plot_metric(3, "Accuracy (%)", "Accuracy vs Learning Rate", "lr_acc.png")
plot_metric(4, "Final Loss", "Final Loss vs Learning Rate", "lr_loss.png")
