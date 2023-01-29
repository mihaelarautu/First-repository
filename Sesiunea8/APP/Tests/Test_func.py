import unittest
from parameterized import parameterized

from Sesiunea8.APP.Func import is_div_3_5, only_ints, NotIntegerNumberException


class TestFunc(unittest.TestCase):
    def test_is_div_3_5_35(self):
        self.assertEqual(is_div_3_5(45), 35)

    def test_is_div_3_5_3(self):
        self.assertEqual(is_div_3_5(9), 3)

    def test_is_div_3_5_5(self):
        self.assertEqual(is_div_3_5(25), 5)

    def test_is_div_3_5_not_div(self):
        self.assertEqual(is_div_3_5(19), None)

    @parameterized.expand([
        (45, 35), (9, 3), (25, 5), (19, None)
    ])
    def test_is_div_3_5(self, n, expected):
        self.assertEqual(is_div_3_5(n), expected)

    def test_only_ints(self, numbers):
        self.assertRaises(NotIntegerNumberException, only_ints, numbers)