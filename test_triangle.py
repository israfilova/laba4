import unittest
from triangle import triangle_area, triangle_perimeter

class TriangleTestCase(unittest.TestCase):
    def test_triangle_area(self):
        """Площадь треугольника: основание и высота положительные."""
        self.assertEqual(triangle_area(10, 5), 25)

    def test_triangle_area_zero(self):
        """Площадь треугольника: основание или высота равны 0."""
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_area(10, 0), 0)

    def test_triangle_area_negative(self):
        """Площадь треугольника: основание или высота отрицательные."""
        with self.assertRaises(ValueError):
            triangle_area(-10, 5)

    def test_triangle_perimeter(self):
        """Периметр треугольника: стороны положительные."""
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)

    def test_triangle_perimeter_negative(self):
        """Периметр треугольника: сторона отрицательная."""
        with self.assertRaises(ValueError):
            triangle_perimeter(-3, 4, 5)

if __name__ == "__main__":
    unittest.main()
