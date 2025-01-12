# Задача
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

from fractions import Fraction

def parse_fraction(fraction_str):
    """Парсит строку вида 'a/b' и возвращает числитель и знаменатель в виде целых чисел."""
    if '/' not in fraction_str:
        raise ValueError("Введите дробь в формате 'a/b', где a и b — целые числа.")
    
    try:
        numerator, denominator = map(int, fraction_str.split('/'))
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю.")
        return numerator, denominator
    except ValueError:
        raise ValueError("Введите дробь в формате 'a/b', где a и b — целые числа.")

def add_fractions(num1, denom1, num2, denom2):
    """Суммирует две дроби."""
    numerator = num1 * denom2 + num2 * denom1
    denominator = denom1 * denom2
    return simplify_fraction(numerator, denominator)

def multiply_fractions(num1, denom1, num2, denom2):
    """Перемножает две дроби."""
    numerator = num1 * num2
    denominator = denom1 * denom2
    return simplify_fraction(numerator, denominator)

def simplify_fraction(numerator, denominator):
    """Упрощает дробь, находя НОД числителя и знаменателя."""
    from math import gcd
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

# Основная программа
while True:
    try:
        fraction1 = input("Введите первую дробь в формате 'a/b': ").strip()
        num1, denom1 = parse_fraction(fraction1)
        break
    except ValueError as e:
        print(e)

while True:
    try:
        fraction2 = input("Введите вторую дробь в формате 'a/b': ").strip()
        num2, denom2 = parse_fraction(fraction2)
        break
    except ValueError as e:
        print(e)

# Сумма и произведение дробей
sum_numerator, sum_denominator = add_fractions(num1, denom1, num2, denom2)
product_numerator, product_denominator = multiply_fractions(num1, denom1, num2, denom2)

# Вывод результатов
print(f"\nСумма дробей: {sum_numerator}/{sum_denominator}")
print(f"Произведение дробей: {product_numerator}/{product_denominator}")

# Проверка с помощью модуля fractions
fraction1_obj = Fraction(num1, denom1)
fraction2_obj = Fraction(num2, denom2)

print("\nПроверка с использованием модуля fractions:")
print(f"Сумма: {fraction1_obj + fraction2_obj}")
print(f"Произведение: {fraction1_obj * fraction2_obj}")

