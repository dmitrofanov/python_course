"""
ЗАДАЧА1: Класс StampCollection (Коллекция марок)

1. В __init__ создай пустой список stamps = [] (список стран, откуда марки)
2. Метод add_stamp(country) - добавляет марку (название страны в список)
3. Метод show_all() - показывает все марки
4. Метод unique_countries() - возвращает множество уникальных стран
   (используй set comprehension)

Это самый простой set comprehension - просто собираем уникальные элементы!
"""

class StampCollection:
    pass

# Тестируем
collection = StampCollection()
collection.add_stamp("Россия")
collection.add_stamp("Франция")
collection.add_stamp("Россия")
collection.add_stamp("Италия")
collection.add_stamp("Франция")

collection.show_all()
print("Уникальные страны:", collection.unique_countries())