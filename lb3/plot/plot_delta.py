import matplotlib.pyplot as plt

data = {
    1e-1: [
        (1e-1, 2.125000),
        (1e-2, 2.125000),
        (1e-3, 2.125000),
        (1e-4, 2.125000),
        (1e-5, 2.125000),
        (0, 2.125000),
    ],
    1e-2: [
        (1e-1, 2.078125),
        (1e-2, 2.078125),
        (1e-3, 2.078125),
        (1e-4, 2.078125),
        (1e-5, 2.078125),
        (0, 2.078125),
    ],
    1e-3: [
        (1e-1, 2.085938),
        (1e-2, 2.085938),
        (1e-3, 2.085938),
        (1e-4, 2.085938),
        (1e-5, 2.083984),
        (0, 2.083984),
    ],
    1e-4: [
        (1e-1, 2.085938),
        (1e-2, 2.085938),
        (1e-3, 2.085938),
        (1e-4, 2.085938),
        (1e-5, 2.085815),
        (0, 2.085815),
    ],
    1e-5: [
        (1e-1, 2.085938),
        (1e-2, 2.085938),
        (1e-3, 2.085938),
        (1e-4, 2.085938),
        (1e-5, 2.085922),
        (0, 2.085922),
    ],
    1e-6: [
        (1e-1, 2.085938),
        (1e-2, 2.085938),
        (1e-3, 2.085938),
        (1e-4, 2.085938),
        (1e-5, 2.085936),
        (0, 2.085936),
    ],
}

plt.figure(figsize=(10, 6))

for eps, points in data.items():
    deltas = [p[0] for p in points]
    roots = [p[1] for p in points]
    plt.plot(deltas, roots, marker='o', label=f'eps = {eps:.0e}')

plt.xscale('log')
plt.xlabel('delta')
plt.ylabel('Результат вычисления')
plt.title('Зависимость результата вычисления от delta')
plt.grid(True)
plt.legend()
plt.tight_layout()


out = "delta_plot.png"
plt.savefig(out, dpi=200, bbox_inches="tight")
plt.show()

print(out)