from time import sleep, perf_counter
from functools import lru_cache, wraps

def timer(func):
    @wraps(func)
    def wrapper(*args):
        x = perf_counter()
        result = func(*args)
        print(perf_counter() - x)
        return result
    return wrapper

def logger(level):
    def inner(func):
        @wraps(func)
        def wrapper(*args):
            if level == 1:
                print("Уровень логирования INFO", func.__name__, args)
            else:
                print("Уровень логирования DEBUG", func.__name__, args)
            return func(*args)
        return wrapper
    return inner

            

@timer
@logger(1)
def greeting():
    sleep(1)
    print("Privet Pavel")

greeting()
print(greeting.__name__)

def show_fun(func):
    print(func.__name__)
show_fun(greeting)


# timer(greeting)

@lru_cache
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 2) + fib(n - 1)
x = perf_counter()
print(fib(30))
print(perf_counter() - x)