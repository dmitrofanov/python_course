persons = [
    {
        'name': 'Дима',
        'organs': [
            {'name': 'Сердце'},
            {'name': 'Печень'}
        ]
    },
    {
        'name': 'Анна',
        'organs': [
            {'name': 'Почки'},
            {'name': 'Глаза'}
        ]
    }
]

for person in persons:
    print(f'Человек: {person['name']}')
    for organ in person['organs']:
        print(f'Орган: {organ['name']}')
