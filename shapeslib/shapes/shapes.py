from abc import ABC
import math

class Shape(ABC):
    def area(self) -> float:
        raise NotImplementedError("Must be implemented by subclass")

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        if not self._is_valid_triangle():
            raise ValueError("The given sides do not form a valid triangle.")
    
    def _is_valid_triangle(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return False
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

def calculate_area(shape: type[Shape]) -> float:
    return shape.area()