class TextAnalyzer:
    def __init__(self, text):
        self.text = text.lower()  # приводим к нижнему регистру
    
    def get_unique_letters(self):
        # Все уникальные буквы
        return {char for char in self.text if char.isalpha()}
    
    def get_vowels(self):
        vowels = "аеёиоуыэюя"
        # Только гласные
        return {char for char in self.text if char in vowels}
    
    def get_consonants(self):
        vowels = "аеёиоуыэюя"
        # Только согласные
        return {char for char in self.text if char.isalpha() and char not in vowels}