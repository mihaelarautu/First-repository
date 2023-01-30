# O clasa abstracta este o clasa care are cel putin o metoda abstracta

# O metoda abstracta este o metoda fara corp -> are pass in interior

# O metoda = o functie intr-o clasa

# O clasa abstracta nu poate fi instantiata

from abc import abstractmethod, ABC  # abstract base class


class Animal(ABC):
    @abstractmethod  # decorator
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        raise NotImplementedError

class Dog(Animal):
    def sound(self):
        print('Ham, ham!')

    def sleep(self):
        print('Zzzzzzzzz')

class Cat(Animal):
    def sound(self):
        print('Miau!')

    def sleep(self):
        print('Prrrrr')

cat1=Cat()
dog1=Dog()

cat1.sound()
cat1.sleep()

dog1.sound()
dog1.sleep()

# a = Animal() -> EROARE pentru ca NU se paote instantia o clasa abstracta
# a.sleep()