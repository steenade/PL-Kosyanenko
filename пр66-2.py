array = []
for i in range(10):
    number = int(input("Число " + str(i + 1) + ": "))
    array.append(number)

# Определение суммы чисел, больших 5
sum5 = sum(num for num in array if num > 5)

# Вывод результатов
print("Введенный массив:", array)
print("Сумма чисел, больших 5:", sum5)
