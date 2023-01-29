# De raspuns la intrebarile:

# 1. Ce inseamna if __name__=="__main__" scris intr-un fisier python?

# Daca conditia __name__=="__main__" este indeplinita, codul se executa, in caz contrar, sare peste codul indentat.


# 2. Cum instalam un pachet extern python?

# View | Tool Windows | Python Packages | Caut pachetul dorit | Click pe 'Install with pip' sau 'Install with conda'
# Alte variante: https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html#interpreter-settings


# 3. Ce este dataclass in python?
# Dataclass este o clasa care contine date de baza, cu o functionalitate deja implementata. (@dataclass - comtine tipul variabilelor etc)


# 4. Ce este functia hash?

# hash - funcție pentru a mapa datele la o valoare numerică sau alfanumerică reprezentativă.
# Pentru funcția hash, indiferent de dimensiunea intrării, ieșirea va rămâne întotdeauna aceeași.
x = 5
hash(x)
# y = ['abc', 2]
# hash(y)
dict_z = {'a': 1}
# hash(dict_z)
# set_w = {'alb', 'negru'}
# hash(set_w)
tuplu_v = ('a', 'b', 'c')
hash(tuplu_v)


# Immutable objects are a type of object that cannot be modified after they were created.
# Hashable objects, on the other hand, are a type of object that you can call hash() on.
# So if you go into the Python interpreter and type hash, open parenthesis, and then put your object in there, close , and hit Enter and it does not error,
# then that means that your object is hashable.
# All immutable objects are hashable, but not all hashable objects are immutable.
# That’s just a rule, so anytime you see some example immutable object, you know for a fact that it’s hashable, but there are some cases where there are hashable
# objects that you actually can mutate. Python sets can only include hashable objects.
# That means that they can include immutable objects because all immutable objects are hashable and they can include mutable objects that are hashable.
# So, some examples that you’ve probably seen of immutable objects are tuples, strings, integers, and Booleans.
# This is because these objects cannot be modified after they were created.
# And then hashable objects sort of encompasses all immutable objects. An example would be you could define a class and then define your own built-in .__hash__()
# method, and this would mean that your object is hashable.


# 5. Cum pot face codul de mai jos sa functioneze corect?

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age and self.name == other.name


s = list()  # seturile nu pot fi hash-uite
p = Person(29, "Adrian")
s.append(p)


# 2. Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum
# împreună).
# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’
# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură
# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)
# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# Creează un obiect de tip Pătrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui

from abc import abstractmethod, ABC

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')

class Pătrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura
    @property
    def latura(self):
        print('Setting as property')
        return self.__latura

    @latura.getter
    def get_latura(self):
        print('Getting value')
        return self.__latura

    @latura.setter
    def set_latura(self, new_latura):
        print('Getting the new value')
        self.__latura = new_latura

    @latura.deleter
    def latura(self):
        print('Deleting value.')
        self.__latura= None



    def aria(self):
        return self.__latura * self.__latura


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        print('Setting as property')
        return self.__raza

    @raza.getter
    def get_raza(self):
        print('Getting value')
        return self.__raza

    @raza.setter
    def set_raza(self, new_raza):
        print('Getting the new value')
        self.__raza = new_raza

    @raza.deleter
    def raza(self):
        print('Deleting value.')
        self.__raza = None

    def aria(self):
        return self.PI * self.__raza * self.__raza

    def descrie(self):
        print('Eu nu am colturi')

P1 = Pătrat(4)
print(P1.get_latura)
P1.set_latura = 2
print(P1.get_latura)
print((P1.aria()))
P1.descrie()

C1 = Cerc(1)
print(C1.get_raza)
C1.set_raza = 2
print(C1.get_raza)
print((C1.aria()))
C1.descrie()