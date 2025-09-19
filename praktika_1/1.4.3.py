class Frac:
    """Класс для работы с обыкновенными дробями"""
    
    def __init__(self, numerator, denominator=1):
        """Конструктор класса Frac"""
        # Проверка, что знаменатель не равен нулю
        if denominator == 0:
            raise ValueError("Знаменатель не может быть нулем")
        
        # Вычисление наибольшего общего делителя для сокращения дроби
        gcd = self._gcd(abs(numerator), abs(denominator))
        # Сокращение числителя и знаменателя
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd
        
        # Нормализация знака: знаменатель всегда положительный
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
    
    def _gcd(self, a, b):
        """Реализация алгоритма Евклида для вычисления НОД"""
        # Алгоритм Евклида для нахождения наибольшего общего делителя
        while b:
            a, b = b, a % b
        return a
    
    def __str__(self):
        """Строковое представление дроби для пользователя"""
        # Если знаменатель равен 1, выводим как целое число
        if self.denominator == 1:
            return str(self.numerator)
        # Иначе выводим как дробь формата "числитель/знаменатель"
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        """Строковое представление дроби для разработчика"""
        # Формат для отладки и воссоздания объекта
        return f"Frac({self.numerator}, {self.denominator})"
    
    def __add__(self, other):
        """Метод сложения двух дробей"""
        # Преобразование целого числа в дробь если необходимо
        if isinstance(other, int):
            other = Frac(other)
        # Проверка типа второго операнда
        elif not isinstance(other, Frac):
            raise TypeError("Можно складывать только с Frac или int")
        
        # Вычисление общего знаменателя
        common_denominator = self.denominator * other.denominator
        # Приведение числителей к общему знаменателю
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        
        # Создание новой дроби с результатом сложения
        return Frac(numerator1 + numerator2, common_denominator)
    
    def __mul__(self, other):
        """Метод умножения двух дробей"""
        # Преобразование целого числа в дробь если необходимо
        if isinstance(other, int):
            other = Frac(other)
        # Проверка типа второго операнда
        elif not isinstance(other, Frac):
            raise TypeError("Можно умножать только на Frac или int")
        
        # Создание новой дроби с результатом умножения
        return Frac(self.numerator * other.numerator, 
                   self.denominator * other.denominator)

# Создание дроби 1/2
frac1 = Frac(1, 3)
# Создание дроби 3/4        
frac2 = Frac(3, 3)

# Вывод созданных дробей
print(f"Дробь 1: {frac1}")
print(f"Дробь 2: {frac2}")

# Сложение дробей:
sum_frac = frac1 + frac2
print(f"Сумма: {sum_frac}")

# Умножение дробей:
product_frac = frac1 * frac2
print(f"Произведение: {product_frac}")