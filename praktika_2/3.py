import scipy.stats as stats  # Импорт библиотеки для статистических вычислений
import numpy as np  # Импорт библиотеки для математических операций

def calculate_critical_values(sample_size, probability, significance_level):
    """
    Вычисляет критические границы для биномиального распределения
    """
    # Основные параметры распределения
    expected_value = sample_size * probability  # Расчет математического ожидания (среднего значения)
    std_deviation = np.sqrt(sample_size * probability * (1 - probability))  # Расчет стандартного отклонения
    
    # Находим критическое значение Z для двустороннего теста
    z_critical = stats.norm.ppf(1 - significance_level / 2)  # Вычисление Z-критического по квантилю нормального распределения
    
    # Вычисляем границы принятия гипотезы
    lower_bound = expected_value - z_critical * std_deviation  # Расчет нижней границы доверительного интервала
    upper_bound = expected_value + z_critical * std_deviation  # Расчет верхней границы доверительного интервала
    
    return round(lower_bound), round(upper_bound), z_critical  # Возврат округленных значений границ и Z-статистики

# Основные параметры исследования
total_shots = 1000  # Общее количество выстрелов в эксперименте
hypothesized_miss_rate = 0.1  # Предполагаемая вероятность промаха (10%)
significance_level = 0.05  # Уровень значимости (5%)

# Вычисляем критические значения
lower_limit, upper_limit, critical_z = calculate_critical_values(
    total_shots, hypothesized_miss_rate, significance_level
)  # Вызов функции для расчета критических границ

print("АНАЛИЗ КРИТИЧЕСКИХ ГРАНИЦ")  # Заголовок раздела результатов
print("=" * 40)
print(f"Общее количество выстрелов: {total_shots}")  # Вывод количества выстрелов
print(f"Предполагаемая вероятность промаха: {hypothesized_miss_rate}")  # Вывод гипотетической вероятности
print(f"Уровень значимости: {significance_level}")  # Вывод уровня значимости
print(f"Критическое значение Z: {critical_z:.3f}")  # Вывод Z-критического значения
print(f"Допустимый диапазон промахов: [{lower_limit}, {upper_limit}]")  # Вывод рассчитанных границ

print("\nВЛИЯНИЕ УРОВНЯ ЗНАЧИМОСТИ НА ГРАНИЦЫ")  # Заголовок раздела анализа зависимости
print("=" * 50)
significance_levels = [0.01, 0.05, 0.1]  # Список уровней значимости для анализа

for level in significance_levels:  # Цикл по всем уровням значимости
    low_bound, up_bound, z_value = calculate_critical_values(
        total_shots, hypothesized_miss_rate, level
    )  # Расчет границ для каждого уровня значимости
    print(f"α = {level:5.2f} | Z = {z_value:5.2f} | Границы: [{low_bound:3d}, {up_bound:3d}]")