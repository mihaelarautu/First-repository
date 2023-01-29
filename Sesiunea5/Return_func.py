def say_hi():
    return 'Hello!' # aici se termina executia functiei (terminates the execution of the function)
text = say_hi()
print(text)


def print_first_50():
    for i in range(51):
        print(i)  # return None / return -> is bt default for every function
elem = print_first_50()
print(elem)