def gcd(a, b):
    """Функция для вычисления НОД с использованием алгоритма Евклида."""
    while b:
        a, b = b, a % b
    return a

def subtract_fractions(A, B, C, D):
    """Функция для вычитания дробей A/B - C/D."""
    # Приведение дробей к общему знаменателю
    numerator = A * D - C * B
    denominator = B * D
    
    # Проверка на отрицательный числитель
    if numerator < 0:
        numerator = -numerator
        denominator = -denominator

    # Нахождение НОД
    common_divisor = gcd(numerator, denominator)

    # Приведение дроби к несократимой форме
    numerator //= common_divisor
    denominator //= common_divisor

    return numerator, denominator

# Ввод данных
A = int(input("Введите A (числитель первой дроби): "))
B = int(input("Введите B (знаменатель первой дроби): "))
C = int(input("Введите C (числитель второй дроби): "))
D = int(input("Введите D (знаменатель второй дроби): "))

# Вычисление результата
result_numerator, result_denominator = subtract_fractions(A, B, C, D)

# Вывод результата
print(f"Результат вычитания: {result_numerator}/{result_denominator}")

def divisors(n):
 result = ""
 for i in range(1, n + 1):
 if n % i == 0:
 result += str(i) + " "
 return result

n = int(input())
result = divisors(n)
print(result)


	





	

	

	
	
