class Dog:
    species = 'mammal'

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        return f'Age: {self.age} years, name: {self.name}'

    def __repr__(self):  # folosit pt printarea colectiilor de obiecte (in principal liste)
        return self.__str__()  ## sau str(self)

    def __eq__(self, other):
        if not isinstance(other,Dog):  # daca other nu este de tipul Dog, practic verific daca ceea ce comparam este de acelasi tip cu clasa
            return False
        return self.age == other.age and self.name == other.name