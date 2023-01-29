# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
# numerele comune.
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}
print(20 * '*', f'Rezolvare exercițiului 1', 20 * '*')
n = int(input("Set dimension of the lists: "))
lst1 = list(map(int, input("Insert the numbers for the first list (separated by space): ").strip().split()))[:n]
print('The first list is:', lst1)
lst2 = list(map(int, input("Insert the numbers for the second list (separated by space): ").strip().split()))[:n]
print('The second list is:', lst2)

def get_intersection(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return set1 & set2

print(f'Common numbers are: {get_intersection(lst1, lst2)}.')

# 2. Funcție care să aplice o reducere de preț.
# Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
# Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110%
# e invalidă.
price = int(input('Insert price: '))
discount_value = int(input('Insert discount value: '))

def get_price_after_discount(price, discount):
    if discount < 0 or discount > 100:
        raise Exception(f'Invalid discount, the discount "{discount}" has to be between 0 and 100')
    return int(price - (price * (discount_value / 100)))

print(f'The price after discount is {get_price_after_discount(price, discount_value)} EUR.')
