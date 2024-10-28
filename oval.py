import numpy as np
import matplotlib.pyplot as plt

# Параметры
A = 12
B = 2
p = 12
N = 10000  # Количество случайных точек

# Функция для вычисления максимальных значений прямоугольника
def calculate_rectangle_limits(A, B, p):
    phi_vals = np.linspace(0, 2 * np.pi, 100)
    rho_max = np.sqrt(p**2 / (A * np.cos(phi_vals)**2 + B * np.sin(phi_vals)**2))
    x_max = np.max(rho_max * np.cos(phi_vals))
    y_max = np.max(rho_max * np.sin(phi_vals))
    return x_max, y_max

# Функция для перевода декартовых координат в полярные
def to_polar(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return rho, phi

# Функция для проверки попадания точки в фигуру
def is_inside_figure(x, y, A, B, p):
    rho, phi = to_polar(x, y)
    return rho < np.sqrt(p**2 / (A * np.cos(phi)**2 + B * np.sin(phi)**2))

# Функция для вычисления площади фигуры
def calculate_area(A, B, p, N):
    x_max, y_max = calculate_rectangle_limits(A, B, p)
    x_points = np.random.uniform(-x_max, x_max, N)
    y_points = np.random.uniform(-y_max, y_max, N)
    M = sum(is_inside_figure(x, y, A, B, p) for x, y in zip(x_points, y_points))
    return (4 * M) / N * x_max * y_max

# Функция для построения графика
def plot_graph(A, B, p, N):
    x_max, y_max = calculate_rectangle_limits(A, B, p)
    x_points = np.random.uniform(-x_max, x_max, N)
    y_points = np.random.uniform(-y_max, y_max, N)
    area_approx = calculate_area(A, B, p, N)
    
    phi = np.linspace(0, 2 * np.pi, 100)
    rho = np.sqrt(p**2 / (A * np.cos(phi)**2 + B * np.sin(phi)**2))
    x_circle = rho * np.cos(phi)
    y_circle = rho * np.sin(phi)
    
    plt.figure(figsize=(8, 8))
    plt.plot([-x_max, x_max, x_max, -x_max, -x_max], [-y_max, -y_max, y_max, y_max, -y_max], 'k--', label='Прямоугольник')
    plt.plot(x_circle, y_circle, 'b-', label='Фигура')
    colors = ['black' if is_inside_figure(x, y, A, B, p) else 'r' for x, y in zip(x_points, y_points)]
    plt.scatter(x_points, y_points, c=colors, s=1, label='Случайные точки')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Площадь фигуры ≈ {area_approx:.4f}')
    plt.legend()
    plt.grid(True)
    plt.show()

# Основная программа
A = 12
B = 2
p = 12
N = 10000
plot_graph(A, B, p, N)
print(f"Площадь фигуры ≈ {calculate_area(A, B, p, N):.4f}")