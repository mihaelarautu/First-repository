"""
Exerciții Opționale - grad de dificultate: Mediu spre greu (s-ar putea să ai
nevoie de Google).
1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
"""
# 1. prima varianta de interpretare a cerintei - ii cer utilizatorului sa introduca OBLIGATORIU un string de dimensiune impara
odd_text = input("Type something: ")

# Now we calculate the length and determine if it is even or odd by using % to find its remainder when divided by 2.
length = len(odd_text)%2

# If a number has a remainder of 0 when divided by 2,the number is even.
# If there is a remainder then it is odd.

if length == 0:
	print (odd_text, "The text you entered is even, please insert a odd number off characters");  #aici ar trebui creat un loop
else:
	print (odd_text, "Thank you. Move forward.");

# 2. a doua varianta de interpretare a cerintei - ii cer programului sa citeasca din string-ul introdus de utilizator, stringurile de dimensiune impara
text = input('Type something: ')
even_chars = []
odd_chars = []

for i in range(len(text)):
    if i % 2 == 0:
        even_chars.append(text[i])
    else:
        odd_chars.append(text[i])

print('Odd characters: {}'.format(odd_chars))
odd_chars_len = odd_chars.__len__()
print(odd_chars_len)
print(f'Caracterul din mijloc este: {text[odd_chars_len//2]}')

# 3. a treia varianta de interpretare a cerintei - ii cer programului sa citeasca din string-ul introdus de utilizator, primul string de dimensiune impara, dimensiunea fiind selectata de mine
text3 = input("Type something: ")
print(f'Stringul gasit: {text3[0:9]}')
print(f'Caracterul din mijloc este: {text3[4]}')

# Varianta cea mai simpla
print(odd_text[len(odd_text) // 2])


'''2. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.'''
text4 = input ('Scrie 3 fructe preferate: '); x, y, z = text4.split(", "); print(x, y, z)

