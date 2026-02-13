class Birthdays:
    def __init__(self):
        self.birthdays = {}
    
    def add_birthday(self, name, date):
        self.birthdays[name] = date
        print(f"Добавлен {name}: {date}")
    
    def show_all(self):
        print("\nДни рождения:")
        for name, date in self.birthdays.items():
            print(f"  {name}: {date}")
    
    def find_by_month(self, month):
        # Ищем людей, родившихся в указанном месяце
        # Просто проверяем, есть ли название месяца в строке даты
        found = [name for name, date in self.birthdays.items() if month in date]
        return found