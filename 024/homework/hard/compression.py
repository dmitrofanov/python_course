"""
Реализуй простое кодирование длин серий (Run-Length Encoding) для списка.
Пример: [1, 1, 1, 2, 2, 3, 3, 3, 3] → [(1, 3), (2, 2), (3, 4)]
"""
#Посчитать сколько раз встречается число в data
#(1 - 6) (2 -4) (3- 5) (5 -1)

data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 1, 4 , 1, 1]


def search_item(result, search_number):
    for number, count in result[::-1]:
        if number == search_number:
            return count
    return 0

result = []
current = data[0]
count = 1
for element in data[1:]:
    if element != current:
        result.append((current, count + search_item(result, current)))
        current = element
        count = 1
    else:
        count += 1
result.append((current, count + search_item(result, current)))
print(result)
