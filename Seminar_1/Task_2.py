# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

# Ввод числа с проверкой ограничений
number = int(input("Введите число (от 1 до 100000): "))

# Проверяем, чтобы число находилось в допустимом диапазоне
if number < 1 or number > 100000:
    print("Ошибка: число должно быть в диапазоне от 1 до 100000.")
else:
    # Проверка на простоту
    if number == 1:
        print("Число 1 не является ни простым, ни составным.")
    else:
        is_prime = True  # Предполагаем, что число простое

        # Проверяем делители от 2 до √number
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False  # Если нашли делитель, число составное
                break

        # Вывод результата
        if is_prime:
            print(f"Число {number} является простым.")
        else:
            print(f"Число {number} является составным.")
