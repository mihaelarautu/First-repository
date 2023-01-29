import pytest
from Sesiunea8.APP.Calculator import Calculator


class TestCalculator:
    @pytest.mark.parametrize("a, b, expected", [(25, 5, 30),
                                                (4, 2, 6),
                                                (6.25, 2.5, 8.75),
                                                (9, 3, 12)
                                                ])
    def test_adunare(self, a, b, expected):
        assert Calculator.adunare(self, a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [(25, 5, 20),
                                                (4, 2, 2),
                                                (6.25, 2.5, 3.75),
                                                (9, 3, 6)
                                                ])
    def test_scadere(self, a, b, expected):
        assert Calculator.scadere(self, a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [(25, 5, 125),
                                                (4, 2, 8),
                                                (6.25, 2.5, 15.625),
                                                (9, 3, 27)
                                                ])
    def test_inmultire(self, a, b, expected):
        assert Calculator.inmultire(self, a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [(25, 5, 5),
                                                (4, 2, 2),
                                                (6.25, 2.5, 2.5),
                                                (9, 3, 3)
                                                ])
    def test_impartire(self, a, b, expected):
        assert Calculator.impartire(self, a, b) == expected

    @pytest.mark.parametrize("a, expected", [(25, 5),
                                                (4, 2),
                                                (6.25, 2.5),
                                                (9, 3)
                                                ])
    def test_radical(self, a, expected):
        assert Calculator.radical(self, a) == expected

