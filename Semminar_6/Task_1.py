# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import argparse
from datetime import datetime

def is_valid_date(date_str):
    """
    Проверяет, является ли строка корректной датой формата YYYY-MM-DD.
    
    :param date_str: Строка с датой.
    :return: True, если дата корректна, иначе False.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def main():
    """
    Основная функция, реализующая парсинг аргументов и проверку даты.
    """
    parser = argparse.ArgumentParser(description="Проверка корректности даты.")
    parser.add_argument("date", type=str, help="Дата для проверки в формате YYYY-MM-DD")
    args = parser.parse_args()

    date_str = args.date

    if is_valid_date(date_str):
        print(f"Дата {date_str} корректна.")
    else:
        print(f"Дата {date_str} некорректна. Убедитесь, что формат YYYY-MM-DD.")

if __name__ == "__main__":
    main()
