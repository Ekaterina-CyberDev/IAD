import math

class Frac:
    """Класс для работы с обыкновенными дробями"""
    
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть нулем")
        
        # Сокращаем дробь при создании
        gcd = math.gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd
        
        # Убеждаемся, что знаменатель положительный
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
    
    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        return f"Frac({self.numerator}, {self.denominator})"
    
    def inverse(self):
        """Обратная дробь"""
        if self.numerator == 0:
            raise ValueError("Нельзя обратить нулевую дробь")
        return Frac(self.denominator, self.numerator)
    
    def __add__(self, other):
        """Сложение дробей"""
        if isinstance(other, int):
            other = Frac(other)
        
        common_denominator = self.denominator * other.denominator
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        
        return Frac(numerator1 + numerator2, common_denominator)
    
    def __mul__(self, other):
        """Умножение дробей"""
        if isinstance(other, int):
            other = Frac(other)
        
        return Frac(self.numerator * other.numerator, 
                   self.denominator * other.denominator)
    
    # Добавим методы для других операций
    def __sub__(self, other):
        if isinstance(other, int):
            other = Frac(other)
        
        common_denominator = self.denominator * other.denominator
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator
        
        return Frac(numerator1 - numerator2, common_denominator)
    
    def __truediv__(self, other):
        if isinstance(other, int):
            other = Frac(other)
        
        return self * other.inverse()

# Пример использования
frac1 = Frac(1, 2)
frac2 = Frac(3, 4)

print(f"Дробь 1: {frac1}")
print(f"Дробь 2: {frac2}")

sum_frac = frac1 + frac2
print(f"Сумма: {sum_frac}")

product_frac = frac1 * frac2
print(f"Произведение: {product_frac}")

inverse_frac = frac1.inverse()
print(f"Обратная к {frac1}: {inverse_frac}")