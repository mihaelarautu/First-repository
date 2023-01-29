# Tema 3 - Structuri de date

# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
musical_notes = ["Do","Re","Mi","Fa","So","La","Si","Do"]
# ● Afișeaz-o.
print(20 * '-','Exercitiul 1',20 * '-')
print(musical_notes)
# ● Inversează ordinea folosind slicing și suprascrie această listă.
musical_notes = (musical_notes[::-1])
# ● Printează varianta actuală (inversată).
print(musical_notes)
# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
musical_notes.reverse()
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.
print(musical_notes)
# Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să
# suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
# suprascrierea automat și permanentizează aceste modificări. Ambele variante
# își găsesc utilitatea în funcție de ce ne dorim în acel moment.

#### Varianta 2: new_musical_notes = [musical_notes[len(musical_notes) - i]
####            for i in range(1, len(musical_notes)+1)]
#### print(new_musical_notes)


# 2. De câte ori apare ‘do’?
print(20 * '-','Exercitiul 2',20 * '-')
print(musical_notes.count("Do"))


# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.
lst1 = [3, 1, 0, 2]
lst2 = [6, 5, 4]
print(20 * '-','Exercitiul 3',20 * '-')
print(lst1 + lst2)

lst1.extend(lst2)
print(lst1)


# 4.
# ● Sortează și afișează lista generată la exercițiul anterior.

print(20 * '-','Exercitiul 4',20 * '-')
lst1.sort()
print(lst1)
# ● Sortează numărul 0 folosind o funcție.
sort_0 = lst1.pop(0)
# ● Afișaza iar lista.
print(lst1)


# 5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
# ● Lista este goală.
# ● Lista nu este goală.
print(20 * '-','Exercitiul 5',20 * '-')
if not lst1:
   print('Empty list')
else:
   print('List is not Empty ',lst1)

#
# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
lst1.clear()


# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
print(20 * '-','Exercitiul 7',20 * '-')
if not lst1:
   print('Empty list')
else:
   print('List is not Empty ',lst1)


# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(20 * '-','Exercitiul 8',20 * '-')
print(list(dict1.keys()))


# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
print(20 * '-','Exercitiul 9',20 * '-')
print(f'Ana a luat nota {dict1.get("Ana")}.')
print(f'Gigel a luat nota {dict1.get("Gigel")}.')
print(f'Dorel a luat nota {dict1.get("Dorel")}.')

#
# 10. Dorel a făcut contestație și a primit 6.
# ● Modifică nota lui Dorel în 6
dict1['Dorel'] = 6
# ● Printează nota după modificare
print(20 * '-','Exercitiul 10',20 * '-')
print(dict1)

#
# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi
print(20 * '-','Exercitiul 11',20 * '-')
dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)