"""
ЗАДАЧА: Класс Library

Создай класс Library, который хранит книги в словаре:
ключ — название, значение — автор.

Методы:
- add_book(title, author) — добавляет книгу
- remove_book(title) — удаляет книгу
- find_by_author(author) — возвращает список книг указанного автора
- show_all() — выводит все книги

Создай библиотеку, добавь несколько книг и найди книги по автору.
"""

class Library:
    def __init__(self):
        self.books = {}
    
    def add_book(self,title, author):
        self.books[title] = author
        print(f"Добавили книгу: {title} , Автор: {author}")

    def remove_book(self,title):
        if title in self.books:
            del self.books[title]
            print(f'Удалена книга {title}')
        else:
            print(f'Книга {title} не найдена')
    
    def find_by_author(self,author):
        find_auth = []
        for title, a in self.books.items():
            if a == author:
                find_auth.append(title)
        return find_auth
    
    def show_all(self):
        for title, author in self.books.items():
            print(f"Книга:  {title} , Автор: {author}")


###### Код для тестирования:

# Создаём библиотеку
library = Library()

# Добавляем книги
library.add_book("Война и мир", "Толстой")
library.add_book("Анна Каренина", "Толстой")
library.add_book("Преступление и наказание", "Достоевский")
library.add_book("Мастер и Маргарита", "Булгаков")

library.remove_book("Мастер и Маргарита")
library.remove_book("Унесенные ветром")

# Ищем книги Толстого
print("\nКниги Толстого:")
tolstoy_books = library.find_by_author("Толстой")
for book in tolstoy_books:
    print(f"  {book}")

library.show_all()

