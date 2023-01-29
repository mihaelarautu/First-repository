def produs(a,b):
    return a*b

p = produs(5,6)
print(p)

def squared_first_nat_num(n):
    result = []
    for i in range(n):
        squered = produs(i,i)
        result.append(squered)
    return result
print(squared_first_nat_num(10))

def get_all_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

print(get_all_even_numbers([5,7,9,18,58,43,11,-13,17,-18]))