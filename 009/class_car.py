class Car:
    def __init__(self, model, color='Black'):
        self.model = model
        self.color = color
    
    def full_name(self, invitation='Hello'):
        return f'{invitation} {self.model} - {self.color}'


car1 = Car('Tesla X')
print(car1.full_name('Greetings'))
car2 = Car('Citroen')
print(car2.full_name())
car3 = Car('Ford', 'Yellow')
print(car3.full_name())