class Menu:
    def __init__(self):
        self.dishes = []
        self.prices = []
        self.calories = []
    
    def add_dish(self, name, price, calories):
        self.dishes.append(name)
        self.prices.append(price)
        self.calories.append(calories)
        print(f"Добавлено: {name} - {price} руб., {calories} ккал")
    
    def show_menu(self):
        print("\nМеню:")
        # Используем zip для обхода трёх списков одновременно
        for name, price, cal in zip(self.dishes, self.prices, self.calories):
            print(f"  {name}: {price} руб. ({cal} ккал)")
    
    def get_light_meals(self, limit):
        # Названия блюд с калориями меньше limit
        light = [name for name, cal in zip(self.dishes, self.calories) if cal < limit]
        return light
    
    def average_price(self):
        if not self.prices:
            return 0
        return sum(self.prices) / len(self.prices)

# Тестируем
menu = Menu()
menu.add_dish("Салат", 250, 150)
menu.add_dish("Суп", 300, 200)
menu.add_dish("Паста", 450, 550)
menu.add_dish("Чай", 100, 0)

menu.show_menu()
print("\nЛёгкие блюда (<200 ккал):", menu.get_light_meals(200))
print(f"Средняя цена: {menu.average_price():.0f} руб.")