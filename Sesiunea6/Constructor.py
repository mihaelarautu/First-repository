class Dog:
    species = 'mammal'   # class atribute -> the same for all objects of this class
    age = 12
    name = 'Spark'

d = Dog()
print(d.name)

d2 = Dog()
print(d2.name)

d3 = Dog()
print(d3.name)

d2.name = "Keemo"   # name -> becomes instance attribute
print(d2.name,d.name)

Dog.name = 'Bruno'
print(d2.name,d.name,d3.name)

# class attributes are usually used for defining constance within a class.

class Dog2:
    species = 'mammal'  # class attribute

    def __init__(self, age, name):  #instance attributes  -------------> constructor
        self.age = age
        self.name = name


my_dog = Dog2(2,'Keemo')   ### ----------> class



print(my_dog.age)
print(my_dog.name)

# Dog2.name          -> incorrect because name is an instance attribute an it can only be accessed
# via an instance(object) of this class.



