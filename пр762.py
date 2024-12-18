import math
def calculate_area(a, b, c, d, p):
    """Функция для вычисления площади выпуклого четырехугольника."""
    s_a = (a + b + c + d) / 2  # Полупериметр
    area = math.sqrt(s_a * (s_a - a) * (s_a - b) * (s_a - c) * (s_a - d) - p**2)
    return area
# Ввод данных от пользователя
a = float(input("Введите длину первой стороны (a): "))
b = float(input("Введите длину второй стороны (b): "))
c = float(input("Введите длину третьей стороны (c): "))
d = float(input("Введите длину четвертой стороны (d): "))
p = float(input("Введите длину диагонали (p): "))
# Проверка, что стороны и диагональ положительные
if a <= 0 or b <= 0 or c <= 0 or d <= 0 or p <= 0:
    print("Пожалуйста, введите положительные значения для сторон и диагонали.")
else:
    # Вычисление площади
    area = calculate_area(a, b, c, d, p) 
    # Вывод результата
    print("Площадь выпуклого четырехугольника =", area)
