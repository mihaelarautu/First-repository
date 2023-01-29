# 1. Sa se scrie un program care citeste un text de la tastatura si ferifica daca are lungimea numar mar sau impar (rezolvat in doua moduri)

# Varianta 1
text = input('Introduceti un text: ')
if len(text)%2==0:
    print('Lungimea textului este numar par')
else:
    print('Lungimea textului este numar impar')

# Varianta 2
paritate='par' if len(text)%2==0 else 'impar'
print(f'Lungimea textului este un numar {paritate}')


# 2. Se citesc doua numere de la tastatura
# Sa se afiseze cuvantul 'Adevarat' daca ambele numere au acelasi semn, altfel se afiseaza cuvantul 'Fals'.
x=int(input('Intrudu un numar'))
y=int(input('Intrudu un numar'))
if (x>0 and y>0) or (x<0 and y<0):
    print ('Adevarat')
else:
    print ('Fals')
