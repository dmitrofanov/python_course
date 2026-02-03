class Wallet:
    def __init__(self):
        # Инициализируй атрибут money значением 0
        self.money = 0
    
    def add_money(self, amount):
        # Увеличь self.money на amount
        self.money += amount
    
    def show_money(self):
        # Напечатай "В кошельке: X рублей"
        print(f"В кошельке: {self.money} рублей")

# Создай кошелек и протестируй
my_wallet = Wallet()
my_wallet.add_money(100)
my_wallet.add_money(50)
my_wallet.show_money()  # Должно показать: В кошельке: 150 рублей