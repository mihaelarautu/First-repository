'''
1. Sa se scrie o functie care primeste oricati parametri si de orice fel
si returneaza lista valorilor argumentelor
'''

def list_all_parameters_values(*args, **kwargs): #ideal pt orice tip de parametri *args, **kwargs
    return list(args) + list(kwargs.values())

print(list_all_parameters_values(2,8,10,a=5))


'''
2. sa se scrie o functie care primeste ca parametru o lista si returneaza inversul acelei liste.
'''
def get_list_reversed(lst):
    return lst[::-1]

print(get_list_reversed([1,2,3,-3,5]))


'''
3. Sa se scrie o functie care primeste ca paramentru 2 numere si il returneaza
pe cel mai mare.'''
def max_between(a,b):
    return a if a > b else b

print(max_between(1,-1))


'''
4. Sa se scrie o functie care primeste ca parametru o lista si un nr.
Functia va returna de cate ori apare acel numar in lista
iar daca nu apare deloc, va arunca o eroare.
'''

def get_count_in_list(lst, a):
    counter = lst.count(a)
    if not counter:
        raise Exception (f'{a} nu se afla in lista')
    return counter
print(get_count_in_list([1,5,8,4,-2,1,4],4))

'''
5. Sa se scrie o functie citeste in string de la tastatura 
si returneaza toate caracterele folosite in acel string
'''

def get_unique_characters():
    exemplu = input('Scrie ceva: \n')
    return list(set(exemplu))
    print(exemplu)
print(get_unique_characters())


'''
6. Sa se scrie o functie ca citeste de la tastatura un string
si returneaza toate caracterele ordonate alfabetic
'''

def get_sorted_unique_characters():
    chars = get_unique_characters()
    chars.sort()
    return chars

print(get_sorted_unique_characters())
