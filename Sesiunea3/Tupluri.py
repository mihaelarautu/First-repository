# tuples are used to store multiple items in a single variable
# tuples are unchangeable

# create
fruits = ('apple','banana','cherry','cherry')


# count
print(20 * '-','count',20 * '-')
print(fruits.count('cherry'))

# indexing
print(20 * '-','indexing',20 * '-')
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])

# adding elements
print(20 * '-','adding element',20 * '-')
fruits += ('pear',)
print(fruits)
# adaugam elemente prin crearea unui tuplu pe care in alaturam

fruits2 = ('mango','papaya','kiwi')
y = list(fruits2)
y.append('orange')
fruits2 = tuple(y)
print(fruits2)

# remove one lement
print(20 * '-','remove',20 * '-')
fruits2 = ('mango','papaya','kiwi')
y = list(fruits2)
y.remove('kiwi')
fruits2 = tuple(y)
print(fruits2)

