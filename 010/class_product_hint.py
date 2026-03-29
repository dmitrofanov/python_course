class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def sell(self, amount):
        # Продай amount товара, если есть достаточно
        if amount <= self.quantity:
            self.quantity -= amount
            print(f"Продано {amount} шт. товара '{self.name}'")
            return True
        else:
            print(f"Недостаточно товара '{self.name}'. Есть только {self.quantity} шт.")
            return False
    
    def restock(self, amount):
        # Пополни запасы
        self.quantity += amount
        print(f"Запасы товара '{self.name}' пополнены на {amount} шт.")
    
    def change_price(self, new_price):
        # Измени цену
        old_price = self.price
        self.price = new_price
        print(f"Цена товара '{self.name}' изменена: {old_price} -> {new_price}")
    
    def total_value(self):
        # Верни общую стоимость всех товаров
        return self.price * self.quantity
    
    def info(self):
        # Покажи информацию о товаре
        return (f"Товар: {self.name}\n"
                f"Цена: {self.price} руб.\n"
                f"Количество: {self.quantity} шт.\n"
                f"Общая стоимость: {self.total_value()} руб.")

# Тестируем
product = Product("Яблоки", 50, 100)
print(product.info())

product.sell(30)
print(f"\nПосле продажи:\n{product.info()}")

product.restock(50)
print(f"\nПосле пополнения:\n{product.info()}")

product.change_price(55)
print(f"\nПосле изменения цены:\n{product.info()}")

# Пробуем продать больше чем есть
product.sell(200)