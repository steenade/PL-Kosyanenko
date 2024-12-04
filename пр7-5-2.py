def find_divisors(n):
    """Функция для нахождения всех делителей числа n."""
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# Ввод числа от пользователя
number = int(input("Введите число: "))

# Получение делителей
divisors = find_divisors(number)

# Вывод делителей в одной строке, разделенных пробелами
print(" ".join(map(str, divisors)))
