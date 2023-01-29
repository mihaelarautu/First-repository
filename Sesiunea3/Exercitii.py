# 1. sa se scrie un program care citeste un text de la tastatura si afiseaza
# o lista cu fiecare caracter, in ordinea inversa a aparitiei in text

text = list(input('Sa se scrie un text: '))
text.reverse()
print(text)


### scoaterea unui element si salvarea intr-o variabila
chrs = text.pop(-2)
print(chrs)
chrs = [text.pop(-2), text.pop(7)]
print(chrs)
print(text)


# 2. Sa se scrie un program care citeste numele, e-mailul si varsta unei persoane de la tastatura si adauga datele
# intr-un dictionar, pe care il afiseaza. Daca persoana nu este multumita cu datele introduse, va putea specifica ca vrea
# sa modifice maxim 1 valoare din dictionar.

nume = input('Numele: ')
email = input('email: ')
varsta = int(input('varsta: '))

details ={
    'nume': nume,
    'email': email,
    'varsta': varsta
}
print(details)

modify = input('Vrei sa modifici datele? (Y/N)')
if modify =='Y':
    key_to_modify = input('Introdu ce vrei sa modifici: ')
    if key_to_modify not in details:
        print('Nu exista aceasta valoare.')
        exit(0)
    value_to_modify = input('Introdu noua valoare: ')
    value_to_modify = int(value_to_modify) if key_to_modify == 'varsta' else value_to_modify
    details[key_to_modify]= False
print(details)

# 3. Fie seturile
# a. toate elementele care apar in set1 si nu apar in set 2
# b. toate elementele care apar in ambele seturi
# c. toate elementele care nu sunt comune

set1 = {'Yellow','Orange','Black'}
set2 = {'Orange', 'Blue', 'Pink'}
print(set1 - set2)
print(set1 & set2)
print(set1 ^ set2)