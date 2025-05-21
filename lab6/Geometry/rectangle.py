class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def inscribed_circle_radius(self) -> float:
        return min(self.width, self.height) / 2

    def circumscribed_circle_radius(self) -> float:
        from math import sqrt
        return sqrt(self.width ** 2 + self.height ** 2) / 2
