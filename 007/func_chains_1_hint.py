def double(x):
    return x * 2

def add_five(x):
    return x + 5

# Способ 1: По шагам
result1 = add_five(10)  # 15
result2 = double(result1)  # 30
print("По шагам:", result2)

# Способ 2: В одну строку
result3 = double(add_five(10))
print("В одну строку:", result3)