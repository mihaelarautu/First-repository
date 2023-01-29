"""
Clasele se scriu cu litara mare si fara _: NumeClasa
Numele fisierelor in care se afla o clasa au acelasi nume cu clasa doar ca se scrie cu litera mica si cu _: nume_clasa
"""

from Magic_methods import Dog
from Class_with_attributes import Dog as DogWithAttributes
from Dogs.Dog.Dog import Dog as Dog2

d = Dog(1,'Dino')
print(d)

d2 = DogWithAttributes()
print(d2)

d3 = Dog2(1,'Rex')
print(d3)


