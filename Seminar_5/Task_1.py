# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def parse_file_path(file_path):
    """
    Функция принимает абсолютный путь до файла и возвращает кортеж из трёх элементов:
    - путь до директории,
    - имя файла без расширения,
    - расширение файла.

    :param file_path: str — абсолютный путь до файла
    :return: tuple — (путь, имя файла, расширение файла)
    """
    # Извлекаем путь до директории
    dir_path = os.path.dirname(file_path)
    
    # Извлекаем имя файла с расширением
    file_name_with_ext = os.path.basename(file_path)
    
    # Разделяем имя файла и его расширение
    file_name, file_ext = os.path.splitext(file_name_with_ext)
    
    return dir_path, file_name, file_ext

# Пример использования
file_path = "/home/user/documents/example.txt"
result = parse_file_path(file_path)
print(result)
