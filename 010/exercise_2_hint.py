class GameCharacter:
    def __init__(self, name, health=100, attack_power=10):
        self.name = name
        self.health = health
        self.max_health = health  # сохраняем максимальное здоровье
        self.attack_power = attack_power
    
    def take_damage(self, damage):
        # Уменьши health на damage, но не ниже 0
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} получил {damage} урона. Здоровье: {self.health}")
    
    def heal(self, amount):
        # Увеличь health на amount, но не выше max_health
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} восстановил {amount} здоровья. Теперь: {self.health}")
    
    def attack(self, target):
        # Атакуй другого персонажа (вызови у него take_damage)
        if self.is_alive():
            print(f"{self.name} атакует {target.name}!")
            target.take_damage(self.attack_power)
        else:
            print(f"{self.name} не может атаковать, он повержен!")
    
    def is_alive(self):
        # Верни True если персонаж жив (health > 0)
        return self.health > 0
    
    def status(self):
        # Покажи статус персонажа
        status = "жив" if self.is_alive() else "мертв"
        return f"{self.name}: здоровье {self.health}/{self.max_health} ({status})"

# Тестируем
hero = GameCharacter("Герой", health=120, attack_power=15)
enemy = GameCharacter("Враг", health=80, attack_power=12)

print("Бой начинается!")
print(hero.status())
print(enemy.status())

print("\n--- Раунд 1 ---")
hero.attack(enemy)
enemy.attack(hero)

print("\n--- Раунд 2 ---")
hero.attack(enemy)
enemy.attack(hero)

print("\n--- Герой лечится ---")
hero.heal(30)

print("\n--- Раунд 3 ---")
hero.attack(enemy)

print("\nИтоговый статус:")
print(hero.status())
print(enemy.status())