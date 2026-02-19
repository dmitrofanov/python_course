class StampCollection:
    def __init__(self):
        self.stamps = []
    
    def add_stamp(self, country):
        self.stamps.append(country)
        print(f"Добавлена марка из {country}")
    
    def show_all(self):
        print("Все марки:", self.stamps)
    
    def unique_countries(self):
        # Простой set comprehension - убираем дубликаты
        return {country for country in self.stamps}