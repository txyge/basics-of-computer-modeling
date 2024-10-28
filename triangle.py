import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import fsolve

def calculate_functions(n):
    def f1(x):
        return (10 * x) / n

    def f2(x):
        return 10 * (x - 20) / (n - 20) + 20

    def dif(x):
        return f1(x) - f2(x)

    def dif1(x):
        return f1(x)

    def dif2(x):
        return f2(x)

    return f1, f2, dif, dif1, dif2

def calculate_intersection(f1, f2):
    init = 0
    inter_x = fsolve(lambda x: f1(x) - f2(x), init)[0]
    inter_y = f1(inter_x)
    return inter_x, inter_y

def calculate_rectangle_area(inter_y, inter_a, inter_b):
    return inter_y * 1/3 * abs(inter_a - inter_b)

def generate_random_points(a, b, N):
    x_random = np.random.uniform(a, b, N)
    y_random = np.random.uniform(0, 30, N)
    return x_random, y_random

def calculate_estimated_area(M, N, rectangle_area):
    return (M / N) * rectangle_area

def calculate_true_area(f1, f2, a, b):
    return quad(lambda x: f2(x) - f1(x), a, b)[0]

def calculate_errors(estimated_area, true_area):
    absolute_error = abs(estimated_area - true_area)
    relative_error = (absolute_error / true_area) * 100
    return absolute_error, relative_error

def plot_graph(f1, f2, x_values, y_f1, y_f2, inter_y):
    plt.plot(x_values, y_f1, label='f1(x)', color='#3498db', linewidth=2, linestyle='--')
    plt.plot(x_values, y_f2, label='f2(x)', color='#f1c40f', linewidth=2, linestyle='-')
    plt.fill_between(x_values, np.minimum(y_f1, y_f2), color='gray', alpha=0.3)
    plt.xlim(0, 40)
    plt.ylim(0, inter_y)
    plt.legend(loc='upper right', fontsize=12)
    plt.title("Графики f1(x) и f2(x)", fontsize=14)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)

def main():
    n = 12
    f1, f2, dif, dif1, dif2 = calculate_functions(n)
    inter_x, inter_y = calculate_intersection(f1, f2)
    inter_a = fsolve(dif1, 0)[0]
    inter_b = fsolve(dif2, 0)[0]
    rectangle_area = calculate_rectangle_area(inter_y, inter_a, inter_b)
    x_values = np.linspace(0, 40, 500)
    y_f1 = f1(x_values)
    y_f2 = f2(x_values)
    x_random, y_random = generate_random_points(0, 40, 100000)
    M = 0
    for i in range(100000):
        if f1(x_random[i]) > y_random[i] < f2(x_random[i]):
            M += 1
    estimated_area = calculate_estimated_area(M, 100000, rectangle_area)
    true_area = calculate_true_area(f1, f2, 0, 40)
    absolute_error, relative_error = calculate_errors(estimated_area, true_area)
    print(f"Приближённая площадь фигуры: {estimated_area:.4f}")
    print(f"Точная площадь фигуры: {true_area:.4f}")
    print(f"Абсолютная погрешность: {absolute_error:.4f}")
    print(f"Относительная погрешность: {relative_error:.2f}%")
    plot_graph(f1, f2, x_values, y_f1, y_f2, inter_y)
    plt.scatter(x_random, y_random, color='red', s=1, alpha=0.5)
    plt.show()

if __name__ == "__main__":
    main()