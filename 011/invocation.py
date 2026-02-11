class A:
    def __init__(self, name):
        self.name = name
    
    def hello(self):
        print(f'Hello {self.name}')


l = [A('Dima'), A('Pavel'), A('Ivan')]

for person in l:
    person.hello()

[person.hello() for person in l]