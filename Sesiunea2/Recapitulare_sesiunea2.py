nota_de_trecere = 4.5
nota = float(input('alege nota'))
if nota >= nota_de_trecere:
    print(f'Ai luat nota {nota}')
    print(f'Felicitari, ai trecut examenul!')

# constanta - are o valoare stabila, nu dorim sa o schimbe nimeni
# standardul este sa o scriem cu litere mari
nota_de_trecere = 4.5
nota = float(input('alege nota'))
if nota >= nota_de_trecere:
    print(f'Ai luat nota {nota}')
    print(f'Felicitari, ai trecut examenul!')
else:
    print(f'Ai luat doar nota {nota}')
    print(f'Ne vedem la vara, nu ai trecut examenul!')


# robotel telefonic
optiunea = int(input('Alege o optiune '));
if optiunea == 0:
    print('Meniu anterior')
elif optiunea == 1:
    print('Ati ales Ro ')
elif optiunea == 2:
    print('Ati ales Eng ')
else:
    print('Nu am identificat optiunea, mai incearca!')
