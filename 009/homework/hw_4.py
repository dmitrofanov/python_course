"""
ЗАДАЧА: Создай класс Calculator (Калькулятор)

1. В __init__ создай атрибут memory = 0 и history как пустой список
2. Создай метод add(x) - прибавляет x к memory, записывает в историю
3. Создай метод subtract(x) - вычитает x из memory, записывает в историю
4. Создай метод clear() - обнуляет memory и очищает историю
5. Создай метод show_history() - показывает все операции

Формат записи в историю: "добавить 5", "вычесть 3" и т.д.
"""

class Calculator:
    def __init__(self):
        self.memory = 0
        self.history = []

    def add(self,x):
        self.memory += x
        self.history.append(f'Добавлено {x}') 
    
    def subtract(self,x):
        self.memory -= x
        self.history.append(f'Вычтено {x}')
    
    def clear(self):
        self.memory = 0
        self.history.clear()
    
    def show_history(self):
        for i, operation in enumerate(self.history,1):
            print(i,operation)

calculator= Calculator()
calculator.add(5)
calculator.add(-1)
calculator.add(1.5)
calculator.clear()
calculator.subtract(5)
calculator.subtract(2)
calculator.subtract(1.5)
calculator.show_history()