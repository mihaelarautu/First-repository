#  a for loop is used fot iterating over sequence (list, tuple, dict, set, string)
for i in range(10):  # 0 - 9
    print(i)

print(50*'#')
for i in range(1,6):  # 1 - 5
    print(i)


print(50*'#')
lst = [1, 2, 3, 4, 5]
for i in range(len(lst)):
    print(lst[i])

print(50*'#')
for i in range(1,6,2):
    print(i)

print(50*'#')
for i in range(5,0,-1):
    print(i)

print(50*'#')
for i in range(len(lst)-1,-1,-1):
    print(lst[i])

print(50*'#')
# for each
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

print(50*'#')
for x in "Ana are mere":
    print(x)

print(50*'#')
dct = {'a':1, 'b':2}
for x in dct:  # in a dict you iterate through keys
    print(x)
    print(dct[x])
for key,value in dct.items():
    print(key,value)

print(50*'#')
# break
for x in fruits:
    print(x)
    if x == 'banana':
        break


print(50*'#')
# continue
for x in fruits:
    if x == "banana":
        continue
    print(x)

print(50*'#')
# else
for x in range(50):
    print(x)
else:
    print("Finally finished.")

print(50*'#')
# nested for
adj = ['red', 'big', 'tasty']
for fruit in fruits:
    for x in adj:
        print(x,fruit)

print(50*'#')
# pass
for x in [1, 2, 3]:
    pass
