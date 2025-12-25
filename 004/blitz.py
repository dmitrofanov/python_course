# Чем список отличается от множества? Когда использовать кортеж? Что хранит словарь?

# В чём разница между for i in range(5): и while x < 5:? Когда цикл while может стать бесконечным?

# Что делает ключевое слово return? Что такое параметр функции? Что такое аргумент функции?

# Как проверить, есть ли ключ "age" в словаре person?

# Что выведет код:
if 4 > 2:
    print("A")
else:
    print("B")

# Сколько раз выполнится тело цикла:
for i in range(5, 10, 2):
    print(i)

# Что выведет код:
a = [1, 2, 3]
b = a
b.append(4)
print(a)

# Что выведет код:
d = {1: "один", 2: "два"}
print(1 in d)
print("один" in d)

# Что выведет код:
total = 0
for i in range(3):
    total += i
print(total)

# Что выведет код:
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
print(grade)

# Что выведет код:
numbers = [1, 2, 3, 4]
for num in numbers:
    numbers.append(num * 2)
    # if len(numbers) > 6:
    #     break
print(numbers)

# Что выведет код:
count = 5
while count > 0:
    print(count)
    count -= 2