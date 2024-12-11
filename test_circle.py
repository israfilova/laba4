import unittest
from circle import circle_area, circle_perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero_value(self):
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_area_positive_value(self):
        res = circle_area(10)
        self.assertAlmostEqual(res, 314.1592653589793)

    def test_perimeter_zero_value(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive_value(self):
        res = circle_perimeter(10)
        self.assertAlmostEqual(res, 62.83185307179586)

    def test_area_negative_value(self):
        with self.assertRaises(ValueError):
            circle_area(-10)

    def test_perimeter_negative_value(self):
        with self.assertRaises(ValueError):
            circle_perimeter(-10)