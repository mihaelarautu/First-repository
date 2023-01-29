# EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ.
#  1. Alege un număr de la tastatură
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777


nr = int(input('Scrie un nr: '))

for i in range(1, nr + 1):
    print(i * str(i))

# varianta 2 piramida crescatoare
numar_randuri = int(input("Selecteaza numarul de randuri: "))

for i in range(numar_randuri):
    for j in range(i+1):
        print(j+1, end=" ")
    print("")

# 2.
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)
# studiu echipa 1
for rand in tastatura_telefon:
    for item in rand:
        print(f'Cifra curenta {item}')




