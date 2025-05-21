from math import sqrt

class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def inscribed_circle_radius(self) -> float:
        s = (self.a + self.b + self.c) / 2
        area = self.area()
        return area / s

    def circumscribed_circle_radius(self) -> float:
        area = self.area()
        return (self.a * self.b * self.c) / (4 * area)