# __get__ __set__ __delete__

class Ten:
    def __get__(self, instance, owner):
        return 10

class A:
    x = 0
    z = Ten()
    def __init__(self):
        self.y = 0

    def increment(self):
        A.x += 1
        self.y += 1

first = A()
first.increment()

second = A()
second.increment()

print(first.x, first.y, first.z)

