def simple_gen():
    yield "первый"
    yield "второй"
    yield "третий"

gen = simple_gen()

print(next(gen))  # первый
print(next(gen))  # второй
print(next(gen))  # третий
# print(next(gen))  # StopIteration!