# # 1. Sa se scrie un program care citeste numere de la tastatura,
# # pana cand se introduce numarul 0
# # pentru fiecare numar introdus, se verfica daca este par, iar la final
# # se vor afisa intr-o lista toate numerele pare.
#
# nr = int(input('Insert number:'))
# result = []
# while nr != 0:
#     if nr % 2 == 0:
#         result.append(nr)
#     nr = int(input('Insert number:'))
# print(result)
#
# # 2.  Sa se scrie un program care citeste un text de la tastatura,
# # si va afisa un dictionar cu toate caracterele din text, in  care cheile
# # vor fi caracterele si valorile faca caracterul este vocala sau consoana.
# txt = input('Insert text: \n')
# dct = {}
#
# vocale = 'aeiou'
# for char in txt:
#     if not char.isalpha():
#         continue
#     char_type = 'vocala' if char in vocale else 'consoana'
#     dct[char] = char_type
# print(dct)
#
# # 3. Sa se scrie un program care citeste de la tastatura o lista de fructe
# # iar la final le va afisa doar pe cele care incep cu 'a'
#
# fruit = None
# result = []
# while fruit != '':
#     fruit = input('Scrie un fruct: ')
#     if fruit.startswith('a'):
#         result.append(fruit)
# print(result)
#
#
# # 4. Fie dictionarul dct. Fiecare element din dictionar sa se afiseze sub formatul
# # cheie -> valoare
#
# dct = {'a': 6, 'b': 9}
#
# for key, value in dct.items():
#     print(f'{key} -> {value}')
#
# # 5. Sa se scrie un program care citeste de la tastatura 6 numere
# # si le afiseaza pe cele mai mari decat 9
#
# result = []
# for i in range(6):
#     numar = int(input("Intrudu' un numar:"))
#     if numar > 9:
#         result.append(numar)
#
# print(result)
#
# '''
# 6. Sa se scrie un program care citeste de la tastatura litere,
# pana cand se introduce un caracter care nu este litera
# La final se vor afisa toate literele unice (o singura data)
# '''
# letters = set()
# while True:
#     char = input('Insert char: ')
#     if not char.isalpha():
#         break
#         letters.add(char)
# lst = list(letters)
# lst.sort()
#
# print(lst)
#

'''
7. Fie lista [1,2,3,6,5,10]. Sa se scrie un program care creaza un dictionar
care contine ca si cheie
elementele din lista, iar ca valori indexul fiecarui element.
'''
lst = [1, 2, 3, 6, 5, 10]
dct = {}
for i in range(len(lst)):
    dct[lst[i]] = i

print(dct)
# v2
for index, elem in enumerate(lst):
    dct[elem] = index

print(dct)



