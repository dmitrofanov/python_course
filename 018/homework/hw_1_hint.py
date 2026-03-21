"""
ЗАДАНИЕ 2: Пакетная обработка данных

Напиши генератор batch_processor(data, batch_size), который выдаёт данные
пачками заданного размера. Это полезно для отправки в API или записи в БД.

Пример: batch_processor([1,2,3,4,5,6,7], 3) -> [1,2,3], [4,5,6], [7]
"""

def batch_processor(data, batch_size):
    result = []
    for item in data:
        result.append(item)
        # print(result)
        if len(result) == batch_size:
            yield result
            result = []
    if result:
        yield result

processor = batch_processor([1,2,3,4,5,6,7,], 3)

for p in processor:
    print(p)