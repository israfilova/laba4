import math

def circle_area(radius):
    """Вычисление площади круга."""
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным.")
    return math.pi * radius ** 2

def circle_perimeter(radius):
    """Вычисление длины окружности."""
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным.")
    return 2 * math.pi * radius

#for commit