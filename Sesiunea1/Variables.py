# variable -> a container from memory for storing values

# 1. creating a variable

x = 5
y = 'John'
print(x)
print(y)
x = y
print(x)

# 2. naming variables
'''
a) a variable must start with a letter or the underscore (_) character
b) a variable cannot start with a number
c) a variable name can only contain alpha-numeric characters and underscores (A-Z, a-z, 0-9, _)
d) variable names are case-sensives
'''
# thisway
myvar = 5
my_var = 5
_var_ = 5
_my_var = 5
myVar = 5
MYVAR = 5
myvar = 5

# NOT thisway
# 2myvar = 5
# my-var = 5
# my var = 5

# 3. Many values to multiple variables.
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
k, h, j = x, 'mere', True
print(k, h, j)

# One value to multiple variables.
x = y = z = 'portocala'
print(x, y, z)