# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

def calculate_bonus(names, salaries, bonuses):
    """
    Генератор словаря, который принимает три списка:
    - names: список имен сотрудников (str),
    - salaries: список ставок (int),
    - bonuses: список премий в процентах (str).
    Возвращает словарь с именем сотрудника в качестве ключа и суммой премии как значение.

    :param names: list[str]
    :param salaries: list[int]
    :param bonuses: list[str]
    :return: dict
    """
    return {name: salary * float(bonus.strip('%')) / 100 for name, salary, bonus in zip(names, salaries, bonuses)}

# Пример входных данных
names = ["Иван", "Мария", "Петр"]
salaries = [50000, 60000, 70000]
bonuses = ["10.25%", "15.50%", "20.00%"]

# Результат
result = calculate_bonus(names, salaries, bonuses)
print(result)
