# Exerciții obligatorii - grad de dificultate: Usor spre Mediu
# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.
from Sesiunea4.For import value

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

print(20*'*',f'Rezolvare exercițiului 1',20*'*')
print(f'Rezolvarea cerintei folosind -> for<-  : \n')

for i in masini:
    print(f'Mașina mea preferată este {i}.')

print(f'\nRezolvarea cerintei folosind -> for each<-  : \n')
for masina in masini:
    print(f'Mașina mea preferată este {masina}.')

print(f'\nRezolvarea cerintei folosind -> while<-  : \n')
while masini:
    print((f'Mașina mea preferată este {masini.pop(0)}.'))



# 2. Aceeași listă:
# Folosește un for else
# În for
#
# - Modifică elementele din listă astfel încât să fie scrise cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.
#
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
print(20*'*',f'Rezolvare exercițiului 2',20*'*')
print(f'Rezolvarea cerintei folosind -> for else<-  : \n')

for i in masini:
    print(f'Mașina mea preferată este {i}.')
else:
    print('Am incheiat lista.')

print(f'Rezolvarea cerintei -> elementele din listă să fie scrise cu majuscule, exceptând primul și ultimul<- : \n')
for i in range(1,len(masini)-1):
    masini[i] = masini[i].upper()
else:
    print(masini)

# 3. Aceeași listă:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Iterează prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘
#
print(20*'*',f'Rezolvare exercițiului 3',20*'*')

for masina in masini:
    if masina == 'Mercedes':
        print(f'Am găsit mașina dorită de dumneavoastră!')
        break
    else:
        print(f'Am găsit mașina {masina}. Mai căutam...!')

# 4. Aceeași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.
#
print(20*'*',f'Rezolvare exercițiului 4',20*'*')

for masina in masini:
    if masina == 'Trabant' or masina == 'Lăstun':
        continue
    print(f'S-ar putea să vă placă mașina modelul {masina}.')

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Iterează prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
#
# ● Printează Modele vechi: x.
# ● Modele noi: x.
#
print(20*'*',f'Rezolvare exercițiului 5',20*'*')
masini_vechi = []

for masina in masini:
    if masina == 'Trabant' or masina == 'Lăstun':
       masini_vechi.append(masina)
       masini[masini.index(masina)] = 'Tesla'
       masini = list(dict.fromkeys(masini))  # doresc sa afisez denumirea modelului, intr-o lista, o singura data

print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')


# 6. Având dict:
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Iterează prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.
print(20*'*',f'Rezolvare exercițiului 6',20*'*')
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
print(f'\nRezolvarea cerintei -> iterare prin pret_masini.items, accesare model si pret<- : \n')
print('Bună ziua, \nBine ați venit la noi! \nSuntem convinși că vă putem fi de ajutor. \n')

for key,values in pret_masini.items():
    if values <= 15000:
        print(f'Pentru un buget de sub 15000 euro puteți alege mașina {key}.')


# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
print(20*'*',f'Rezolvare exercițiului 7',20*'*')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
aparitii_nr3 = 0

for numar in numere:
    if numar == 3:
        aparitii_nr3 += 1
print(f'Lista de numere este: \n{numere}')
print(f'Numarul 3 apare de {aparitii_nr3} ori.')


# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
print(20*'*',f'Rezolvare exercițiului 8',20*'*')
suma = 0

for numar in numere:
    suma += numar
print(f'Suma este: {suma}.')


# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).
#
print(20*'*',f'Rezolvare exercițiului 9',20*'*')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr_max = numere[0]

for numar in numere:
    if numar > nr_max:
        nr_max = numar
print(f'Numarul maxim din listă este: {nr_max}.')


# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.
print(20*'*',f'Rezolvare exercițiului 10',20*'*')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

print(f'Lista dată este: {numere}')

for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = -numere[i]
print(f'Lista actualizată este: {numere}')