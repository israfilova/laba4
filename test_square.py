import unittest
from square import square_area, square_perimeter

class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
        """Площадь квадрата: сторона положительная."""
        self.assertEqual(square_area(4), 16)

    def test_square_area_zero(self):
        """Площадь квадрата: сторона равна 0."""
        self.assertEqual(square_area(0), 0)

    def test_square_area_negative(self):
        """Площадь квадрата: сторона отрицательная."""
        with self.assertRaises(ValueError):
            square_area(-4)

    def test_square_perimeter(self):
        """Периметр квадрата: сторона положительная."""
        self.assertEqual(square_perimeter(4), 16)

    def test_square_perimeter_zero(self):
        """Периметр квадрата: сторона равна 0."""
        self.assertEqual(square_perimeter(0), 0)

    def test_square_perimeter_negative(self):
        """Периметр квадрата: сторона отрицательная."""
        with self.assertRaises(ValueError):
            square_perimeter(-4)

if __name__ == "__main__":
    unittest.main()
