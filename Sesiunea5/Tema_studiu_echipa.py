# 1. Functie care sa afiseze data si ora curenta din ro
# (bonus: afisati si data si ora curenta din China)
from datetime import datetime, timedelta, timezone


# v1
def display_date_time_v1():
    now = datetime.now()
    print(f"Date and time Romania: {now}")
    print(f"Date and time China: {now + timedelta(hours=5)}")


display_date_time_v1()

# v2
import pytz


def display_date_time_v2():
    timezone_ro = pytz.timezone(
        'Europe/Bucharest')  # pt v2, trebuie stiute timezone-uri sau aflate (print(pytz.all_timezones))
    now = datetime.now(timezone_ro)
    print(f"Date and time Romania: {now}")

    timezone_cn = pytz.timezone('Asia/Hong_Kong')
    now = datetime.now(timezone_cn)
    print(f"Date and time China: {now}")


display_date_time_v2()


############ rezolvarea noastra # 1
from datetime import datetime
import datetime
import pytz


def data_si_ora():
    data_si_ora = datetime.datetime.now()
    print(data_si_ora)


data_si_ora()

x = pytz.timezone('Asia/Hong_Kong')

print(datetime.datetime.now(tz=x))


# varianta 2
def current_date_time(country):
    if country == 'Romania':
        current_time = datetime.datetime.now(pytz.timezone('Europe/Bucharest'))
        print(f"The current time in {country} is:")
        print(f"Date: {current_time.year}-{current_time.month}-{current_time.day}")
        print(f"Hour: {current_time.hour}:{current_time.minute}:{current_time.second}")
    if country == 'China':
        current_time = datetime.datetime.now(pytz.timezone('Asia/Hong_Kong'))
        print(f"The current time in {country} is:")
        print(f"Date: {current_time.year}-{current_time.month}-{current_time.day}")
        print(f"Hour: {current_time.hour}:{current_time.minute}:{current_time.second}")


current_date_time('Romania')
current_date_time('China')

"""
2. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
"""


def get_days_until_christmas():
    today = datetime.date.today()
    future = datetime.date(2022, 12, 25)
    diff = future - today
    print(f'Pana la Crăciun mai sunt: {diff.days} de zile')


get_days_until_christmas()


# varianta 2 zi nastere

def get_days_until_birthday():
    today = datetime.date.today()
    future = datetime.date(2023, 5, 13)
    diff = future - today
    print(f'Pana la ziua mea mai sunt: {diff.days} de zile')


get_days_until_birthday()
#varianta 3

from datetime import date

date_components = input('Enter your birthday formatted as YYYY-MM-DD: ').split('-')
year, month, day = [int(item) for item in date_components]
birthday = date(year, month, day)

today = date.today()

def calculate_dates(birthday, today):
    birthday = date(today.year, birthday.month, birthday.day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
        return birthday
    else:
        return birthday




bday = birthday
t = calculate_dates(birthday, today)
time_to_birthday = abs(t-today)
days=str(time_to_birthday.days)
print("Time to Birthday is :" + days + " days")