import unittest
from parameterized import parameterized

from Sesiunea8.APP.Maximum_number import get_max


class TestMaximum(unittest.TestCase):
    def test_get_max(self):
        self.assertEqual(15, get_max(10, 15, 0))

    def test_get_max(self):
        self.assertEqual(5, get_max(5, 2, -1))

    @parameterized.expand([
        (15, 10, 15, 0), (5, 5, 2, -1)

    ])
    def test_get_max(self, expected, a, b, c):
        self.assertEqual(expected, get_max(a, b, c))
