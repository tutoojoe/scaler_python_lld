import unittest
import io
from unittest.mock import patch
from .threedPoint import Point,ThreedPoint

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point = Point(2, 3)  # Sample Point

    def test_display(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.point.display()
            self.assertEqual(mock_stdout.getvalue(), "[2, 3]\n")


class TestThreedPoint(unittest.TestCase):
    def setUp(self):
        self.threed_point = ThreedPoint(2, 3, 4)  # Sample ThreedPoint

    def test_display(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.threed_point.display()
            self.assertEqual(mock_stdout.getvalue(), "[2, 3, 4]\n")


if __name__ == '__main__':
    unittest.main()