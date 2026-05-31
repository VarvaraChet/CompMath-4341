import matplotlib.pyplot as plt
import numpy as np

file = open('./conv.txt', 'r')
# eps, delta, cnt_it, ans = list(), list(), list(), list()
n, c=list(), list()

for line in file:
    a, b = map(float, line.split())
    n.append(int(a))
    c.append(b)
    # eps.append(a)
    # delta.append(b)
    # cnt_it.append(c)
    # ans.append(abs(d))

file.close()

# eps_array = np.array(eps)
# delta_array = np.array(delta)
# cnt_array = np.array(cnt_it)
# ans_array = np.array(ans)

# log_eps = np.log(1/eps_array)
# k = np.mean(cnt_array/log_eps)
# theor = k*log_eps

plt.figure(figsize=(14, 8))
# plt.xscale('log')
# plt.yscale('log')

plt.plot(n, c, 'o-', linewidth=2, markersize=8, color='blue')

# plt.plot(eps, theor, 'g--', linewidth=2, label='Теоретическая')

plt.xlabel('Итерация', fontsize=14, fontweight='bold')
plt.ylabel('Скорость сходимости', fontsize=14, fontweight='bold')
# plt.legend(loc='upper left', fontsize=12)

plt.grid(True, which='both', alpha=0.6, linestyle='--')

plt.tight_layout()
plt.savefig('./conv_speed.png')