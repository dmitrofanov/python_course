"""
ЗАДАЧА 1: Создай класс Wallet (Кошелек)

1. В методе __init__ создай атрибут money со значением 0
2. Создай метод add_money(amount), который увеличивает money на amount
3. Создай метод show_money(), который печатает "В кошельке: X рублей"

Создай кошелек, добавь 100 рублей, потом еще 50, и покажи сколько денег.
"""


class Wallet:
    def __init__(self):
        self.money = 0

    def add_money(self, amount):
        self.money += amount
    
    def show_money(self):
        print(f"В кошельке: {self.money} рублей")

my_wallet = Wallet()
my_wallet.add_money(100)
my_wallet.add_money(50)
my_wallet.show_money()

    