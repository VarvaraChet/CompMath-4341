import matplotlib.pyplot as plt
import numpy as np

eps = np.array([1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6])
iterations = np.array([2, 5, 9, 12, 15, 19])


left = 2
right = 2.5
theory = np.log2((right - left) / eps)

plt.figure(figsize=(8, 5))
plt.plot(eps, iterations, marker='o', label='Практическое число итераций')
plt.plot(eps, theory, marker='o', label='Теоретическая оценка')
plt.xscale('log')
plt.gca().invert_xaxis()
plt.xlabel('eps')
plt.ylabel('N')
plt.title('Зависимость числа итераций от eps')
plt.grid(True)
plt.legend()

out = "iterations_plot.png"
plt.savefig(out, dpi=200, bbox_inches="tight")
plt.show()

print(out)