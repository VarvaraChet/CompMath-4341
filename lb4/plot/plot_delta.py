import matplotlib.pyplot as plt

data = {
    1e-1: [
        (1e-1, 2.078560),
        (1e-2, 2.072178),
        (1e-3, 2.071767),
        (1e-4, 2.071830),
        (1e-5, 2.071829),
        (1e-6, 2.071828),
    ],
    1e-2: [
        (1e-1, 2.078560),
        (1e-2, 2.086215),
        (1e-3, 2.085559),
        (1e-4, 2.085585),
        (1e-5, 2.085585),
        (1e-6, 2.085585),
    ],
    1e-3: [
        (1e-1, 2.078560),
        (1e-2, 2.086215),
        (1e-3, 2.085941),
        (1e-4, 2.085877),
        (1e-5, 2.085880),
        (1e-6, 2.085880),
    ],
    1e-4: [
        (1e-1, 2.078560),
        (1e-2, 2.086215),
        (1e-3, 2.085941),
        (1e-4, 2.085928),
        (1e-5, 2.085926),
        (1e-6, 2.085926),
    ],
    1e-5: [
        (1e-1, 2.078560),
        (1e-2, 2.086215),
        (1e-3, 2.085941),
        (1e-4, 2.085928),
        (1e-5, 2.085935),
        (1e-6, 2.085933),
    ],
    1e-6: [
        (1e-1, 2.078560),
        (1e-2, 2.086215),
        (1e-3, 2.085941),
        (1e-4, 2.085928),
        (1e-5, 2.085935),
        (1e-6, 2.085935),
    ],
}

plt.figure(figsize=(10, 6))

for eps_value, points in data.items():
    deltas = [p[0] for p in points]
    roots = [p[1] for p in points]
    plt.plot(deltas, roots, marker='o', label=f'eps = {eps_value:.0e}')

plt.xscale('log')
plt.gca().invert_xaxis()
plt.xlabel('delta')
plt.ylabel('Результат вычисления')
plt.title('Зависимость результата вычисления от delta')
plt.grid(True)
plt.legend()
plt.tight_layout()

out2 = "delta_plot.png"
plt.savefig(out2, dpi=200, bbox_inches="tight")
plt.show()

print(out2)