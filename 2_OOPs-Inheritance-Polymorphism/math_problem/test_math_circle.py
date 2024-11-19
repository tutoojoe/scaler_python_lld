import unittest

from .math_circle import Math


class TestMath(unittest.TestCase):
    def test_getCircleArea(self):
        # Test for radius = 1
        self.assertAlmostEqual(Math.getCircleArea(1), 3.14)
        # Test for radius = 2
        self.assertAlmostEqual(Math.getCircleArea(2), 12.56)
        # Test for radius = 0
        self.assertAlmostEqual(Math.getCircleArea(0), 0.0)

    def test_static_data_member(self):
        self.assertEqual(Math.PI, 3.14)


if __name__ == "__main__":
    unittest.main()
