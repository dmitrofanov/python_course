me = dict(name='Dima', city='Saint-Petersburg', age=34)
print(me['name']) # Dima
print(me['city']) # Saint-Petersburg
print(me['age']) # 34

me = dict(name='Dima', city='Saint-Petersburg', age=34)
print('age' in me) # True
print('wrong' in me) # False

me = dict(name='Dima', city='Saint-Petersburg', age=34)
print(me.keys()) # dict_keys(['name', 'city', 'age'])
print(me.values()) # dict_values(['Dima', 'Saint-Petersburg', 34])
print(me.items()) # dict_items([('name', 'Dima'), ('city', 'Saint-Petersburg'), ('age', 34)])

me = dict(name='Dima', city='Saint-Petersburg', age=34)
keys = me.keys()
me['qweq234234we'] = 'zxcvxcvxcvxcvzxcv'
print(keys) # dict_keys(['name', 'city', 'age', 'new key'])

me = dict(name='Dima', city='Saint-Petersburg', age=34)
print(len(me)) # 3