# Задача
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

def to_hexadecimal(num):
    """Функция для перевода числа в шестнадцатеричную систему."""
    if num == 0:
        return "0"
    
    hex_chars = "0123456789ABCDEF"  # Символы для шестнадцатеричной системы
    result = ""
    is_negative = num < 0  # Проверка на отрицательное число
    
    if is_negative:
        num = abs(num)  # Берем модуль числа
    
    # Перевод в шестнадцатеричное представление
    while num > 0:
        remainder = num % 16
        result = hex_chars[remainder] + result  # Добавляем символ справа
        num //= 16  # Целочисленное деление на 16
    
    if is_negative:
        result = "-" + result  # Добавляем знак минуса для отрицательных чисел
    
    return result

# Проверка функции
number = int(input("Введите целое число: "))
custom_hex = to_hexadecimal(number)
builtin_hex = hex(number).upper().replace("0X", "")  # Убираем префикс "0x" для сравнения

print(f"Результат функции: {custom_hex}")
print(f"Результат hex(): {builtin_hex}")

# Сравнение результатов
if custom_hex == builtin_hex:
    print("Результаты совпадают!")
else:
    print("Есть расхождение в результатах.")
