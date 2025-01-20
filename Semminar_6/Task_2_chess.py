# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

import random

def generate_random_positions():
    """
    Генерирует случайную расстановку ферзей на доске 8x8.
    :return: Список кортежей (x, y) с координатами ферзей.
    """
    rows = list(range(1, 9))
    random.shuffle(rows)  # Перемешиваем строки
    columns = list(range(1, 9))
    return list(zip(rows, columns))


def find_successful_arrangements(num_solutions=4):
    """
    Находит случайные успешные расстановки ферзей.
    :param num_solutions: Количество успешных решений, которые нужно найти.
    :return: Список из num_solutions успешных расстановок.
    """
    successful_arrangements = []
    
    while len(successful_arrangements) < num_solutions:
        positions = generate_random_positions()
        if are_queens_safe(positions):  # Проверяем корректность расстановки
            successful_arrangements.append(positions)
    
    return successful_arrangements

def are_queens_safe(positions):
    """
    Проверяет, находятся ли 8 ферзей в безопасной позиции.
    
    :param positions: Список из 8 пар координат (x, y), где 1 <= x, y <= 8.
    :return: True, если ферзи не атакуют друг друга, иначе False.
    """
    rows = set()  # Хранит строки, занятые ферзями
    cols = set()  # Хранит столбцы, занятые ферзями
    diag1 = set()  # Хранит главные диагонали (x - y)
    diag2 = set()  # Хранит побочные диагонали (x + y)

    for x, y in positions:
        # Если ферзь занимает ту же строку, столбец или диагональ
        if x in rows or y in cols or (x - y) in diag1 or (x + y) in diag2:
            return False

        # Добавляем координаты ферзя в соответствующие множества
        rows.add(x)
        cols.add(y)
        diag1.add(x - y)
        diag2.add(x + y)

    return True
