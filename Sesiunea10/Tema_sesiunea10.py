# 1. Sa se implementeze un decorator care masoara timpul necesar executiei unei functii.
import functools
from functools import wraps
import time


def time_it(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds.')
        return result

    return timeit_wrapper


@time_it
def calculate_sum_of_squares(num):
    """
    Simple function that returns sum of all numbers up to the square of numbers.
    """
    total = sum((x for x in range(0, num ** 2)))
    return total


if __name__ == '__main__':
    calculate_sum_of_squares(10)
    calculate_sum_of_squares(100)
    calculate_sum_of_squares(1000)
    calculate_sum_of_squares(5000)
    calculate_sum_of_squares(10000)

# 2. Sa se genereze primele 100 de numere prime folosind liste, si apoi folosind generator. Comparati diferenta de timp necesara generarii.


lst = list(range(1, 101))
print(lst)



n = 100


@time_it
def gen_first_100(n):
    generated_numbers = 0
    current_number = 1
    while generated_numbers < n:
        if current_number < 101:
            print(f'We are at:{current_number}')
            generated_numbers += 1
            yield current_number
        current_number += 1
        print(f'Going to next number.')
    if current_number <= 101:
        print('Finally ended!')


for i in gen_first_100(n):
    print(i)

# 3. Scrieti un decorator care primeste ca argument numele unui fisier si pentru orice functie apelata, el va scrie in acel fisier numele functiei,
# lista de argumente ca si string si rezultatul apelului. Fisierul este de tip csv. Functiile decorate pot primi oricate argumente.
# defining a decorator
import csv
def function_decorator(file_name):
	def inner(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			function_name = f'The function name is {func.__name__}()'
			function_param = f'The function parameters are: {str(func.__code__.co_varnames)}'
			function_results = f'The results of the function are:  {func(*args, **kwargs)}'
			with open(file_name, 'a', newline='') as f:
				writer = csv.writer(f)
				writer.writerow([function_name, function_param, function_results])

		return wrapper

	return inner


@function_decorator('data_homework.csv')
def add_person(name, age, residence):
	return f' {name} is {age} years old and lives in {residence} .'


@function_decorator('data_homework.csv')
def add_degree(name, university, certificate, dream_job):
	return f' {name} studied at {university} , where obtained a certificate in  {certificate} and his/hers dream job is {dream_job}.'


add_person('John', 28, 'Timisoara')
add_degree('John','UPT University', 'Computer engeneering', 'Computer engeneer')




