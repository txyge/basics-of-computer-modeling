def modified_middle_square_method(R0, R1, n):
    
    #:R0: первое начальное число (например, 0.5836)
    #:R1: второе начальное число (например, 0.2176)
    #:n: количество чисел в последовательности
    
    # Инициализируем список первыми двумя числами
    sequence = [R0, R1]
    # Генерируем последовательность псевдослучайных чисел
    for _ in range(n - 2):
        # Вычисляем среднее значение между последними двумя числами
        avg = (sequence[-2] + sequence[-1]) / 2
        # Возводим среднее в квадрат и удаляем точку
        squared = str(avg ** 2).replace('.', '').zfill(8)
        # Извлекаем четыре средние цифры и преобразуем их в следующее число
        next_number = float('0.' + squared[2:6])
        # Добавляем новое число в список
        sequence.append(next_number)
    # Возвращаем сгенерированную последовательность
    return sequence

# Пример вызова
R0 = 0.5836
R1 = 0.2176
n = 6
sequence = modified_middle_square_method(R0, R1, n)
print(sequence)