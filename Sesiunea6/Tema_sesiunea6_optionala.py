# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google
# 1. Clasa Factură
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fără serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
#
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x număr y
# Data: generează automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# Indiciu pentru dată:
# https://www.geeksforgeeks.org/get-current-date-using-python/
print(20 * '*', f'Rezolvare exercițiului 1', 20 * '*')

from datetime import date


class Factura:
    seria = 'SE'
    data = date.today()

    def __init__(self, număr, nume_produs, cantitate, pret_buc):
        self.număr = număr
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def numar_factura(self):
        numar = 0
        for i in range(10000):
            numar = numar + 1
            return numar

    def schimba_nume_produs(self):
        nume = input('Redenumiti produsul? (Y/N): ')
        if nume == 'Y':
            self.nume_produs = input ('Inserati denumirea dorita: \n')
            return self.nume_produs
        else:
            return self.nume_produs

    def schimba_cantitatea(self):
        cantitate = input('Modificati cantitatea achizitionata? (Y/N)')
        if cantitate == 'Y':
            self.cantitate = int(input('Inserati cantitatea achizitionata: \n'))
            return self.cantitate
        else:
            return self.cantitate

    def schimba_pretul(self):
        pret = input('Doriti sa modificati pretul? (Y/N)')
        if pret == 'Y':
            self.pret_buc = int(input('Inserati pret: \n'))
            return self.pret_buc
        else:
            return self.pret_buc

    def total_factura(self):
        return self.pret_buc * self.cantitate

    def generează_factura(self):
        print('=' * 80)
        print(30 * ' ', f'Factura')
        print(25 * ' ', f'Seria: {Factura.seria}  Număr: {Factura.numar_factura(0)} ')
        print(25 * ' ', f'Data: {Factura.data}')
        print('=' * 80)
        print('Produs', 12 * ' ', '|' 'Cantitate', 12 * ' ', '|' 'Preț bucată', 12 * ' ', '|' 'Total')
        print(Factura.schimba_nume_produs(self), 9 * ' ', '|', Factura.schimba_cantitatea(self), 19 * ' ', '|',
              Factura.schimba_pretul(self), 21 * ' ', '|', Factura.total_factura(self))
        print(50 * ' ', f'Total factura: {Factura.total_factura(self)} lei ')


produs1 = Factura(număr='1', nume_produs='Glob 6 cm', cantitate=6, pret_buc=2.5)
Factura.generează_factura(produs1)


# 2. Clasa Mașină
# Atribute: marca, model, viteza maximă, viteza_actuală, culoare, culori
# disponibile (set), înmatriculată (bool)
# Culoare = gri - toate mașinile când ies din fabrică sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrică
# Culori disponibile = alege tu 5-7 culori
# Marca = alege tu - fabrica produce o singură marcă, dar mai multe modele
# Înmatriculată = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e
# negativă-eroare, dacă viteza e mai mare decât viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0
print(20 * '*', f'Rezolvare exercițiului 2', 20 * '*')

class Mașină:

    culoare = 'gri'
    viteza_actuală = 0
    culori_disponibile = {'alb', 'rosu', 'verde', 'albastru', 'negru', 'visiniu', 'argintiu'}
    înmatriculată = False
    marca = 'Renault'
    model = {'Talisman', 'Laguna', 'Megane', 'Clio', 'Captur', 'Arkana'}

    def __init__(self, model, viteza_maximă):
        self.model = model
        self.viteza_maximă = viteza_maximă

    def descrie(self):
        return f'Marca: {self.marca}\n'\
               f'Model: {self.model}\n'\
               f'Viteza maxima: {self.viteza_maximă}\n' \
               f'Viteza actuala: {self.viteza_actuală}\n' \
               f'Culoare: {self.culoare}\n'\
               f'Înmatriculată : {self.înmatriculată}\n'\

    def înmatriculare(self):
        self.înmatriculată = True

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
        else:
            print(f'Eroare! Nu avem această culoare. Puteți selecta una dintre următoarele culori: {self.culori_disponibile} .')

    def accelerează(self, viteza):
        if viteza < 0:
            f'Eroare! Selecteaza din nou viteaza dorita!'
        if viteza > self.viteza_maximă:
            self.viteza_actuală = self.viteza_maximă

    def franează(self):
        self.viteza_actuală = 0



prima_masina = Mașină(model = 'Talisman',  viteza_maximă = 220)
print(Mașină.descrie(prima_masina))
Mașină.înmatriculare(prima_masina)
culoare = 'negru'
Mașină.vopseste(prima_masina, culoare)
print(Mașină.descrie(prima_masina))
viteza = 240
Mașină.accelerează(prima_masina, viteza)
print(Mașină.descrie(prima_masina))
Mașină.franează(prima_masina)
print(Mașină.descrie(prima_masina))