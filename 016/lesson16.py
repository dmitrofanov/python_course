import time

a=time.perf_counter()
time.sleep(1)
print(time.perf_counter()-a)

# нам нужно написать контекстный менджер, который говорит о том,сколько времени заняло его тело

class Timer:
    def __init__(self):
        self.start_time = None
    
    def __enter__(self):
        self.start_time = time.perf_counter()

    def __exit__(self, exc_type, exc, tb):
        print(f'Время выполнения составило: {time.perf_counter()-self.start_time} сек')

with Timer():
    [object() for _ in range(100000000)]g
    