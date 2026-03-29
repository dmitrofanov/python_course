def generator1():
    yield "один"
    yield "два"

def generator2():
    yield "три"
    yield "четыре"

def combined_generator():
    yield from generator1()
    yield from generator2()
    yield "пять"

for val in combined_generator():
    print(val)