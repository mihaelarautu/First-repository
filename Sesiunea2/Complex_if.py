# 1. Nested if (imbricat)
a = 50
b = 6
c = 9
if a > b:
    if c != 0:
        print('c diferit de 0')
    else:
        print('c')
else:
    if c == 0:
        print('c este 0')

# 2. Multiple conditions
x = 1
y = 5
z = 7
# verificam daca toate numerele sunt pare
if x%2==0 and y%2==0 and z%2==0:
    print('toate sunt pare')
elif x%2==0 or y%2==0 or z%2==0:
    print('cel putin unul este par')
else:
    print('toate sunt impare')