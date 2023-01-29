class Dog:
    species = 'mammal'

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def bark(self):          # self --> reference to the current object
        print('Ham, Ham')

    def get_owner(self):
        return f'I am {self.name} and Andrei ownes me'

dog = Dog(2,'Keemo')
dog.bark()
print(dog.get_owner())

dog2 = Dog(3,'Mimi')
print(dog2.get_owner())

print(type(dog2))
print(type(Dog))
print(type(int))
