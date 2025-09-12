import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Предположим, что у нас есть данные о температурах
# В реальности нужно скачать данные с Gismeteo

def create_sample_data():
    """Создает примерные данные для демонстрации"""
    # 12 месяцев, для каждого месяца 30-31 значение температур
    data = {}
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
              'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    
    # Средние температуры для Москвы и Анадыря (примерные)
    moscow_means = [-10, -8, -3, 6, 14, 18, 20, 18, 12, 5, -2, -7]
    anadyr_means = [-22, -21, -18, -10, -1, 6, 10, 8, 2, -6, -14, -20]
    
    moscow_data = []
    anadyr_data = []
    
    for i, month in enumerate(months):
        # Генерируем случайные температуры вокруг среднего значения
        days = 30 if month in ['Апрель', 'Июнь', 'Сентябрь', 'Ноябрь'] else 31
        days = 28 if month == 'Февраль' else days
        
        # Температуры с нормальным распределением
        moscow_temps = np.random.normal(moscow_means[i], 5, days)
        anadyr_temps = np.random.normal(anadyr_means[i], 4, days)
        
        moscow_data.append(moscow_temps)
        anadyr_data.append(anadyr_temps)
    
    return months, moscow_data, anadyr_data

def calculate_std_deviation(temperatures):
    """Вычисляет стандартное отклонение для каждого месяца"""
    std_devs = []
    for month_temps in temperatures:
        std_dev = np.std(month_temps)
        std_devs.append(std_dev)
    
    return std_devs

# Получаем данные
months, moscow_temps, anadyr_temps = create_sample_data()

# Вычисляем стандартные отклонения
moscow_std = calculate_std_deviation(moscow_temps)
anadyr_std = calculate_std_deviation(anadyr_temps)

# Строим график
plt.figure(figsize=(12, 6))
x_pos = np.arange(len(months))

plt.plot(x_pos, moscow_std, 'o-', label='Москва', linewidth=2, markersize=8)
plt.plot(x_pos, anadyr_std, 's-', label='Анадырь', linewidth=2, markersize=8)

plt.xlabel('Месяцы')
plt.ylabel('Стандартное отклонение температуры')
plt.title('Стандартное отклонение температур по месяцам')
plt.xticks(x_pos, months, rotation=45)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("Стандартные отклонения для Москвы:", [f"{x:.2f}" for x in moscow_std])
print("Стандартные отклонения для Анадыря:", [f"{x:.2f}" for x in anadyr_std])