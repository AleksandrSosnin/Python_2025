# Дополнение к шахматному модулю (Task_2_chess.py)

# import random

# def generate_random_positions():
#     """
#     Генерирует случайную расстановку ферзей на доске 8x8.
#     :return: Список кортежей (x, y) с координатами ферзей.
#     """
#     rows = list(range(1, 9))
#     random.shuffle(rows)  # Перемешиваем строки
#     columns = list(range(1, 9))
#     return list(zip(rows, columns))


# def find_successful_arrangements(num_solutions=4):
#     """
#     Находит случайные успешные расстановки ферзей.
#     :param num_solutions: Количество успешных решений, которые нужно найти.
#     :return: Список из num_solutions успешных расстановок.
#     """
#     successful_arrangements = []
    
#     while len(successful_arrangements) < num_solutions:
#         positions = generate_random_positions()
#         if are_queens_safe(positions):  # Проверяем корректность расстановки
#             successful_arrangements.append(positions)
    
#     return successful_arrangements 
