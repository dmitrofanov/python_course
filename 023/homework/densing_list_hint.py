data = [10, None, 20, 30, None, 40, 50, None, 60]

# Способ 1
cleaned = [x for x in data if x is not None]

# Способ 2 (без comprehension)
cleaned2 = []
for x in data:
    if x is not None:
        cleaned2.append(x)

print(f"Исходный: {data}")
print(f"После удаления None: {cleaned}")