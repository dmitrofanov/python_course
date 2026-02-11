# Список - List
l = [1, 2, 3, 4, 5, 6, 1, 1, 1, 1]
even_odds = ['Even' if v % 2 == 0 else 'Odd' for v in l]
print(l)
print(even_odds)
squares = [v for v in l if v % 2 == 0]
print(squares)
# Множество - Set
s = {v for v in l if v % 2 == 1}
print(s)
# Словарь - Dict
# d1 = {}
# d1['key1'] = 'value1'
d2 = dict(key1='value1', key2='ABRACADABRA', key3='AZAZAZAZA')

d3 = {}
for key, value in d2.items():
    if len(value) > 6:
        d3[key] = value + ' HELLO'

d4 = {key: value + ' HELLO' for key, value in d2.items() if len(value) > 6}

print(d2)
print(d3)
print(d4)