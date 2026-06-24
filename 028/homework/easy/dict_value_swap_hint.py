pair = {"first": "яблоко", "second": "банан"}

print(f"До обмена: {pair}")

# Обмен значениями
pair["first"], pair["second"] = pair["second"], pair["first"]

print(f"После обмена: {pair}")