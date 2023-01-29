from abc import ABC, abstractmethod
from dataclasses import dataclass
import math

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    @abstractmethod
    def perimetrul(self):
        pass


@dataclass
class Patrat(FormaGeometrica):
    latura: float

    def __init__(self, latura):
        self._latura = latura

    def aria(self):
        return self._latura * self._latura

    def perimetrul(self):
        return self._latura * 4


@dataclass
class Dreptunghi(FormaGeometrica):
    lungime: float
    latime: float

    def __init__(self, lungime, latime):
        self._lungime = lungime
        self._latime = latime

    def aria(self):
        return self._lungime * self._latime

    def perimetrul(self):
        return 2 * (self._lungime + self._latime)


@dataclass
class Cerc(FormaGeometrica):
    PI = math.pi

    def __init__(self, raza):
        self._raza = raza

    def aria(self):
        return round(self.PI * self._raza * self._raza, 2)

    def perimetrul(self):
        return round(2 * self.PI * self._raza, 2)
