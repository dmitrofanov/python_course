def half(x):
    result = x / 2
    print(f"half({x}) = {result}")
    return result

def square(x):
    result = x * x
    print(f"square({x}) = {result}")
    return result

def increment(x):
    result = x + 1
    print(f"increment({x}) = {result}")
    return result

# Выполняем цепочку
final_result = increment(square(half(10)))
print("\nИтоговый результат:", final_result)