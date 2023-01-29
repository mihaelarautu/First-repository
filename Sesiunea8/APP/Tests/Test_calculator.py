import unittest
from Sesiunea8.APP.Calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_adunare(self):
        calc = Calculator()
        self.assertEqual(10, calc.adunare(7, 3))

    def test_scadere(self):
        calc = Calculator()
        self.assertEqual(4, calc.scadere(7, 3))

    def test_inmultire(self):
        calc = Calculator()
        self.assertEqual(21, calc.inmultire(7, 3))

    def test_impartire(self):
        calc = Calculator()
        self.assertEqual(5, calc.impartire(10, 2))

    def test_radical(self):
        calc = Calculator()
        self.assertEqual(2, calc.radical(4))


