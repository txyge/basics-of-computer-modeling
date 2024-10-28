import numpy as np
import matplotlib.pyplot as plt

# Функция для вычисления приближённого значения числа π
def calculate_pi(radius, num_points):
    # Генерация случайных точек в квадрате со стороной 2R
    x_points = np.random.uniform(-radius, radius, num_points)
    y_points = np.random.uniform(-radius, radius, num_points)
    
    # Определение функции для проверки попадания точки в круг
    is_inside_circle = np.vectorize(lambda x, y: x**2 + y**2 <= radius**2)
    
    # Подсчёт количества точек внутри круга
    num_inside_circle = np.sum(is_inside_circle(x_points, y_points))
    
    # Вычисление приближённого значения числа π
    pi_approx = (4 * num_inside_circle) / num_points
    
    # Истинное значение числа π
    pi_true = np.pi
    
    # Вычисление абсолютной и относительной погрешностей
    absolute_error = abs(pi_true - pi_approx)
    relative_error = (absolute_error / pi_true) * 100
    
    return pi_approx, pi_true, absolute_error, relative_error, x_points, y_points

# Функция для построения графика
def plot_graph(radius, num_points, pi_approx, x_points, y_points):
    # Генерация точек для построения круга
    theta = np.linspace(0, 2 * np.pi, 100)
    circle_x = radius * np.cos(theta)
    circle_y = radius * np.sin(theta)
    
    # Создание графика
    plt.figure(figsize=(8, 8))
    
    # Построение квадрата
    plt.plot([-radius, radius, radius, -radius, -radius], [-radius, -radius, radius, radius, -radius], 'k--', label='Квадрат')
    
    # Построение круга
    plt.plot(circle_x, circle_y, 'b-', label='Круг')
    
    # Определение цветов для точек
    colors = np.where(x_points**2 + y_points**2 <= radius**2, 'black', 'r')
    
    # Построение точек
    plt.scatter(x_points, y_points, c=colors, s=1, label='Случайные точки')
    
    # Настройка графика
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Приближённое значение π: {pi_approx:.4f}')
    plt.legend()
    plt.grid(True)
    plt.show()

# Основные параметры
radius = 12
num_points = 10000

# Вычисление приближённого значения числа π
pi_approx, pi_true, absolute_error, relative_error, x_points, y_points = calculate_pi(radius, num_points)

# Построение графика
plot_graph(radius, num_points, pi_approx, x_points, y_points)

# Вывод результатов
print(f"Приближённое значение числа π: {pi_approx:.4f}")
print(f"Истинное значение числа π: {pi_true:.4f}")
print(f"Абсолютная погрешность: {absolute_error:.6f}")
print(f"Относительная погрешность: {relative_error:.6f}%")