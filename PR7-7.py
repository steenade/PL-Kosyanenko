def area_triangle(base, height):
    """Вычисляет площадь прямоугольного треугольника."""
    return 0.5 * base * height

def area_rectangle(length, width):
    """Вычисляет площадь прямоугольника."""
    return length * width

def area_quadrilateral(X, Y, Z, T):
    """Вычисляет площадь четырехугольника с прямым углом между X и Y."""
    triangle_area = area_triangle(X, Y)
    rectangle_area = area_rectangle(Z, T)
    return triangle_area + rectangle_area

# Пример использования
X = float(input("Введите длину стороны X: "))
Y = float(input("Введите длину стороны Y: "))
Z = float(input("Введите длину стороны Z: "))
T = float(input("Введите длину стороны T: "))

total_area = area_quadrilateral(X, Y, Z, T)
print(f"Площадь четырехугольника: {total_area}")

def to_octal_with_leading_zeros(n):
    """Преобразует неотрицательное целое число в 10-значный восьмеричный код."""
    if n < 0:
        raise ValueError("Число должно быть неотрицательным.")
    
    # Преобразуем число в восьмеричную систему и удаляем '0o' в начале
    octal_str = oct(n)[2:]
    
    # Добавляем ведущие нули, чтобы получить длину 10
    octal_str = octal_str.zfill(10)
    
    return octal_str

# Пример использования
try:
    number = int(input("Введите неотрицательное целое число: "))
    result = to_octal_with_leading_zeros(number)
    print(f"Восьмеричный код (10 знаков): {result}")
except ValueError as e:
    print(e)






	

	

	
	
