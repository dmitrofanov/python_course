"""
ЗАДАЧА: Класс Recipes (Кулинарная книга)

1. В __init__ создай списки: names = [], ingredients_count = [], cooking_time = []
2. Метод add_recipe(name, ingredients, time) - добавляет рецепт
3. Метод show_recipes() - показывает все рецепты
4. Метод get_fast_recipes(max_time) - быстрые рецепты (время меньше max_time)
5. Метод get_simple_recipes(max_ingredients) - простые рецепты (ингредиентов меньше)

zip для фильтрации по разным критериям!
"""

class Recipes:
    pass

# Тестируем
recipes = Recipes()
recipes.add_recipe("Яичница", 2, 5)
recipes.add_recipe("Салат", 5, 10)
recipes.add_recipe("Борщ", 8, 60)
recipes.add_recipe("Бутерброд", 3, 3)

recipes.show_recipes()
print("\nБыстрые рецепты (<10 мин):", recipes.get_fast_recipes(10))
print("Простые рецепты (<4 ингр.):", recipes.get_simple_recipes(4))