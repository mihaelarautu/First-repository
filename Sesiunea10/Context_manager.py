# pentru a implementa un context manager avem nevoie de o clasa car5e implementeazaq functiile __enter__ si __exit__
# * __enter__ - deschide accesul la resurse si returneaza resursa
# * __exit__ - inchide accesul la resurse


class FileManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.f = None

    def __enter__(self):
        self.f = open(self.file_name, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


with FileManager("data.txt", "w") as f:
    f.write("Ana are mere si pere")


class HelloManager:
    def __enter__(self):
        print('Entering in the context manager')
        return (f"Hello world")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Leaving the context manager')
        if exc_type == IndexError:
            print(f'Exception happend: {exc_val}')
        return True  # opreste eroarea, si doar va printa
        # return False = lasa eroarea sqa se propage mai departe in cod


with HelloManager() as h:
    print(h)
    print(h[100])

print('Finally!')

########################################################################
# Context manager ca si functie
from contextlib import contextmanager


@contextmanager
def file_manager(file_name, mode):
    f = open(file_name, mode)
    yield f
    f.close()

with file_manager('data.txt','r') as f:
    print(f.read())

@contextmanager
def hello_manager():
    print('Enter in the context manager')
    yield 'Hello world again!'
    print('Leaving the context manager.')

with hello_manager() as h:
    print(h)