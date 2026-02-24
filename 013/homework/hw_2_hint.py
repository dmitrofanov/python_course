class Recipes:
    def __init__(self):
        self.names = []
        self.ingredients_count = []
        self.cooking_time = []
    
    def add_recipe(self, name, ingredients, time):
        self.names.append(name)
        self.ingredients_count.append(ingredients)
        self.cooking_time.append(time)
        print(f"Добавлен рецепт: {name} ({ingredients} ингр., {time} мин.)")
    
    def show_recipes(self):
        print("\nВсе рецепты:")
        for name, ingr, time in zip(self.names, self.ingredients_count, self.cooking_time):
            print(f"  {name}: {ingr} ингредиентов, {time} минут")
    
    def get_fast_recipes(self, max_time):
        # Рецепты, которые готовятся быстро
        fast = [name for name, time in zip(self.names, self.cooking_time) if time < max_time]
        return fast
    
    def get_simple_recipes(self, max_ingredients):
        # Рецепты с небольшим количеством ингредиентов
        simple = [name for name, ingr in zip(self.names, self.ingredients_count) 
                  if ingr < max_ingredients]
        return simple

# Тестируем
recipes = Recipes()
recipes.add_recipe("Яичница", 2, 5)
recipes.add_recipe("Салат", 5, 10)
recipes.add_recipe("Борщ", 8, 60)
recipes.add_recipe("Бутерброд", 3, 3)

recipes.show_recipes()
print("\nБыстрые рецепты (<10 мин):", recipes.get_fast_recipes(10))
print("Простые рецепты (<4 ингр.):", recipes.get_simple_recipes(4))