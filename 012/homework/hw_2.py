"""
ЗАДАЧА 2: Класс TextAnalyzer (Анализатор текста)

1. В __init__ сохраняй переданный текст в self.text
2. Метод get_unique_letters() - возвращает множество всех букв в тексте
3. Метод get_vowels() - возвращает множество гласных букв из текста
   (используй set comprehension с условием)

Гласные: а, е, ё, и, о, у, ы, э, ю, я
"""

class TextAnalyzer:
    pass

# Тестируем
analyzer = TextAnalyzer("Привет, как дела?")
print("Текст:", analyzer.text)
print("Уникальные буквы:", analyzer.get_unique_letters())
print("Гласные:", analyzer.get_vowels())
print("Согласные:", analyzer.get_consonants())

class TextAnalyzer:
    def __init__(self,text):
        self.text =text
    
    def get_unique_letters(self):
        return {self.text}
    



analyzer = TextAnalyzer("Привет, как дела?")
print("Текст:", analyzer.text)
print("Уникальные буквы:", analyzer.get_unique_letters())
print("Гласные:", analyzer.get_vowels())
print("Согласные:", analyzer.get_consonants())