def maxandmintomat(mat):
    maxmat = [max(ryad) for ryad in mat]
    minmat = [min(ryad) for ryad in mat]
    return maxmat, minmat
# Чтение из файла
with open('KosyanenkoVyacheslavAndreevich_VVOD.txt', 'r') as file:
    # Читаем размеры матрицы
    n, m = map(int, file.readline().strip().split())
    mat = []
    # Читаем строки матрицы
    for i in range(n):
        ryad1 = file.readline().strip()
        ryad = list(map(int, ryad1.split()))
        mat.append(ryad)
maxmat, minmat = maxandmintomat(mat)
# Запись результатов в отдельный файл
with open('KosyanenkoVyacheslavAndreevich_VIVOD.txt', 'w') as output_file:
    output_file.write(' '.join(map(str, maxmat)) + '\n')
    output_file.write(' '.join(map(str, minmat)) + '\n')

