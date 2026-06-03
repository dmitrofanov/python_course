class Mammal:
    instance_count = 0

    def __init__(self, name, legs_count):
        self.name = name
        self.legs_count = legs_count
        Mammal.instance_count += 1


class Cat(Mammal):
    def lick(self):
        print(self.name, 'вылизывается')


class Dog(Mammal):
    def wobble(self):
        print(self.name, 'виляет хвостом')



cat = Cat('Мурка', 4)
dog = Dog('Шарик', 4)
dog2 = Dog('Шарик', 4)

print(Mammal.instance_count)

cat.lick()  
dog.wobble()