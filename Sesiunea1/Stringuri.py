name = 'Dragos'
print(len(name))  # length of the string

print(name.upper())  # convert string to uppercase

print(name.lower())  # convert string to lowercase

name = "Anamaria"
print(name.count('a'))
print(name.count('s'))  # counts the number of occurrences of the given characters

prop = 'Oare vreau sa merg acolo!\nUnde sa mergi!'  #\n = linie noua
print(prop)
prop = prop.replace('!','?')
print(prop)

food = 'pizza'
print(food.replace('zz','t'))



name = 'John'
print(name.index('o'))  #finds the index of the given character
print(name[0])
print(name[-1])  #negative sign = tranversare inversa a stringului

d = 'Hello world'
print(d[2:5])  # from 2 to 5 (without 5) = slicing
print(d[:5])   # from start to 4
print(d[2:])   # from 2 to end
print(d[-5:-8:-1])  # -1 -> traversare inversa
print(d[2:8:2])


