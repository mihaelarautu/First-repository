'''1. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.'''
cuvinte = input('Scrie doua cuvinte: ')  #definim exemplul
prima_litera = cuvinte[0]  # stocam prima litera intr-o variabila
ultima_litera = cuvinte [-1]  #s tocam ultima litera intr-o variabila
mijloc = cuvinte[1:-1] # stocam restul intr-o a treia variabila
print(f'{prima_litera}{mijloc.replace(prima_litera, prima_litera.upper())}{ultima_litera}')  #facem replace in fuctie de primul caracter si printam

'''2.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****'''
user = input('Insert user: ')
parola = input('Parola: ')
caracter_parola = input('Alege caracterul ce inlocuieste parola: ')
print(f'Parola pentru {user} este {caracter_parola*len(parola)} si are {len(parola)} caractere.')