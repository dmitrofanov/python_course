"""
ЗАДАЧА: Создай класс Rectangle (Прямоугольник)

1. В __init__ принимай width и height, сохраняй в атрибуты
2. Создай метод area() - возвращает площадь (ширина * высота)
3. Создай метод perimeter() - возвращает периметр (2 * (ширина + высота))
4. Создай метод scale(factor) - умножает ширину и высоту на factor
5. Создай метод info() - печатает ширину, высоту, площадь и периметр

Создай прямоугольник 5x3, вычисли площадь и периметр, увеличь в 2 раза.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (2 *(self.width + self.height))
    
    def scale(self, factor):
        self.width =self.width * factor
        self.height = self.height * factor
    
    def info(self):
        print(f'Ширина: {self.width} Высота: {self.height} Периметр: {self.perimeter()} Площадь: {self.area()}')

rectangle = Rectangle(5, 3)
rectangle.area()
rectangle.perimeter()
rectangle.scale(2)
rectangle.info()
