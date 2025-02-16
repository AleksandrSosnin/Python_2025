# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

from Task_2_chess import are_queens_safe

# Пример ввода: координаты 8 ферзей, здесь можем изменять координаты для тестирования.

positions = [
    (1, 5),
    (2, 8),
    (3, 1),
    (4, 6),
    (5, 3),
    (6, 7),
    (7, 2),
    (8, 4)
]

# Проверяем расположение ферзей
if are_queens_safe(positions):
    print("Ферзи не бьют друг друга.")
else:
    print("Ферзи атакуют друг друга.")
