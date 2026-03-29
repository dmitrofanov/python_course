"""
ЗАДАЧА: Создай класс Product (Товар)

1. В __init__ принимай name, price, quantity
2. Сохрани их в атрибуты
3. Создай метод sell(amount) - продает amount товара (уменьшает quantity)
4. Создай метод restock(amount) - пополняет запасы (увеличивает quantity)
5. Создай метод change_price(new_price) - меняет цену
6. Создай метод total_value() - возвращает общую стоимость (цена * количество)
7. Создай метод info() - показывает информацию о товаре

Протестируй: создай товар, продай часть, пополни запасы, измени цену.
"""

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f'Создали товар: {name}, Стоимость товара: {price}, Количество товара {quantity}')

    def sell(self, amount):
        if amount < self.quantity:
            self.quantity -= amount
            print(f'Продано {amount} шт. товара {self.name}, осталось {self.quantity} шт.')
        else:
            print(f'Ошибка,{amount} шт. товара нет, есть только {self.quantity}' )
    
    def restock(self, amount):
        if amount > 0:
            self.quantity += amount
            print(f'Запасы товара {self.name} пополнены на {amount} шт., стало {self.quantity} шт.')
        else:
            print('Так нельзя!,Количество товара должно быть положительным')
    
    def change_price(self, new_price):
        old_price = self.price
        self.price = new_price
        print(f'Цена товара: {self.name}, была {old_price}, Новая цена {new_price}')
    
    def total_value(self):
        return self.price * self.quantity
    
    def info(self):
        print(f'Товар {self.name}, Стоимость товара: {self.price}, Количество товара {self.quantity}')
    
    


product = Product('Картошка', 100, 5)
product.sell(4)
product.restock(-10)
product.change_price(200)
product.info()
    
