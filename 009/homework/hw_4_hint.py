class Calculator:
    def __init__(self):
        self.memory = 0
        self.history = []
    
    def add(self, x):
        # Прибавь x к memory
        self.memory += x
        # Добавь в историю строку f"добавить {x}"
        self.history.append(f"добавить {x}")
    
    def subtract(self, x):
        # Вычти x из memory
        self.memory -= x
        # Добавь в историю строку f"вычесть {x}"
        self.history.append(f"вычесть {x}")
    
    def clear(self):
        # Обнули memory и очисти history
        self.memory = 0
        self.history.clear()
        print("Калькулятор очищен")
    
    def show_history(self):
        # Покажи всю историю операций
        print("История операций:")
        for i, operation in enumerate(self.history, 1):
            print(f"{i}. {operation}")
        print(f"Текущий результат: {self.memory}")
    
    def get_result(self):
        # Дополнительный метод: возвращает текущий результат
        return self.memory

# Тестируем
calc = Calculator()
calc.add(10)
calc.subtract(3)
calc.add(5)
calc.subtract(2)

calc.show_history()
print(f"Итог: {calc.get_result()}")

calc.clear()
calc.add(100)
calc.show_history()