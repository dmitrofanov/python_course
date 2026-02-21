"""
ЗАДАЧА1: Класс StampCollection (Коллекция марок)

1. В __init__ создай пустой список stamps = [] (список стран, откуда марки)
2. Метод add_stamp(country) - добавляет марку (название страны в список)
3. Метод show_all() - показывает все марки
4. Метод unique_countries() - возвращает множество уникальных стран
   (используй set comprehension)

Это самый простой set comprehension - просто собираем уникальные элементы!
"""

# class StampCollection:
#     pass

# # Тестируем
# collection = StampCollection()
# collection.add_stamp("Россия")
# collection.add_stamp("Франция")
# collection.add_stamp("Россия")
# collection.add_stamp("Италия")
# collection.add_stamp("Франция")

# collection.show_all()
# print("Уникальные страны:", collection.unique_countries())

class StampCollection:
    def __init__(self):
        self.stamps = []
    
    def add_stamp(self,country):
        self.stamps.append(country)
        print(f'Добавили марку {country}')
    
    def show_all(self):
        print("Все марки:", self.stamps)
    
    def unique_countries(self):
        return {country for country in self.stamps}

collection = StampCollection()
collection.add_stamp("Россия")
collection.add_stamp("Франция")
collection.add_stamp("Россия")
collection.add_stamp("Италия")
collection.add_stamp("Франция")
collection.show_all()
print("Уникальные страны:", collection.unique_countries())