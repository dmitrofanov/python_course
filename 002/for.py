# Цикл for

for digit in (1, 2, 3):
    print(digit)

for char in 'Hello there!':
    print(char)

for i in range(10):
    print(i)

products = [
    {'name': 'Toaster', 'price': 3000},
    {'name': 'Teapot', 'price': 2500},
    {'name': 'Aerogrill', 'price': 7000},
]

for product in products:
    print(product['name'])


# Вложенные циклы

for x in (1, 2, 3):
    for y in 'ABCD':
        print(x, y)