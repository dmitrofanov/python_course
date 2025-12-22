# 3. «Поисковик дубликатов»
#     Дан список: items = ["яблоко", "банан", "киви", "яблоко", "апельсин", "банан", "яблоко"].
#     С помощью вложенных циклов for (или for и оператора in) найти и вывести все элементы, которые встречаются больше одного раза, но каждый дубликат вывести только один раз (например, "яблоко, банан").

items = ["apple", "banana", "kiwi", "apple", "orange", "banana", "apple"]
seen = []
for idx in range(len(items)):
    item = items[idx]
    if item in items[idx+1:] and item not in seen:
        print(item)
        seen.append(item)

