list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

result = []
for i in range(len(list1)):
    result.append(list1[i])
    result.append(list2[i])

print(f"Результат: {result}")