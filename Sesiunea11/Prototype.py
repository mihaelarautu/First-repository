'''
Creational Patterns
Prototype - a creational design pattern that lets you copy existing objects without making your
            code dependent on their classes.

PROS

- Reusability: In case we want to create an instance of a class with many default values,
             or in the same complicated processes, Prototype Pattern is useful.
             We can focus on other activities instead.
- Reducing initialization: We can get new instances at a cheaper cost. The clients can get new objects
                         without knowing which type of object it will be.
- Simple copy process: It hides the complexities of creating objects.
                     We only need to call clone() method,it is simple and easy to read.
                     It reduces the need for sub-classing. It lets you add or remove objects at runtime.


CONS

This model is costly. There is certainty in determining the number of iterations.
Each subclass has to implement clone() methods or alternative copy methods.
Building clones for existing classes may be complicated.
For example, implementing Cloneable interface can constrain all subclasses/implementation
to implement theclone() method (some class may not need).
If the class is in circular references, implementing theclone() method in a shallow copy way may cause problems.
 In the example with fields that are primitive, it is ok, but when a class object contains many fields that have references to other objects,
 we need to implement deep copy.
'''

from abc import ABCMeta, abstractmethod

class IProtoType(metaclass=ABCMeta):
    "interface with clone method"
    @staticmethod
    @abstractmethod
    def clone():
        """The clone, deep or shallow.
        It is up to you how you want to implement
        the details in your concrete class"""

class MyClass(IProtoType):
    "A Concrete Class"

    def __init__(self, field):
        self.field = field  # any value of any type

    def clone(self):
        " This clone method uses a shallow copy technique "
        return type(self)(
            self.field  # a shallow copy is returned
            # self.field.copy() # this is also a shallow copy, but has
            # also shallow copied the first level of the field.
            # So it is essentially a shallow copy but 2 levels deep.
            # To recursively deep copy collections containing inner
            # collections, example: lists of lists.

        )

    def __str__(self):
        return f"{id(self)}\tfield={self.field}\ttype={type(self.field)}"

# The Client
OBJECT1 = MyClass([1, 2, 3, 4])  # Create the object containing a list
print(f"OBJECT1 {OBJECT1}")

OBJECT2 = OBJECT1.clone()  # Clone

# Changing the value of one of the list elements in OBJECT2,
# to see if it also modifies the list element in OBJECT1.
# If it changed OBJECT1s copy also, then the clone was done
# using a 1 level shallow copy process.
# Modify the clone method above to try a 2 level shallow copy instead
# and compare the output
OBJECT2.field[1] = 101

# Comparing OBJECT1 and OBJECT2
print(f"OBJECT2 {OBJECT2}")
print(f"OBJECT1 {OBJECT1}")