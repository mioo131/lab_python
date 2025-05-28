from Geometry.Shape import Shape
from math import sqrt

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value <= 0:
            raise ValueError("Side 'a' must be positive.")
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if value <= 0:
            raise ValueError("Side 'b' must be positive.")
        self._b = value

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        if value <= 0:
            raise ValueError("Side 'c' must be positive.")
        self._c = value

    def area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def inscribed_circle_radius(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return self.area() / p

    def circumscribed_circle_radius(self) -> float:
        return (self.a * self.b * self.c) / (4 * self.area())

    def __str__(self):
        return f"Triangle: a={self.a}, b={self.b}, c={self.c}"
