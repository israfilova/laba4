def area(length, width):
    """Вычисление площади прямоугольника."""
    if length < 0 or width < 0:
        raise ValueError("Длина и ширина не могут быть отрицательными.")
    return length * width

def perimeter(length, width):
    """Вычисление периметра прямоугольника."""
    if length < 0 or width < 0:
        raise ValueError("Длина и ширина не могут быть отрицательными.")
    return 2 * (length + width)
