#Exerciții obligatorii - grad de dificultate: Ușor spre Mediu
# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.

# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
# if else verifica veridicitatea primei conditii impuse, daca aceasta este adevarata, programul se opreste aici
# daca conditia nu este indeplinita, se executa else, acesta nu mai necesita conditie, deoarece reprezinta deja celalalt caz.

# 2. Verifică și afișează dacă x este număr natural sau nu.
x = int(input('2) Enter value: '))
if x > 0 and isinstance(x, int):
    print(f'2) {x} is a natural number.')
else:
    print(f'2) {x} is a real number')

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
x = int(input('3) Enter your number: '))
if x < 0:
    print(f'3) {x} is a negative number')
elif x > 0:
    print(f'3) {x} is a positive number')
else:
    print(f'3) {x} is a neutral')

# 4. Verifică și afișează dacă x este între -2 și 13.
if x >= -2 and x <= 13:  # La 4. se poate scrie mai concis -2 <= x <= 13acxz
    print(f'4) {x} is between -2 and 13.')
else:
    print(f'4) {x} is not found in the range given.')

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
x = int(input('5) Insert two numbers, first number is: \n'))
y = int(input('5) Insert the second number: \n'))
if (x - y) < 5:
    print('5) The difference between the two numbers given is smaller than 5.')
else:
    print('5) The difference between the two numbers given is greater than 5.')

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
if not (x >= 5 and x <= 27):
    print(f'6) {x} is in range given, 5 and 27')
else:
    print(f'6) {x} is not contained by the range given.')

# 7.
# x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
if x > y:
    print(f'7) {x} is greater than {y}.')
elif y > x:
    print(f'7) {y} is greater than {x}.')
else:
    print(f'7) {x} and {y} are equals.')

# 8.
# X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
latura_x = int(input('8) Introduceti dimensiunea primei laturi a triunghiului:\n'))
latura_y = int(input('8) A doua latura are dimensiunea: \n'))
latura_z = int(input('8) A treia latura are dimensiunea:\n'))

if latura_x == latura_y == latura_z:
    print('Triunghiul este echilateral.')
elif latura_x == latura_y or latura_x == latura_z or latura_y == latura_z:
    print('Triunghiul este isoscel.')
else:
    print('Triunghiul este oarecare.')

# 9. Citește o literă de la tastatură.
# Verifică și afișează dacă este vocală sau nu.
vocale = ['a', 'e', 'i', 'o', 'u']
litera =input('9) Scrieti litera:\n')

if litera in vocale:
    print('Litera este o vocala.')
else:
    print('Litera este o consoana.')

# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
grade = int(input('10) What grade did you took?\n'))
if grade > 9:
    print('You got a A!')
# Peste 8 => B
elif grade > 8:
    print('You got a B!')
# Peste 7 => C
elif grade > 7:
    print('You got a C!')
# Peste 6 => D
elif grade > 6:
    print('You got a D!')
# Peste 4 => E
elif grade > 4:
    print('You got a E!')
# 4 sau sub => F
else:
    print('You got a F!')




