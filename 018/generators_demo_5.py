import sys

# Список
list_squares = [x**2 for x in range(10000)]
print(f"Список: {sys.getsizeof(list_squares)} байт")

# Генератор
gen_squares = (x**2 for x in range(10000))
print(f"Генератор: {sys.getsizeof(gen_squares)} байт")

# Список из миллиона
list_million = [x for x in range(1_000_000)]
print(f"Миллион в списке: {sys.getsizeof(list_million) / 1024 / 1024:.1f} МБ")

# Генератор
gen_million = (x for x in range(1_000_000))
print(f"Миллион в генераторе: {sys.getsizeof(gen_million)} байт")