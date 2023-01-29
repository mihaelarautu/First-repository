# dictionaries are used to store data values in key:value pairs
# create
car = {
    'brand':'Ford',
    'model':'Mustang',
    'year':1964

}
# accesing elements
print(20 * '-','accesing elements',20 * '-')
print(car['brand'])
print(car.get('model'))
print(car.get('is_new')) # get - in cazul in care cheia nu exista, ofera raspunsul None
#  print(car.get('is_new',True)) # get - in cazul in care cheia nu exista, ofera raspunsul True

# adding elements
print(20 * '-','adding elements',20 * '-')
car['Is_new'] = True
print(car)

print(car.setdefault('Serie', 12345))
print(car)
print(car.setdefault('is_new', False))
print(car)

# replace
print(20 * '-','replace',20 * '-')
car['is_new'] = False
print(car)

car.update({'is_new':True, 'price': 10000})
print(car)

# remove elememnt
print(20 * '-','remove element',20 * '-')

car.pop('is_new')
print(car)

car.popitem()  # removes last inserted
print(car)

del car["Serie"]
print(car)


# remove all elements
print(20 * '-','remove all element',20 * '-')
a = {1:3,2:True}
a.clear()
print(a)

# all keys
print(20 * '-','all keys',20 * '-')
print(car.keys())
print(list(car.keys()))

# all values
print(20 * '-','all values',20 * '-')
print(car.values())
print(list(car.values()))

# all items
print(20 * '-','all items',20 * '-')
print(car.items())
print(list(car.items()))



# !!!! se verificat cu cea scrisa de colegi, de pe discord, is_new e dublat!

