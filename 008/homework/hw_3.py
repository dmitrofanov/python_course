"""
ЗАДАЧА 2: Создай класс Book (Книга)

1. В __init__ принимай параметры: title, author, pages
2. Сохраняй их в атрибуты: self.title, self.author, self.pages
3. Создай метод describe(), который печатает:
   "Книга 'Название' автор Автор, X страниц"

Создай книгу "Война и мир".
"""

class Book:
   def __init__(self, title, author, pages):
      self.title = title
      self.author = author
      self.pages = pages
   
   def describe(self):
      print(f'Книга {self.title} автор {self.author}, {self.pages} страниц')

book1 = Book("Вий", "Гоголь", 45)
book2 = Book("Три мушкетера", "Дюма", 500)

book1.describe()
book2.describe()
       
