def triangle_area(base, height):
    """Вычисление площади треугольника."""
    if base < 0 or height < 0:
        raise ValueError("Основание и высота не могут быть отрицательными.")
    return 0.5 * base * height

def triangle_perimeter(a, b, c):
    """Вычисление периметра треугольника."""
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны треугольника не могут быть отрицательными.")
    return a + b + c