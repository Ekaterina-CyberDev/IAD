import random
import time

# Создаем множество из 10000 случайных натуральных чисел
random_set = set()
while len(random_set) < 10000:
    random_set.add(random.randint(1, 1000000))  # большие числа для разнообразия

random_list = list(random_set)

def custom_sample_without_replacement(population, k):
    """Случайная выборка без возвращения (вручную)"""
    sample = []
    indices_used = set()
    
    while len(sample) < k:
        idx = random.randint(0, len(population) - 1)
        if idx not in indices_used:
            sample.append(population[idx])
            indices_used.add(idx)
    
    return sample

def custom_sample_with_replacement(population, k):
    """Случайная выборка с возвращением (вручную)"""
    sample = []
    for _ in range(k):
        idx = random.randint(0, len(population) - 1)
        sample.append(population[idx])
    
    return sample

# Замер времени для ручной реализации
start_time = time.time()
sample_without = custom_sample_without_replacement(random_list, 10)
manual_time_without = time.time() - start_time

start_time = time.time()
sample_with = custom_sample_with_replacement(random_list, 10)
manual_time_with = time.time() - start_time

# Замер времени для встроенных методов
start_time = time.time()
builtin_sample_without = random.sample(random_list, 10)
builtin_time_without = time.time() - start_time

start_time = time.time()
builtin_sample_with = [random.choice(random_list) for _ in range(10)]
builtin_time_with = time.time() - start_time

print("Ручная реализация (без возвращения):", sample_without)
print("Встроенный метод (без возвращения):", builtin_sample_without)
print(f"Время ручной: {manual_time_without:.6f} сек, встроенной: {builtin_time_without:.6f} сек")

print("\nРучная реализация (с возвращением):", sample_with)
print("Встроенный метод (с возвращением):", builtin_sample_with)
print(f"Время ручной: {manual_time_with:.6f} сек, встроенной: {builtin_time_with:.6f} сек")