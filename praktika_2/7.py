import math

def f_norm(x, mu=0, sigma=1):
    """Аппроксимация функции нормального распределения"""
    z = (x - mu) / sigma  # Нормировка значения x
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))  # Вычисление функции распределения через функцию ошибок

def p_value(x, mu=0, sigma=1):
    """Вычисление двустороннего p-значения"""
    if x >= mu:  # Если x больше или равно среднему
        return 2 * (1 - f_norm(x, mu, sigma))  # Правый хвост × 2
    else:  # Если x меньше среднего
        return 2 * f_norm(x, mu, sigma)  # Левый хвост × 2

def gauss(M, b):
    """Решение СЛАУ методом Гаусса"""
    n = len(b)  # Размер системы уравнений
    for i in range(n):  # Прямой ход метода Гаусса
        max_row = max(range(i, n), key=lambda r: abs(M[r][i]))  # Поиск строки с максимальным элементом
        M[i], M[max_row] = M[max_row], M[i]  # Обмен строк для устойчивости
        b[i], b[max_row] = b[max_row], b[i]  # Обмен правых частей
        
        for j in range(i+1, n):  # Исключение переменных из нижележащих строк
            factor = M[j][i] / M[i][i]  # Вычисление множителя
            for k in range(i, n):  # Вычитание строки i из строки j
                M[j][k] -= factor * M[i][k]  # Обновление матрицы
            b[j] -= factor * b[i]  # Обновление правой части
    
    x = [0] * n  # Инициализация вектора решений
    for i in range(n-1, -1, -1):  # Обратный ход метода Гаусса
        x[i] = (b[i] - sum(M[i][j] * x[j] for j in range(i+1, n))) / M[i][i]  # Вычисление x[i]
    return x  # Возврат решения системы

def approx_poly(x, t, r):
    """Полиномиальная аппроксимация r-го порядка"""
    M = [[] for _ in range(r+1)]  # Инициализация матрицы системы
    b = []  # Инициализация правой части системы
    
    for l in range(r+1):  # Построение системы нормальных уравнений
        for q in range(r+1):  # Для каждого столбца матрицы
            M[l].append(sum(z**(l+q) for z in t))  # Вычисление элемента матрицы
        b.append(sum(xi * ti**l for xi, ti in zip(x, t)))  # Вычисление элемента правой части
    
    return gauss(M, b)  # Решение системы и возврат коэффициентов

# Данные
x_hat = [7, 13.3, 11.1, 14.4, 16.2]  # Исходные значения y
t = list(range(len(x_hat)))  # Временные точки (x координаты)

# Аппроксимация полиномом 7-го порядка
coefficients = approx_poly(x_hat, t, 7)  # Получение коэффициентов полинома

# Вычисление предсказанных значений
x_pred = []  # Инициализация списка предсказанных значений
for ti in t:  # Для каждой временной точки
    pred = sum(c * ti**i for i, c in enumerate(coefficients))  # Вычисление значения полинома
    x_pred.append(pred)  # Добавление в список

# Вычисление отклонений
errors = [xi - pred for xi, pred in zip(x_hat, x_pred)]  # Разности между исходными и предсказанными значениями

# Статистика отклонений
mu_error = sum(errors) / len(errors)  # Среднее значение ошибок
sigma_error = math.sqrt(sum((e - mu_error)**2 for e in errors) / len(errors))  # Стандартное отклонение ошибок

# P-значение для наибольшего отклонения
max_error = max(errors, key=abs)  # Нахождение максимального по модулю отклонения
p_val = p_value(max_error, mu_error, sigma_error)  # Вычисление p-значения

print("Коэффициенты полинома:", [round(c, 3) for c in coefficients])  # Вывод коэффициентов
print("P-значение:", round(p_val, 4))  # Вывод p-значения