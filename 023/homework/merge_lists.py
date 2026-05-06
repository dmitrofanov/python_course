"""
Даны два списка одинаковой длины. Создай новый список,
чередуя элементы из первого и второго.

Пример: [1, 2, 3] и ['a', 'b', 'c'] → [1, 'a', 2, 'b', 3, 'c']
"""

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

new_list = []
for i in range(len(list1)):
    new_list.append(list1[i])
    new_list.append(list2[i])
print(new_list)
