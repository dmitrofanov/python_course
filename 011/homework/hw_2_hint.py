class Cart:
    def __init__(self):
        self.cart = {}
    
    def add_item(self, name, price):
        self.cart[name] = price
        print(f"Добавлен {name}: {price} руб.")
    
    def show_cart(self):
        print("\nКорзина:")
        for name, price in self.cart.items():
            print(f"  {name}: {price} руб.")
    
    def total_price(self):
        return sum(self.cart.values())
    
    def get_expensive(self, limit):
        # Dict comprehension с условием
        expensive = {name: price for name, price in self.cart.items() if price > limit}
        return expensive