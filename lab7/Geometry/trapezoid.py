from Geometry.Shape import Shape

class Trapezoid(Shape):
    def __init__(self, a: float, b: float, c: float, d: float, height: float):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive.")
        self._height = value

    def area(self) -> float:
        return (self.a + self.b) / 2 * self.height

    def inscribed_circle_radius(self):
        if abs((self.a + self.b) - (self.c + self.d)) < 1e-6:
            p = (self.a + self.b + self.c + self.d) / 2
            return self.area() / p
        return None

    def circumscribed_circle_radius(self):
        return None  # For simplicity, assuming it doesn't exist

    def __str__(self):
        return f"Trapezoid: a={self.a}, b={self.b}, c={self.c}, d={self.d}, height={self.height}"
