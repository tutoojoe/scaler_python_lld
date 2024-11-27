import unittest
import math

from .shape import Rectangle, Circle


class TestShapes(unittest.TestCase):
    def test_rectangle(self):
        rectangle = Rectangle(5, 4)
        self.assertEqual(rectangle.area(), 20)
        self.assertEqual(rectangle.perimeter(), 18)

    def test_circle(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.area(), math.pi * 3 ** 2, delta=0.0001)
        self.assertAlmostEqual(circle.perimeter(), 2 * math.pi * 3, delta=0.0001)


if __name__ == '__main__':
    unittest.main()
