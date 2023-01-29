# relatii copil-parinte intre clase



class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_name(self):
        print(f'My name is {self.name}')

class Student(Person):
    def __init__(self, age, name, university):
        # Person.init(self, age, name)
        super().__init__(age, name)
        self.university = university
    def print_name(self): # suprascrie aceeasi functie definita in clasa Person
        print(f'My name is {self.name} and i study at {self.university}')

s1 = Student(18, 'John', 'UCLA')
print(s1.age)
s1.print_name()