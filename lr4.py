import math
import matplotlib.pyplot as plt

#Функция варианта 19
def function(x, delta=0.0):
    result = (math.log(x))**2 - 1.0/x
    if delta > 0:
        return round(result, delta)
    return result

#Функция округления
def round(x, delta):
    """
    Округление числа с точностью
    x - число для округления
    delta - точность округления
    """
    if delta <= 1e-9:
        print("Неверное задание точности округления: delta должно быть > 1e-9")
        return
    if x > 0.0:
        return delta * int((x / delta) + 0.5)
    else:
        return delta * int((x / delta) - 0.5)


#метод  хорд
def chord(left, right, eps, f):
    """
    Решение уравнения f(x)=0 методом хорд
    left, right - границы интервала
    eps - точность
    f - функция f(x)
    Возвращает кортеж:
    x - найденный корень
    n - число итераций
    """
    f_left = f(left)
    f_right = f(right)

    # Проверка корректности интервала
    if f_left * f_right > 0.0:
        print("Неверное задание интервала: на концах одинаковые знаки")
        return None, 0

    if eps <= 0.0:
        print("Неверное задание точности: eps должно быть > 0")
        return None, 0

    n = 0 #счетчик
    #попали ли сразу на корень
    if f_left == 0.0:
        return left, n
    if f_right == 0.0:
        return right, n

    # Основной цикл
    while True:
        # Вычисление точки пересечения хорды с осью X
        x = left - (right - left) * f_left / (f_right - f_left)
        y = f(x)

        # Если нашли точный корень
        if y == 0.0:
            return x, n

        # Выбор нового интервала
        if y * f_left < 0.0:
            right = x
            f_right = y
        else:
            left = x
            f_left = y

        n += 1

        #условие окончания: пока |f(x)| >= eps
        if abs(y) < eps:
            return x, n


def main():
    a = float(input("Левая граница a (0< a < 2.021): "))
    b = float(input("Правая граница b (> 2.021): "))
    eps = float(input("Точность Eps (от 0.1 до 0.000001): "))

    if a >= b:
        print("Ошибка: a должно быть меньше b")
        return

    # Проверка знаков
    f_a, f_b = function(a), function(b)
    print(f"\nf({a}) = {f_a:.6f}, f({b}) = {f_b:.6f}")
    if f_a * f_b >= 0:
        print("Ошибка: интервал не подходит")
        return

    #Поиск корня методом хорд
    x_root, iterations = chord(a, b, eps, function)

    if x_root is None:
        return

    print(f"\nКорень: x = {x_root:.8f}")
    print(f"Итераций: {iterations}")
    print(f"f(x) = {function(x_root):.2e}")

    #Исследование 1: Зависимость от точности
    print("\nИССЛЕДОВАНИЕ 1: Зависимость от точности")


    eps_values = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]
    iter_counts = []

    print("\nEps\t\tИтерации\tКорень")
    print("-" * 50)
    for eps_val in eps_values:
        x_val, iter_val = chord(a, b, eps_val, function)
        iter_counts.append(iter_val)
        print(f"{eps_val:.6f}\t{iter_val}\t\t{x_val:.8f}")

    #Исследование 2: Обусловленность
    print("\nИССЛЕДОВАНИЕ 2: Влияние ошибок в данных")


    # Точный корень (без ошибок)
    x_exact, _ = chord(a, b, 1e-10, function)
    delta_values = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]

    print(f"\nТочный корень: {x_exact:.8f}\n")
    print("Delta\t\tКорень\t\tПогрешность")
    print("-" * 50)

    x_values_delta = []
    for delta_val in delta_values:
        f_with_delta = lambda x: function(x, delta_val)
        x_val, _ = chord(a, b, 1e-6, f_with_delta)
        x_values_delta.append(x_val)
        error = abs(x_val - x_exact)
        print(f"{delta_val:.6f}\t{x_val:.8f}\t{error:.2e}")

    #графики
    plt.figure(figsize=(12, 5))

    # График 1: зависимость от точности
    plt.subplot(1, 2, 1)
    plt.plot(eps_values, iter_counts, 'bo-')
    plt.xscale('log')
    plt.xlabel('Точность Eps')
    plt.ylabel('Число итераций')
    plt.title('Метод хорд: зависимость от точности')
    plt.grid(True)

    # График 2: влияние ошибок
    plt.subplot(1, 2, 2)
    errors = [abs(x - x_exact) for x in x_values_delta]
    plt.plot(delta_values, errors, 'ro-')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Delta (ошибка)')
    plt.ylabel('Погрешность корня')
    plt.title('Влияние ошибок входных данных')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

main()
