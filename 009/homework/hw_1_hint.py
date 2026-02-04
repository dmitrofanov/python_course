class Student:
    def __init__(self, name, age):
        # Сохрани name и age в атрибуты
        self.name = name
        self.age = age
        # Создай атрибут grades как пустой список
        self.grades = []
    
    def add_grade(self, grade):
        # Добавь grade в список self.grades
        self.grades.append(grade)
    
    def get_average(self):
        # Если есть оценки, верни среднее (сумма / количество)
        # Если оценок нет, верни 0
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        else:
            return 0
    
    def info(self):
        # Напечатай: "Студент Имя, возраст: X, средний балл: Y"
        avg = self.get_average()
        print(f"Студент {self.name}, возраст: {self.age}, средний балл: {avg:.1f}")

# Создай студента и протестируй
anna = Student("Анна", 20)
anna.add_grade(5)
anna.add_grade(4)
anna.add_grade(5)
anna.info()  # Должно показать: Студент Анна, возраст: 20, средний балл: 4.7

# Проверим средний балл отдельно
print(f"Средний балл: {anna.get_average():.1f}")