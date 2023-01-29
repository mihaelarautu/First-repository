# lists are used to store multiple itims in a single variable
# list items are ordered, changeable and allow duplicates

# Create
fruits = ["appe","banana","cherry"]
numbers = [1, 2, 3, 4, 5]
cars = list(("BMW","Audi","Tesla"))

# Indexing - accesing elements
print(20 * '-','indexing',20 * '-')
print(numbers[0])
print(numbers[-1])
print(numbers[2:4])
print(numbers[::2])  # din 2 in 2 de la inceput pana la sfarsit
print(numbers[::-1])  # inversare

# Adding elements
print(20 * '-','add element',20 * '-')
numbers.append(10)
print(numbers)  # append-ul adauga la final

numbers.insert(4,6)  # insert baga elementul la indexul dorit (adauga 6 in locul elementului cu index 6
print(numbers)
print(20 * '-','remove element',20 * '-')
elem = numbers.pop()  #elimina ultimul element, si il si returneaza
print(elem)
print(numbers)

numbers.pop(0)
print(numbers)

numbers.remove(3) # (elimina elementul dorit, primul)
print(numbers)

# remove all elements
print(20 * '-','remove all element',20 * '-')
numbers.clear()
print(numbers)

numbers = [1, 2, 3, 4, 5]

# replace
print(20 * '-','replace',20 * '-')
fruits[1] = 'pear'
print(fruits)

# count
print(20 * '-','count',20 * '-')
print(numbers.count(3))

#add two list
print(20 * '-','add two list',20 * '-')
numbers2 = [10, 11, 12]
print(numbers + numbers2) # se creaza o noua lista

numbers.extend(numbers2) # se surascrie prima lista, cu lista cu toate elementele
print(numbers)

# reverse
print(20 * '-','reverse',20 * '-')
print(numbers[::-1])  # creaza lista noua

numbers.reverse()  # in place
print(numbers)

# sort
numbers = [1, 8, 7, 5, 9, 11]
numbers.sort()  # in place
print(numbers)
numbers.sort(reverse=True)
print(numbers)