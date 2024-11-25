import numpy as np
import matplotlib.pyplot as plt

# Определение параметров
a = 5  # Ширина прямоугольника
b = np.sqrt(29)  # Высота прямоугольника
N = 1000

def f(x, u):
    return np.sqrt(29 - u * np.cos(x)**2)


def monte_carlo_integral(a, b, N):
    M = 0
    x_points = np.random.uniform(0, a, N)
    y_points = np.random.uniform(0, b, N)
    
    for x, y in zip(x_points, y_points):
        u = np.random.uniform(0, 5)  # Для каждой точки случайное значение u
        if y < f(x, u):
            M += 1
    
    # Приближённое значение интеграла
    return (M / N) * a * b


def plot_graph(a, b, N, integral_approx):
    x = np.linspace(0, 5, 1000)
    u_mean = np.mean(np.linspace(0, 5, 1000))  # Среднее значение для u
    y = f(x, u_mean)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='$\sqrt{29 - u \cdot \cos^2(x)}$', color='blue')

    # Заполнение области под графиком
    plt.fill_between(x, 0, y, color='gray', alpha=0.5, label='Интегрируемая область')

    # Добавление случайных точек
    x_points = np.random.uniform(0, a, N)
    y_points = np.random.uniform(0, b, N)
    u_points = np.random.uniform(0, 5, N)
    for x_pt, y_pt, u_pt in zip(x_points, y_points, u_points):
        if y_pt < f(x_pt, u_pt):
            plt.scatter(x_pt, y_pt, color='red', s=10, alpha=0.5)

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'График функции и интегрируемая область (приближённое значение интеграла: {integral_approx:.2f})')
    plt.legend()
    plt.grid(True)
    plt.show()


def calculate_errors(exact_value, integral_approx):
    absolute_error = abs(exact_value - integral_approx)
    relative_error = absolute_error / abs(exact_value)
    return absolute_error, relative_error

integral_approx = monte_carlo_integral(a, b, N)
plot_graph(a, b, N, integral_approx=integral_approx)

exact_value = 35.75  # Например, если у нас есть точное значение интеграла (поставьте ваше значение)
absolute_error, relative_error = calculate_errors(exact_value, integral_approx)

print(f"Приближённое значение интеграла: {integral_approx}")
print(f"Абсолютная погрешность: {absolute_error:.2f}")
print(f"Относительная погрешность: {relative_error:.2%}")