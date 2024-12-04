def swap_max_min(matrix):
    if not matrix or not matrix[0]:
        return matrix
    max_value = float('-inf')
    min_value = float('inf')
    max_position = (-1, -1)
    min_position = (-1, -1)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_position = (i, j)
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_position = (i, j)
    if max_position != (-1, -1) and min_position != (-1, -1):
        matrix[max_position[0]][max_position[1]], matrix[min_position[0]][min_position[1]] =\
            matrix[min_position[0]][min_position[1]], matrix[max_position[0]][max_position[1]]
    return matrix

n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество столбцов матрицы: "))
matrix = []
print("Введите элементы матрицы построчно (через пробел):")
for i in range(n):
    row_input = input(f"Строка {i + 1}: ")
    row = list(map(int, row_input.split()))
    matrix.append(row)
result_matrix = swap_max_min(matrix)
print("Изменённая матрица:")
for row in result_matrix:
    print(" ".join(map(str, row)))