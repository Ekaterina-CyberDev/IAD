import math
import matplotlib.pyplot as plt  # Импорт библиотеки для построения графиков
from typing import List, Tuple  # Импорт типов для аннотаций

def normal_cdf(x: float, mean: float = 0, std: float = 1) -> float:
    """Функция нормального распределения"""
    z = (x - mean) / (std * math.sqrt(2)) if std != 0 else 0  # Вычисление стандартизированного значения
    return 0.5 * (1 + math.erf(z))  # Возврат значения функции нормального распределения

def two_sided_p_value(x: float, mean: float, std: float) -> float:
    """Двустороннее p-значение для нормального распределения"""
    return 2 * (1 - normal_cdf(x, mean, std)) if x >= mean else 2 * normal_cdf(x, mean, std)  # Вычисление p-значения

def compute_normal_params(residuals: List[float]) -> Tuple[float, float]:
    """Вычисление среднего и стандартного отклонения"""
    n = len(residuals)  # Количество элементов в списке остатков
    mu = sum(residuals) / n  # Вычисление среднего значения остатков
    variance = sum((r - mu) ** 2 for r in residuals) / n  # Вычисление дисперсии остатков
    return mu, math.sqrt(variance)  # Возврат среднего и стандартного отклонения

def exponential_fit(y: List[float], t: List[int]) -> Tuple[float, float, float]:
    """Аппроксимация экспонентой y = A * exp(b * t)"""
    min_y = min(y)  # Нахождение минимального значения в данных
    shift = abs(min_y) + 0.01 if min_y <= 0 else 0  # Вычисление сдвига для положительных значений
    y_shifted = [yi + shift for yi in y]  # Создание сдвинутого массива данных
    log_y = [math.log(yi) for yi in y_shifted]  # Вычисление натуральных логарифмов

    n = len(y)  # Количество точек данных
    sum_t = sum(t)  # Сумма всех временных точек
    sum_logy = sum(log_y)  # Сумма логарифмов данных
    sum_t2 = sum(ti ** 2 for ti in t)  # Сумма квадратов временных точек
    sum_t_logy = sum(ti * yi for ti, yi in zip(t, log_y))  # Сумма произведений времени на логарифмы

    denom = n * sum_t2 - sum_t ** 2  # Вычисление знаменателя для формул МНК
    b = (n * sum_t_logy - sum_t * sum_logy) / denom  # Вычисление коэффициента b
    a = (sum_logy - b * sum_t) / n  # Вычисление коэффициента a
    A = math.exp(a)  # Вычисление коэффициента A через экспоненту

    return A, b, shift  # Возврат параметров модели

# --- Основной блок ---
data_values = [1.7, -5.4, -4.0, -5.9, -1.6, 0.0, 0.6, 2.1, 0.1, -4.9, -3.5, 5.9, 8.5, 9.9, 13.3, 11.1, 14.4, 16.2]  # Исходные данные
time_points = list(range(len(data_values)))  # Создание списка временных точек [0, 1, 2, ..., 17]

# Аппроксимация экспонентой
A_val, b_val, shift_val = exponential_fit(data_values, time_points)  # Получение параметров экспоненциальной модели
predicted = [A_val * math.exp(b_val * ti) - shift_val for ti in time_points]  # Вычисление предсказанных значений

# Остатки и проверка нормальности
residuals = [data_values[i] - predicted[i] for i in range(len(data_values))]  # Вычисление разностей между данными и моделью
mu_res, sigma_res = compute_normal_params(residuals)  # Вычисление параметров распределения остатков
D_max = max(abs(r - mu_res) for r in residuals)  # Нахождение максимального отклонения от среднего
p_val = two_sided_p_value(mu_res + D_max, mu_res, sigma_res)  # Вычисление p-значения

print(f"  A = {A_val:.4f}, b = {b_val:.4f}, shift = {shift_val:.2f}")  # Вывод параметров модели
print(f"  p-значение = {p_val:.4f}")  # Вывод p-значения
print(f"  Гипотеза принята (p ≥ 0.05): {p_val >= 0.05}")  # Вывод результата проверки гипотезы

# --- График ---
plt.figure(figsize=(6, 4))  # Создание фигуры размером 6x4 дюйма
plt.plot(time_points, data_values, 'ro', label='Исходные данные')  # Построение графика исходных данных красными точками
plt.plot(time_points, predicted, 'b-', label='Аппроксимация экспонентой')  # Построение графика модели синей линией
plt.title('Экспоненциальная аппроксимация последовательности')  # Заголовок графика
plt.xlabel('Индекс')  # Подпись оси X
plt.ylabel('Значение')  # Подпись оси Y
plt.legend()  # Добавление легенды
plt.grid(True)  # Включение сетки
plt.show()  # Отображение графика