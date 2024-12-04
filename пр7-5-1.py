def gcd(a, b):
    """Функция для нахождения НОД (алгоритм Евклида)."""
    while b:
        a, b = b, a % b
    return a
def subtract_fractions(A, B, C, D):
    """Функция для вычитания дробей A/B - C/D."""
    # Находим общий знаменатель
    common_denominator = B * D
    new_numerator = A * D - C * B
    # Если результат отрицательный, делаем его положительным
    if new_numerator < 0:
        new_numerator = -new_numerator
    # Находим НОД для сокращения дроби
    divisor = gcd(new_numerator, common_denominator)
    simplified_numerator = new_numerator // divisor
    simplified_denominator = common_denominator // divisor
    
    return simplified_numerator, simplified_denominator

# Ввод данных
A = int(input("Введите числитель первой дроби (A): "))
B = int(input("Введите знаменатель первой дроби (B): "))
C = int(input("Введите числитель второй дроби (C): "))
D = int(input("Введите знаменатель второй дроби (D): "))

# Выполнение вычитания дробей
result_numerator, result_denominator = subtract_fractions(A, B, C, D)

# Вывод результата
print(result_numerator/result_denominator)
