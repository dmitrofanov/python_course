# l = [5,6,2,21,23,5,11,4,2]
# print(l)


# l = sorted(l)
# print(l)

d = [
    {'name': 'Dima'},
    {'name': 'Alex'},
    {'name': 'Vera'},
    {'name': 'Nikolay'},
    {'name': 'Pavel'},
]

# print(d)

def name_getter(d):
    return d['name']

d = sorted(d, key=lambda x: x['name'])
print(d)


# ID, NAME, PRICE
t = [
    (1, 'Phone', 300),
    (2, 'Oven', 5000),
    (3, 'Fork', 20),
    (4, 'Bag', 500),
]

print(sorted(t, key=lambda x: x[2]))