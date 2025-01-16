
# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    """
    Транспонирует заданную матрицу.
    
    :param matrix: Список списков (матрица).
    :return: Транспонированная матрица.
    """
    # Проверяем, что матрица не пустая
    if not matrix or not matrix[0]:
        raise ValueError("Матрица не должна быть пустой")
    
    # Используем вложенные списковые включения для транспонирования
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)
print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nТранспонированная матрица:")
for row in transposed_matrix:
    print(row)
