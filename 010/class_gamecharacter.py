"""
ЗАДАЧА: Создай класс GameCharacter (Игровой персонаж)

1. В __init__ принимай name, health=100, attack_power=10
2. Сохрани их в атрибуты
3. Создай метод take_damage(damage) - уменьшает health
4. Создай метод heal(amount) - увеличивает health (не больше максимума)
5. Создай метод attack(target) - атакует другого персонажа
6. Создай метод is_alive() - возвращает True если health > 0
7. Создай метод status() - показывает состояние персонажа

Создай двух персонажей, заставь их подраться.
"""



class GameCharacter:
    def __init__(self, name, health=100, attack_power=10):
        self.name = name
        self.health =  health
        self.max_health = health
        self.attack_power = attack_power
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f'Персонаж {self.name} получил урон {damage}, стало {self.health}')

    def heal(self,amount):
        old_health = self.health 
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f'Персонаж {self.name} вылечился на {self.health - old_health} здоровья ')

    def attack(self,target):
        print(f'{self.name} атакует {target.name}')
        target.take_damage(self.attack_power)
    
    def is_alive(self):
        return self.health > 0
    
    def status(self):
        print(f'Персонаж {self.name} имеет {self.health} здоровья')


char1 = GameCharacter('Alex',100,50)
char1.take_damage(0)
char1.heal(0)
print(char1.health)

char2 = GameCharacter('Bib')
char1.attack(char2)
print(char1.is_alive())
print(char2.is_alive())

char1.status()
char2.status()