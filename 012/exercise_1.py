"""
ЗАДАЧА: Создай класс ShoppingCart (Корзина покупок)

1. В __init__ создай словарь items = {} (название -> количество)
2. Метод add_item(name, quantity=1) - добавляет товар (увеличивает количество)
3. Метод remove_item(name, quantity=1) - уменьшает количество или удаляет
4. Метод get_items_by_quantity(threshold) - возвращает товары, которых больше threshold
   (используй dict comprehension)
5. Метод total_items() - возвращает общее количество товаров (сумма values)
6. Метод unique_items() - возвращает количество уникальных товаров (len)
7. Метод most_popular(n) - возвращает n самых популярных товаров
   (используй sorted() и list comprehension)
8. Метод show_cart() - показывает корзину

Протестируй добавление разных товаров.
"""
class ShoppingCart:
    pass

# Тестируем
cart = ShoppingCart()
cart.add_item("яблоки", 5)
cart.add_item("бананы", 3)
cart.add_item("яблоки", 2)
cart.add_item("молоко", 2)
cart.add_item("хлеб", 1)
cart.add_item("бананы", 2)

cart.show_cart()

print("\nТовары, которых >3 шт.:", cart.get_items_by_quantity(3))
print("Топ-2 популярных товара:", cart.most_popular(2))

cart.remove_item("бананы", 3)
cart.remove_item("молоко", 2)
cart.show_cart()