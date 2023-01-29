'''1. Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat'''
sentence = input('Please insert any string: \n').lower()
assert sentence[0] == sentence[-1]

'''2. Având stringul '0123456789'
● Afișează doar numerele pare
● Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)'''
string_given = ('0123456789')
even = string_given[1::2]
print(even)
odd = string_given[0:-1:2]
print(odd)
digits_string = list(string_given)

# varianta in care se cere un input de la tastatura- mai complex
ifre_stringg = input('Scrie un sir de numere: ')
lista_string = list(map(int, cifre_stringg))

lista_pare = []
lista_impare = []
for i in lista_string:
    if i % 2 == 0:
        lista_pare.append(i)
    else:
        lista_impare.append(i)

print(lista_pare)
print(lista_impare)