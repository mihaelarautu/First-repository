########################################################################################
def plus(a,b):  # a,b positional arguments
    return a+b

plus(1,2)
########################################################################################
# default arguments
def plus(a,b=2):  # b has default value 2
    return a+b

print(plus(1))
plus(1,3)
########################################################################################
# keyword arguments

def plus(a,b):
    return a+b
plus(a=1,b=2)
plus(b=2,a=1)  # specificand argumentele prin nume, nu mai8 este necesar sa pasrtram ordinea lor
########################################################################################
# variable number of arguments  ->args

def plus(*args):
    print(args)
    return sum(args)
plus(1,2,3)
plus()
plus(5)
plus(*[1,2,3])  # * dezbraca lista de paranteze, linia29 = linia26   # *-> unpacking


def plus(**kwargs): #keywordargs (kwargs) is a dict
    print(kwargs)
    return sum(kwargs.values())

plus(a=1,b=2)
plus()
plus(c=5)
plus(**{'a':1,'b':2})  # echivalent cu linia 36

def plus(*args, **kwargs):
    return sum(args)+sum(kwargs.values())
plus(1)
plus(1,d=7)
plus()
plus(1,2,3, c=9)
plus(z=13)
# plus(d=7, 1) -> error because positional argument after keyword argument
########################################################################################

def plus(a,b):
    print(a,b)
    return a+b

plus(1,2)
plus(*[1,2])
plus(**{'a':1,'b':2})
plus(a=1,b=2)
