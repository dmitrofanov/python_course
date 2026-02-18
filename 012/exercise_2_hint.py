class ShoppingCart:
    def __init__(self):
        self.items = {}  # {название: количество}
    
    def add_item(self, name, quantity=1):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
        print(f"Добавлено {quantity} шт. товара '{name}'")
    
    def remove_item(self, name, quantity=1):
        if name not in self.items:
            print(f"Товар '{name}' не в корзине")
            return
        
        if self.items[name] <= quantity:
            del self.items[name]
            print(f"Товар '{name}' полностью удалён из корзины")
        else:
            self.items[name] -= quantity
            print(f"Удалено {quantity} шт. товара '{name}'. Осталось: {self.items[name]}")
    
    def get_items_by_quantity(self, threshold):
        # Верни товары, которых больше threshold
        return {name: qty for name, qty in self.items.items() if qty > threshold}
    
    def total_items(self):
        # Общее количество товаров
        return sum(self.items.values())
    
    def unique_items(self):
        # Количество уникальных товаров
        return len(self.items)
    
    def most_popular(self, n):
        # Верни n самых популярных товаров (по количеству)
        sorted_items = sorted(self.items.items(), key=lambda x: x[1], reverse=True)
        return [name for name, qty in sorted_items[:n]]
    
    def show_cart(self):
        if not self.items:
            print("Корзина пуста")
            return
        
        print("\nКорзина:")
        for name in sorted(self.items.keys()):
            print(f"  {name}: {self.items[name]} шт.")
        print(f"  Всего: {self.total_items()} шт. {self.unique_items()} разных товаров")

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