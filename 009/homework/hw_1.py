"""
ЗАДАЧА: Создай класс Student (Студент)

1. В __init__ принимай name и age, сохраняй в атрибуты
2. В __init__ добавь атрибут grades как пустой список
3. Создай метод add_grade(grade) - добавляет оценку в список
4. Создай метод get_average() - возвращает средний балл
5. Создай метод info() - печатает имя, возраст и средний балл

Создай студента, добавь оценки 5, 4, 5, выведи информацию.
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
        
    def get_average(self):
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        else:
            return 0
    
    def info(self):
        print(f'Имя: {self.name} Возраст: {self.age} Средний балл: {self.get_average()} ')

student1 = Student("Павел", 36)
student1.add_grade(5)
student1.add_grade(4)
student1.add_grade(5)
student1.info()





