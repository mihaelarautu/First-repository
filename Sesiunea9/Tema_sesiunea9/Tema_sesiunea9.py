# 1. Sa se scrie o functie care citeste date dintr-un fisier csv si le scrie intr-un fisier json. Functia primeste numele fisierelor ca parametri.
import csv
import json


def convert_CSV_to_JSON(read_file_name, write_file_name):
    with open(read_file_name, "r") as f:
        reader = csv.DictReader(f)
        data = list(reader)
    with open(write_file_name, "w") as f:
        json.dump(data, f, indent=4)


convert_CSV_to_JSON('read.csv', 'write.json')


# 2. Sa se scrie o functie care citeste date dintr-un fisier json si le imparte in alte doua fisiere astfel incat prima jumatate a datelor va fi in fisierul prima_jumatate.json,
# iar a doua in a_doua_jumatate.json.

def split_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    jumatate = len(data) // 2
    with open('prima_jumatate.json', 'w') as f:
        json.dump(data[:jumatate], f)
    with open('a_doua_jumatate.json', 'w') as f:
        json.dump(data[jumatate:], f)


split_json('write.json')

# 3. Sa se scrie o functie care citeste date dintr-un fisier csv si le elimina pe cele care in oricare coloana contin litera ‘a’. Dupa aceea va actualiza fisierul cu datele ce raman.
def delete_element_in_CSV(file_name, char):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        for i in range(len(data)):
            for elem in data[i]:
                if char in elem:
                    data[i].remove(elem)
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


delete_element_in_CSV('email.csv', 'a')