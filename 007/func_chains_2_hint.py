def make_upper(text):
    return text.upper()

def add_farewell(text):
    return text + " прощай!!!"

# Цепочка 1: Сначала верхний регистр, потом восклицание
result1 = add_farewell(make_upper("привет"))
print("1. ВЕРХНИЙ РЕГИСТР + прощай!!!:", result1)

# Цепочка 2: Сначала восклицание, потом верхний регистр
result2 = make_upper(add_farewell("привет"))
print("2. прощай!!! + верхний регистр:", result2)

# Объяснение: Порядок важен! Сначала выполняется ВНУТРЕННЯЯ функция