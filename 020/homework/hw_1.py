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
    pass # здесь твой код

###### Код для тестирования:

# Создаём библиотеку
library = Library()

# Добавляем книги
library.add_book("Война и мир", "Толстой")
library.add_book("Анна Каренина", "Толстой")
library.add_book("Преступление и наказание", "Достоевский")
library.add_book("Мастер и Маргарита", "Булгаков")

library.show_all()

# Ищем книги Толстого
print("\nКниги Толстого:")
tolstoy_books = library.find_by_author("Толстой")
for book in tolstoy_books:
    print(f"  {book}")