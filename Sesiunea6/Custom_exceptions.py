class CustomException(Exception):
    pass


# Sa se scrie o functie care verifica daca o lista de numere intregi contine numere negative.
# Daca da, sa se arunce o exceptie specifica.

class ContainsNegativeNumberException(Exception):
    pass


def check_negative_numbers(numbers):
    for number in numbers:
        if number < 0:
            raise ContainsNegativeNumberException(f'Contine {number}')


check_negative_numbers([5, 0, -8, -1, 7])