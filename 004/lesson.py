# Методы словаря
car = dict(brand='Citroen', model='C4')
print(car.items())
print(car.get('brand', 'Volvo'))
print(car.get('engine_volume', 1.6))

phrase = 'Hello from there'
letter_count = {}
for letter in phrase:
    letter_count[letter] = letter_count.get(letter, 0) + 1
print(letter_count)