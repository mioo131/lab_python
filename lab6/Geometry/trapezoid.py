from math import sqrt

class Trapezoid:
    def __init__(self, a: float, b: float, c: float, d: float, height: float):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.height = height

    def area(self) -> float:
        return (self.a + self.b) / 2 * self.height

    def inscribed_circle_radius(self):
        if abs((self.a + self.b) - (self.c + self.d)) < 1e-6:
            # формула радиуса вписанной окружности
            p = (self.a + self.b + self.c + self.d) / 2
            area = self.area()
            return area / p
        else:
            return None  # окружность не существует

    def circumscribed_circle_radius(self):
        if abs(self.c - self.d) < 1e-6:
            return None
        else:
            return None
