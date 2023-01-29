# Exerciții Opționale - grad de dificultate: Mediu spre greu: may needGoogle.
# 1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
# Itereaza prin listă alte_numere
print(20*'*',f'Rezolvare exercițiului 1',20*'*')
print(f'Lista este: {alte_numere}')

# Populează corect celelalte liste
# Afișează cele 4 liste la final
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    if numar % 2 != 0:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    if numar < 0:
        numere_negative.append(numar)
print(f'Numerele pare sunt: {numere_pare}.')
print(f'Numerele impare sunt: {numere_impare}.')
print(f'Numerele pozitive sunt: {numere_pozitive}.')
print(f'Numerele negative sunt: {numere_negative}.')



# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Te poți inspira vizual de aici.
# https://www.youtube.com/watch?v=lyZQPjUT5B4
print(20*'*',f'Rezolvare exercițiului 2',20*'*')
lista_noua = []

while alte_numere:
    min = alte_numere[0]
    for numar in alte_numere:
        if numar < min:
            min = numar
    lista_noua.append(min)
    alte_numere.remove(min)
print(f'Lista ordonată este: {lista_noua}.')

print(20*'*',f'Aplicatie dansatori',20*'*')
dansatori = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]
print(f'Lista de dansatori este: {dansatori}')

for i in range(len(dansatori)-1):
    print(f'{dansatori[i]} danseaza cu {dansatori[i + 1]}')
    if dansatori[i] > dansatori[i + 1]:
        print(f'Nr {dansatori[i]} este mai mare ca {dansatori[i + 1]}')
        print(f'Nr {dansatori[i + 1]} coboara iar nr {dansatori[i]} urca')
        swap = dansatori[i]
        dansatori[i] = dansatori[i + 1]
        dansatori[i + 1] = swap
    else:
        print(f'Nr {dansatori[i]} ramane pe pozitie deoarece e mai mic ca {dansatori[i + 1]}')

print(f'Lista sortata de dansatori: {dansatori}')


# 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!
print(20*'*',f'Rezolvare exercițiului 3',20*'*')
import random
numar_secret = random.randint(1, 30)
numar_ghicit = None

while True:
    numar_ghicit = int(input('Alege un număr între 1 și 30: '))
    if 1 <= numar_ghicit <= 30:
        if numar_ghicit < numar_secret:
            print(f'Numărul secret este mai mare.')
        elif numar_ghicit > numar_secret:
            print(f'Numărul secret este mai mic.')
        else:
            print('Felicitări! Ai ghicit!')
            break
    else:
        print('Atenție! Trebuie sa alegi un număr între 1 si 30, alege altă valoare!')