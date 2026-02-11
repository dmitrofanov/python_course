fruits = ["яблоко", "банан", "апельсин", "киви"]
prices = [50, 30, 80, 45]

# 1. Словарь цен
price_dict = {fruit: price for fruit, price in zip(fruits, prices)}
print("Цены:", price_dict)

# 2. Цены со скидкой
discount_dict = {fruit: price * 0.8 for fruit, price in zip(fruits, prices)}
print("Со скидкой 20%:", discount_dict)

# 3. Длина названия
length_dict = {fruit: len(fruit) for fruit in fruits}
print("Длина названия:", length_dict)

# 4. Только дорогие фрукты (> 40)
expensive_dict = {fruit: price for fruit, price in zip(fruits, prices) if price > 40}
print("Дороже 40 руб.:", expensive_dict)

# 5. Категория цены
category_dict = {fruit: "дорогой" if price > 50 else "дешёвый" 
                 for fruit, price in zip(fruits, prices)}
print("Категории:", category_dict)