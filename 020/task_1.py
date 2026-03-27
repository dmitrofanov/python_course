"""
ЗАДАЧА: Корзина интернет-магазина

Дан список товаров в корзине. Каждый товар — словарь с полями:
- name: название
- price: цена
- quantity: количество

Напиши программу, которая:
1. Выводит список товаров с их итоговой стоимостью (цена × количество)
2. Считает общую сумму корзины
3. Находит самый дорогой товар (по цене за единицу)
4. Находит товар с максимальной итоговой стоимостью
"""

cart = [
    {"name": "Футболка", "price": 1000, "quantity": 20},
    {"name": "Джинсы", "price": 2500, "quantity": 2},
    {"name": "Кепка", "price": 800, "quantity": 3},
    {"name": "Кроссовки", "price": 3500, "quantity": 1},
    {"name": "Носки", "price": 200, "quantity": 5},
]

# Решение
# for product in cart:
#     print(f"товар: {product["price"]} стоимость: {product["price"] * product["quantity"]}")

print([print(f"товар: {product["name"]} стоимость: {product["price"] * product["quantity"]}") for product in cart])

print(f'общая стоимость корзины: {sum([(product["price"] * product["quantity"]) for product in cart])}')

# max_price = 0
# max_price_product = None
# for product in cart:
#     if product["price"] > max_price:
#         max_price_product = product["name"]
#         max_price = product["price"]
# print(f'Товар с мах стоимостью: {max_price_product}')
    
def get_price(product):
    return product["price"]


print(f'Товар с мах стоимостью: {max(cart, key = get_price )["name"]}')  #или вместо key = lambda x : x["price"]

print(f'Товар с максимальной итоговой стоимостью: {max(cart, key = lambda x : x["price"] * x["quantity"]) ["name"]}')


