import itertools

# Бесконечный цикл по списку
colors = ["красный", "зелёный", "синий"]
n = 0
for color in itertools.cycle(colors):
    print(color)
    if n > 20:
        break  # иначе бесконечно
    n += 1

# Комбинации
for combo in itertools.combinations([1, 2, 3, 4], 2):
    print(combo)

# Цепочка генераторов
gen1 = (x for x in range(3))
gen2 = (x for x in range(10, 13))
for val in itertools.chain(gen1, gen2):
    print(val)