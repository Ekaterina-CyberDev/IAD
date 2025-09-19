# Импорт необходимых модулей
import random  # для генерации случайных чисел
import time    # для замера времени выполнения

# Создаем множество из 10000 случайных натуральных чисел
random_set = set()  # создаем пустое множество для хранения уникальных чисел
while len(random_set) < 10000:  # цикл пока не наберем 10000 уникальных чисел
    random_set.add(random.randint(1, 1000000))  # добавляем случайное число от 1 до 1,000,000

# Преобразуем множество в список для удобства работы с индексами
random_list = list(random_set)  # конвертируем множество в список

def custom_sample_without_replacement(population, k):
    """Случайная выборка без возвращения (вручную)"""
    sample = []  # список для хранения выбранных элементов
    indices_used = set()  # множество для отслеживания использованных индексов
    
    while len(sample) < k:  # пока не выбрали k элементов
        idx = random.randint(0, len(population) - 1)  # генерируем случайный индекс
        if idx not in indices_used:  # если индекс еще не использовался
            sample.append(population[idx])  # добавляем элемент в выборку
            indices_used.add(idx)  # помечаем индекс как использованный
    
    return sample  # возвращаем готовую выборку

def custom_sample_with_replacement(population, k):
    """Случайная выборка с возвращением (вручную)"""
    sample = []  # список для хранения выбранных элементов
    for _ in range(k):  # повторяем k раз
        idx = random.randint(0, len(population) - 1)  # генерируем случайный индекс
        sample.append(population[idx])  # добавляем элемент в выборку
    
    return sample  # возвращаем готовую выборку

# Замер времени для ручной реализации (без возвращения)
start_time = time.time()  # фиксируем начальное время
sample_without = custom_sample_without_replacement(random_list, 10)  # делаем выборку
manual_time_without = time.time() - start_time  # вычисляем время выполнения

# Замер времени для ручной реализации (с возвращением)
start_time = time.time()  # фиксируем начальное время
sample_with = custom_sample_with_replacement(random_list, 10)  # делаем выборку
manual_time_with = time.time() - start_time  # вычисляем время выполнения

# Замер времени для встроенных методов (без возвращения)
start_time = time.time()  # фиксируем начальное время
builtin_sample_without = random.sample(random_list, 10)  # используем встроенный sample
builtin_time_without = time.time() - start_time  # вычисляем время выполнения

# Замер времени для встроенных методов (с возвращением)
start_time = time.time()  # фиксируем начальное время
builtin_sample_with = [random.choice(random_list) for _ in range(10)]  # 10 раз используем choice
builtin_time_with = time.time() - start_time  # вычисляем время выполнения

# Вывод результатов сравнения
print("Ручная реализация (без возвращения):", sample_without)  # показываем ручную выборку
print("Встроенный метод (без возвращения):", builtin_sample_without)  # показываем встроенную выборку
print(f"Время ручной: {manual_time_without:.6f} сек, встроенной: {builtin_time_without:.6f} сек")  # сравниваем время

print("\nРучная реализация (с возвращением):", sample_with)  # показываем ручную выборку
print("Встроенный метод (с возвращением):", builtin_sample_with)  # показываем встроенную выборку
print(f"Время ручной: {manual_time_with:.6f} сек, встроенной: {builtin_time_with:.6f} сек")  # сравниваем время