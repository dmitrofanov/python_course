"""
ЗАДАЧА: Класс Menu (Меню ресторана)

1. В __init__ создай три списка: dishes = [], prices = [], calories = []
2. Метод add_dish(name, price, calories) - добавляет блюдо во все списки
3. Метод show_menu() - показывает все блюда (используй zip для обхода)
4. Метод get_light_meals(limit) - возвращает блюда с калориями меньше limit
   (используй zip в list comprehension)

zip поможет объединить данные из трёх списков!
"""

class Menu:
   def __init__(self):
      self.dishes = []
      self.prices = []
      self.calories = []
   
   def add_dish(self, name, price, calories):
      self.dishes.append(name)
      self.prices.append(price)
      self.calories.append(calories)
   
   def show_menu(self):
      for name,price,calories in zip(self.dishes, self.prices, self.calories):
         print(f'Блюдо: {name}, Цена: {price}, Калорий: {calories}')

   def get_light_meals(self,limit):
      return [dish for dish, cal in zip(self.dishes,self.calories) if cal < limit]
   
menu = Menu()
menu.add_dish("Цезарь",100,200)
menu.add_dish("Плов",50,100)
print(f'Блюда: {menu.dishes}, Цены: {menu.prices}, Калории: {menu.calories}')
menu.show_menu()
print(f'Цена меньше лимита:{menu.get_light_meals(150)}')
