"""
ЗАДАНИЕ: Пакетная обработка данных

Напиши генератор batch_processor(data, batch_size), который выдаёт данные
пачками заданного размера. Это полезно для отправки в API или записи в БД.

Пример: batch_processor([1,2,3,4,5,6,7], 3) -> [1,2,3], [4,5,6], [7]
"""

def batch_processor(data, batch_size):
    assert batch_size > 0
    proc_list = []
    for i in data:
        proc_list.append(i)
        if len(proc_list) == batch_size:
            yield proc_list
            proc_list = []
    if proc_list:
        yield proc_list


processor = batch_processor([1,2,3,4,5,6,7,], 0)

for p in processor:
    print(p)