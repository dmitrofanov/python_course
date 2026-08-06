"""
Дан список и размер чанка. Разбей список на подсписки указанного размера.
Последний чанк может быть короче.
Пример: [1, 2, 3, 4, 5, 6, 7, 8], chunk_size=3 → [[1, 2, 3], [4, 5, 6], [7, 8]]
"""



def to_chunks(lst, chunk_size):
    if chunk_size <= 0:
        raise ValueError(f"chunk_size должен быть больше 0, получено {chunk_size}")
    result = []
    for i in range(0, len(lst), chunk_size):
        chunk = lst[i:i + chunk_size]
        result.append(chunk)
    return result
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = -1
print(to_chunks(lst, chunk_size))


#дерево ошибок python