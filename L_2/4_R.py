def multiplicative_congruential_method(A, M, X0, n):

    # Инициализируем список для хранения последовательности
    sequence = []
    # Инициализируем текущее число начальным числом
    current = X0

    # Генерируем последовательность псевдослучайных чисел
    for _ in range(n):
        # Вычисляем следующее число как произведение текущего числа и множителя по модулю
        next_number = (A * current) % M
        # Добавляем следующее число в список, нормализованное к диапазону [0, 1)
        sequence.append(next_number / M)
        # Обновляем текущее число
        current = next_number

    # Возвращаем сгенерированную последовательность
    return sequence

# Пример вызова
A = 265
M = 129
X0 = 122
n = 12
sequence = multiplicative_congruential_method(A,M, X0, n)
print(sequence)