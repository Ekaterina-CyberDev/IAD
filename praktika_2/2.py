import scipy.stats as stats  # Импортируем модуль для статистических расчетов
import numpy as np  # Импортируем модуль для математических операций

def compute_acceptance_range(total_attempts, success_prob, confidence):
    """
    Определяет диапазон принятия гипотезы для биномиального теста
    """
    # Вычисляем параметры нормальной аппроксимации
    center = total_attempts * success_prob  # Математическое ожидание числа промахов
    spread = (total_attempts * success_prob * (1 - success_prob)) ** 0.5  # Стандартное отклонение
    
    # Определяем граничные точки распределения
    tail_probability = confidence + (1 - confidence) / 2  # Вероятность для правого хвоста
    boundary_coef = stats.norm.ppf(tail_probability)  # Z-критическое значение
    
    # Рассчитываем область принятия гипотезы
    min_accept = center - boundary_coef * spread  # Нижняя граница диапазона
    max_accept = center + boundary_coef * spread  # Верхняя граница диапазона
    
    return int(round(min_accept)), int(round(max_accept)), boundary_coef  # Возвращаем округленные значения

def demonstrate_confidence_impact():
    """Демонстрирует влияние уровня достоверности на диапазон принятия"""
    attempts = 1000  # Общее количество выстрелов
    theoretical_rate = 0.1  # Гипотетическая вероятность промаха
    confidence_levels = [0.99, 0.95, 0.90]  # Уровни доверительной вероятности
    
    print("ИССЛЕДОВАНИЕ ДИАПАЗОНА ПРИНЯТИЯ ГИПОТЕЗЫ")
    print("=" * 55)
    print(f"Количество испытаний: {attempts}")  # Вывод числа испытаний
    print(f"Теоретическая частота: {theoretical_rate}")  # Вывод теоретической вероятности
    print(f"Ожидаемое значение: {attempts * theoretical_rate:.0f}")  # Расчет ожидаемого значения
    print()
    
    for conf in confidence_levels:  # Цикл по всем уровням доверия
        low, high, z_score = compute_acceptance_range(attempts, theoretical_rate, conf)  # Расчет границ
        significance = 1 - conf  # Расчет уровня значимости
        print(f"Достоверность: {conf:.0%} | "  # Вывод доверительной вероятности
              f"Уровень значимости: {significance:.3f} | "  # Вывод уровня значимости
              f"Z-показатель: {z_score:.2f} | "  # Вывод Z-статистики
              f"Диапазон: [{low:3d}, {high:3d}]")  # Вывод диапазона принятия

def main():
    """Основная функция выполнения анализа"""
    # Базовый расчет для стандартных условий
    base_low, base_high, base_z = compute_acceptance_range(1000, 0.1, 0.95)  # Расчет для 95% доверия
    
    print("БАЗОВЫЙ АНАЛИЗ ПРИНЯТИЯ ГИПОТЕЗЫ")
    print("=" * 45)
    print(f"При 95% достоверности диапазон принятия: [{base_low}, {base_high}]")  # Основной результат
    print(f"Критическое значение: {base_z:.3f}")  # Критическое значение Z
    print()
    
    # Расширенный анализ влияния уровня достоверности
    demonstrate_confidence_impact()  # Вызов функции анализа

if __name__ == "__main__":  # Проверка запуска как основной программы
    main()  # Запуск основной функции