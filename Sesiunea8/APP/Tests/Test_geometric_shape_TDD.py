import pytest
from Sesiunea8.APP.Geometric_shape import Patrat, Dreptunghi, Cerc


class TestPatrat:


    @pytest.mark.parametrize('n, expected', [
        (Patrat(5), 25),
        (Dreptunghi(5, 2), 10),
        (Cerc(2), 12.57)
     ])

    def test_aria(self,n, expected):
        assert n.aria() == expected

    @pytest.mark.parametrize('n, expected', [
        (Patrat(5), 20),
        (Dreptunghi(5, 2), 14),
        (Cerc(2), 12.57)
    ])
    def test_perimetrul(self, n, expected):
        assert n.perimetrul() == expected