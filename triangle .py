def area(a, h):
    """
            возвращает площадь треугольника
            a(int) - основание треугольника
            h(int) - выоста треугольника
            возвращаемое значение: a * h/2 - искомая площадь
        """
    return a * h / 2
def perimeter(a, b, c):
    """
                возвращает периметр прямоугольника
                a(int) - длина
                b(int) - ширина
                возвращаемое значение: a * b - искомая периметр
            """
    if type(a) is not int and type(b) is not int and  type(b) is not int:
        raise TypeError("аргументы должны быть int")
    if a <= 0 or b <= 0 or c<= 0:
        raise ValueError("аргументы должны быть > 0")
    return a + b + c