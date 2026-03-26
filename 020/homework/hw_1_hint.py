class Library:
    def __init__(self):
        self.books = {}
    
    def add_book(self, title, author):
        self.books[title] = author
        print(f"Добавлена книга: {title} ({author})")
    
    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"Удалена книга: {title}")
        else:
            print(f"Книга '{title}' не найдена")
    
    def find_by_author(self, author):
        found = []
        for title, auth in self.books.items():
            if auth == author:
                found.append(title)
        return found
    
    def show_all(self):
        if not self.books:
            print("Библиотека пуста")
            return
        print("\nВсе книги:")
        for title, author in self.books.items():
            print(f"  {title} - {author}")
