import math

def normal_cdf(x, mu=0, sigma=1):
    # Вычисляет вероятность того, что случайная величина ≤ x
    return (1 + math.erf((x - mu) / (sigma * math.sqrt(2)))) / 2

def check_shooting_hypothesis(n_shots, n_misses, p_null=0.1, p_alt=0.13, alpha=0.05, power=0.8):
    """
    n_shots: общее число выстрелов
    n_misses: число промахов
    p_null: вероятность промаха по нулевой гипотезе
    p_alt: вероятность промаха по альтернативной гипотезе
    alpha: уровень значимости
    power: желаемая мощность проверки
    """
    
    mu_null = n_shots * p_null # Математическое ожидание при нулевой гипотезе (среднее количество промахов)
    sigma_null = math.sqrt(n_shots * p_null * (1 - p_null)) # Стандартное отклонение при нулевой гипотезе
    mu_alt = n_shots * p_alt # Математическое ожидание при альтернативной гипотезе
    sigma_alt = math.sqrt(n_shots * p_alt * (1 - p_alt)) # Стандартное отклонение при альтернативной гипотезе

    # РАСЧЕТ ДОВЕРИТЕЛЬНОГО ИНТЕРВАЛА
    z_alpha = 1.96  # Критическое значение для 95% доверительного интервала
    lower_bound = mu_null - z_alpha * sigma_null # Нижняя граница доверительного интервала
    upper_bound = mu_null + z_alpha * sigma_null # Верхняя граница доверительного интервала
    
    # ПРОВЕРКА ГИПОТЕЗЫ
    hypothesis_accepted = lower_bound <= n_misses <= upper_bound # Проверяем, попадает ли фактическое число промахов в доверительный интервал
    
    # РАСЧЕТ МОЩНОСТИ ТЕСТА
    power_calculated = (normal_cdf(upper_bound, mu_alt, sigma_alt) - 
                       normal_cdf(lower_bound, mu_alt, sigma_alt)) # Вероятность правильно отвергнуть ложную гипотезу
    
    # РАСЧЕТ P-ЗНАЧЕНИЯ
    # Вероятность получить такие или более крайние результаты при верной нулевой гипотезе
    if n_misses >= mu_null:
        # Для значений выше среднего - правый хвост распределения
        p_value = 2 * (1 - normal_cdf(n_misses, mu_null, sigma_null))
    else:
        # Для значений ниже среднего - левый хвост распределения
        p_value = 2 * normal_cdf(n_misses, mu_null, sigma_null)
    
    return {
        'hypothesis_accepted': hypothesis_accepted,  # Принята ли гипотеза
        'confidence_interval': (lower_bound, upper_bound),  # Границы доверительного интервала
        'p_value': p_value,  # Статистическая значимость
        'power': power_calculated,  # Реальная мощность теста
        'required_power': power  # Желаемая мощность
    }

result = check_shooting_hypothesis(
    n_shots=1000, # кол-во всех выстрелов
    n_misses=105, # Фактическое количество промахов в середине доверительного интервала 82-118
    p_null=0.1, # гипотеза Сидорова: "1 промах из 10" (10%)
    p_alt=0.13, # альтернативная гипотеза тренера: "13 промахов из 100" (13%)
    alpha=0.05, # стандартный уровень значимости 5% (вероятность ошибки 1-го рода)
    power=0.8 # желаемая мощность проверки (обычно берут 0.8)
)

print("Результаты проверки гипотезы:")
print(f"Гипотеза принята: {result['hypothesis_accepted']}")  # True/False
print(f"Доверительный интервал: ({result['confidence_interval'][0]:.1f}, {result['confidence_interval'][1]:.1f})")  # Интервал промахов
print(f"P-значение: {result['p_value']:.3f}")  # Вероятность случайного результата
print(f"Мощность проверки: {result['power']:.3f}")  # Способность обнаружить разницу
print(f"Требуемая мощность: {result['required_power']}")  # Минимальная желаемая мощность