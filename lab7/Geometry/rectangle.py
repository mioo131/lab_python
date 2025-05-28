from Geometry.Shape import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive.")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive.")
        self._height = value

    def area(self) -> float:
        return self.width * self.height

    def inscribed_circle_radius(self) -> float:
        if self.width == self.height:
            return self.width / 2
        return None

    def circumscribed_circle_radius(self) -> float:
        return (self.width**2 + self.height**2) ** 0.5 / 2

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.height}"
