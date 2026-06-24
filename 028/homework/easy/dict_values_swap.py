"""
Дан словарь с двумя ключами. Поменяй местами их значения.
"""

pair = {"first": "яблоко", "second": "банан"}
pair["first"], pair["second"] = pair["second"],pair["first"]
print(pair)
