# sets are used to store multiple unique items in a single variable

# create
fruits = {'apple','banana','cherry'}
cars = {}  #atentie, acesta este un dictionar!
cars = set()


# add elements
print(20 * '-','add elements',20 * '-')
fruits.add('pear')
print(fruits)
fruits.add('pear')
print(fruits)
tropical ={'papaya','mango'}
fruits.update(tropical)
print(fruits)

mylist = ['kiwi','orange']
fruits.update(mylist)
print(fruits)

# remove
print(20 * '-','remove',20 * '-')
fruits.remove('mango')
print(fruits)


fruits.discard('pear')
print(fruits)

# fruits.remove('grapes')  # can't eliminate elements that don't exist
fruits.discard('grapes')  # ruleaza chiar si daca elementul cautat nu exista

fruits.pop()  # removes ramdom elements
print(fruits)
a = fruits.pop()
print(a)

# remove all elememnts
print(20 * '-','remove all elements',20 * '-')
a = {1, 2, 3}
a.clear()
print(a)

# join
print(20 * '-','join',20 * '-')
s1 = {'a','b','c'}
s2 = {1, 2, 3}
s3 = s1.union(s2)
print(s3)
print(s1^s2)


# intersection
print(20 * '-','intersection',20 * '-')
x = {'apple','Banana','Cherry'}
y = { 'Google', 'Microsoft','apple'}
z = x.intersection(y)
print(z)

print(x & y)

# difference
print(20 * '-','difference',20 * '-')
x = {'apple','Banana','Cherry'}
y = { 'Google', 'Microsoft','apple'}
z = x.difference(y)
print(z)
print(x - y)  #operator simplu

# symmetric difference
print(20 * '-','symmetric difference',20 * '-')
x = {'apple','Banana','Cherry'}
y = { 'Google', 'Microsoft','apple'}
z = x.symmetric_difference(y)
print(z)
print(x^y)  #operator simplu

#issubset, issuperset
print(20 * '-','issubset, issuperset',20 * '-')
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
print(b.issubset(a))
print(a.issuperset(b))
