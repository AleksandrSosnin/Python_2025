# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

# Генерация случайного числа от 0 до 1000
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Программа загадала число от 0 до 1000. Угадайте его за 10 попыток!")

# Переменная для подсчета попыток
attempts = 10

for attempt in range(1, attempts + 1):
    # Пользователь вводит число
    try:
        guess = int(input(f"Попытка {attempt}. Введите ваше число: "))
    except ValueError:
        print("Ошибка: введите целое число.")
        continue
    
    # Проверяем, угадано ли число
    if guess == secret_number:
        print(f"Поздравляем! Вы угадали число {secret_number} за {attempt} попыток!")
        break
    elif guess < secret_number:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")
    
    # Если попытки закончились
    if attempt == attempts:
        print(f"Вы исчерпали все попытки. Загаданное число было: {secret_number}")