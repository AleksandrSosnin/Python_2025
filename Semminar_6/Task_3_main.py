from Task_2_chess import find_successful_arrangements

# Ищем 4 успешные расстановки ферзей
solutions = find_successful_arrangements(4)

# Выводим решения
print("Найдено 4 успешных расстановки ферзей:")
for i, solution in enumerate(solutions, start=1):
    print(f"Расстановка {i}: {solution}")
