import unittest
from parameterized import parameterized

from Sesiunea8.APP.Geometric_shape import Patrat, Dreptunghi, Cerc


class TestPatrat(unittest.TestCase):

    @parameterized.expand([
        [Patrat(5), 25],
        [Patrat(10), 100],
        [Patrat(7), 49],
        [Patrat(2.5), 6.25]
    ])
    def test_aria(self, patrat, expected):
        self.assertEqual(patrat.aria(), expected)

    @parameterized.expand([
        [Patrat(5), 20],
        [Patrat(10), 40],
        [Patrat(7), 28],
        [Patrat(2.5), 10]
    ])
    def test_perimetrul(self, patrat, expected):
        self.assertEqual(patrat.perimetrul(), expected)


class TestDreptunghi(unittest.TestCase):

    @parameterized.expand([
        [Dreptunghi(5, 2), 10],
        [Dreptunghi(10, 7), 70],
        [Dreptunghi(7, 4), 28],
        [Dreptunghi(2.5, 1), 2.5]
    ])
    def test_aria(self, dreptunghi, expected):
        self.assertEqual(dreptunghi.aria(), expected)

    @parameterized.expand([
        [Dreptunghi(5, 2), 14],
        [Dreptunghi(10, 7), 34],
        [Dreptunghi(7, 4), 22],
        [Dreptunghi(2.5, 1), 7]
    ])
    def test_perimetrul(self, dreptunghi, expected):
        self.assertEqual(dreptunghi.perimetrul(), expected)


class TestCerc(unittest.TestCase):
    @parameterized.expand([
        [Cerc(2), 12.57],
        [Cerc(1), 3.14],
        [Cerc(10), 314.16]
    ])
    def test_aria(self, cerc, expected):
        self.assertEqual(cerc.aria(), expected)

    @parameterized.expand([
        [Cerc(2), 25.12],
        [Cerc(1), 6.28],
        [Cerc(10), 62.83]
    ])
    def test_perimetrul(self, cerc, expected):
        self.assertEqual(cerc.perimetrul(), expected)
