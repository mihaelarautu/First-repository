
""" Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă. """
# zona din memorie ce contine/stocheaza date


'''2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabile: 
string, int, float, bool'''
nume_animal = 'Keemo'  # string
varsta_in_luni = 30  # int
greutate = 26.40  # float
sex_masculin = True  # bool


'''3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.'''
print(type(nume_animal))
print(type(varsta_in_luni))
print(type(greutate))
print(type(sex_masculin))


'''4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere). Verifică tipul acesteia.'''
greutate = round(greutate)
print(greutate)
print(type(greutate))  # verificarea tipului variabilei


'''5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.'''
print('Numele cainelui meu este'+' '+nume_animal+'.')
if sex_masculin == True:
        print('Este de sex masculin.')
print(f'Are varsta de {varsta_in_luni} luni.')
print(f'Si o greutate de {greutate} kg.')


'''6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.'''
nume = input('Care este numele tau: ')
prenume = input('Care este prenumele tau: ')
print(f"numele complet are {len(nume) + len(prenume)} caractere")



'''7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.'''
lungime = input('Introduceti lungimea: ')
latime = input('Introduceti latimea: ')
print(f'Aria dreptunghiului este {int(lungime) * int(latime)}.')


'''8. Având stringul: 'Coral is either the stupidest animal or the smartest rock', afișează de câte ori apare cuvântul 'the';'''
fraza = 'Coral is either the stupidest animal or the smartest rock'
print('Number of occurrence of "the":', fraza.count('the'))


'''9. Același string:
Inlocuieste 'the' cu 'THE' peste tot;
Printează rezultatul.'''
print(fraza.replace('the','THE'))

'''10. Același string:
Folosește un assert ca să verifici dacă acest string conține doar numere.'''
verificare = fraza.isdigit()  # varianta 1
print("Does string contain any digit ? : " + str(verificare))
assert fraza.isdigit(), 'The string does not contain any digits'  #verificare





