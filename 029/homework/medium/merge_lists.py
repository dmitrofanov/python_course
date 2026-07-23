"""
Даны два списка разной длины. Создай новый список, чередуя элементы
из обоих списков. Если один список закончился — продолжай брать из другого.
Пример: [1, 2, 3], ['a', 'b'] → [1, 'a', 2, 'b', 3]
"""

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']

new_list = []

for i in range(max(len(list1), len(list2))):
    if i < len(list1):
        new_list.append(list1[i])
    if i < len(list2):
        new_list.append(list2[i])

print(new_list)
