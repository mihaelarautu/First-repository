# 1. Sa se scrie un context manager care masoara durata de executie a unei bucati
# de  cod
from contextlib import contextmanager
from time import perf_counter, sleep


class TimmerManager:
    def __enter__(self):
        self.start = perf_counter()
        return self.start

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter()
        print(self.end - self.start)


with TimmerManager():
    sleep(5)
    print('M-am trezit!')

@contextmanager
def time_manager():
    start = perf_counter()
    yield
    stop = perf_counter()
    print(stop-start)

with time_manager() as t:
    sleep(2)
    print(t)

