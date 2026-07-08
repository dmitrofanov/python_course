items = ["a", "b", "c", "d", "e", "f", "g", "h"]

even_index_items = []
for i in range(0, len(items), 2):
    even_index_items.append(items[i])

print(f"Элементы на чётных индексах: {even_index_items}")