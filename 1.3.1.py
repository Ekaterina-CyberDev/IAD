def find_zeros_reliable(func, start, end, step=0.001):
    """Надежный поиск нулей функции"""
    zeros = []
    x = start
    
    while x <= end:
        # Просто ищем точки, где функция близка к нулю
        if abs(func(x)) < 0.00001:
            zero = round(x, 3)  # Округляем до 3 знаков
            # Проверяем на дубликаты
            if not zeros or abs(zeros[-1] - zero) > 0.01:
                zeros.append(zero)
        x += step
    
    return zeros

# Сначала определяем функцию, ПЕРЕД тем как ее использовать
def my_function(x):
    return x**2 - 9  # Нули при x = -3 и x = 3
    #Нули x^2 - 4: [-2.0, 2.0]
    #Нули 2x + 3: [-1.5]
    #Нули x^3 - x: [-1.0, 0.0, 1.0]

# Теперь вызываем функцию поиска нулей
zeros = find_zeros_reliable(my_function, -5, 5)
print("Найдены нули:", zeros)