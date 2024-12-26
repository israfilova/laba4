import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    # Тесты для area
    def test_area_positive_values(self):
        """Площадь: обе стороны положительные."""
        self.assertEqual(area(5, 10), 50)

    def test_area_zero_value(self):
        """Площадь: одна из сторон равна 0."""
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(10, 0), 0)

    def test_area_negative_value(self):
        """Площадь: одна из сторон отрицательная."""
        with self.assertRaises(ValueError):
            area(-5, 10)
        with self.assertRaises(ValueError):
            area(10, -5)

    # Тесты для perimeter
    def test_perimeter_positive_values(self):
        """Периметр: обе стороны положительные."""
        self.assertEqual(perimeter(5, 10), 30)

    def test_perimeter_zero_value(self):
        """Периметр: одна из сторон равна 0."""
        self.assertEqual(perimeter(0, 10), 20)
        self.assertEqual(perimeter(10, 0), 20)

    def test_perimeter_negative_value(self):
        """Периметр: одна из сторон отрицательная."""
        with self.assertRaises(ValueError):
            perimeter(-5, 10)
        with self.assertRaises(ValueError):
            perimeter(10, -5)

if __name__ == "__main__":
    unittest.main()
