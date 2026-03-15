import matplotlib.pyplot as plt
import numpy as np

eps = np.array([1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6], dtype=float)
iterations = np.array([1, 3, 4, 5, 6, 8], dtype=float)

x = -np.log10(eps)
coef = np.polyfit(x, iterations, 1)
theory = np.polyval(coef, x)

plt.figure(figsize=(8, 5))
plt.plot(eps, iterations, marker='o', label='Практическое число итераций')
plt.plot(eps, theory, marker='o', linestyle='--', label='Теоретическая оценка')
plt.xscale('log')
plt.gca().invert_xaxis()
plt.xlabel('eps')
plt.ylabel('N')
plt.title('Зависимость числа итераций от eps')
plt.grid(True)
plt.legend()

out1 = "iterations_plot.png"
plt.savefig(out1, dpi=200, bbox_inches="tight")
plt.show()

print(out1)