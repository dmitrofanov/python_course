class Rectangle:
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def area(self):
        return self.dx * self.dy

    def __repr__(self):
        return f"Rectangle(x={self.x}, y={self.y}, dx={self.dx}, dy={self.dy})"

rectangle = Rectangle(5,5,3,10)
print(rectangle)

from dataclasses import dataclass

@dataclass
class Rectangle2:
    x: int
    y: int
    dx: int
    dy: int

    def area(self):
        return self.dx * self.dy

rectangle2 = Rectangle2(0,0,25,100)
print(rectangle2)
rectangle3 =Rectangle2(x=0, y=0, dx=25, dy=100)


         
