# Exerciții Opționale - grad de dificultate: Mediu spre greu - might need Google

# 1.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = int(input('1) Insert a number:\n'))
if len(str(x)) <= 3:
    print(f'{x} has 4 digits.')
else:
    print(f'{x} has 4 digits, minimum.')

# 2.Verifică dacă x are exact 6 cifre.
x = input('2) Insert a number:\n')
if len(x) == 6:
    print(f' {x} has exactly 6 digits.')
else:
    print(f' {x} does not have 6 digits.')

# 3.Verifică dacă x este număr par sau impar (x e int).
x = int(input('3) Insert a number:\n'))
if x % 2 == 0:
    print('The number is even.')
else:
    print('The number is odd.')

# 4. x, y, z (int)
# Afișează care este cel mai mare dintre ele?
y = int(input('4) Please insert two numbers, the first one is: \n'))
z = int(input('The second is: \n'))

if x > y and x > z:
    print('First number is greater than others.')
elif y > x and y > z:
    print('The second number is greater than others.')
elif z > x and z > y:
    print('The third number is greater than others.')
elif x == y == z:
    print('The numbers are equal.')
else:
    print('Two numbers are equal.')

# 5.
# X, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.
x_angle = int(input('5) Insert the first angle:\n'))
y_angle = int(input('Insert the second angle:\n'))
z_angle = int(input('Insert the third angle:\n'))

if x_angle <= 0 or y_angle <= 0 or z_angle <= 0:
    print('Angles cannot have negative values, please insert again')
elif x_angle + y_angle + z_angle == 180:
    print('This is a valid triangle.')
else:
    print('This is not a valid triangle.')


# 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citește de la tastatură un int x
# ● Afișează stringul fără ultimele x caractere
# Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
sentence_6 = 'Coral is either the stupidest animal or the smartest rock'
number_of_letters = int(input('6) How many numbers you want to cut?\n'))
number_of_letters = -number_of_letters
if number_of_letters > len(sentence_6):
    print(f'You can not cut that many letters, because lenght of the sentence given is {len(exemplu_6)}.')
else:
    print(f'{sentence_6[0:number_of_letters]}')

# 7. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
first_characters = sentence_6[:5]
last_characters = sentence_6[-5:]
sentence_7 = first_characters + last_characters
print(f'7) {sentence_7}')


# 8. Același string.
# ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
# este o funcție care te ajuta sa faci asta)
# ● Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
# ● output: 'Coral is either the stupidest animal or the smartest'
index_rock = sentence_8.index('rock')

print(f'8) The start index of the word "rock" is {index_rock}.')
print(f'8) "{sentence_8[:index_rock]}"')
