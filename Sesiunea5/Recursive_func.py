# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34....  # functia se apelaza pe ea insasi
def recursive_Fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_Fibonacci(n-1)+recursive_Fibonacci(n-2)

for i in range(10):
    print(recursive_Fibonacci(i))



def suma_primelor_n_nr(n):
    if n == 0:
        return 0
    return n + suma_primelor_n_nr(n-1)  # in acest caz nu e  necesar else

print(suma_primelor_n_nr(50))