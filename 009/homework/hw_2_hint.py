class Rectangle:
    def __init__(self, width, height):
        # Сохрани width и height в атрибуты
        self.width = width
        self.height = height
    
    def area(self):
        # Верни площадь (ширина * высота)
        return self.width * self.height
    
    def perimeter(self):
        # Верни периметр (2 * (ширина + высота))
        return 2 * (self.width + self.height)
    
    def scale(self, factor):
        # Умножь self.width и self.height на factor
        self.width *= factor
        self.height *= factor
    
    def info(self):
        # Напечатай информацию о прямоугольнике
        print(f"Прямоугольник {self.width}x{self.height}")
        print(f"Площадь: {self.area()}, Периметр: {self.perimeter()}")

# Создай прямоугольник и протестируй
rect = Rectangle(5, 3)
rect.info()  # Должно показать: Прямоугольник 5x3, Площадь: 15, Периметр: 16

# Увеличим прямоугольник
rect.scale(2)
rect.info()  # Теперь: Прямоугольник 10x6, Площадь: 60, Периметр: 32

# Проверим методы отдельно
print(f"Площадь: {rect.area()}")
print(f"Периметр: {rect.perimeter()}")