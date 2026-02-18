"""
ЗАДАЧА 4: Класс "Корзина покупок"

1. В __init__ создай словарь self.cart = {} (товар -> цена)
2. Метод add_item(name, price) - добавляет товар в словарь self.cart
3. Метод show_cart() - показывает все товары
4. Метод total_price() - возвращает общую стоимость (sum). Пригодится метод .values() на словаре с товарами.
5. Метод get_expensive(limit) - возвращает товары дороже limit
   (используй dict comprehension: {name: price for name, price in self.cart.items() if ____})
"""

# class Cart:
#     pass # вставь свой код вместо pass

# # Тестируем
# cart = Cart()
# cart.add_item("книга", 500)
# cart.add_item("ручка", 50)
# cart.add_item("тетрадь", 100)
# cart.add_item("рюкзак", 2000)

# cart.show_cart()
# print(f"Общая стоимость: {cart.total_price()} руб.")

# expensive = cart.get_expensive(300)
# print(f"Товары дороже 300 руб.: {expensive}")

class Cart:
    def __init__(self):
        self.cart = {}
    
    def add_item(self, name, price):
        self.cart[name] = price
    
    def show_cart(self):
        print(f'Список товаров: ')
        for name, price in self.cart.items():
            print(f'  {name}, {price}')

    def total_price(self):
        return sum(self.cart.values())
    
    def get_expensive(self,limit):
        return {name: price for name, price in self.cart.items() if price > limit}


cart = Cart()
cart.add_item("книга", 500)
cart.add_item("ручка", 50)
cart.add_item("тетрадь", 100)
cart.add_item("рюкзак", 2000)

cart.show_cart()
print(f'Общая стоимость: {cart.total_price()}')

price= 50
print(f'Товары дороже {price} руб.: {cart.get_expensive(price)}')
