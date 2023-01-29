# 1.Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
# printăm detalii suplimentare.
# ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
# adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
# dict

class TodoList:
    todo = {}

    def str(self):
        return f'{self.todo}'

    def repr(self):
        return str(self)

    def adauga_task(self, nume, descriere):
        self.todo.setdefault(nume, descriere)

    def finalizeaza_task(self, nume):
        if nume in self.todo.keys():
            self.todo.pop(nume)

    def afiseaza_todo_list(self):
        print('My todo list:')
        for key in self.todo.keys():
            print(key)

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task not in self.todo.keys():
            question = input('Am detectat un task nou. Doresti sa il adaugi in lista (Y/N)? ').upper()
            if question == 'Y':
                descriere_task = input('Scrie detalii legate de task-ul nou. ')
                self.todo.setdefault(nume_task, descriere_task)
            elif question == 'N':
                pass
        else:
            print(self.todo.get(nume_task))


task1 = TodoList()

task1.adauga_task('Preda tema', 'Trebuie sa finalizezi tema astazi!')   # 1
task1.adauga_task('Gateste', 'Trebuie sa gatesti la pranz.')            # 2
task1.finalizeaza_task('Preda tema')
task1.afiseaza_todo_list()

# task1.afiseaza_detalii_suplimentare('Preda tema')
task1.afiseaza_detalii_suplimentare('Gateste')
task1.afiseaza_detalii_suplimentare('Uda florile')

print(task1)

