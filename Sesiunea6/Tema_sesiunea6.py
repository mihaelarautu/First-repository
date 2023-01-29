# Exerciții obligatorii - grad de dificultate: Usor spre Mediu
# 1.Clasa Cerc
# Atribute: rază, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()
print(20 * '*', f'Rezolvare exercițiului 1', 20 * '*')
from math import pi


class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def __str__(self):
        return f'Raza:{self.raza}, Culoare: {self.culoare}'

    def descrie_cerc(self):
        return f'Cercul are raza de {self.raza} cm si culoarea {self.culoare}.'

    def aria(self):
        return round(pi * self.raza * self.raza, 2)

    def diametru(self):
        return 2 * self.raza

    def circumferinta(self):
        return round(2 * self.raza * pi, 2)


cerc1 = Cerc(raza=5, culoare='verde')

print(Cerc.descrie_cerc(cerc1))
print(f'Aria cercului este de {Cerc.aria(cerc1)} centimetri patrati.')
print(f'Diametrul cercului este de {Cerc.diametru(cerc1)} centimetri.')
print(f'Circumferinta cercului este de {Cerc.circumferinta(cerc1)} centimetri.')

# 2. Clasa Dreptunghi
# Atribute: lungime, lățime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Poți verifica schimbarea culorii prin apelarea metodei
# descrie().
print(20 * '*', f'Rezolvare exercițiului 2', 20 * '*')


class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def __str__(self):
        return f'Lungimea dreptunghiului:{self.lungime}, Latimea dreptunghiului:{self.latime}, Culoarea dreptunghiului: {self.culoare}'

    def __repr__(self):
        return str(self)

    def descrie(self):
        return f'Dreptunghiul are:{self.lungime} cm lungime, {self.latime} cm latime si culoarea {self.culoare}.'

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return (2 * self.lungime) + (2 * self.latime)

    def schimbă_culoarea(self):
        self.culoare = noua_culoare


dreptunghi1 = Dreptunghi(lungime=6, latime=2, culoare='galben')
noua_culoare = 'rosu'

print(Dreptunghi.descrie(dreptunghi1))
print(f'Aria dreptunghiului este de {Dreptunghi.aria(dreptunghi1)} cm patrati.')
print(f'Perimetrul dreptunghiului este de {Dreptunghi.perimetru(dreptunghi1)} cm.')
Dreptunghi.schimbă_culoarea(dreptunghi1)
print(dreptunghi1.descrie())

# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)
print(20 * '*', f'Rezolvare exercițiului 3', 20 * '*')


class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def __str__(self):
        pass

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, Angajat):
            return False
        return self.nume == other.nume and self.prenume == other.prenume and self.salariu == other.salariu

    def descrie(self):
        return f'Numele angajatului este:{self.nume} {self.prenume}, salariul negociat este de : {self.salariu} lei.'

    def nume_complet(self):
        return f'Numele complet este: {self.nume + " " + self.prenume}'

    def salariu_lunar(self):
        ore_lucrate = int(input(f'Inserati numarul de ore lucrate pe zi in medie: \n'))
        zile_lucrate = int(input(f'Inserati numarul de zile lucrate in luna: \n'))
        if ore_lucrate > 8:
            return f'Salariul obtinut in aceasta luna este de: {int((((self.salariu/zile_lucrate)/8)*8*zile_lucrate)+((1.5*(self.salariu/zile_lucrate)/8))*(ore_lucrate-8)*zile_lucrate)} lei.'
        else:
            return f'Salariul obtinut in aceasta luna este de: {int((((self.salariu / zile_lucrate) / 8) * 8 * zile_lucrate))} lei.'

    def salariu_anual(self):
        return f'Anual, valoarea salariului este de {self.salariu*12} lei.'


    def marire_salariu(self):
        valoare_crestere = int(input(f'Inserati suma cu care salariul a fost marit:\n'))
        if valoare_crestere == 0:
            return 'Salariul nu  avut o marire.'
        else:
            return f'Salariul a crescut cu {int(valoare_crestere/self.salariu*100)} %.'


angajat1 = Angajat(nume = 'Popescu', prenume = 'Ioana', salariu = 5000)
print(Angajat.descrie(angajat1))
print(Angajat.nume_complet(angajat1))
print(Angajat.salariu_lunar(angajat1))
print(Angajat.marire_salariu(angajat1))




# 4. Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)
# 4. Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)
print(20 * '*', f'Rezolvare exercițiului 4', 20 * '*')


class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def __str__(self):
        pass

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, Cont):
            return False
        return self.iban == other.iban and self.titular_cont == other.titular_cont and self.sold == other.sold

    def afisare_sold(self):
        return f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei.'

    def debitare_cont(self):
        valoare_debitata = int(input('Inserati valoarea pe care doriti sa o retrageti din cont: \n'))
        self.sold = self.sold - valoare_debitata
        return f'Soldul dumneavoastra a fost debitat cu suma de {valoare_debitata} lei, soldul actual al contului este de {self.sold} lei.'


    def creditare_cont(self):
        valoare_creditata = int(input('Inserati valoarea pe care doriti sa o depuneti in cont: \n'))
        self.sold = self.sold + valoare_creditata
        return f'Ati depus suma de {valoare_creditata} lei, soldul actual al contului este de {self.sold} lei.'



cont1 =  Cont(iban = 'XXXXXXXXXXXXXXXXXXXXX', titular_cont = 'Popescu Ioana', sold = 10000)
print(Cont.afisare_sold(cont1))
print(Cont.debitare_cont(cont1))
print(Cont.creditare_cont(cont1))
