"""
ЗАДАЧА: Класс "Дни рождения" (Birthdays)

1. В __init__ создай словарь self.birthdays = {} (имя -> день рождения)
2. Метод add_birthday(name, date) - добавляет день рождения. Добавь новое значение в self.birthdays.
3. Метод show_all() - показывает все дни рождения. Выведи все значения из self.birthdays.
4. Метод find_by_month(month) - возвращает имена людей, родившихся в указанном месяце
   (используй list comprehension: [name for name, date in self.birthdays.items() if ____])

Дата может быть просто строкой "15 мая", ищем месяц по вхождению подстроки.
"""

# class Birthdays:
#     pass # вставь свой код вместо pass

# # Тестируем
# bday = Birthdays()
# bday.add_birthday("Анна", "15 мая")
# bday.add_birthday("Иван", "23 марта")
# bday.add_birthday("Мария", "7 мая")
# bday.add_birthday("Петр", "1 июня")

# bday.show_all()

# may_bdays = bday.find_by_month("мая")
# print(f"\nРодившиеся в мае: {may_bdays}")


class Birthdays:
    def __init__(self):
        self.birthdays = {}
        
    def add_birthday(self, name, date):
        self.birthdays[name] = date
        print(f'Создали Словарь:{self.birthdays}')

    def show_all(self):
        for date in self.birthdays.values():
            print(f'Значение: {date}')
    
    def find_by_month(self, month):
        found = [name for name, date in self.birthdays.items() if month in date]
        return found

bday = Birthdays()
bday.add_birthday("Анна", "15 мая")
bday.add_birthday("Иван", "23 марта")
bday.add_birthday("Мария", "7 мая")
bday.add_birthday("Петр", "1 июня")
bday.show_all()
may_bdays = bday.find_by_month("мая")
print(f"\nРодившиеся в мае: {may_bdays}")