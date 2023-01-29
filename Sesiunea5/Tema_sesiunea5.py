# Exerciții obligatorii - grad de dificultate: Ușor spre Mediu
# 1.Funcție care să calculeze și să returneze suma a două numere
print(20 * '*', f'Rezolvare exercițiului 1', 20 * '*')

a = int(input('Inserati primul numar: \n'))
b = int(input('Inserati al doilea numar: \n'))
def sum_of_two(a,b):
    return a + b


print(f' Suma celor doua numere este: {sum_of_two(a, b)}.')


# 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar
print(20 * '*', f'Rezolvare exercițiului 2', 20 * '*')
x = sum_of_two(a, b)
def num_parity(x):
    if x % 2 == 0:
        return True
    return False

print(f'Paritatea numarului de mai sus este (T/F): {num_parity(x)}.')
print('Numarul este par.') if num_parity(x) else print('Numarul este impar.')

############# Varianta Recomandata de Sergiu
def is_even(number):
    # return not number % 2
    return number % 2 == 0

##############################################################################
#  update dupa comentariu Sergiu
# # 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar
# print(20 * '*', f'Rezolvare exercițiului 2', 20 * '*')
# x = sum_of_two(a, b)
# def num_parity(x):
#     if x % 2 == 0:
#         return x % 2 == 0
#
# print(f'Paritatea numarului de mai sus este (T/F): {num_parity(x)}.')
# print('Numarul este par.') if num_parity(x) else print('Numarul este impar.')


# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)
print(20 * '*', f'Rezolvare exercițiului 3', 20 * '*')
nume = input('Care este numele dumneavoastra complet? \n')

def count_chars(nume):
    result = 0
    for char in nume:
        if char != ' ':
            result += 1
    return result

print(f'Numele dumneavoastra este {nume}, aceste cuprinde {count_chars(nume)} caractere.')


# 4. Funcție care returnează aria dreptunghiului
print(20 * '*', f'Rezolvare exercițiului 4', 20 * '*')
print('Inserati valorile pentru laturile dreptunghiului')
L = int(input('Lungimea = '))
l = int(input('Latimea = '))

def rectangele_area(L,l):
    return L*l

print(f'Aria dreptunghiului este de {rectangele_area(L,l)} centimetri patrati.')


# 5. Funcție care returnează aria cercului
print(20 * '*', f'Rezolvare exercițiului 5', 20 * '*')
from math import pi
l = float(input('Inserati raza cercului:\n'))

def circle_area(pi,l):
    return round(pi*l*l, 2)
print(f'Aria cercului este de {circle_area(pi,l)} centimetri patrati.')

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și False dacă nu găsește.
print(20 * '*', f'Rezolvare exercițiului 6', 20 * '*')
txt = input('Inserati textul pentru studiu:\n')
char = input('Caracterul cautat este: ')

def find_char_in_str(txt,char):
    return char in txt

print(f'Caracterul cautat -{char}- se regaseste in text.') if find_char_in_str(txt, char) else print("Caracterul cautat nu se regaseste in text.")


# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Numărul de caractere lower case este x
# # ● Numărul de caractere upper case este y
print(20 * '*', f'Rezolvare exercițiului 7', 20 * '*')
txt = input('Inserati textul pentru studiu:\n')
upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low = "abcdefghijklmnopqrstuvwxyz"

def count_lower_upper_chrs(txt):
    upper_chrs = 0
    lower_chrs = 0
    for i in txt:
        if i in upp:
            upper_chrs += 1
        elif i in low:
            lower_chrs += 1
    print(f'Numărul de caractere scrise upper case este:', upper_chrs)
    print(f'Numărul de caractere scrise lower case este:', lower_chrs)
count_lower_upper_chrs(txt)


# 8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu
# numerele pozitive.
print(20 * '*', f'Rezolvare exercițiului 8', 20 * '*')
# input size of the list
n = int(input("Selecteaza dimesiunea sirului de numere: "))
# store integers in a list using map, split and strip functions
lst = list(map(int, input("Introduceti numerele analizate (separate prin spatiu): ").strip().split()))[:n]
print('Lista este:', lst)   # printing the list
positive_num = []

def list_positive_num(lst):
    for i in lst:
        if i >= 0:
            positive_num.append(i)
    return positive_num

print(f'Numerele pozitive sunt:\n{list_positive_num(lst)}')


# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
# ● Primul număr x este mai mare decat al doilea număr y
# ● Al doilea număr y este mai mare decat primul număr x
# ● Numerele sunt egale.
print(20 * '*', f'Rezolvare exercițiului 9', 20 * '*')
first_num = int(input('Care este primul numar?\n'))
second_num = int(input('Care este al doilea numar?\n'))

def compare_num(first_num, second_num):
    if first_num > second_num:
        print(f'Primul număr {first_num} este mai mare decat al doilea număr {second_num}.')
    elif first_num < second_num:
        print(f'Al doilea număr {second_num} este mai mare decat primul număr {first_num}.')
    else:
        print(f'Numerele sunt egale.')

compare_num(first_num,second_num)


# 10. Funcție care primește un număr și un set de numere.
# ● Printează ‘am adaugat numărul nou în set’ + returnează True
# ● Printează ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False
print(20 * '*', f'Rezolvare exercițiului 10', 20 * '*')
n = int(input("Selecteaza dimesiunea sirului de numere: "))
# store integers in a list using map, split and strip functions
set_input = list(map(int, input("Introduceti numerele analizate (separate prin spatiu): ").strip().split()))[:n]
print('Lista este:', set_input)   # printing the list
the_set = set(set_input)
numar = input('Inserati un numar:\n')


def check_uni_num(numar, the_set):
    if numar not in the_set:
        the_set.add(numar)
        print('Am adaugat numărul nou în set.')
        return True
    print('Nu am adaugat numărul în set. Acesta există deja.')
    return False
print('True') if check_uni_num(numar, the_set) else print('False')