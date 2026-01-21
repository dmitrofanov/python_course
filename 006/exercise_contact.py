"""
Ты создаёшь простую контактную книгу.
Все контакты хранятся в одном словаре.

ШАГ 1: Создай пустой словарь:
contacts = {}

ШАГ 2: Напиши функцию add_contact(name, phone):
    - Добавляет в словарь contacts новую пару name: phone
    - Ничего не возвращает, просто меняет словарь
    - Пример: add_contact("Анна", "+79161234567")

ШАГ 3: Напиши функцию find_contact(name):
    - Принимает имя
    - Возвращает телефон, если имя есть в contacts
    - Если имени нет, возвращает строку "Контакт не найден"
    - Используй оператор in для проверки

ШАГ 4: Протестируй:
1. Добавь 2-3 контакта через add_contact()
2. Найди один существующий контакт через find_contact()
3. Попробуй найти несуществующий

ШАГ 5 (дополнительно): Напиши функцию show_all(),
    которая красиво выводит все контакты.
"""
contacts = {}
def add_contact(name, phone):
    contacts[name] = phone
def find_contact(name):
    if name in contacts:
          return contacts[name]
    else:
        return 'Контакт не найден'
def show_all():
     for name,phone in contacts.items():
          print(name,':', phone)
    





# Готовые вызовы для теста (расскомментируй):
add_contact("Мама", "12345")
add_contact("Друг", "67890")
show_all()
# print(contacts)

# print(find_contact("Мама"))  # должен вывести 12345
# print(find_contact("Незнакомец"))  # "Контакт не найден"

