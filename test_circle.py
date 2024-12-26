import unittest
from circle import circle_area, circle_perimeter
import math

class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
        """Площадь круга: радиус положительный."""
        self.assertAlmostEqual(circle_area(5), math.pi * 25)
    
    def test_circle_area_zero(self):
        """Площадь круга: радиус равен 0."""
        self.assertEqual(circle_area(0), 0)

    def test_circle_area_negative(self):
        """Площадь круга: радиус отрицательный."""
        with self.assertRaises(ValueError):
            circle_area(-5)

    def test_circle_perimeter(self):
        """Длина окружности: радиус положительный."""
        self.assertAlmostEqual(circle_perimeter(5), 2 * math.pi * 5)

    def test_circle_perimeter_zero(self):
        """Длина окружности: радиус равен 0."""
        self.assertEqual(circle_perimeter(0), 0)

    def test_circle_perimeter_negative(self):
        """Длина окружности: радиус отрицательный."""
        with self.assertRaises(ValueError):
            circle_perimeter(-5)

if __name__ == "__main__":
    unittest.main()
