# List comprehension — создаёт список
list_squares = [x**2 for x in range(10)]
print(f"Список: {list_squares}")
print(f"Тип: {type(list_squares)}")

# Generator expression — создаёт генератор
gen_squares = (x**2 for x in range(10))
print(f"Генератор: {gen_squares}")
print(f"Тип: {type(gen_squares)}")

# Генератор не хранит значения — выдаёт по одному
for val in gen_squares:
    print(val, end=" ")

'''
yield приостанавливает функцию, сохраняя её состояние

При следующем вызове функция продолжается с того же места
'''