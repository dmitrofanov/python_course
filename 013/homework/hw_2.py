"""
ЗАДАЧА: Класс Recipes (Кулинарная книга)

1. В __init__ создай списки: names = [], ingredients_count = [], cooking_time = []
2. Метод add_recipe(name, ingredients, time) - добавляет рецепт
3. Метод show_recipes() - показывает все рецепты
4. Метод get_fast_recipes(max_time) - быстрые рецепты (время меньше max_time)
5. Метод get_simple_recipes(max_ingredients) - простые рецепты (ингредиентов меньше)

zip для фильтрации по разным критериям!
"""

# class Recipes:
#     pass

# Тестируем
# recipes = Recipes()
# recipes.add_recipe("Яичница", 2, 5)
# recipes.add_recipe("Салат", 5, 10)
# recipes.add_recipe("Борщ", 8, 60)
# recipes.add_recipe("Бутерброд", 3, 3)

# recipes.show_recipes()
# print("\nБыстрые рецепты (<10 мин):", recipes.get_fast_recipes(10))
# print("Простые рецепты (<4 ингр.):", recipes.get_simple_recipes(4))

class Recipes:
    def __init__(self):
        self.names = []
        self.ingredients_count = []
        self.cooking_time = []

    def add_recipe(self, name, ingredients, time):
        self.names.append(name)
        self.ingredients_count.append(ingredients)
        self.cooking_time.append(time)

    def show_recipes(self):
       for self.name, self.ingredients, self.time in zip(self.names, self.ingredients_count, self.cooking_time):
         print(f'Блюдо: {self.name}, Количество ингредиентов: {self.ingredients}, Калорий: {self.time}')
    
    def get_fast_recipes(self,max_time):
       return [names for names, cooking_time in zip(self.names, self.cooking_time) if cooking_time < max_time]
    
    def get_simple_recipes(self,max_ingredients):
       return [names for names, ingredients in zip(self.names, self.ingredients_count) if ingredients < max_ingredients]
       

recipes = Recipes()
recipes.add_recipe("Яичница", 2, 5)
recipes.add_recipe("Салат", 5, 10)
recipes.add_recipe("Борщ", 8, 60)
recipes.add_recipe("Бутерброд", 3, 3)

recipes.show_recipes()
print("\nБыстрые рецепты (<10 мин):", recipes.get_fast_recipes(10))
print("Простые рецепты (<4 ингр.):", recipes.get_simple_recipes(4))