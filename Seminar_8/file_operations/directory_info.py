import os

def get_directory_info(directory):
    """
    Рекурсивно обходит директорию и возвращает структуру данных с информацией о файлах и папках.

    :param directory: Путь к директории.
    :return: Список словарей с информацией о файлах и папках.
    """
    result = []

    for root, dirs, files in os.walk(directory):
        for d in dirs:
            dir_path = os.path.join(root, d)
            dir_size = calculate_directory_size(dir_path)
            result.append({
                "name": d,
                "path": dir_path,
                "type": "directory",
                "size_bytes": dir_size,
                "parent_directory": root,
            })

        for f in files:
            file_path = os.path.join(root, f)
            file_size = os.path.getsize(file_path)
            result.append({
                "name": f,
                "path": file_path,
                "type": "file",
                "size_bytes": file_size,
                "parent_directory": root,
            })

    return result

def calculate_directory_size(directory):
    """
    Вычисляет общий размер всех файлов в директории, включая вложенные папки.

    :param directory: Путь к директории.
    :return: Размер в байтах.
    """
    total_size = 0
    for root, _, files in os.walk(directory):
        for f in files:
            file_path = os.path.join(root, f)
            total_size += os.path.getsize(file_path)
    return total_size
