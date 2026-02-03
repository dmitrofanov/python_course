class Book:
    def __init__(self, title, author, pages):
        # Сохрани параметры в атрибуты
        self.title = title
        self.author = author
        self.pages = pages
    
    def describe(self):
        # Напечатай информацию о книге
        print(f"Книга '{self.title}' автор {self.author}, {self.pages} страниц")

# Создай книгу и протестируй
war_and_peace = Book("Война и мир", "Лев Толстой", 1225)
war_and_peace.describe()  # Должно показать информацию о книге