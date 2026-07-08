list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']

result = []
max_len = max(len(list1), len(list2))

for i in range(max_len):
    if i < len(list1):
        result.append(list1[i])
    if i < len(list2):
        result.append(list2[i])

print(f"Результат чередования: {result}")