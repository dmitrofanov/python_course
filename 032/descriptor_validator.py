from abc import ABC, abstractmethod

class Validator(ABC):
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass

class OneOf(Validator):
    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f"Ожидается {value!r} среди {self.options!r}")

class Number(Validator):
    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Ожидается {value!r} числом")
        if value < self.min_value:
            raise ValueError(f"Ожидается значение {value!r} > {self.min_value!r}")
        if value > self.max_value:
            raise ValueError(f"Ожидается значение {value!r} < {self.max_value!r}")

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        
class Component:
    kind = OneOf("Металл", "Дерево", "Пластик")
    quantity = Number(10,100)

    def __init__(self, kind , quantity):
        self.kind = kind
        self.quantity = quantity

component1 = Component("Пластик", 9)
print(component1.kind)