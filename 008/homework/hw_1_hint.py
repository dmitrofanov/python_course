def take_food(food):
    """Берет еду"""
    if food in ['яблоко', 'морковь']:
        return food
    else:
        return "неизвестная еда"

def wash(food):
    """Моет еду"""
    return f"чистое {food}"

def cut(food):
    """Режет еду"""
    return f"порезанное {food}"

def serve(food):
    """Подает еду"""
    return f"Подано: {food}"

# Преобразуем яблоко волшебной цепочкой
result = serve(cut(wash(take_food('яблоко'))))
print("Волшебный аппарат работает:")
print(result)

# Посмотрим на шаги в обратном порядке (как готовилось)
print("\nПроцесс приготовления (с конца):")
final = serve("порезанное чистое яблоко")
print(f"4. {final}")

third = cut("чистое яблоко")
print(f"3. После нарезки: '{third}'")

second = wash("яблоко")
print(f"2. После мойки: '{second}'")

first = take_food("яблоко")
print(f"1. Взяли: '{first}'")

# Попробуем с морковью
print("\nГотовим морковь:")
print(serve(cut(wash(take_food('морковь')))))

# А что будет с неизвестной едой?
print("\nПробуем неизвестную еду:")
print(serve(cut(wash(take_food('картошка')))))