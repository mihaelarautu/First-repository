# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google
# 1. Funcție care primește o lună din an și returnează câte zile are acea lună.
print(20 * '*', f'Rezolvare exercițiului 1', 20 * '*')
year = int(input('Insert year:\n'))
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month = input('Insert month:\n')
def is_leap_year(year):  # verificare an bisect sau nu
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):

    if month in ['September', 'April', 'June', 'November']:
        print('30 days')

    elif month in ['January', 'March', 'May', 'July', 'August','October','December']:
        print('31 days')

    elif month == 'February' and is_leap_year(year) == True:
        print('29 days')

    elif month == 'February' and is_leap_year(year) == False:
        print('28 days')
    else:
        print('Error! Reinsert month!')

print(days_in_month(month, year))


##############################################################################
#  update dupa comentariu Sergiu
# # 1. Funcție care primește o lună din an și returnează câte zile are acea lună.
# print(20 * '*', f'Rezolvare exercițiului 1', 20 * '*')
# year = int(input('Insert year:\n'))
# print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
# month = input('Insert month:\n')
# def is_leap_year(year):  # verificare an bisect sau nu
#     return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
#
# def days_in_month(month, year):
#
#     if month in ['September', 'April', 'June', 'November']:
#         print('30 days')
#
#     elif month in ['January', 'March', 'May', 'July', 'August','October','December']:
#         print('31 days')
#
#     elif month == 'February' and is_leap_year(year):
#         print('29 days')
#
#     elif month == 'February' and not is_leap_year(year):
#         print('28 days')
#     else:
#         print('Error! Reinsert month!')
#
# print(days_in_month(month, year))



# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)
print(20 * '*', f'Rezolvare exercițiului 2', 20 * '*')
first_num = int(input('Insert first number: '))
second_num = int(input('Insert second number: '))

def calculator(first_num,second_num):
    assert second_num > 0, 'First number can not be divided by 0.'
    return [(first_num + second_num), (first_num - second_num), (first_num * second_num), float(first_num / second_num)]

a, b, c, d = calculator(first_num, second_num)

print("Add: ", a)
print("Substract: ", b)
print("Multiply: ", c)
print("Divide: ", d)


# 3. Funcție care primește o listă de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
print(20 * '*', f'Rezolvare exercițiului 3', 20 * '*')
n = int(input("Set dimension of the list: "))
lst = list(map(int, input("Insert the numbers (separated by space): ").strip().split()))[:n]
print('The list is:', lst)

def num_count_into_dict(lst):
    dict = {}
    for i in range(len(lst)):
        dict.setdefault(i, 0)
    for key in dict.keys():
        if key in lst:
            count = lst.count(key)
            dict[key] = count
    return dict

print(f'The result is:{num_count_into_dict(lst)}')


# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
print(20 * '*', f'Rezolvare exercițiului 4', 20 * '*')
lst = list(map(int, input("Insert the numbers (separated by space): ").strip().split()))[:3]

def get_max(lst):
    maximum = lst[0]
    for number in lst:
        if number > maximum:
            maximum = number
    return maximum

print(f'Max is {get_max(lst)}.')



# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr.
# Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)
print(20 * '*', f'Rezolvare exercițiului 5', 20 * '*')
num = int(input('Insert number: '))

def sum_of_num(num):
    the_sum = 0
    for i in range(num + 1):
        the_sum += i
    return the_sum

print(f'The sum is: {sum_of_num(num)}.')